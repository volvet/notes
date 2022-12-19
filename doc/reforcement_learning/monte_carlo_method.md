# 蒙特卡洛方法

## Monte Carlo Prediction

### First-visit MC prediction, for estimating $V \approx v_{\pi}$
* Input: a policy $\pi$ to be evaluated
* Initialize:  
&nbsp;&nbsp;$V(s) \in \mathbb{R}$, arbitrarily, for all $s \in \mathbb{S}$  
&nbsp;&nbsp;$Returns(s)$, an empty list, for all $s \in \mathbb{S}$
* Loop for ever(for each episode):  
&nbsp;&nbsp;Generate an episode following $\pi$: $S_0, A_0, R_1, S_1, A_1, R_2, \cdots, S_{T-1}, A_{T-1}, R_T$  
&nbsp;&nbsp;$G = 0$  
&nbsp;&nbsp;Loop for each step of episode, $t=T-1, T-2, \cdots, 0$:  
&nbsp;&nbsp;&nbsp;&nbsp; $G=\gamma G + R_{t+1}$  
&nbsp;&nbsp;&nbsp;&nbsp; Unless $S_t$ appears in $S_0, \cdots, S_{t-1}$:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Append $G$ to $Returns(S_t)$  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$V(S_t) = average(Returns(S_t))$

## Monte Carlo Estimation of Action Values

## Reference
* Reinforcement Learning An Introduction by Richard S. Sutton and Andrew G. Barto
