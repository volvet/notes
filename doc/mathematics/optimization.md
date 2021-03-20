# 优化
给一个代价函数$f(x): D \rightarrow R$, 数学优化的目标是在域$D$中找到$x^\*$, 使得对于任意$x \in D$, 都有$f(x^\*) \leq f(x)$.
通常记为:
$$
\underset{x \in D}{min}f(x)
$$
使得$f(x)$最小的解$x^\*$是$f$的一个最小值解， 记为:
$$
x^\* = \underset{x \in D}{argmin} f(x)
$$

## 凸优化
在优化领域， 有些函数具有比其他函数更好的特性， 例如凸函数， 凸函数的任意局部极小也是全局极小. 
若$S \subseteq R^d$, 并且对于任意$x \in R^d, y \in R^d$, 以及$0 \leq \lambda \leq 1$, $\lambda x + (1 - \lambda) y \in S$总是成立， 则$S$是一个凸集(convex set).

若函数$f(x)$其域为凸集$S$, 对于$S$中任意$x, y$,以及$0 \leq \lambda \leq 1$, 都有:
$$
f(\lambda x + (1 - \lambda) y) \leq \lambda f(x) + (1 - \lambda)f(y)
$$
则称$f(x)$是凸函数.

## 约束优化
