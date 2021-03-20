
## 角度与不等式
如果$x^Ty = 0$, 则我们称这两个向量是正交的.
令向量$x$和$y$之间的夹角为$\theta (0 \leq \theta \leq \pi)$, 则:
$$
x^Ty = \Vert x \Vert \Vert y \Vert cos \theta
$$

$$
\theta = arccos(\frac{x^Ty}{\Vert x \Vert \Vert y \Vert})
$$

于是:
$$x^Ty \leq \vert x^Ty \vert \leq \Vert x \Vert \Vert y \Vert
$$

## 向量投影
记 $x_y$ 为向量$x$到$y$的投影. 则：
$$
\Vert x_y \Vert = \Vert x \Vert  cos \theta = \Vert x \Vert \frac{x^Ty}{\Vert x \Vert \Vert y \Vert}
$$
