# 支持向量机(Support Vector Machines)

## 定义
（1）训练数据集和标签 $D = \\{(x_1, y_1), (x_2, y_2), \cdots, (x_N, y_N)\\}$, 其中$y \in \\{-1, 1\\}$

（2）线性模型（超平面)$(\omega, b)$: $\omega^Tx + b = 0$

（3）训练集线性可分是指:
$$
D = {(x_i, y_i)}, i =  1 \to N, 存在 （\omega, b)，  使得， 对于任意(x_i, y_i), 下式都成立 \\\\
\begin{cases}
\omega^Tx_i + b \geq 0,  \ if \  y_i = 1 \\\\
\omega^Tx_i + b< 0,  \ if \ y_i = -1
\end{cases}
$$
上式也可以写为$y_i(\omega^Tx_i + b) \geq 0$

## 支持向量 
离划分超平面最近的训练样本， 并且$y_i(\omega^Tx_i + b) \geq 0$成立， 则称这几个训练样本为支持向量.

## 优化问题
样本空间中的任意样本$x$到超平面的距离为$\frac{\vert \omega^Tx + b \vert}{\vert \omega \vert}$. 则取距离超平面最近的两个异类样本， 使得这两个异类样本到超平面的距离之和为：
$$
\gamma = \frac{2}{\vert \omega \vert}
$$
这是由于超平面跟$\omega，b$相对关系决定， 所以可以取值令$\vert \omega^Tx + b \vert = 1$
所以， 支持向量机的优化问题可以写为:
$$
\underset{\omega, b}{max}\frac{2}{\vert \omega \vert} \\\\
s.t. \  y_i(\omega^Tx_i + b) \geq 0, i = 1, 2, \cdots, N
$$
这个跟下式等价:
$$
\underset{\omega, b}{argmin}\frac{1}{2} \Vert \omega \Vert^2 \\\\
s.t. \  y_i(\omega^Tx_i + b) \geq 0, i = 1, 2, \cdots, N
$$
显然， 这是一个凸优化问题， 更具体的说， 这是一个二次规划问题（目标函数是二次的， 约束条件是线性的）

## 线性不可分问题
 如果样本不是线性可分的， 将样本映射到更高的维度空间， 它将有更高的概率是线性可分的. 如果映射到无限维空间， 那么样本线性可分的概率为1.
 
求解线性不可分问题， 优化问题写为:
$$
argmin \frac{1}{2} \Vert \omega \Vert^2 + C\sum_{i=1}^{N}\xi_i\\\\
s.t. \ y_i(\omega^T \phi(x_i) + b) \geq 1 - \xi_i,  \  i = 1, 2, \cdots, N
$$

## 核函数
只要知道一个核函数:
$$
K(x_1, x_2) = \phi(x_1)^T\phi(x_2)
$$
则上面的优化式可解.

$K(x_1, x_2) = \phi(x_1)^T\phi(x_2)$的充要条件是:
$$
\begin{align}
& K(x_1, x_2) = K(x_2, x_1) \ \ \ \ \  & 交换性  \\\\
& 存在C_i, x_i, i = 1, 2, \cdots, N, 有:  \sum_{i=1}^{N}\sum_{i=1}^{N}C_iC_jK(x_i, x_j) \geq 0 & 半正定性
\end{align}
$$

### 常用的核函数
$$
(1)\ 高斯核: \ K(x_1, x_2) = e^{-\frac{\Vert x_1 - x_2 \Vert^2}{2\sigma^2}} \\\\
(2)\ 多项式核: \ K(x_1, x_2) = (x_1^Tx_2 + 1)^d  \\\\
$$


## Reference
* 胡浩基 - 浙江大学机器学习课程6 - 支持向量机
* 机器学习 - 周志华

