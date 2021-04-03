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
Y = AX + b
$$
$X是一个N阶列向量, A是M \times N的矩阵, b 是M阶列向量, 显然Y是M阶列向量, 其中 M < N$

主成分分析可以看成是一个1层的， 有$M$个神经元的神经网络. 其本质是寻找使方差最大的方向， 并在该方向上投影.

改写上式
$$
Y = A(X - \overline X)
$$



## Reference
浙江大学机器学习课程38 - 特征提取
