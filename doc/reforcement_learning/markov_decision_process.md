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
Q_\pi(s_t,a_t) = \mathbb{E}
$$

## Reference
* 王树森 张志华 深度强化学习
