# 增强学习(Reinformance Learning)

## 定义
$R_t$: $t$时刻的奖励函数值  
$S_t$: $t$时刻的状态  
$A_t$: $t$时刻的行为

## 假设
* 马尔可夫假设: $P[S_{t+1} | S_t] = P[S_{t+1} | S_1, \cdots, S_t]$
* 下一时刻的状态只与这一时刻的状态以及行为有关: $P_{ss^{'}}^a = P[S_{t+1} = s^{'} | s_t = s, A_t = a] $

## Reference
* 浙江大学机器学习课程 35 - 胡浩基
