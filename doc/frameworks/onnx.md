# ONNX浅析

## 概述
AlphaGo击败围棋世界冠军李世石以来， 关于人工智能和深度学习的研究呈现井喷之势。 各种新的算法和网络模型层出不穷， 令人眼花缭乱。  与之相随的， 深度学习的训练和推理框架也在不断的推陈出新。 比较著名的有微软的CNTK, Google的TensorFlow， Facebook的PyTorch, Apple的CoreML, Intel的OpenVINO，英伟达的cuDNN和TensorRT, 腾讯的TNN和NCNN, 阿里的MNN等等.  这些框架都有相似之处， 他们的输入是一个或者一组多维数据， 数据经过多层运算单元之后输出运算结果.  训练框架支持BackPropogation等训练方法， 可以自动调整模型参数, 用于算法设计。 推理框架则是单纯只能用于模型推理运算，不能调整模型本身， 用于算法部署落地. 这些框架中， Google的TensorFlow的这个名字尤其具有美感.  多维数据是为张量(Tensor)， 数据在多层运算单元中的运算和传递是为流(FLow),  看到这个词就仿佛看到了一个数据和运算的图(Computation Graph), 真可谓妙手偶得之佳作.  这些框架都需要构建运算单元， 并且将这些运算单元按照一定的次序将这些单元连接起来，可以称之为网络模型。 不过每个深度学习框架都有自己独有的格式来解释和存储网络模型， 并且这些框架的侧重点不同， 有些用于训练学习， 有些用于部署推理， 在深度学习算法开发中， 在不同的阶段会选择不同的框架， 所以模型描述格式的不同， 在客观上造成了深度学习算法开发和落地的困难.  笔者之前曾开发深度神经网络算法， 当时选择的训练框架是Caffe,  需要落地部署到Linux，iOS, Android等多个平台.  Linux选择的是Nvidia的cuDNN, iOS选择的是CoreML, Android选择的是NNAPI,  Caffe的模型描述格式是caffemodel. 它使用自定义的Protobuf(https://github.com/BVLC/caffe/tree/master/src/caffe/proto)， 但是显然， 无论是cuDNN，CoreML, NNAPI都无法直接使用caffemodel,  CoreML的模型描述使用另一种定义(https://apple.github.io/coremltools/mlmodel/index.html)， cuDNN和NNAPI都是low-level的推理引擎，需要使用者将这个模型组装起来。 对于CoreML来说， 我们需要把caffemodel转为coremlmodel格式， 对于cuDNN和NNAPI， 我们需要解析caffemodel， 然后自己组装出完整的网络模型.  这个过程繁琐而且容易出错， 当时有强烈的冲动，希望定义一个统一的模型描述格式， 所有的训练框架训练所得的网络模型， 都是用这个格式来描述， 在设备上部署推理时，相应的推理引擎支持解析这个统一的描述格式，直接完成部署落地， 岂不美哉.  当然此事并不容易， 要定义个统一的模型描述格式， 不仅仅需要对深度学习技术有足够深入的理解， 而且将之推广成为事实上的行业标准， 更需要有很大的行业影响力， 并不是如笔者这样的无名小卒可以为之. 所幸已经有社区在做这个事情了， 这就是Open Neural Network Exchange(ONNX).  

用ONNX自己的话来说， ONNX是一个对计算网络(Computation Graph)的一个通用描述(Intermediate Representation). 它希望被设计成为开放的网络描述格式， 减少开发者在各个训练和推理框架间切换的代价， 可以让开发者专注于算法和优化.  虽然ONNX还处于比较早期的阶段， 不过已经有约来越多的人开始关注到它，未来会有机会得到更广泛的应用. 

## Reference
1. ONNX: https://github.com/onnx/onnx
2. TENSORFLOW: https://www.tensorflow.org/
3. CNTK: https://github.com/Microsoft/CNTK
4. PYTORCH: https://pytorch.org/
5. TNN: https://github.com/Tencent/TNN
6. MNN: https://github.com/alibaba/MNN
7. CUDNN: https://developer.nvidia.com/zh-cn/cudnn
8. TENSORRT: https://developer.nvidia.com/zh-cn/tensorrt
9. COREML: https://developer.apple.com/documentation/coreml
10. NCNN: https://github.com/Tencent/ncnn
11. NNAPI: https://developer.android.com/ndk/guides/neuralnetworks
