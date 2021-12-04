# 卷积神经网络（Convolutional Neural Network）

## 卷积神经网络中的卷积核
* 除了宽度和高度， 还具有深度
* 卷积核参数还包括一个偏置值
* 卷积层的超参数： 卷积核的尺寸， 卷积核的个数， 填充， 卷积步长
## 池化层
简化模型， 防止过拟合;  增加感受野;  
池化层的超参数：  池化窗口尺寸， 池化步长， 池化操作（平均池化， 最大池化)

## 图像数据增强
从现有的训练样本中生成更多的训练数据. 利用多种能够生成可信图像的随机变换来增加样本.
* 翻转
* 随机缩放或抠图
* 色彩抖动

### LeNet (LeCun 于上世纪90年代提出)

### AlexNet (Alex Krizhevsky 等人于2012年提出)
* 以ReLU函数来代替Sigmoid或Tanh函数: 这样可以使网络以更快速度收敛.
* 池化(Pooling)
* 随机丢弃(Dropout): 避免过拟合
* 增加训练样本
* 使用GPU加速训练

## 经典网络解析
### AlexNet
 CONV1 MAX_POOL1 NORM1 CONV2 MAX_POOL2 NORM2 CONV3 CONV4 CONV5 MAX_POOL3 FC6 FC7 FC8： 8层神经网络.   
 局部响应归一化层(NORM): 后来的研究表明： 更深的网络中该层对性能的提升效果不明显， 而且会增加计算量和存储空间.  
 CONV1 11x11, 96个， 步长为4， 无填充
 
### ZFNet
 ZFNet的网络结构跟AlexNet基本上一致.   
 CONV1 MAX_POOL1 NORM1 CONV2 MAX_POOL2 NORM2 CONV3 CONV4 CONV5 MAX_POOL3 FC6 FC 7 FC8: 8层神经网络.   
主要改进:
* CONV1的卷积核大小改为7x7
* CONV2和CONV3的步长为2
* 增加了CONV3和CON4的卷积核的个数

### VGG16

CONV1-1 CONV1-2 MAX_POOL1 CONV2-1 CONV2-2 MAX_POOL2 CONV3-1 CONV3-2 CONV3-3 MAX_POOL3 CONV4-1 CONV4-2 CONV4-3 MAX_POOL4 CONV5-1 CONV5-2 CONV5-3 MAX_POOL5 FC6 FC7 FC8: 16层神经网络.   
* 13个卷积层和3个全连接层
* 所有的卷积层都是3x3的卷积核和RELU激活函数
* 所有的池化层都是最大池化， 窗口大小为2x2， 步长为2
* 每段卷积层的卷积核个数均相同， 经过一次池化操作， 卷积核的个数增加一倍， 直至到达512
* 移除了局部响应归一化层

### GoogleNet
* 提出了Inception结构， 它能保留输入信号中的更多特征信息
* 去掉了AlexNet的前两个全连接层， 并采用了平均池化， 使得GoogleNet的网络比AlexNet小了12倍.
* 网络中部引入了辅助分类器

### ResNet
* 提出残差模块， 通过堆叠残差模块可以构建任意深度的神经网络， 不会出现退化现象.
* 批归一化方法来对抗梯度消失， 该方法降低了网络训练过程中对于权重初始化的依赖.

## Reference
* 浙江大学机器学习课程 24 - 胡浩基
* 北邮 机器视觉 - 鲁鹏
* AlexNet https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
* ZFNet https://paperswithcode.com/method/zfnet
* VGG-16/VGG-19 https://arxiv.org/abs/1409.1556
* GoogleNet https://arxiv.org/abs/1409.4842
* ResNet https://paperswithcode.com/method/resnet
