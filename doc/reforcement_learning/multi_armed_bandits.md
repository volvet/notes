# 多臂赌博机

##  Gradient Bandit Algorithm
令$H_t(a)$是于Action$a$被选中的概率相关的函数， 那么我们可以定义$a$被选中的概率为:
$$
Pr\\\{A_t=a\\\} \frac{e^{H_t(a)}}{\sum_{b=1}^ke^{H_t(b)}} = \pi_t(a)
$$

## Reference
* Reforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto
