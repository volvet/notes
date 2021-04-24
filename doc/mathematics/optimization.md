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
除了代价函数$f(x)$之外， 有时候还需要变量$x$满足一些条件, 例如$g(x) = 0$.  这就是约束优化:
$$
min\ f(x)
$$

$$
s.t.\ g(x)=0
$$
这里的$s.t.$ 就是 subject to, 表示约束为.

### 拉格朗日乘子法
拉格朗日乘子法就是解决约束优化的很有用的工具. 该方法定义了一个拉格朗日函数为:
$$
L(x, \lambda) = f(x) - \lambda ^T g(x)
$$

$\lambda ^T = (\lambda_1, \lambda_2, \cdots, \lambda_m)$ 是拉格朗日乘子, $g(x) = (g_1(x), g_2(x), \cdots, g_m(x))$是$m$个约束.
则：
$$
\frac{\partial L}{\partial x} = 0
$$

$$
\frac{\partial L}{\partial \lambda} = 0
$$
是$(x, \lambda)$成为$L(x, \lambda)$的一个驻点的必要条件.

## 源问题与对偶问题
### 原问题(Prime Problem)
$$
\begin{align}
 最小化: & f(\omega) \\\\
 s. t. \ & g_i(\omega) \leq 0, \  i=1, 2, \cdots, K \\\\
& h_i(\omega) = 0, \ i=1, 2, \cdots, M \\\\
\end{align}
$$

### 对偶问题(Dual Problem)
定义： 
$$
\begin{align}
L(\omega, \alpha, \beta) & = f(\omega) + \sum_{i=1}^{K}\alpha_ig_i(\omega) + \sum_{i=1}^{M}\beta_ih_i(\omega) \\\\
& = f(\omega) + \alpha^Tg(\omega) + \beta^Th(\omega) \\\\
\end{align}
$$
对偶问题定义
$$
\begin{align}
& \mathop{argmax}\theta(\alpha, \beta) = \mathop{inf} \limits_{所有 \omega}\\{L(\omega, \alpha, \beta)\\} \\\\
& s.t. \ \alpha \geq 0， (\alpha_i \geq 0, i = 1, \cdots, K)
\end{align}
$$

注: $\inf$ infimum  最大下界

### 原问题与对偶问题的关系
定理： 如果$\omega^\*$是原问题的解， $\alpha^\*， \beta^\*$是对偶问题的解， 则下式成立:
$$
f(\omega^\*) \geq \theta(\alpha^\*, \beta^\*)
$$

## Reference
* 模式识别 by 吴建鑫
* 胡浩基 - 浙江大学机器学习课程 11
