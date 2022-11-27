# 动态规划(Dynamic Programming)

## Policy Evaluation
$$
\begin{align}
v_{\pi}(s) &= \mathbb{E}[G_t | S_t = s] \\\\
&= \mathbb{E}[R_{t+1} + \gamma G_{t+1} | S_t = s] \\\\
&= \mathbb{E}[R_{t+1} + \gamma v_{\pi}(S_{t+1} | S_t=s] \\\\
&= \sum_{a}\pi(a|s)\sum_{s^{'}, r}p(s^{'}, r|s, a)[r+\gamma v_{\pi}(s^{'}]
\end{align}
$$

### Iterative Policy Evaluation, for estimating $V \approx v_{\pi} $
Loop:   
&nbsp;&nbsp;$\Delta \leftarrow 0$    
&nbsp;&nbsp;Loop for each $s \in \cal{S}$    
&nbsp;&nbsp;&nbsp;&nbsp;$v \leftarrow V(s)$    
&nbsp;&nbsp;&nbsp;&nbsp;$V(s) = \sum_a \pi(a|s)\sum_{s^{'}, r} p(s^{'}, r|s, a) [r+\gamma V(s^{'})]$    
&nbsp;&nbsp;&nbsp;&nbsp;$\Delta \leftarrow \mathop{max}(\Delta, \vert v - V(s) \vert)$    
until $\Delta \lt \theta$

## Refernece
* Reinforcement Learning An Introduction by Richard S. Sutton and Andrew G. Barto
