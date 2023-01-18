# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:04:10 2023

@author: Administrator
"""

import random
import gymnasium as gym
import numpy as np
import collections
from tqdm import tqdm
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt


class ReplayBuffer():
  def __init__(self, capacity):
    self.buffer = collections.deque(maxlen=capacity)
    
  def add(self, state, action, reward, next_state, done):
    self.buffer.append((state, action, reward, next_state, done))
    
  def sample(self, batch_size):
    transitions = random.sample(self.buffer, batch_size)
    state, action, reward, next_state, done = zip(*transitions)
    return np.array(state), action, reward, np.array(next_state), done
    
    

class Qnet(torch.nn.Module):
  def __init__(self, state_dim, hidden_dim, action_dim):
    pass


def dqn_main():
  print('Hello, dqn')

if __name__ == '__main__':
  dqn_main()


