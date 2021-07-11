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

## Reference
* 浙江大学机器学习课程 41 - 胡浩基
