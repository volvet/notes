# 马尔可夫决策过程(MDP)

## 基本概念

* 状态空间(State Space): 所有可能存在的状态的集合， 记作$S$
* 动作(Action): 指作出的决策
* 动作空间(Action Space)
* 智能体(Agent)
* 策略函数(Policy Function): $\pi (a|s)$
* 奖励(Reward)
* 状态转移(State Transition)
* 状态转移函数(State Transition Function)
状态转移函数记作：$p(s^{'}|s, a)$, 是一个条件概率密度函数.
* 回报(Return): 回报是当前时刻开始到一回合结束的所有奖励的综合. 定义如下:
$$
U_t = R_t + R_{t+1} + R_{t+2} + \cdots
$$
折扣回报(Discount Return)给未来的奖励做折扣,
$$
U_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \cdots,  0 \leq \gamma \leq 1
$$

## 价值函数
* 动作价值函数
$$
\begin{align}
Q_\pi(s_t,a_t) &= \mathbb{E} _ {S_{t+1}, A_{t+1}, \cdots, S_n, A_n}[U_t | S_t=s_t, A_t=a_t] \\\\
&=\int_Sd_{s_{t+1}}\int_Ad_{a_{t+1}} \cdots \int_Sd_{s_n}\int_Ad_{a_n}[\prod_{k=t+1}^{n}p(s_k|s_{k-1},a_{k-1})\pi(a_k|s_k)]U_t
\end{align}
$$
最优动作价值函数: $Q_{\*}(s_t, a_t) = \mathop{max} \limits_{\pi} Q_{\pi}(s_t, a_t)$

* 状态价值函数
$$
\begin{align}
V_\pi(s_t) &= \mathbb{E} _ {A_t \sim \pi(\cdot | s_t)}[Q_\pi(s_t, A_t] \\\\
&=\sum_{a \in A}\pi(a|s_t)Q_\pi(s_t,a)
\end{align}
$$

* 策略学习和价值学习   
价值学习通常是指学习最优价值函数$Q_{\*}(s,a)$, 智能体(Agent)的决策可以用这个公式表示:
$$
a_t = \mathop{argmax} \limits_{a \in A} Q_{\*}(s_t, a)
$$

## Reference
* 王树森 张志华 深度强化学习 https://www.math.pku.edu.cn/teachers/zhzhang/