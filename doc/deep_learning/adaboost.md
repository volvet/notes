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
* 初始化采样权重 $D_1 = (\omega_{11}, \omega_{12}, \cdots, \omega_{1N}), \omega_{1i} = \frac{1}{N}, i = 1, 2, \cdots, N$
* 对$m = 1, 2, \cdots, M$, $M$为弱分类器的个数， 用$D_m$采集$N$个训练样本， 在训练样本上获得弱分类器
$$
G_m(x) = \begin{cases} 1 \\\\ 
-1
\end{cases}
$$
* 计算加权错误率, $\alpha_m$为分类器$G_m$的权重
$$
e_m = P(G_m(x_i) \neq y_i) = \sum_{i=1}^{N}\omega_iI(G_m(x_i) \neq y_i) \\\\
\alpha_m = \frac{1}{2} \log \frac{1 - e_m}{e_m}
$$
* 更新权值分布
$$
D_{m+1} = (\omega_{m+1, 1}, \omega_{m+1, 2}, \cdots, \omega_{m+1, N}) \\\\
\omega_{m+1, i} = \frac{\omega_{m, i}}{z_m} e^{-\alpha_my_iG_m(x_i)} \\\\ 
z_m = \sum_{i=1}^{N}\omega_{m, i} e^{-\alpha_my_iG_m(x_i)}
$$
* 回到step 2, 循环 $m$次
* 最终识别器为$G(x)$
$$
f(x) = \sum_{m=1}^{M}\alpha_mG_m(x) \\\\
g(x) = \mathop{sign}(f(x))
$$

## AdaBoost 定理
随着$M$增加， AdaBoost最终的分类器$G(x)$在训练集上的错误率将会越来越小.

## Reference
* 浙江大学机器学习课程 39 - 胡浩基
