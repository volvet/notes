# 卷积

### 卷积的定义
令$F$为图像, $H$为卷积核， $F$与$H$的卷积计为$R = F * H$：
$$
R_{ij} = \sum_{u, v} H_{i-u, j-v}F_{u,v}
$$

### 卷积的性质
$$
叠加性： filter(f_1 + f_2) = filter(f_1) + filter(f_2)
平移不变性： filter(shift(f)) = shift(filter(f))
$$

## Reference
* 北京邮电大学 鲁鹏 机器视觉
