# 增强学习(Reinformance Learning)

## 定义
$R_t$: $t$时刻的奖励函数值  
$S_t$: $t$时刻的状态  
$A_t$: $t$时刻的行为

## 假设
* 马尔可夫假设: $p[S_{t+1} | S_t] = p[S_{t+1} | S_1, \cdots, S_t]$
* 下一时刻的状态只与这一时刻的状态以及行为有关: $p_{ss^{'}}^a = p[S_{t+1} = s^{'} | s_t = s, A_t = a] $
* 下一时间的奖励函数只与这一时刻的状态以及行为有关: $R_s^a = E[R_{t+1} | S_t= s, A_t = a]$  

注: $s^{'}$表示下一时刻的状态.

## 马尔可夫决策过程(Markov Decision Process)
* $t=0$, 初始状态: $s_0, p(s_0)$
* for $t=0:end$
    Agent 选择行为$a_t$  
    Env 采样奖励函数$r_t： R(. | s_t, a_t)$  
    Env 产生下一个状态: $s_{t+1}： P(. | s_t, a_t)$  
    Agent 获得奖励函数$r_t$和下一个状态$s_{t+1}$
* 学习一个策略(Policy)$\pi ^{\*}$, 这是从状态到行为的映射函数.

## 目标函数
增强学习中的待优化目标函数是累积奖励， 即一段时间内的奖励函数的加权平均值, $\gamma$是衰减项.
$$
G_t = R_{t+1} + \gamma R_{t+2} + \cdots = \sum_{k=0}^{\infty}\gamma^kR_{t+k+1}
$$

## Q-learning
根据决策策略$\pi$(Policy)， 可以获得一条路径: $s_0, a_0, r_0, s_1, a_1, r_1, \cdots$.  
定义1： 估值函数是衡量某个状态最终能获得多少累积奖励的函数:  
$$
V^{\pi}(s) = E[\sum_{t \geq 0}\gamma^t r_t|s_0=s, \pi]
$$
定义2: Q函数是衡量某个状态下采取某个行为后， 最终能获得多少累积奖励的函数:
$$
Q^{\pi}(s, a) = E[\sum_{t \geq 0}\gamma^tr_t|s_0=s, a_0=a, \pi]
$$
显然:
$$
V^{\pi}(s) = \sum_{a \in A}p(a|s)Q^{\pi}(s, a)
$$
再来观察$V^{\pi}(s)$
$$
\begin{align}
V^{\pi}(s) & = E[\sum_{t \geq 0}\gamma^t r_t|s_0=s, \pi] \\\\
& = E[r_0 + \gamma \sum_{t \geq 0}\gamma^t r_{t+1} | s_0 = s, \pi] \\\\
& = \sum_{a \in A}p(a | s) \sum_{s^{'} \in S}p_{ss^{'}}^a(R_s^a + \gamma V^{\pi}(s^{'})) \\\\
\end{align}
$$
其中： $\pi(s, a) = p(a | s)$.
$$
\begin{align}
& Q^{\pi}(s, a) =  \sum_{s^{'} \in S}p_{ss^{'}}^a(r_s^a + \gamma V^{\pi}(s^{'})) \\\\
& \pi(s, a) = \begin{cases}
1:  if \  a = \mathop{argmax} Q(s, a) \\\\
0,  others \\\\
\end{cases} \\\\
& 则有: V^{\pi}(s) = \sum_{a \in A}\pi(s, a)Q^{\pi}(s, a) \\\\
\end{align}
$$

## Deep Q-Network(DQN)




## Reference
* 浙江大学机器学习课程 35 - 胡浩基
