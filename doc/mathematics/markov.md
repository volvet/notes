# 隐含马尔可夫模型 - HMM(Hide Markov Models)

一个HMM是由三部分组成:  $\lambda = \\{ A, B, \Pi \\}$.  
$$
A: 状态转移矩阵  \\\\
B: 观测概率 \\\\
\Pi: 状态先验概率
$$
假设共有$P$中状态: $\\{ S_0, S_1, \cdots, S_{P-1} \\}$.  
$$
\Pi(S_i)： 刚开始在状态S_i的概率 \\\\
A = \\{ a_{ij} \\}: 表示状态转移概率(P \times P 矩阵), 一阶马尔可夫链假设 \\\\
a_{ij} = P(q_{t+1} = S_j | q_t = s_i) \\\\
B = \\{ b_j(O)\\}: 若输入向量O是属于S_j的， 则它的概率分布用b_j(O)来表示, 传统的方法是用高斯混合模型(GMM)来估计b_j(O).
$$

## 识别问题
给出$O = O_1, O_2, \cdots, O_T$, 给出一个HMM模型 $\lambda = \\{ A, B, \Pi \\}$, 求$P(O | \lambda)$
$$
P(O | \lambda) = \sum_{q_1=S_0}^{S_{P-1}}\Pi(q_1)b_{q_1}(O_1)\sum_{q_2=S_0}^{S_P-1}a_{q_1q_2}b_{q_2}(O_2)\sum_{q_3=S_0}^{S_P-1}a_{q_2q_3}b_{q_3}(O_3) \cdots \sum_{q_T=S_0}^{S_P-1}a_{q_{T-1}q_T}b_{q_T}(O_T)
$$
### 识别问题的简便算法
定义： $\alpha_t(i) = P(O_1, O_2, O_3, \cdots, O_t, q_t = S_i | \lambda)$, 则有:
$$
\begin{align}
\alpha_1(i) &= P(O_1, q_t = S_i | \lambda) \\\\
&= \Pi(S_i)P(O_1 | \lambda) \\\\
&= \Pi(S_i)b_i(O_1) \\\\
\alpha_{t+1}(j) &= P(O_1, O_2, \cdots, O_{t+1}, q_{t+1} = S_j | \lambda)\\\\
&= \sum_{i=1}^PP(O_1, O_2, \cdots, O_t, q_t = S_i | \lambda) \\\\
\end{align}
$$

## Reference
* 胡浩基 - 浙江大学机器学习课程 50
* MFCC (Mel-Frequency Cepstral Coefficients)

