# Fisher线性判别
主成分分析是无监督的数据线性降维方法， 当有监督的情形下， Fisher线性判别分析（Fisher Linear Discriminative Analysis）则是一种经典的数据降维方法. 为简单起见， 我们先来看一个二分类的数据降维.

## 二分类问题
训练样本$(x_i, y_i)$, 训练集$X$, $y_i \in \\{1, 2\\}$, $x_i \in \mathbb{R}^N$, $i = 1, 2, \cdots, P$
