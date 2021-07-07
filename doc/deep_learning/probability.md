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
P(\omega_1 | x) = \frac{P(x, \omega_1)}{P(x)} = \frac{P(x | \omega_1)P(\omega_1)}{p(x)} \\\\
P(\omega_2 | x) = \frac{p(x, \omega_2)}{P(x)} = \frac{P(x | \omega_2)P(\omega_2)}{P(x)}
$$
于是， 分类问题可以写为:
$$
若 P(x | \omega_1)P(\omega_1) > P(x | \omega_2)P(\omega_2), 则 x \in \omega_1 \\\\
若 P(x | \omega_1)P(\omega_1) < P(x | \omega_2)P(\omega_2), 则 x \in \omega_2 \\\\
$$

$P(\omega_1) 和 P(\omega_2)$ 是$\omega$的先验概率, $P(\omega_1 | x) 和 P(\omega_2 | x)$是$\omega$在$x$上的后验概率.



## Reference
* 浙江大学机器学习课程 41 - 胡浩基
