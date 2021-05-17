## 神经元的数学模型
$$
y_k = \phi(\sum_{i=1}^{M}\omega_{ki}x_i + b_k) = \phi(W_k^TX_k + b)
$$
$\phi$为激活函数， $b$为偏置(偏移)， $W$为权重向量， $(X_k，y_k)$为输入输出对.

### 常用激活函数
* Sigmoid 函数
$$
\phi(x) = \frac{1}{1 + e^{-x}} \\\\
$$
对Sigmoid求导， 可得:
$$
\phi^{\prime}(x) = \frac{e^{-x})}{(1+e^{-x})^2} = \phi(x)(1 - \phi(x))
$$

* Tanh 函数
$$
\phi(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$
对Tanh求导， 可得:
$$
\phi^{\prime}(x) = \frac{(e^x + e^{-x})^2 - (e^x - e^{-x})^2}{(e^x + e^{-x})^2} = 1 - \phi(x)^2
$$

* ReLU 函数
$$
\phi(x) = 
\begin{cases}
x, & x \geq 0 \\\\
0, & x < 0 \\\\
\end{cases}
$$
对ReLU函数求导, 可得:
$$
\phi^{\prime}(x) =
\begin{cases}
1, & x \geq 0 \\\\
0, & x < 0 \\\\
\end{cases}
$$
* Leaky ReLU函数
$$
\phi(x) = 
\begin{cases}
x, & x > 0 \\\\
\gamma x, & x \leq 0 \\\\
\end{cases}
$$
其中， $\gamma$是一个很小的常数. 对Leaky ReLU求导， 可得:
$$
\phi^{\prime}(x) = 
\begin{cases}
1, & x > 0 \\\\
\gamma , & x \leq 0 \\\\
\end{cases}
$$


## 后向传播算法(Back Propogation)


## Reference
* 浙江大学机器学习课程 24 - 胡浩基
* 神经网络与深度学习 - 邱锡鹏
