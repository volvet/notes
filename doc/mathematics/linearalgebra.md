
### 角度与不等式
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

### 向量投影
记 $x_y$ 为向量$x$到$y$的投影. 则：
$$
\Vert x_y \Vert = \Vert x \Vert  cos \theta = \Vert x \Vert \frac{x^Ty}{\Vert x \Vert \Vert y \Vert}
$$
投影的方向即$y$的方向， 单位向量是$\frac{y}{\Vert y \Vert}$ 则有:
$$
x_y = \Vert x \Vert \frac{x^Ty}{\Vert x \Vert \Vert y \Vert} \frac{y}{\Vert y \Vert} = \frac{x^Ty}{y^Ty}y
$$

### 超平面的法向量
记超平面为: $\omega^Tx + b = 0$, 则超平面的法向量为$\omega$.  $\omega = [\omega_1, \omega_2, \cdots, \omega_N]$, $x = [x_1, x_2, \cdots, x_N]$ 均为向量.

证明:

在超平面上取任意两点$x_1， x_2$, 则连接两点的向量为 $x_1 - x_2$. (注意: 这边的$x_1$, $x_2$ 都指的是向量.

这两点都满足:
$$
\omega^Tx_1 + b = 0  \\\\
\omega^Tx_2 + b = 0  \\\\
$$
则:
$$
\omega^T(x_1 - x_2) = 0
$$
显然, $\omega$与向量$x_1 - x_2$正交， 所以$\omega$ 是超平面的法向量

### 点到超平面的距离
超平面为$\omega^Tx + b = 0$,    超平面之外点为$x_0$, 点$x_0$到超平面的投影为$x_0'$, 则$d = \vert x_0 - x_0' \vert$为点到超平面的距离.
因为$x_0'$在超平面上, 所以它满足:$\omega^Tx_0' + b = 0$, 
$$
\omega^T(x_0 - x_0') = \vert \omega \vert \vert x_0 - x_0' \vert cos\theta = \vert \omega \vert \vert x_0 - x_0' \vert
$$
$\theta$为两个向量的夹角, 显然投影与向量平行,  所以$\theta = 0 或者 \pi$, $d \geq 0$, 所以:
$$
\vert \omega^T(x_0 - x_0') \vert = \vert \omega \vert d
$$
则:
$$
\begin{align}
d & = \frac{\vert \omega^T(x_0 - x_0') \vert}{\vert \omega \vert} \\\\
& = \frac{\vert \omega^Tx_0 - \omega^Tx_0' \vert}{\vert \omega \vert} \\\\
& = \frac{\vert \omega^Tx_0 + b \vert}{\vert \omega \vert} \\\\
\end{align}
$$
此即点到超平面的距离.

### 向量的导数
定义： 若$\oemga = (\oemga_1, \oemga_2, \cdots, \omega_N)^T, 则:
$$
\frac{\partial f(\oemga}{\partial \omega} = (\frac{\partial f(\omega}{\partial \omega_1}, {\partial f(\omega}{\partial \omega_2}, \cdots, {\partial f(\omega}{\partial \omega_N})^T
$$





