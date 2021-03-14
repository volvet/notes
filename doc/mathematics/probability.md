
# 马尔可夫不等式
如果$x$是一个非负的随机变量， 并且$a > 0$是一个标量， 则:
$$
p(x \geq a) \leq \frac{E[x]}{a}
$$
证明：

（1） 若$x$连续分布，且$x$非负 则
$$
E(x) = \int_{0}^{\infty}xp(x)
$$

因为$a > 0$, 显然
$$
E(x) \geq \int_{a}^{\infty}xp(x) \geq a \int_{a}^{\infty}p(x) = ap(x \geq a)
$$

上式可以写为:
$$
p(x \geq a) \leq \frac{E(x)}{a}
$$ 
 (2) 若$x$离散分布， 证明思路近似于连续分布.

证毕

# 切比雪夫不等式
若随机变量$x$的具有数学期望$E(x) = \mu$, 方差$D(x) = \sigma ^2$, 则对于任意正数$\epsilon$, 不等式：
$$
p（|x-\mu| \geq \epsilon）\leq \frac{\sigma ^2}{\epsilon ^2}
$$
成立

证明：
（1）若$x$连续分布, 则有:
$$
p(|x-\mu| \geq \epsilon) = \int_{|x-\mu| \geq \epsilon} \frac{|x-\mu|^2}{\epsilon ^2}f(x)dx
$$
