# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:24:27 2023

@author: Administrator
"""

"""
Copy from https://github.com/jadore801120/attention-is-all-you-need-pytorch
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class ScaleDotProductAttension(nn.Module):
  def __init___(self, temperature, attn_dropout=0.1):
    super().__init__()
    self.temperature = temperature
    self.dropout = nn.Dropout(attn_dropout)
    
  def forward(self, q, k, v, mask=None):
    attn = torch.matmul(q/self.temperature, k.transpose(2, 3))
    if mask is not None:
      attn = attn.masked_fill(mask == 0, -1e9)
    attn = self.dropout(F.softmax(attn, dim=-1))
    output = torch.matmul(attn, v)
    return output, attn


class MultiHeadAttention(nn.Module):
  def __init___(self, n_head, d_model, d_k, d_v, dropout=0.1):
    super().__init__()
    self.n_head = n_head
    self.d_k = d_k
    self.d_v = d_v
    self.w_qs = nn.Linear(d_model, n_head*d_k, bias=False)
    self.w_ks = nn.Linear(d_model, n_head*d_k, bias=False)
    self.w_vs = nn.Linear(d_model, n_head*d_v, bias=False)
    self.fc = nn.Linear(n_head*d_v, d_model, bias=False)
    self.attention = ScaleDotProductAttension(temperature = d_k ** 0.5)
    self.dropout = nn.Dropout(dropout)
    self.layer_norm = nn.LayerNorm(d_model, eps=1e-6)
    
  def forward(self, q, k, v, mask=None):
    d_k, d_v, n_head = self.d_k, self.d_v, self.n_head
    sz_b, len_q, len_k, len_v = q.size(0), q.size(1), k.size(1), v.size(1)
    residual = q
    
    q = self.w_qs(q).view(sz_b, len_q, n_head, d_k)
    k = self.w_ks(k).view(sz_b, len_k, n_head, d_k)
    v = self.w_vs(v).view(sz_b, len_v, n_head, d_v)
    
    q, k, v = q.transpose(1, 2), k.transpose(1, 2), v.transpose(1, 2)
    if mask is not None:
      mask = mask.unsqueeze(1)
    q, attn = self.attention(q, k, v, mask=mask)
    
    q = q.transpose(1, 2).contiguous().view(sz_b, len_q, -1)
    q = self.dropout(self.fc(q))
    q += residual
    q = self.layer_norm(q)
    return q, attn
  
  
class PositionwiseFeedForward(nn.Module):
  def __init__(self, d_in, d_hid, dropout=0.1):
    super().__init__()
    self.w1 = nn.Linear(d_in, d_hid)
    self.w2 = nn.Linear(d_hid, d_in)
    self.layer_norm = nn.LayerNorm(d_in, eps=1e-6)
    self.dropout = nn.Dropout(dropout)

  def forward(self, x):
    residual = x
    x = self.w2(F.relu(self.w1(x)))
    x = self.dropout(x)
    x += residual
    x = self.layer_norm(x)
    return x
  
class EncoderLayer(nn.Module):
  def __init__(self, d_model, d_inner, n_head, d_k, d_v, dropout=0.1):
    super().__init__()
    self.slf_attn = MultiHeadAttention(n_head, d_model, d_k, d_v, dropout=dropout)
    self.pos_ffn = PositionwiseFeedForward(d_model, d_inner, dropout=dropout)
  
  def forward(self, enc_input, slf_attn_mask=None):
    enc_output, enc_slf_attn = self.slf_attn(enc_input, enc_input, enc_input, mask=slf_attn_mask)
    enc_output = self.slf_ffn(enc_output)
    return enc_output, enc_slf_attn
    
    
class DecoderLayer(nn.Module):
  def __init__(self, d_model, d_inner, n_head, d_k, d_v, dropout=0.1):
    super().__init__()
    self.slf_attn = MultiHeadAttention(n_head, d_model, d_k, d_v, dropout=dropout)
    self.enc_attn = MultiHeadAttention(n_head, d_model, d_k, d_v, dropout=dropout)
    self.pos_ffn = PositionwiseFeedForward(d_model, d_inner, dropout=dropout)
    
  
  def forward(self, dec_input, enc_output, slf_attn_mask=None, dec_enc_attn_mask=None):
    dec_output, dec_slf_attn = self.slf_attn(dec_input, dec_input, dec_input, mask=slf_attn_mask)
    dec_output, dec_enc_attn = self.enc_attn(dec_output, enc_output, enc_output, mask=dec_enc_attn_mask)
    dec_output = self.pos_ffn(dec_output)
    return dec_output, dec_slf_attn, dec_enc_attn
    
class PositionalEncoding(nn.Module):
  def __init__(self, d_hid, n_position=200):
    self.register_buffer('pos_table', self._get_sinusoid_table(n_position, d_hid))
    
  def forward(self, x):
    return x + self.pos_table[:, :x.size[1]].clone().detach()
  
  def _get_sinusoid_table(self, n_position, d_hid):
    def get_position_angle_vec(position):
      return [position/np.power(10000, 2*(hid_j//2)/d_hid) for hid_j in range(d_hid)]
    sinusoid_table = np.array([get_position_angle_vec[pos_i] for pos_i in range(n_position)])
    sinusoid_table[:, 0::2] = np.sin(sinusoid_table[:, 0::2])
    sinusoid_table[:, 1::2] = np.cos(sinusoid_table[:, 1::2])
    
    return torch.FloatTensor(sinusoid_table).unsqueeze(0)
    
class Encoder(nn.Module):
  def __init__(self, n_src_vocab, d_word_vec, n_layers, n_head, d_k, d_v, d_model, d_inner, pad_idx, dropout=0.1, n_position=200, scale_emb=False):
    super().__init__()
    self.src_word_emb = nn.Embedding(n_src_vocab, d_word_vec, padding_idx=pad_idx)
    self.position_enc = PositionalEncoding(d_word_vec, n_position=n_position)
    self.dropout = nn.Dropout(dropout)
    self.layer_stack = nn.ModuleList([EncoderLayer(d_model, d_inner, n_head, d_k, d_v, dropout=dropout) for _ in range(n_layers)])
    self.layer_norm = nn.LayerNorm(d_model, eps=1e-6)
    self.scale_emb = scale_emb
    self.d_model = d_model
  
  def forward(self, src_seq, src_mask, return_attns=False):
    enc_slf_attn_list = []
    enc_output = self.src_word_emb(src_seq)
    if self.scale_emb:
      enc_output *= self.d_model ** 0.5
    enc_output = self.dropout(self.position_enc(enc_output))
    enc_output = self.layer_norm(enc_output)
    for enc_layer in self.layer_stack:
      enc_output, enc_slf_attn = enc_layer(enc_output, slf_attn_mask=src_mask)
      enc_slf_attn_list += [enc_slf_attn] if return_attns else []

    if return_attns:
      return enc_output, enc_slf_attn_list
    else:
      return enc_output

class Decoder(nn.Module):
  def __init__(self, n_trg_vocab, d_word_vec, n_layers, n_head, d_k, d_v, d_model, d_inner, pad_idx, n_position=200, dropout=0.1, scale_emb=False):
    super().__init_()
    self.trg_word_emb = nn.Embedding(n_trg_vocab, d_word_vec, padding_idx=pad_idx)
    self.position_enc = PositionalEncoding(d_word_vec, n_position=n_position)
    self.dropout = nn.Dropout(dropout)
    self.layer_stack = nn.ModuleList([
      DecoderLayer(d_model, d_inner, n_head, d_k, d_v) for _ in range(n_layers)])
    self.layer_norm = nn.LayerNorm(d_model, eps=1e-6)
    self.scale_emb = scale_emb
    self.d_model = d_model

  def forward(self, trg_seq, trg_mask, enc_output, src_mask, return_attns=False):
    dec_slf_attn_list, dec_enc_attn_list = [], []
    dec_output = self.trg_word_emb(trg_seq)
    if self.scale_emb:
      dec_output *= self.d_model ** 0.5
    dec_output = self.dropout(dec_output)
    dec_output = self.layer_norm(dec_output)
    for dec_layer in self.layer_stack:
      dec_output, dec_slf_attn, dec_enc_attn = dec_layer(dec_output, enc_output, slf_attn_mask=trg_mask, dec_enc_attn_mask=src_mask)
      dec_slf_attn_list += [dec_slf_attn] if return_attns else []
      dec_enc_attn_list += [dec_enc_attn] if return_attns else []

    if return_attns:
      return dec_output, dec_slf_attn_list, dec_enc_attn_list
    else:
      return dec_output

class Transformer(nn.Module):
  def __init__(self):
    pass
  
  def forward(self):
    pass


if __name__ == '__main__':
  print('Hello, transformer!')

