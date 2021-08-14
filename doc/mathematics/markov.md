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

## 问题一： 识别
给出$O = O_1, O_2, \cdots, O_T$, 给出一个HMM模型 $\lambda = \\{ A, B, \Pi \\}$, 求$P(O | \lambda)$
$$
P(O | \lambda) = \sum_{q_1=S_0}^{S_{P-1}}\Pi(q_1)b_{q_1}(O_1)\sum_{q_2=S_0}^{S_P-1}a_{q_1q_2}b_{q_2}(O_2)\sum_{q_3=S_0}^{S_P-1}a_{q_2q_3}b_{q_3}(O_3) \cdots \sum_{q_T=S_0}^{S_P-1}a_{q_{T-1}q_T}b_{q_T}(O_T)
$$
### 简便算法
定义： $\alpha_t(i) = P(O_1, O_2, O_3, \cdots, O_t, q_t = S_i | \lambda)$, 则有:
$$
\begin{align}
\alpha_1(i) &= P(O_1, q_t = S_i | \lambda) \\\\
&= \Pi(S_i)P(O_1 | \lambda) \\\\
&= \Pi(S_i)b_i(O_1) \\\\
\alpha_{t+1}(j) &= P(O_1, O_2, \cdots, O_{t+1}, q_{t+1} = S_j | \lambda)\\\\
&= \sum_{i=1}^PP(O_1, O_2, \cdots, O_t, q_t = S_i | \lambda) a_{ij} b_j(O_{t+1}) \\\\
&= \sum_{i=1}^P \alpha_t(i) a_{ij} b_j(O_{t+1}) \\\\
P(O | \lambda) &= \sum_{i=1}^P\alpha_t(i) \\\\
\end{align}
$$

## 问题二
给定$\lambda = \\{ \Pi, A, B\\}$, 给定输入$O = O_1, O_2, \cdots, O_T$, 求一串状态序列$Q = q_1, q_2, \cdots, q_T$, 
使得: $E(Q) = \Pi(S_{q_1})b_{q_1}(O_1)a_{q_1q_2}b_{q_2}(O_2)\cdots a_{q_{T-1}q_T}b_{q_T}(O_T)$ 最大.

### 维特比算法(Viterbi ALgorithm)
 * 定义 $\delta_t(i) = max(P(q_1,q_2, \cdots, q_{T-1}, q_T=S_i, O_1, O_2, \cdots, O_T))$
 * 递推公式:
$$
\begin{align}
\delta_1(i) &= \Pi(S_i)b_i(O_1) \\\\
\phi_1(i) &= 0 \\\\
\delta_T(j) &= \mathop{max} \limits_{i} (\delta_{T-1}(i) a_{ij})b_j(O_T) \\\\
\phi_T(j) &= \mathop{argmax} \limits_{i} (\delta_{T-1}(i) a_{ij}) \\\\
\end{align}
$$
* $E(Q) = \mathop{max} \limits_{i} (\delta_T(i))$.  
 $q_T = \mathop{argmax}(\delta_T(i)), q_T = \phi_{T+1}(q_{T+1})$

## 问题三: 训练
给定$O=O_1, O_2, \cdots, O_T$, 选择$\lambda = \\{ \Pi, A, b\\}$, 使得$P(O | \lambda)最大$
$$
定义: \alpha_t(i) = P(O_1, O_2, O_3, \cdots, O_t, q_t = S_i | \lambda) \\\\
定义: \beta_t(i) = P(O_{t+1}, O_{t+2}, \cdots, O_T | q_t = S_i, \lambda) \\\\
\beta_T(i) = 1,  i = 1, 2, \cdots, P \\\\
\beta_t(i) = \sum_{j=1}^P a_{ij} \beta_{t+1}(j) b_j(O_{t+1})
$$
* 随机化 $\lambda = \\{ \Pi, A, b\\}$
* 计算 $\xi(i,j) = P(q_t = S_i, q_{t+1} = S_j | O, \lambda)$
$$
\xi(i,j) = \alpha_t(i)a_{ij}b_j(O_{t+1})\beta_{t+1}(j)
$$

## Reference
* 胡浩基 - 浙江大学机器学习课程 50
* MFCC (Mel-Frequency Cepstral Coefficients)

