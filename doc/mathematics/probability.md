
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
