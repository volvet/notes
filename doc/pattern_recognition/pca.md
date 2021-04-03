# 主成分分析(Principal Component Aanlysis)

有一组向量 $[x_1, x_2, \cdots, x_p]$, 其中:
$x_i = [ x_{i1}, x_{i2}, \cdots, x_{iN} ]$, 
每一个$x_i$ 属于 $C_1$或者$C_2$, 
这是一个二分类问题.
如果$N$个维度有冗余,  如何从$N$个维度中选取$M$个维度， 其中$M < N$, 使得识别率最高. 这是特征选择问题(Feature Selection）

向量$x_i$的维度为$N$, 构造$M$个函数, $[f_1(x_i), f_2(x_i), \cdots, f_M(x_i)]$, 这是特征提取问题(Feature Extraction)

## 主成分分析
构造一个$A, b$, 使得:
$$
y = Ax + b
$$
$x是一个N阶列向量, A是M \times N的矩阵, b是M阶列向量, 显然y是M阶列向量, 其中 M < N$

主成分分析可以看成是一个1层的， 有$M$个神经元的神经网络. 其本质是寻找使方差最大的方向， 并在该方向上投影.

改写上式
$$
y = A(x - \overline X）
$$

$$
\overline X = E(X), 为X的均值.
$$
令$A$的行向量为$a_i, i = 1, 2, \cdots, M$, 则$A$可以写为:
$$
A = 
\begin{pmatrix}
a_1\\\\
a_2\\\\
.\\\\
.\\\\
.\\\\
a_M\\\\
\end{pmatrix}
$$
则$y$可以写为:
$$
\begin{pmatrix}
a_1(x-\overline x)\\\\
a_2(x-\overline x)\\\\
.\\\\
.\\\\
.\\\\
a_M(x-\overline x)\\\\
\end{pmatrix}
$$
若训练样本的个数为$P$.  $X = [x_1, x_2, \cdots, x_P]$, 则$Y = [y_1, y_2, \cdots, y_P]$.
$$
y_i = 
\begin{pmatrix}
a_1(x_i-\overline x)\\\\
a_2(x_i-\overline x)\\\\
.\\\\
.\\\\
.\\\\
a_M(x_i-\overline x)\\\\
\end{pmatrix} = 
\begin{pmatrix}
y_{i1}\\\\
y_{i2}\\\\
.\\\\
.\\\\
.\\\\
y_{iM}\\\\
\end{pmatrix}
$$

所以， 主成分分析的目标就是使$Y=[y_1, y_2, \cdots, y_P]$的方差最大。写为:
$$
最大化: \sum_{i=1}^P(y_{i1} - \overline y_{i1})^2
$$

$$
\overline y_{i1} = \frac{1}{P} \sum_{i=1}^P y_{i1} \\\\
= \frac{1}{P}\sum_{i=1}^P a_1(x_i - \overline x) = \frac{a_1}{P}(\sum_{i=1}^{P}x_i - P \overline x) = 0
$$

于是, 最大化$\sum_{i=1}^P(y_{i1} - \overline y_{i1})^2$ 就可以写为:
$$
最大化: \sum_{i=1}^P(y_{i1})^2 = \sum_{i=1}^{P}[a_1(x_i - \overline x)]^2  = \sum_{i=1}^{P}[a_1(x_i - \overline x)] [a_1(x_i - \overline x)]^T \\\\
= \sum_{i=1}^{P}a_1[(x_i - \overline x)(x_i - \overline x)^T]a_1^T \\\\
= a_1[\sum_{i=1}^{P}(x_i - \overline x)(x_i - \overline x)^T]a_1^T
$$
显然, $\sum_{i=1}^{P}(x_i - \overline x)(x_i - \overline x)^T$是一个$N \times N$矩阵, 而且是协方差矩阵（Convariance Matrix）. 记为$\Sigma$, 于是， 上式就简写为:
$$
最大化: a_1 \Sigma a_1^T
$$
因为$a_1$的幅值不影响对这个优化问题的求解，  于是可以限定$a_1a_1^T = \Vert a_1 \Vert ^2 = 1$,  于是这个优化问题可以写为:
$$
argmax(a_1 \Sigma a_1^T) \\\\
s.t.  \  \Vert a_1 \Vert ^2 = 1
$$
使用拉格朗日乘子法来求这个优化问题:
$$
E(a_1) = a_1 \Sigma a_1^T - \lambda (a_1 a_1^T - 1) \\\\
\frac{\partial E}{\partial a_1} = (\Sigma a_1^T - \lambda a_1^T)^T = 0
$$
所以:
$$
\Sigma a_1^T = \lambda a_1^T
$$
这个式子很熟悉， $a_1^T$是$\Sigma$的特征向量， $\lambda$是$\Sigma$的特征值.
$$
argmax(a_1 \Sigma a_1^T) = argmax(a_1 \lambda a_1^T) = \lambda
$$
所以$\lambda$是$\Sigma$的最大特征值, 且满足$a_1^a_1^T = 1$


## Reference
浙江大学机器学习课程38 - 特征提取
