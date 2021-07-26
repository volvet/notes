# ONNX浅析

## 概述
AlphaGo击败围棋世界冠军李世石以来， 关于人工智能和深度学习的研究呈现井喷之势。 各种新的算法和网络模型层出不穷， 令人眼花缭乱。  与之相随的， 深度学习的训练和推理框架也在不断的推陈出新。 比较著名的有微软的CNTK, Google的TensorFlow， Facebook的PyTorch, Intel的OpenVINO， 腾讯的TNN, 阿里的MNN等等.  这些框架都有相似之处， 他们的输入和输出是一个或者一组多维数据， 这些数据经过多层运算单元之后输出运算结果.  训练框架支持BackPropogation等训练方法， 可以自动调整模型参数, 推理框架则是单纯只能用于输出运算结果，不能调整模型本身. Google的TensorFlow的这个名字尤其具有美感.  多维数据是为张量(Tensor)， 数据在多层运算单元中的运算和传递是为流(FLow),  看到这个词就仿佛看到了一个数据和运算的图(Graph)。

## Reference
1. https://github.com/onnx/onnx
2. https://www.tensorflow.org/
3. https://github.com/Microsoft/CNTK
4. https://pytorch.org/
