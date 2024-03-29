# 凸函数

## 基本性质
凸函数$f: R^n \rightarrow R$是凸的， 如果$domf$是凸集， 且对于任意$x, y \in domf$和任意$0 \leq \theta \leq 1$, 有:
$$
f(\theta x + (1-\theta)y) \leq \theta f(x) + (1 - \theta)f(y)
$$

另一个定义:
$$
任意 x \in domf, 任意一个方向 v \\\\
g(t) = f(x+tv) 为凸， x+tv \in domf
$$

### 凸函数的扩展
如果$f$是凸函数， 我们定义它的扩展至延伸$\tilde f : R^n \rightarrow R \cup \infty$:  
$$
\tilde f(x) = \begin{cases}
f(x), \  x \in domf \\\\
\infty, \  x \notin domf \\\\
\end{cases}
$$

### 示性函数
设$C \subseteq R^n$是一个凸集， 考虑函数$I(C), 对于所有x \in C, f(x) = 0$, 对$I(C)$扩展：
$$
\tilde I_C(x) = \begin{cases}
0, \  x \in C \\\\
\infty, \  x \notin C \\\\
\end{cases}
$$

### 一阶条件
假设函数$f$可微， 则函数$f$是凸函数的充要条件是对于任意$x, y \in domf$, 下式成立:
$$
f(y) \geq f(x) + \nabla f(x)^T(y-x)
$$
**证明**:  
先考虑n=1的情况:
$$
假设f是凸函数， 且x, y \in domf, domf是凸集, 对于任意0 \lt t \leq 1, 我们有 \\\\
x+t(y-x) \in domf, 由于函数的凸性， 可得: f(x+t(y-x)) \leq (1-t)f(x) + tf(y) \\\\
f(y) \geq f(x) + \frac{f(x+t(y-x)-f(x)}{t} \\\\
令 t \rightarrow 0, 则 f(y) \leq f(x) + f^\prime(x)(y-x)
$$
再来证明充分性:
$$
domf 内任意x, y, x \neq y, 0 \leq \theta \leq 1, z = \theta x + (1 - \theta)y \\\\
f(x) \geq f(z) + f^\prime(z)(x-z),  f(y) \geq f(z) + f^\prime(z)(y-z) \\\\
\theta f(x) + (1-\theta)f(y) \geq f(z), 说明函数f是凸函数
$$
现在来证明一般情况:
$$
设f为凸函数， x, y \in domf \\\\
g(t) = f(ty + (1-t)x) = f(x + t(y-x)) \\\\
g^\prime(t) = \nabla f(ty + (1-t)x)^T(y-x) \\\\
g(t)也是凸函数， 所以: g(t_1) \geq g(t_2) + g^\prime(t_2)(t_1 - t_2) \\\\
令t_1=1, t_2=0, 则: f(y) \geq f(x) + \nabla f(x)^T(y-x)
$$
证明充分性:
$$
存在x,y \in domf \\\\
ty + (1-t)x \in domf, \tilde ty + (1-\tilde t)x \in domf \\\\
则: f(ty + (1-t)x) \geq f(\tilde ty + (1-\tilde t)x) + \nabla f(\tilde ty + (1-\tilde t)x)^T(ty+(1-t)x-\tilde ty -(1-\tilde t)x) \\\\
可以简化为: f(ty + (1-t)x) \geq f(\tilde ty + (1-\tilde t)x) + \nabla f(\tilde ty + (1-\tilde t)x)^T(y-x)(t-\tilde t) \\\\
即: g(t) \geq g(\tilde t) + g^\prime(\tilde t)(t-\tilde t) \\\\
g 是凸函数， 则f是凸函数.
$$

### 二阶条件
若$f$二阶可微， 则$f$为凸函数的充要条件是:
$$
domf 为凸集， \nabla^2f(x) \succeq 0, x \in domf
$$
$ \nabla^2f(x) $ 是Hessian矩阵.  
例子: 二次函数 $f:R^n \rightarrow R, domf = R^n$:
$$
f(x) = \frac{1}{2}x^TPx + q^Tx = r \\\\
P \in S^n,  q \in R^n, r \in R
$$

**例子**  
* 仿射函数: $f(x) = Ax + b, \nabla^2f(x) = 0$  
* 指数函数: $f(x) = e^{ax}, \nabla^2f(x) = a^2e^{ax} \geq 0$  
* 幂函数: $f(x) = x^a, x \in R_{++}, a \geq 1 或者 a \leq 0时， f(x)是凸函数， 0 \leq x \leq 1时， f(x)是凹函数$  
* 绝对值的幂函数: $f(x) = \vert x \vert^p, x \in R, p \geq 1时， f(x)是凸函数$  
* 对数函数: $f(x) = \log(x)$, 是凹函数. $x \in R_{++}$  
* 负墒：$f(x) = x\log(x), x \in R_{++}$ 是严格凸函数.  
* 范数: $R^n$空间的任意范数均为凸函数.  
* 最大值函数: $f(x) = max \\{x_1, x_2, \cdots, x_n \\}$是凸函数.
* Log-sum-up: $f(x) = \log (e^{x_1} + \cdots + e^{x_n}), x \in R^n$ 是凸函数.
* 几何平均: $f(x)=(x_1 \cdots x_n)^{\frac{1}{n}}, x \in R_{++}^n$
* 对数行列式: $f(x) = \log detX$

## Reference
* 凌青 - 中科大公开课 最优化理论
* Stephen Boyd - Connvex Optimization
