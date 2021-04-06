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


## Reference
* 胡浩基 - 浙江大学机器学习课程6 - 支持向量机
* 模式识别 by 吴建鑫

