# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:01:28 2023

@author: Administrator
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../reinforcement_learning')
from dp import dp_main



def test_dp():
  dp_main()

