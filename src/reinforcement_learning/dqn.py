# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:04:10 2023

@author: Administrator
"""
import sys
import os
import random
import gymnasium as gym
import numpy as np
import collections
from tqdm import tqdm
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

class ReplayBuffer():
  def __init__(self, capacity):
    self.buffer = collections.deque(maxlen=capacity)
    
  def add(self, state, action, reward, next_state, done):
    self.buffer.append((state, action, reward, next_state, done))
    
  def sample(self, batch_size):
    transitions = random.sample(self.buffer, batch_size)
    state, action, reward, next_state, done = zip(*transitions)
    return np.array(state), action, reward, np.array(next_state), done
  
  def size(self):
    return len(self.buffer)
  
  def __len__(self):
    return len(self.buffer)
    

class Qnet(torch.nn.Module):
  def __init__(self, state_dim, hidden_dim, action_dim):
    super(Qnet, self).__init__()
    self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
    self.fc2 = torch.nn.Linear(hidden_dim, action_dim)
    
  def forward(self, x):
    x = F.relu(self.fc1(x))
    return self.fc2(x)


class DQN():
  def __init__(self, state_dim, hidden_dim, action_dim, learning_rate, gamma, epsilon, target_update, device):
    self.action_dim = action_dim
    self.qnet = Qnet(state_dim, hidden_dim, action_dim).to(device)
    self.target_qnet = Qnet(state_dim, hidden_dim, action_dim).to(device)
    self.optimizer = torch.optim.Adam(self.qnet.parameters(), lr=learning_rate)
    self.gamma = gamma
    self.epsilon = epsilon
    self.target_update = target_update
    self.device = device
    self.count = 0
    
  def take_action(self, state):
    if np.random.random() < self.epsilon:
      action = np.random.randint(self.action_dim)
    else:
      state = torch.tensor([state], dtype=torch.float).to(self.device)
      action = self.qnet(state).argmax().item()
    #print(action)
    return action

  def update(self, transition_dict):
    states = torch.tensor(transition_dict['states'], dtype=torch.float).to(self.device)
    actions = torch.tensor(transition_dict['actions']).view(-1, 1).to(self.device)
    rewards = torch.tensor(transition_dict['rewards'], dtype=torch.float).to(self.device)
    next_states = torch.tensor(transition_dict['next_states'], dtype=torch.float).to(self.device)
    dones = torch.tensor(transition_dict['dones'], dtype=torch.float).view(-1, 1).to(self.device)
    q_value = self.qnet(states).gather(1, actions)
    max_next_q_values = self.target_qnet(next_states).max(1)[0].view(-1, 1)
    q_targets = rewards + self.gamma * max_next_q_values*(1-dones)

    dqn_loss = torch.mean(F.mse_loss(q_value, q_targets))
    self.optimizer.zero_grad()
    dqn_loss.backward()
    self.optimizer.step()
    
    if self.count % self.target_update == 0:
      self.target_qnet.load_state_dict(self.qnet.state_dict())
    self.count += 1
    

def extract_state(observation):
  if isinstance(observation, tuple):
    return observation[0]
  if isinstance(observation, np.ndarray):
    return observation
  raise NotImplementedError


def dqn_main():
  lr = 2e-3
  num_episodes = 500
  hidden_dim = 128
  gamma = 0.98
  epsilon = 0.01
  target_update = 10
  buffer_size = 10000
  minimal_size = 500
  batch_size = 64
  env_name = 'CartPole-v1'
  device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
  print('Using device: ', device)
  
  env = gym.make(env_name)
  random.seed(0)
  np.random.seed(0)
  torch.manual_seed(0)
  replay_buffer = ReplayBuffer(buffer_size)
  state_dim = env.observation_space.shape[0]
  action_dim = env.action_space.n
  #print('state_dim:', state_dim, 'action_dim:', action_dim)
  agent = DQN(state_dim, hidden_dim, action_dim, lr, gamma, epsilon, target_update, device)
  #print(agent)
  return_list = []
  for i in range(10):
    with tqdm(total=int(num_episodes/10), desc='Iteration %d' % i) as pbar:
      #print('')
      for i_episode in range(int(num_episodes/10)):
        episode_return = 0
        state = extract_state(env.reset())
        done = False
        while not done:
          action = agent.take_action(state)
          observation, reward, terminated, truncated, info = env.step(action)
          #print(observation, reward, terminated, truncated, info)
          next_state = extract_state(observation)
          #print(state, next_state)
          if terminated or truncated:
            done = True
          replay_buffer.add(state, action, reward, next_state, done)
          state = next_state
          episode_return += reward
          if len(replay_buffer) > minimal_size:
            b_s, b_a, b_r, b_ns, b_d = replay_buffer.sample(batch_size)
            transition_dict = {
                'states': b_s,
                'actions': b_a,
                'next_states': b_ns,
                'rewards': b_r,
                'dones': b_d
              }
            agent.update(transition_dict)
          return_list.append(episode_return)
          if (i_episode + 1)%10 == 0:
            pbar.set_postfix({
                'episode': '%d' % (num_episodes/10*i + i_episode + 1),
                'return': '%.3f' % np.mean(return_list[-10:])
              })
          pbar.update(1)

  episodes_list = list(range(len(return_list)))
  plt.plot(episodes_list, return_list)
  plt.xlabel('Episodes')
  plt.ylabel('Returns')
  plt.title('DQN on {}'.format(env_name))
  plt.show()
  
  

if __name__ == '__main__':
  dqn_main()


