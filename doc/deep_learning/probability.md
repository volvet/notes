# 概率分类法

## 基本问题
假设有两个分类$\omega_1, \omega_2$, 某样本$x$, 要么$x \in \omega_1$, 要么$x \in \omega_2$, 求 $P(\omega_1 | x)$与$P(\omega_2 | x)$, 并且$P(\omega_1 | x) + P(\omega_2 | x) = 1$  
分类问题：
$$
若 P(\omega_1 | x） > P(\omega_2 | x), 则 x \in \omega_1 \\\\
若 P(\omega_1 | x） < P(\omega_2 | x), 则 x \in \omega_2
$$

由贝叶斯定理， 可得
$$
P(\omega_1 | x) = \frac{P(x, \omega_1)}{P(x)} = \frac{P(x | \omega_1)P(\omega_1)}{P(x)} \\\\
P(\omega_2 | x) = \frac{p(x, \omega_2)}{P(x)} = \frac{P(x | \omega_2)P(\omega_2)}{P(x)}
$$
于是， 分类问题可以写为:
$$
若 P(x | \omega_1)P(\omega_1) > P(x | \omega_2)P(\omega_2), 则 x \in \omega_1 \\\\
若 P(x | \omega_1)P(\omega_1) < P(x | \omega_2)P(\omega_2), 则 x \in \omega_2 \\\\
$$

$P(\omega_1) 和 P(\omega_2)$ 是$\omega$的先验概率, $P(\omega_1 | x) 和 P(\omega_2 | x)$是$x$在$\omega$上的后验概率.  
若不知道先验概率， 则可以假设所有先验概率是一样的， 于是分类问题写为：
$$
若 P(x | \omega_1) > P(x | \omega_2), 则 x \in \omega_1 \\\\
若 P(x | \omega_1) < P(x | \omega_2), 则 x \in \omega_2 \\\\
$$
那么如何估计$P(x | \omega)$, 或者说， 给定一组$\\{x_i\\} \in \omega, x = 1, 2, \cdots, N$, 如何求$P(x | \omega)$, 这是概率密度估计问题
## 朴素贝叶斯分类(Naive Bayesian Classifier)
TODO

## 高斯概率密度估计

###  一维高斯概率密度
假设$x_i, i = 1, 2, \cdots, N \in C$, $x_i$ 是一维的情况:
$$
P(x | C) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}} \\\\
\mu = \frac{1}{N}\sum_{i=1}^N x_i \\\\
\sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2
$$

###  多维高斯概率密度
若$x$是$d$维向量, 即$x = [x_1, x_2, \cdots, x_d]^T$, 各维度的均值和反差分别为$\mu_1, \sigma_1, \cdots, \mu_d, \sigma_d$, 且各个维度是独立同分布（IID）的高斯分布.
则它们的联合概率分布为各自概率密度函数的乘积. 计为:
$$
\begin{align}
f(x) &= \frac{1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}} \cdots \frac{1}{\sqrt{2\pi}\sigma_d}e^{-\frac{(x-\mu_d)^2}{2\sigma_d^2}} \\\\
& = \frac{1}{(\sqrt{2\pi})^d\\sigma_1\sigma_2\cdots\sigma_d}e^{-\frac{1}{2}\sum_{i=1}^d(\frac{x_i-\mu_i}{\sigma_i})^2} \\\\
\end{align}
$$
写成矩阵的形式:
$$
\begin{align}
d^2(x) &= (\frac{x_1 - \mu_1}{\sigma_1})^2 + \cdots + (\frac{x_d - \mu_d}{\sigma_d})^2 \\\\
&= [x_1 - \mu_1, \cdots, x_d - \mu_d]
\begin{bmatrix}
\frac{1}{\sigma_1^2} & 0 & 0 & \cdots \\\\
0 & \frac{1}{\sigma_2^2} & 0 & \cdots \\\\
\cdots \\\\
0 & 0 & 0 & \frac{1}{\sigma_d^2} \\\\
\end{bmatrix}
\end{align}
$$




## Reference
* 浙江大学机器学习课程 41 - 胡浩基
