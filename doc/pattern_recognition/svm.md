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
s.t. y_i(\omega^Tx_i + b) \geq 0, i = 1, 2, \cdots, N
$$


## Reference
* 胡浩基 - 浙江大学机器学习课程6 - 支持向量机
* 模式识别 by 吴建鑫

