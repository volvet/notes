## 感知器算法(Perceptron Algorithm)

### 算法描述
感知器是一个线性分类器， 其训练算法由Frank Roseblatt于1957年提出。 可以描述为:  
(1)随机选择$W$和$b$  
(2)取一个训练样本$(X, y)$  
(i) 若 $W^TX + b > 0$, 且$y = -1$, 则:  
$$
W = W - X, b = b - 1
$$

(ii) 若$W^Tx + b < 0$, 且$y = 1$, 则:  
$$
W = W + X, b = b + 1
$$

(3)再取另一个$(X, y)$, 回到(2)  
(4)终止条件： 知道所有的输入输出对都不满足(2)中的两个条件之一， 退出循环.

### 感知机的收敛性
定义:  
$$
若 y = 1, 则令\overrightarrow X = 
\begin{bmatrix}
X \\\\
1
\end{bmatrix} \\\\
若 y = -1, 则令\overrightarrow X = 
\begin{bmatrix}
X \\\\
-1
\end{bmatrix} \\\\ 
\overrightarrow W =
\begin{bmatrix}
W \\\\
b
\end{bmatrix}
$$
为书写方便， 下文的$W$即为$\overrightarrow W$, 则感知机的的训练目标可以写为:
$$
找到W, 使得: W^T\overrightarrow X \geq 0
$$

感知机收敛定理:  
训练集$[\overrightarrow X_i], i=1, 2, \cdots N$, 若它是线性可分的， 即$\exists W_{opt}$, 使得:  
$$
W_{opt}^T\overrightarrow X_i > 0,  i = 1, 2, \cdots, N
$$
则: 使用上文的感知机算法， 经过若干步后可以求的$W$， 使得
$$
W^T\overrightarrow X_i > 0,  i = 1, 2, \cdots, N
$$
成立

### Reference
* 胡浩基 浙江大学机器学习20 人工神经网络
* 邱锡鹏 神经网络与深度学习
