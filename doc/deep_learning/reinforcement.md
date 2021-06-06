# 增强学习(Reinformance Learning)

## 定义
$R_t$: $t$时刻的奖励函数值  
$S_t$: $t$时刻的状态  
$A_t$: $t$时刻的行为

## 假设
* 马尔可夫假设: $P[S_{t+1} | S_t] = P[S_{t+1} | S_1, \cdots, S_t]$
* 下一时刻的状态只与这一时刻的状态以及行为有关: $P_{ss^{'}}^a = P[S_{t+1} = s^{'} | s_t = s, A_t = a] $
* 下一时间的奖励函数只与这一时刻的状态以及行为有关: $R_s^a = E[R_{t+1} | S_t= s, A_t = a]$  

注: $s^{'}$表示下一时刻的状态.

## 马尔可夫决策过程(Markov Decision Process)
* $t=0$, 初始状态: $s_0, p(s_0)$
* for $t=0:end$
    Agent 选择行为$a_t$  
    Env 采样奖励函数$r_t - R(. | s_t, a_t)$  
    Env 产生下一个状态: $s_{t+1} - P(. | s_t, a_t)$ 


## Reference
* 浙江大学机器学习课程 35 - 胡浩基
