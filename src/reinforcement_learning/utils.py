# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:18:34 2023

@author: Administrator
"""

import numpy as np

def extract_state(observation):
  if isinstance(observation, tuple):
    return observation[0]
  if isinstance(observation, np.ndarray):
    return observation
  raise NotImplementedError