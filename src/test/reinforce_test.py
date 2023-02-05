# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 10:20:43 2023

@author: Administrator
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../reinforcement_learning')
from reinforce import reinf_main


def test_reinfore():
  reinf_main()