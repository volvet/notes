# DQN与Q学习

## DQN(Deep Q-Network)
实践中， 近似学习$Q_{\*}$最有效的方法是深度Q网络, 缩写是DQN, 记作$Q(s,a;\omega)$, 其中$\omega$表示神经网络的参数.  
DQN的梯度: 训练DQN的时候， 需要对DQN关于神经网络的参数$\omega$求导， 用下式表示:  
$$
\nabla_\omega Q(s,a;\omega) = \frac{\partial Q(s,a;\omega)}{\partial \omega}
$$

## 时间差分算法(TD)

### 贝尔曼方程
$$
U_t = \sum_{k=t}^n\gamma^{k-t}R_k = R_t + \gamma U_{t+1} \\\\
用符号 S_{t+1:} = \\{S_{t+1}, S_{t+2}, \cdots \\}, A_{t+1:} = \\{A_{t+1}, A_{t+2}, \cdots \\} \\\\
Q_{\pi}(s_t, a_t) = \mathbb{E} _ {S_{t+1:}, A_{t+1:}}[U_t｜S_t=s_t, A_t=a_t]
$$


## Reference
* 王树森 张志华 深度强化学习 https://www.math.pku.edu.cn/teachers/zhzhang/