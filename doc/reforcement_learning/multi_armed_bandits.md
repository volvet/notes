# 多臂赌博机

##  Gradient Bandit Algorithm
令$H_t(a)$是于Action$a$被选中的概率相关的函数， 那么我们可以定义$a$被选中的概率为:
$$
Pr\\\{A_t=a\\\} = \frac{e^{H_t(a)}}{\sum_{b=1}^ke^{H_t(b)}} = \pi_t(a)
$$
$H_t(a)$的计算:  
$$
H_1(a) = 0 \\\\
H_{t+1}(A_t) = H_t(A_t) + \alpha (R_t - \overline R_t)(1 - \pi_t(A_t)) \\\\
H_{t+1}(a_t) = h_t(a) - \alpha (R_t - \overline R_t)\pi_t(a_t),  for\ all\ a \neq A_t
$$
其中， $\overline R_t$是包括$t$在那的所有$R$的平均.

### 算法的数学推导
$$
\mathbb{E}(R_t) = \sum_x \pi_t(x)q_{\*}(x) \\\\
H_{t+1}(a) = H_t(a) + \frac{\partial \mathbb{E}}{\partial H_t(a)} \\\\
\begin{align}
\frac{\partial \mathbb{E}(R_t}{\partial H_t(a)} &= \frac{\partial \sum_x\pi_t(x)q_{\*}(x)}{\partial H_t(a)}
\end{align}
$$

## Reference
* Reforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto
