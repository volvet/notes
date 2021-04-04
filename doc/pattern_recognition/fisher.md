# Fisher线性判别
主成分分析是无监督的数据线性降维方法， 当有监督的情形下， Fisher线性判别分析（Fisher Linear Discriminative Analysis）则是一种经典的数据降维方法. 为简单起见， 我们先来看一个二分类的数据降维.

## 二分类问题
训练样本$(x_i, y_i)$, $y_i \in \\{1, 2\\}$, $x_i \in \mathbb{R}^N$, 训练集$X = [(x_1, y_1), (x_2, y_2), \cdots, (x_P, y_P)]$, 令:
$$
X_1 = \\{x_i | 1 \leq i \leq P, y_i = 1 \\} \\\\
X_2 = \\{x_i | 1 \leq i \leq P, y_i = 2 \\} \\\\
$$
若$N_1, N_2$为子集$X_1, X_2$的大小， 则:
$$
\overline x_1 = \frac{1}{N_1}\sum_{x \in X_1}x \\\\
\overline x_2 = \frac{1}{N_2}\sum_{x \in X_2}x \\\\
$$
同主成分分析类似， 协方差矩阵定义为:
$$
C_1 = \frac{1}{N_1}\sum_{x \in X_1}(x - \overline x_1)(x - \overline x_1)^T \\\\
C_2 = \frac{1}{N_2}\sum_{x \in X_2}(x - \overline x_2)(x - \overline x_2)^T \\\\
$$
给定任意投影方向$\omega$, 可以限定$\Vert \omega \\Vert = 1$. 则$X_i$的投影为$X_i^T\omega$,   则这两个类别， 投影的均值为:
$$
\overline x_1^T\omega \\\\
\overline x_2^T\omega \\\\
$$
投影的方差是:
$$
\begin{align}
\sigma_1^2 & = \frac{1}{N_1}\sum_{x \in X_1}(x^T\omega - \overline x_1^T\omega)^2 \\\\
& = \frac{1}{N_1}\sum_{x \in X_1}(\omega^T(x - \overline x_1)(x - \overline x_1)^T\omega \\\\
& = \omega^T(\frac{1}{N_1}\sum_{x \in X_1}(x - \overline x_1)(x - \overline x_1)^T)\omega \\\\
& = \omega^T C_1 \omega \\\\
\end{align}
$$
同理:
$$
\sigma_2^2 = \omega^T C_2 \omega
$$
于是， 标准差为：
$$
\begin{align}
\sigma_1 & = \sqrt{\omega^T C_1 \omega} \\\\
\sigma_2 & = \sqrt{\omega^T C_2 \omega} \\\\
\end{align}
$$
我们希望这两类的均值之差尽量大， 而且相同类尽量聚集到一起， 所以， 优化方程可以写为:
$$
最大化: \frac{\vert \overline x_1^T\omega - \overline x_2^T\omega \vert}{\sigma_1 + \sigma_2} \ 或者 \\\\
最大化: \frac{\vert \overline x_1^T\omega - \overline x_2^T\omega \vert}{\sqrt{\sigma_1^2 + \sigma_2^2}} \\\\
$$

### 优化求解

## 多分类问题

## Reference
* 模式识别 by 吴建鑫
