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

###  一维高斯概率密度估计
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
\frac{1}{\sigma_1^2} & 0 & \cdots & 0 \\\\
0 & \frac{1}{\sigma_2^2} & \cdots & 0 \\\\
. & . & \cdots & . \\\\
0 & 0 & \cdots & \frac{1}{\sigma_d^2} \\\\
\end{bmatrix}
[x_1 - \mu_1, \cdots, x_d - \mu_d]^T \\\\
&= (X - \mu)^T \Sigma^{-1} (X - \mu) \\\\
\end{align}
$$
因为$X$各个维度独立， 所以$\Sigma$是$X$的协方差矩阵. 于是:
$$
f(x) = \frac{1}{\sqrt{(2\pi)^d |\Sigma|}}e^{-\frac{1}{2}(X - \mu)^T\Sigma^{-1}(X - \mu)}
$$

### 多维高斯概率密度估计(极大似然法)
已知$X_i, i = 1, 2, \cdots, N$
令 $P(X|C) = \frac{1}{\sqrt{(2\pi)^d |\Sigma|}}e^{-\frac{1}{2}(X - \mu)^T\Sigma^{-1}(X - \mu)}$, 估计$\Sigma, \mu$  
构建目标函数$E(\mu, \Sigma) = \sum_{i=1}^{N}ln(P(X_i|C)）$
假设所有$X_i, i = 1, 2, \cdots, N$是独立同分布的.  问题就是要求$\mu, \Sigma$使得$X_i$的概率最大.
$$
E(\mu, \Sigma) = -\frac{Nd}{2}ln(2\pi) - \frac{N}{2}ln(|\Sigma|) - \frac{1}{2}\sum_{i=1}^N(X_i - \mu)^T\Sigma^{-1}(X_i - \mu)
$$
对$\mu$求导
$$
\frac{\partial E}{\partial \mu} = 0 \\\\
\sum_{i=1}^{N}(X_i - \mu) = 0 \\\\
\mu = \frac{1}{N}\sum_{i=1}^{N}X_i
$$
对$\Sigma^{-1}$求导
$$
\frac{\partial E}{\partial \Sigma^{-1}} = 0 \\\\
\frac{N}{2}\Sigma^T - \frac{1}{2}\sum_{i=1}^{N}(X_i - \mu)(X_i - \mu)^T = 0 \\\\
\Sigma^T = \frac{1}{N}\sum_{i=1}^{N}(X_i - \mu)(X_i - \mu)^T \\\\
\Sigma = \Sigma^T = \frac{1}{N}\sum_{i=1}^{N}(X_i - \mu)(X_i - \mu)^T \\\\
$$

## 混合高斯模型(Gaussian Mixture Model)
$$
p(x) = \sum_{k=1}^{K}\pi_{k}N(x|\mu_k, \Sigma_k)
$$
其中：
$$
N(x|\mu_k, \Sigma_k) = \frac{1}{\sqrt{(2\pi)^d|\Sigma_k|}}e^{-\frac{1}{2}(x - \mu_k)^T\Sigma_{k}^{-1}(x - \mu_k)} \\\\
\sum_{k=1}^{K}\pi_k = 1
$$
使用极大似然法估计混合高斯模型的概率密度：
$$
输入: x_i, i = 1, 2, \cdots, N \\\\
最小化: E(\pi_k, \mu_k, \Sigma_k | k = 1, 2, \cdots, N) \\\\
= - \sum_{k=1}^Klog(p(x_k))
$$
这是一个非凸优化问题， 无法求的全局最优解, 只能求求解局部最优.  可以使用梯度下降， 启发式方法（基因算法/退火算法）, EM算法来求解.

## 混合高斯模型EM算法(Expectation-Maximization)
* 随机化$(\pi_k, \mu_k, \Sigma_k), k=1, 2, \cdots, K$
* E-step: ($\gamma_{nk}$是第$n$歌样本落在第$k$个高斯的概率)
$$
\gamma_{nk} = \frac{\pi_kN(x_n|\mu_k, \Sigma_k)}{\sum_{k=1}^{K}\pi_kN(x_n |\mu_k, \Sigma_k)}, n=1,2,\cdots,N, k=1,2,\cdots,K
$$
* M-step:
$$
N_k = \sum_{n=1}^{N}\gamma_{nk}
$$
$N_k$是所有$N$个样本中有多少个属于第$k$个高斯, 可知: $\sum_{k=1}^{K}N_k = N$.  
$$
\begin{cases}
\pi_k^{new} = \frac{N_k}{N} \\\\
\mu_k^{new} = \frac{1}{N_k}\sum_{n=1}^{N}\gamma_{nk}x_n \\\\
\Sigma_k^{new} = \frac{1}{N_k}\sum_{n=1}^{N}\gamma_{nk}(x_n - \mu_k^{new})(x_n - \mu_k^{new})^T \\\\
\end{cases}
$$
* 回到 E-step, 到收敛为止

## K-均值聚类(K-means Clustering)

## EM算法的一般形式
输入样本$x_i, i=1, 2, \cdots, N$  
定义 $z_i, i=1, 2, \cdots, N$ 为隐含变量  
目的： 最大化$E(\theta) = \sum_{i=1}^N log(p(x_i | \theta)) = \sum_{i-1}^N log(\sum){z_i}p(x_i, z_i | \theta)$ (最大似然估计)

## Reference
* 浙江大学机器学习课程 41 - 胡浩基
