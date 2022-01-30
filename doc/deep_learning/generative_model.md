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
E(X^2) = E(X)^2 + D(X) = \mu^2 + \sigma^2
$$

正态分布 $N(\mu, \sigma)$与标准正态分布$N(0, 1)$的KL距离为:
$$
\begin{align}
KL(N(\mu, \sigma) || N(0, 1)) &= \sum_{x \in X} \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \ln \frac{1 / \sqrt{2\pi \sigma^2} e^{-\frac{(x-\mu)^2}{2\sigma^2}} }{ 1 / \sqrt{2\pi} e^{ -\frac{x^2}{2} } } \\\\
&=  \frac{1}{2}\sum_{x \in X} \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} (-\ln \sigma^2 + x^2 - (x-\mu)^2 / \sigma^2) \\\\
&= \frac{1}{2} (-\ln \sigma^2 + \mu^2 + \sigma^2 - 1)
\end{align}
$$

### 采样:  
$$
标准正态分布x： N(0, 1) \\\\
令 z = \mu + \sigma x, 则 z： N(\mu, \sigma^2)
$$
所以正态分布的采样可以根据标准正态分布采样的平移和拉伸来实现. 


## GAN

## Reference
* 北邮 机器视觉 - 鲁鹏
