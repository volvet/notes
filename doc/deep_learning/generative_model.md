# 生成模型

## PixelCNN/PixelRNN

## VAE

### KL散度(Kullback-Leibler Divergence)
KL散度的定义:
$$
KL(P || Q) = \sum_{x \in X} P(x) \log \frac{P(x)}{Q(x)}
$$

KL散度的非负性(凸函数的性质)
$$
\begin{align}
KL(P || Q) &= \sum P(x) \log \frac{P(x)}{Q(x)} \\\\
&= - \sum P(x) \log \frac{Q(x)}{P(x)} \\\\
& \geq - \log \sum P(x) \frac{Q(x)}{P(x)} = 0 
\end{align}
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

正态分布 $N(\mu, \sigma)$与标准正态分布$N(0, 1)$的KL散度为:
$$
\begin{align}
KL(N(\mu, \sigma^2) || N(0, 1)) &= \sum_{x \in X} \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \log \frac{1 / \sqrt{2\pi \sigma^2} e^{-\frac{(x-\mu)^2}{2\sigma^2}} }{ 1 / \sqrt{2\pi} e^{ -\frac{x^2}{2} } } \\\\
&=  \frac{1}{2}\sum_{x \in X} \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} (-\log \sigma^2 + x^2 - (x-\mu)^2 / \sigma^2) \\\\
&= \frac{1}{2} (-\log \sigma^2 + \mu^2 + \sigma^2 - 1)
\end{align}
$$

### 采样:  
$$
标准正态分布x： N(0, 1) \\\\
令 z = \mu + \sigma x, 则 z： N(\mu, \sigma^2)
$$
所以正态分布的采样可以根据标准正态分布采样的平移和拉伸来实现. 
通常我们训练的时候会直接输出$\mu$和$\ln \sigma^2$, 那采样过程就可以写为:
$$
\mu + e^{\frac{1}{2}(\ln \sigma^2)} \epsilon
$$
$\epsilon$为标准正态分布采样


## GAN
### JS散度(Jensen Shannon Divergence)
$$
M = \frac{1}{2}(P + Q) \\\\
JS(P || Q) = \frac{1}{2}KL(P||M) + \frac{1}{2}KL(Q||M)
$$
JS散度的缺点  
$$
\begin{align}
JS(P || Q) &= \frac{1}{2}(\sum P(x) \log \frac{P(x)}{\frac{1}{2}(P(x) + Q(x))} + \sum Q(x) \log \frac{Q(x)}{\frac{1}{2}(P(x) + Q(x))}) \\\\
&= \frac{1}{2}(\sum P(x) \log \frac{2P(x)}{P(x) + Q(x)} + \sum Q(x) \log \frac{2Q(x)}{P(x) + Q(x)}) \\\\
&= \frac{1}{2}(\sum P(x) (\log \frac{P(x)}{P(x) + Q(x)} + \log 2) + \sum Q(x) (\ln \frac{Q(x)}{P(x) + Q(x)} + \log2)) \\\\
&= \frac{1}{2}(\sum P(x) \log \frac{P(x)}{P(x) + Q(x)} + \sum Q(x) \log \frac{Q(x)}{P(x) + Q(x)}) + \log2 \\\\
\end{align}
$$
可见： 若$P(x)$与$Q(x)$无重叠区， $JSD(P || Q) = \log2$

### DCGAN
* 使用卷积层代替池化层
* 去除全连接层
* 使用批归一化
* 使用恰当的激活函数： 生成网络使用ReLU, 输出使用Tanh, 判别使用LeaklyReLU
### LSGAN
### WGAN
### OptionGAN

* CGAN/SGAN/ACGAN/InfoGAN

## Reference
* 北邮 机器视觉 - 鲁鹏
