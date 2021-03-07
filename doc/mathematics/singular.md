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
对于方阵$A$， 若存在一个非零向量$x$和标量$\lambda$, 使得：
$$
Ax = \lambda x
$$
则称$\lambda$是方阵$A$的特征值(eigenvalue), $x$是$A$的特征向量.

假设$n$阶方阵$A$有$n$个线性无关的特征向量$x_1, x_2, ..., x_n$, 对应的特征值$\lambda_1, \lambda_2, ..., \lambda_n$, 特征向量是规范化的， 即对于任意$1 \leq i \leq n, \lVert x_i \rVert = 1$, 则我们可以将特征向量张成方阵， 记为$E$, 
$$
E = [x_1, x_2, ..., x_n]

$$
显然, $E^TE = I$, 即$E$为酉矩阵
$$
\Lambda = diag(\lambda_1, \lambda_2, ..., \lambda_n)
$$


## Reference
1. 模式识别  吴建鑫
2. 矩阵分析 姜志侠等
