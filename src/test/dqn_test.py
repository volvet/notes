# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:05:19 2023

@author: Administrator
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../reinforcement_learning')
from dqn import dqn_main


def test_dqn():
  dqn_main()