# DQN与Q学习

## DQN(Deep Q-Network)
实践中， 近似学习$Q_{\*}$最有效的方法是深度Q网络, 缩写是DQN, 记作$Q(s,a;\omega)$, 其中$\omega$表示神经网络的参数.  
DQN的梯度: 训练DQN的时候， 需要对DQN关于神经网络的参数$\omega$求导， 用:  
$$
\nabla_\omega Q(s,a;\omega) = \frac{\partial Q(s,a;\omega)}{\partial \omega}
$$

## 时间差分算法(TD)

## Reference
* 王树森 张志华 深度强化学习 https://www.math.pku.edu.cn/teachers/zhzhang/
