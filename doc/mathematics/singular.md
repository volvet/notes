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
对于方阵$A$， 若存在一个非零向量$x$和标量$\lamda$, 使得：
$$
Ax = \lamda x
$$
