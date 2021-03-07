# 矩阵奇异值分解

## 1. H-矩阵， 酉矩阵
对于复矩阵
$$
A = [a_{ij}] _ {m \times n}
$$
定义其共轭矩阵为 
$$
\overline A = [\overline a_{ij}] _ {m \times n}
$$
记矩阵$A$的共轭转置矩阵为$A^H$, 即$A^H = \overline {A^T}$.

若方阵$A$满足$A^H = A$, 则称$A$为**Hermite矩阵**， 简称**H-矩阵**.

若$n$阶复矩阵$A$满足$A^HA=AA^H$, 则称$A$是一个**酉矩阵**或者**U-矩阵**.

## 2. 特征值分解
对于实方阵$A$， 若存在一个非零向量$x$和标量$\lambda$, 使得：
$$
Ax = \lambda x
$$
则称$\lambda$是方阵$A$的特征值(eigenvalue), $x$是$A$的特征向量.

假设$n$阶方阵$A$有$n$个线性无关的特征向量$x_1, x_2, ..., x_n$, 对应的特征值$\lambda_1, \lambda_2, ..., \lambda_n$, 特征向量是规范化的， 即对于任意$1 \leq i \leq n, \lVert x_i \rVert = 1$, 则我们可以将特征向量张成方阵， 记为$E$, 
$$
E = [x_1, x_2, ..., x_n]
$$

显然, $E^TE = I, E^T = E^{-1}$, 即$E$为酉矩阵
令：
$$
\Lambda = diag(\lambda_1, \lambda_2, ..., \lambda_n)
$$
若$A$为实对称阵， 即$A = A^T$, 则:

$$
(AE)^T = \Lambda E^T
$$

$$
E^TA^T = \Lambda E^T
$$

$$
A = E \Lambda E^T
$$

此即方阵的特征值分解.

## 3. 奇异值分解
任何矩阵$A_{m \times n}$都可以表示为两个酉矩阵中间夹着一个奇异值矩阵的连乘， 即:
$$
A = U \Sigma V^T
$$

其中， $U$是一个$m \times m$的矩阵， $\Sigma$是一个$m \times n$的矩阵， $V$是一个$n times n$的矩阵.

$AA^T$是一个$m \times m$的矩阵， 则可以求$AA^T$的m个特征向量, $AA^T \mu_i = \lambda_i \mu_i, 1 \leq i \leq m$,

同理， $A^TA$是一个$n \times n$的矩阵， 则可以求其特征向量为： $A^TA v_i = \lambda_i v_i, 1 \leq i \leq n$

$AA^T$的特征向量可以张成矩阵$U$, $A^TA$的特征向量可以张成矩阵$V$, 下面来求奇异值矩阵$\Sigma$
## Reference
1. 模式识别  吴建鑫
2. 矩阵分析 姜志侠等
