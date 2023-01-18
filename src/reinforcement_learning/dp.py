# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 21:10:01 2023

@author: Administrator
"""

import gymnasium as gym


class PolicyIteration:
  def __init__(self, env, theta, gamma):
    self.env = env


def dp_main():
  env = gym.make('CliffWalking-v0')
  env.reset()
  print(env.P)

if __name__ == '__main__':
  dp_main()

