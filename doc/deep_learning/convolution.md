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
G_{\sigma} = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

如何设计卷积核： 方差和卷积核的尺寸

## Reference
* 北京邮电大学 鲁鹏 机器视觉
