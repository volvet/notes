# 蒙特卡洛方法

## Monte Carlo Prediction

### First-visit MC prediction, for estimating $V \approx v_{\pi}$
* Input: a policy $\pi$ to be evaluated
* Initialize:  
&nbsp;&nbsp;$V(s) \in \mathbb{R}$, arbitrarily, for all $s \in \mathbb{S}$  
&nbsp;&nbsp;$Returns(s)$, an empty list, for all $s \in \mathbb{S}$
* Loop for ever(for each episode):
&nbsp;&nbsp;Generate an episode following $\pi$: $S_0, A_0, R_1, S_1, A_1, R_2, \codts, S_{T-1}, A_{T-1}, R_T$

## Monte Carlo Estimation of Action Values

## Reference
* Reinforcement Learning An Introduction by Richard S. Sutton and Andrew G. Barto
