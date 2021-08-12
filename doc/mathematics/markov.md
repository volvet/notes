# 隐含马尔可夫模型 - HMM(Hide Markov Models)

一个HMM是由三部分组成:  $\lambda = \\{ A, B, \Pi \\}$.  
$$
A: 状态转移矩阵  \\\\
B: 观测概率 \\\\
\Pi: 状态先验概率
$$
假设共有$P$中状态: $\\{ S_0, S_1, \cdots, S_P \\}$.  
$$
\Pi(S_i)： 刚开始在状态S_i的概率 \\\\
A = \\{ a_{ij} \\}: 表示状态转移概率(P \times P 矩阵), 一阶马尔可夫链假设 \\\\
a_{ij} = P(q_{t+1} = S_j | q_t = s_i) \\\\
B = \\{ b_j(O)\\}: 若输入向量O是属于S_j的， 则它的概率分布用b_j(O)来表示.
$$


## Reference
* 胡浩基 - 浙江大学机器学习课程 50
* MFCC (Mel-Frequency Cepstral Coefficients)

