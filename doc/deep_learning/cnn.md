# 卷积神经网络（Convolutional Neural Network）

## 卷积神经网络中的卷积核
* 除了宽度和高度， 还具有深度
* 卷积核参数还包括一个偏置值
* 卷积层的超参数： 卷积核的尺寸， 卷积核的个数， 填充， 卷积步长
## 池化层
池化层的超参数：  池化窗口尺寸， 池化步长

### LeNet (LeCun 于上世纪90年代提出)


### AlexNet (Alex Krizhevsky 等人于2013年提出)
* 以ReLU函数来代替Sigmoid或Tanh函数: 这样可以使网络以更快速度收敛.
* 池化(Pooling)
* 随机丢弃(Dropout): 避免过拟合
* 增加训练样本
* 使用GPU加速训练

## Reference
* 浙江大学机器学习课程 24 - 胡浩基
* 北邮 机器视觉 - 鲁鹏
