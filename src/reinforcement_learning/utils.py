# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:18:34 2023

@author: Administrator
"""

import numpy as np
from tqdm import tqdm

def extract_state(observation):
  if isinstance(observation, tuple):
    return observation[0]
  if isinstance(observation, np.ndarray):
    return observation
  raise NotImplementedError
  

def train_on_policy_agent(env, agent, num_episodes):
  return_list = []
  for i in range(10):
    with tqdm(total=int(num_episodes/10), desc='Iteration %d' % i) as pbar:
      for i_episode in range(int(num_episodes/10)):
        episode_return = 0
        transition_dict = {'states': [], 'actions': [], 'next_states': [], 'rewards': [], 'dones': []}
        state = extract_state(env.reset())
        done = False
        while not done:
          action = agent.take_action(state)
          observation, reward, terminated, truncated, info = env.step(action)
          next_state = extract_state(observation)
          if terminated or truncated:
            done = True 
          transition_dict['states'].append(state)
          transition_dict['actions'].append(action)
          transition_dict['next_states'].append(next_state)
          transition_dict['rewards'].append(reward)
          transition_dict['dones'].append(done)
          state = next_state
          episode_return += reward
        return_list.append(episode_return)
        agent.update(transition_dict)
        if (i_episode+1) % 10 == 0:
          pbar.set_postfix({'episode': '%d' % (num_episodes/10 * i + i_episode+1), 'return': '%.3f' % np.mean(return_list[-10:])})
        pbar.update(1)
  return return_list