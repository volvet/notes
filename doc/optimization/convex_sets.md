# Convex Sets
## 仿射集(Affine Sets)
$x_1$, $x_2$为$R^n$空间中两个不同的点， 则
$$
y = \theta x_1 + (1 - \theta) x_2,  \theta \in R
$$
是一个穿过点$x_1$和$x_2$的直线.  
仿射集： 一个集合$C$是仿射集， 若存在$x_1, x_2 \in C$, 则连接$x_1与x_2$的直线也在集合内.  
设: $x_1, x_2, \cdots, x_k \in C$, $\theta_1, \cdots, \theta_k \in R, \theta_1 + \cdots + \theta_k = 1$.   
那么仿射组合 $\theta_1 x_1 + \dots + \theta_k x_k \in C$   
如果$C$是一个仿射集， 并且$x_0 \in C$, 则集合
$$
V = C - x_0 = \\{x - x_0 | x \in C \\}
$$
是一个子空间.

## 线性空间
设$V$是一个非空集合， $F$为一数域， 如果存在一种规则叫做$V$的加法运算， 对于$V$中任意两个元素$\alpha, \beta$, 总有一个确定的元素$\gamma$与之对应， $\gamma$称为$\alpha, \beta$的和, 计为$\gamma = \alpha + \beta$, 另有一种规则， 叫做$V$对于$F$的数乘运算， 对于$F$中的任意数$k$以及$V$中任意元素$\alpha$， $V$中总有一个确定的元素$\sigma$与之对应，叫做$k$与$\alpha$的数乘， 计为$\sigma = k\alpha$, 而且以上两种运算还有如下性质:  
$$
\begin{align}
\alpha + \beta = \beta + \alpha \\\\
(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma) \\\\
V中存在零元素， 对于任意 \alpha \in V, 恒有 \alpha + 0 = \alpha \\\\
\end{align}
$$
则称$V$为数域$F$上的一个线性空间， 也称为向量空间.
## Refrences
* 凌青 - 中科大公开课 最优化理论
* Stephen Boyd - Connvex Optimization
