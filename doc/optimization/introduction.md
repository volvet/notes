# 优化/数学规划 (Optimization/Methematical Programming）
从一个可行解的集合， 寻找最优的元素, 可以写成如下的数学形式
$$
\mathop{minimize} \  f_0(x) \\\\
s.t. \  f_i(x) \leq b_i \  i = 1, \cdots, m \\\\
x = [x_1, \cdots, x_n]^T 为优化变量 \\\\
函数 f_0 是目标函数， 函数f_i 为约束函数, b_i为约束边界
$$

## 优化问题的分类
* 线性规划/非线性规划   
若优化问题的目标函数和约束函数均为线性函数， 则此问题为线性规划问题. 
$$
\mathop{minimize} \  c^Tx \\\\
s.t. \  a_i^Tx \leq b_i \  i = 1, \cdots, m 
$$
反之， 则为非线性规划.

* 凸规划/非凸规划.  
凸函数的性质： $f_i(\alpha x + \beta y) \leq \alpha f_i(x) + \beta f_i(y)$


## Reference
* 凌青 - 中科大公开课 最优化理论
* Stephen Boyd - Connvex Optimization
