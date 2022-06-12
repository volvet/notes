**2.1**   设$C \subseteq R^n$为一个凸集， 且$x_1, ..., x_k \in C$, 令$\theta_1, ..., \theta_k \in R$, 且满足$\theta_i \geq 0, \theta_1 + ... + \theta_k = 1$。  证明: $\theta_1 x_1 + ... + \theta_k x_k \in C$  
Solution:  
显然$k=2$时成立， 下面我们证明$k=3$的时候, 若$\theta_1 = 0$, 则等价于$k=2$, 所以我们可以设定$\theta_1 \neq 0$.  
$$
y = \theta_1x_1 + \theta_2x_2 + \theta_3x_3,   \   \theta_i \geq 0, \sum_{i=1}^3\theta_i = 1 \\\\
y = \theta_1x_1 + (1-\theta_1)(\frac{\theta_2}{1-\theta_1}x_2 + \frac{\theta_3}{1-\theta_1}x_3) \\\\
显然: \frac{\theta_2}{1-\theta_1} + \frac{\theta_3}{1-\theta_1} = \frac{1-\theta_1}{1-\theta_1} = 1 \\\\
于是: (\frac{\theta_2}{1-\theta_1}x_2 + \frac{\theta_3}{1-\theta_1}x_3) \in C \\\\
然后可以推出: y = \theta_1x_1 + \theta_2x_2 + \theta_3x_3 \in C
$$
得证.


**2.2**   证明一个集合是凸集当且仅当它与任意直线的交是凸的.  证明一个集合是仿射集当且仅当它与任意直线的交是仿射的.  
Solution:  
若集合为凸集，直线也是凸集， 集合的交为保凸运算， 显然它与任意直线的交必为凸集.  
若集合$C$与任意直线的交为凸集， 则在此集合中任意选两点$x_1, x_2$, 则此集合与连接$x_1, x_2$的直接的交为凸集， 则$\theta_1x_1 + (1-\theta_1)x_2 \in C$， 所以$C$为凸集.
命题1得证.  

**2.3**   中点凸性. 集合$C$是中点凸的， 当$C$中任意两点$a, b$的平均或者中点$\frac{a+b}{2}$也属于$C$. 显然凸集是中点凸的。 可以证明在一些很微弱的条件下， 中点凸可以导出凸性。 试证明如果$C$是闭和中点凸的， 那么$C$是凸集.  
Solution:  
$$
令 \theta^k = \sum_{i=1}^kc_i2^{-i},  其中c_i \in \\{0, 1\\} \\\\
中点凸, 即: \theta^ka + (1-\theta^k)b \in C \\\\
\lim_{k\rightarrow\infty}(\theta^ka+(1-\theta^k)b) = \theta a + (1-\theta)b \in C
$$
得证.  

**2.4**   证明集合$S$的凸包是所有包含$S$的凸集的交。  
Solution:  
$$
令H = S的凸包， D为包含S的所有凸集的交，  显然H是一个凸集， 所以 D \subseteq H \\\\
对于任意 x \in H, 显然 x 可以写为 x_1, x_2, ..., x_n \in S 的凸组合. 凸集的交是保凸运算， 所以D是凸集. S \subseteq D， 所以 x \ in D. 由此可以推论: H \subseteq D \\\\
由此： H = D
$$
得证.

**2.5**   两个平行的超平面$\\{x \in R^n | a^Tx = b_1 \\}, \\{x \in R^n | a^Tx = b_2 \\}$的距离是多少？  
**2.6**   什么时候超平面包含另一个？ 给出下式成立的条件： $\\{a^Tx\leq b\\} \subseteq \\{\tilde a^Tx\leq \tilde b\\}$.   
**2.7**   半空间的Voronol描述.  令$a, b$为$R^n$上互异的亮点， 证明所有距离$a$比距离$b$更近的点的集合， 即$\\{x | \Vert x - a \Vert_2 \leq \vert x - b \Vert_2 \\}$, 是一个超平面. 用形如$c^Tx \leq d$的不等式表示并绘出图像.  


