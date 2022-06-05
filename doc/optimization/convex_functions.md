# 凸函数

## 基本性质
凸函数$f: R^n \rightarrow R$是凸的， 如果$domf$是凸集， 且对于任意$x, y \in domf$和任意$0 \leq \theta \leq 1$, 有:
$$
f(\theta x + (1-\theta)y) \leq \theta f(x) + (1 - \theta)f(y)
$$

### 凸函数的扩展
如果$f$是凸函数， 我们定义它的扩展至延伸$\tilde f : R^n \rightarrow R \cup \infty$:  
$$
\tilde f(x) = \begin{cases}
f(x), x \in domf \\\\
\infty, x \notin domf \\\\
\end{cases}
$$

### 示性函数
设$C \subset R^n$是一个凸集， 考虑函数$I(C), 对于所有x \in C, f(x) = 0$, 对$I(C)$扩展：
$$
\tilde I_C(x) = \begin{cases}
0, x \in C \\\\
\infty, x \notin C \\\\
\end{cases}
$$
