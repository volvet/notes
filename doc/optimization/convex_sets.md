# 凸集(Convex Sets)
## 线性空间与线性子空间
设$V$是一个非空集合， $F$为一数域， 如果存在一种规则叫做$V$的加法运算， 对于$V$中任意两个元素$\alpha, \beta$, 总有一个确定的元素$\gamma$与之对应， $\gamma$称为$\alpha, \beta$的和, 计为$\gamma = \alpha + \beta$, 另有一种规则， 叫做$V$对于$F$的数乘运算， 对于$F$中的任意数$k$以及$V$中任意元素$\alpha$， $V$中总有一个确定的元素$\sigma$与之对应，叫做$k$与$\alpha$的数乘， 计为$\sigma = k\alpha$, 而且以上两种运算还有如下性质:  
$$
\begin{align}
& \alpha + \beta = \beta + \alpha \\\\
& (\alpha + \beta) + \gamma = \alpha + (\beta + \gamma) \\\\
& V中存在零元素， 对于任意 \alpha \in V, 恒有 \alpha + 0 = \alpha \\\\
& 对于任意 \alpha \in V, 都存在负元素 \beta, 使得 \alpha + \beta = 0 \\\\
& 1 \alpha = \alpha \\\\
& k(l \alpha) = (kl) \alpha;  k, l \in F \\\\
& (k + l) \alpha = k \alpha + l \alpha \\\\
& k( \alpha + \beta) = k \alpha + k \beta \\\\
\end{align}
$$
则称$V$为数域$F$上的一个线性空间， 也称为向量空间. 

设$V_1$是数域$F$上的线性空间$V$的一个非空子集， 如果它对$V$中的线性运算满足以下条件:
$$
\begin{align}
& \alpha, \beta \in V_1, 则: \alpha + \beta \in V_1 \\\\
& \alpha \in V_1, k \in F, 则: k \alpha \in V_1 \\\\
\end{align}
$$
则称$V_1$为$V$的线性子空间， 也称为子空间.


## 仿射集(Affine Sets)
$x_1$, $x_2$为$R^n$空间中两个不同的点， 则
$$
y = \theta x_1 + (1 - \theta) x_2,  \theta \in R
$$
是一个穿过点$x_1$和$x_2$的直线.  
仿射集： 一个集合$C$是仿射集， 若存在$x_1, x_2 \in C$, 则连接$x_1与x_2$的直线也在集合内.  
设: $x_1, x_2, \cdots, x_k \in C$, $\theta_1, \cdots, \theta_k \in R, \theta_1 + \cdots + \theta_k = 1$.   
那么仿射组合 $\theta_1 x_1 + \dots + \theta_k x_k \in C$。
利用数学归纳法，易得证.

如果$C$是一个仿射集， 并且$x_0 \in C$, 则集合
$$
V = C - x_0 = \\{x - x_0 | x \in C \\}
$$
是一个子空间. 我们定义仿射集的维数为子空间$V$的维数.  


### 线性方程组的解集是仿射集
$$
C = \\{  x | Ax = b \\}, A \in R^{m \times n}, b \in R^m 是一个仿射集 \\\\
与C相关的子空间就是A的零空间
$$

### 任意集合$C$构造最小的仿射集
$$
\mathop{aff} C = \\{ \theta_1 x_1 + ... + \theta_k x_k | x_1, ..., x_k \in C, \theta_1 + ... + \theta_k = 1\\} 
$$
$\mathop{aff}C$称为仿射包.

## 凸集
一个集合$C$是凸集， 当任意两点间的线段仍然在$C$内, 即:
$$
对于任意x_1, x_2 \in C, 且满足 0 \leq \theta \leq 1, 都有: \\\\
\theta x_1 + (1 - \theta)x_2 \in C
$$
凸组合:
$$
C为凸集，
x_1, ..., x_k \in C, \theta_1, ..., \theta_k \in R, 且 \sum_{i=1}^k \theta_i = 1, 且 0 \leq \theta_i \leq 1， 则 \\\\
凸组合 \sum_{i=1}^k \theta_i x_i \in C
$$
凸包: $集合C内所有点的凸组合的集合称为其凸包， 记为: \mathop{conv}C$

## 锥(Cone), 凸锥
对于任意$x \in C$和$\theta \geq 0$, 都有$\theta x \in C$, 则我们称集合$C$是锥或者非负齐次.  
对于任意$x_1, x_2 \in C$和$\theta_1, \theta_2 \geq 0$, 都有$\theta_1 x_1 + \theta_2 x_2 \in C$, 则我们称锥$C$为凸锥.  
凸锥组合:$\theta_1x_1 + ... + \theta_kx_k$
凸锥包:  
集合$C$的凸锥包是$C$中包含元素的所有锥组合, 即:
$$
\\{ \theta_1x_1 + ... + \theta_kx_k | x_i \in C, \theta_i \geq 0  \\}
$$

## 几种重要的凸集
* $R^n$空间
* $R^n$空间的子空间
* 任意直线
* 任意线段
* $\\{ x_0 + \theta v |  \theta \geq 0 \\},  x_0 \in R^n, \theta \in R, v \in R^n$

### 超平面与半空间
$$
\\{ x | a^Tx = b \\},  x, a \in R^n,  b \in R, a \neq 0
$$
$x$的集合称为超平面, 超平面将$R^n$分为两个半空间, 半空间是具有下列形式的点的集合: $\\{ x | a^Tx \leq b\\}, a \neq 0$

### Euclid球
$$
B(x_c, r) = \\{ x | \lVert x - x_c \rVert_2 \leq r \\} = \\{ x | (x-x_c)^T(x-x_c) \leq r^2 \\}
$$

### 椭球
$$
\epsilon(x_c, P) = \\{ x | (x - x_c)^T p^{-1} (x - x_c) \leq 1 \\\} \\\\
x_c \in R^n, P \in S^n_{++}
$$
$S^n_{++}$表示 $n \times n$对称正定矩阵

### 多面体(Polyhedra)
$$
P = \\{ x | a_j^Tx \leq b_j, j=1,...,m, \  b_j^Tx=d_j, j=1,...,p\\}
$$

### 单纯形(Simplex)
$$
R^n空间中选k+1个点, v_0, v_1, ... , v_k, v_1 - v_0, ... , v_k - v_0线性无关 \\\\
则与上述点相关的单纯形为: \\\\
C = \mathop{conv} \\{v_0, ..., v_k  \\} = \\{\theta_0v_0 + ... + \theta_kv_k | \theta \geq 0, 1^T\theta = 1\\}
$$

单纯形一定是多面体的证明:(TODO)



## Refrences
* 凌青 - 中科大公开课 最优化理论
* Stephen Boyd - Connvex Optimization
* 姜志侠等 矩阵分析
