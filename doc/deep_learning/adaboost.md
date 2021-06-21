# 特征选择 - AdaBoost
特征选择问题: $X$有$N$个特征值
$$
X = 
\begin{bmatrix}
x_1 \\\\
x_2 \\\\
. \\\\
. \\\\
. \\\\
x_N
\end{bmatrix}
$$
在这$N$个特征值中如何选取$M$个特征值， 使识别率最高.

## AdaBoost 算法流程
数据集$T = \\{ (x_1, y_1), (x_2, y_2), \cdots, （x_N, y_N） \\}$  
二分类问题： $y_i = \\{ -1, 1\\}$  
* 初始化采样权重 $D_1 = (\omega_{11}, \omega_{12}, \cdots, \omega_{1N}), \omega_{1i} = \frac{1}{N}, i = 1 ~ N$

## Reference
* 浙江大学机器学习课程 39 - 胡浩基
