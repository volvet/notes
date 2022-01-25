# 生成模型

## PixelCNN/PixelRNN

## VAE

### KL距离(Kullback-Leibler Divergence)
KL距离的定义:
$$
KL(P || Q) = \sum_{x \in X} P(x) \ln \frac{P(x)}{Q(x)}
$$

正态分布:
$$
f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
$$
E(X) = \mu \\\\
D(X) = \sigma^2 \\\\
E(X^2) = E(X) + D(X) = \mu + \sigma^2
$$

正态分布 $N(\mu, \sigma)$与标准正态分布$N(0, 1)$的KL距离为:
$$
\begin{align}
KL(N(\mu, \sigma) || N(0, 1)) &= \sum_{x \in X} \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \ln \frac{1/\sqrt{2\pi \sigma^2}{} \\\\
\end{align}
$$


## GAN

## Reference
* 北邮 机器视觉 - 鲁鹏
