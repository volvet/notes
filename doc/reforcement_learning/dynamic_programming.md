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
     $\Delta \leftarrow 0$
     Loop for each $s \in \cal{S}$


## Refernece
* Reinforcement Learning An Introduction by Richard S. Sutton and Andrew G. Barto
