# 卷积

## 卷积的基本概念

### 卷积的定义
令$F$为图像, $H$为卷积核， $F$与$H$的卷积计为$R = F * H$：
$$
R_{ij} = \sum_{u, v} H_{i-u, j-v}F_{u,v}
$$

### 卷积的性质
$$
叠加性： filter(f_1 + f_2) = filter(f_1) + filter(f_2) \\\\
平移不变性： filter(shift(f)) = shift(filter(f))
$$

### 边界填充
零填充  
边缘像素填充  
镜像填充  

### 高斯卷积核
$$
G_{\sigma}(x, y) = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

如何设计卷积核： 方差和卷积核的尺寸。  
经验法则: 将卷积核的半窗宽度设置为3$\sigma$, 最终卷积模版的尺寸为$2 \times 3 \sigma + 1$。  
高斯卷积核的特性:
* 去除图像中的高频成分(低通滤波)
* 两个高斯卷积核卷积后得到的还是高斯卷积核
* 可分离 -  二维卷积可以分离成两个一维卷积

### 图像噪声
* 椒盐噪声
* 脉冲噪声
* 高斯噪声

### 图像边缘
*  表面法向不连续
*  深度不连续
*  表面颜色不连续
*  光照不连续

### 边缘检测

### 图像梯度
$$
\nabla f = 
\begin{bmatrix}
\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}
\end{bmatrix}
$$

梯度方向: $\theta = \mathop{arctan}(\frac{\frac{\partial f}{\partial y}}{\frac{\partial f}{\partial x}})$

### 高斯一阶偏导核
$$
\frac{\partial G_{\sigma}(x,y)}{\partial x} = \frac{1}{2\pi \sigma^4}xe^{-\frac{x^2 + y^2}{2\sigma^2}}\\\\
\frac{\partial G_{\sigma}(x,y)}{\partial y} = \frac{1}{2\pi \sigma^4}ye^{-\frac{x^2 + y^2}{2\sigma^2}}\\\\
$$

### 非极大值抑制

### Canny 边缘检测器
1.  高斯一阶偏导核卷积图像
2.  计算每个点的梯度幅值和方向
3.  非极大值抑制： 将宽的边缘细化到单个像素宽度
4.  连接和阈值： 定义两个阈值，地和高， 使用高阈值开始边缘曲线， 使用低阈值连接边缘曲线

## 图像纹理
1. 纹理基元
2. 利用纹理基元来表示纹理

### 基于卷积核组的图像表示
利用卷积核组对图像卷积， 得到对应的特征响应图组.

### 忽略位置
使用特征响应图的均值组来表示图像

### 卷积核组设计
类型: 
* 边缘 - 高斯一阶偏导核
* 条形 - 高斯二阶偏导核
* 点状 - 高斯-拉普拉斯核 (Laplacian of Guassian)
尺度: 三~六个尺度  
方向: 六个方向  
 


## Reference
* 北京邮电大学 鲁鹏 机器视觉
