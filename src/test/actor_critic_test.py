# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:27:28 2023

@author: Administrator
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../reinforcement_learning')
from actor_critic import ac_main


def test_reinfore():
  ac_main()