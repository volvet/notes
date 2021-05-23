## Training

### 随机梯度下降(SGD)
 输入一批样本， 求出这些样本的梯度平均值， 根据平均值改变参数, 称为Batch或者Mini-Batch, batch的样本数量大致设置为50~200不等.

### 训练数据初始化
 常用的归一化:
$$
newX = \frac{X - mean(X)}{std(X)}
$$

### 参数初始化
初始化的原则是：$W^TX +b$一开始就在零附近.  
一种比较简单的方法是:  $(W, b)$初始化从区间$(-\frac{1}{\sqrt {d}}, \frac{1}{\sqrt {d}})$均匀随机取值， 其中$d$为所在层的神经元个数, 如果$X$服从正态分布， 均值0， 方差1， 且各个维度无关， 则
$W^TX +b$是均值为0， 方差为$\frac{1}{3}$的正态分布.

### Batch Normalization
TODO

### 目标函数选择
* 正则项
* SoftMax 应用于分类问题
$$
q_i = \frac{e^{z_i}}{\sum_{j=1}^{N}e^{z_j}}
$$
* 交叉熵(Cross Entropy)
$$
E = - \sum_{i=1}^Np_i \mathop{log}(q_i)
$$
SoftMax/交叉熵的求导:  
$$
\frac{\partial q_i}{\partial z_j}  = \frac{\frac{\partial e^{z_i}}{\partial z_j} \sum - e^{z_i} \frac{\partial \sum}{\partial z_j}}{\sum ^2}
$$
如果 $j = i$:
$$
\frac{\partial q_i}{\partial z_j} = \frac{e^{z_i}\sum - e^{z_i}e^{z_j}}{\sum ^2} = q_i(1 - q_j)
$$
如果 $j \neq i$:
$$
\frac{\partial q_i}{\partial z_j} = - \frac{e^{z_i}e^{z_j}}{\sum ^2} = - q_i q_j
$$


对交叉熵求导:
$$
\frac{\partial E}{\partial q_i} = -\frac{p_i}{q_i}
$$
于是:
$$
\begin{align}
\frac{\partial E}{\partial z_i} & = \sum_j \frac{\partial E}{\partial q_i} \frac{\partial q_i}{\partial z_j} \\\\
& = \frac{\partial E}{\partial q_i} \frac{\partial q_i}{\partial z_i} + \sum_{j \neq i}\frac{\partial E}{\partial q_i}\frac{\partial q_i}{\partial z_j} \\\\
& = -{p_i}(1-q_i) + \sum_{j \neq i} p_j q_i \\\\
& = q_i - p_i
\end{align}
$$






### 参数更新策略
* AdaGrad:  解决各个方向梯度不一致的问题
* RMSProp:  解决各个方向梯度不一致的问题
* Momentum: 解决梯度随机性问题
* Adam

## Reference
* 浙江大学机器学习课程 25 - 胡浩基
