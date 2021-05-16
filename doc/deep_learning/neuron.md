## 神经元的数学模型
$$
y_k = \phi(\sum_{i=1}^{M}\omega_{ki}x_i + b_k) = \phi(W_k^TX_k + b)
$$
$\phi$为激活函数， $b$为偏置(偏移)， $W$为权重向量， $(X_k，y_k)$为输入输出对.

### 激活函数
* Sigmoid 函数
$$
\sigma(x) = \frac{1}{1 + e^{-x}} \\\\
$$
对 $\sigma(x)$求导， 可得:
$$
\sigma^{\prime}(x) = \frac{e^{-x})}{(1+e^{-x})^2} = \sigma(x)(1 - \sigma(x))
$$

## 后向传播算法(Back Propogation)
