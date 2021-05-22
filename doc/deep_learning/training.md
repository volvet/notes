## Training

### 随机梯度下降(SGD)
 输入一批样本， 求出这些样本的梯度平均值， 根据平均值改变参数, 称为Batch或者Mini-Batch, batch的样本数量大致设置为50~200不等.

### 训练数据初始化
 常用的归一化:
$$
newX = \frac{X - mean(X)}{std(X)}
$$

### 参数初始化
初始化的原则是：$\Omega^TX +b$一开始就再零附近.

## Reference
* 浙江大学机器学习课程 24 - 胡浩基
