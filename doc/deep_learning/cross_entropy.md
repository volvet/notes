## 交叉熵
### 熵
熵是接受到的每条消息所包含的信息的平均量.
$$
H(p) = - \sum_xp(x) \log p(x)
$$
### 交叉熵
$$
H(p, q) = -\sum_xp(x) \log q(x)
$$
### 相对熵
相对熵也称为KL散度， 用于度量两个分布之间的不相似性.
$$
KL(p || q) = -\sum_x p(x) \log \frac{q(x)}{p(x)}
$$
三者的关系:
$$
\begin{align}
H(p, q) &= - \sum_xp(x) \log q(x) \\\\
&= - \sum_xp(x) \log p(x) - \sum_xp(x) \log \frac{q(x)}{p(x)} \\\\
&= H(p) + KL(p, q)
\end{align}
$$



## Reference
* 鲁鹏 - 机器视觉
