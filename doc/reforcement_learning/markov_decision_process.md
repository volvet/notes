# 马尔可夫决策过程(Finite Markov Decision Processes)

## The Agent-Environment Interface
* Agent: The learner and decision maker.
* Environment: The things agent interacts with, comprising everything outside.

The agent and environment interact at each of a sequence of discrete time steps, $t = 0, 1, 2, \cdots$. At each step $t$, the agent receives some representation of the environment's state, $S_t \in \cal{S}$, and on the basis select an action, $A_t \in \cal{A}(s)$. One time step later, in part as a consequence of its action, the agent receives a numerical reward, $R_{t+1} \in \cal{R} \subset \mathbb{R}$, and find itself in a new state, $S_{t+1}$. The MDP and agent together thereby give rise to a sequence or trajectory that begin like this:
$$
S_0, A_0, R_1, S_1, A_1, R_2, S_2, A_2, R_3, \cdots
$$
$$
p(s^{'}, r | s, a) =  Pr\\{S_t=s^{'}, R_t = r | S_{t-1}=s, A_{t-1}=a\\}
$$
$$
\sum_{s^{'}\in\cal{S}}\sum_{r\in\cal{R}}p(s^{'},r|s,a) = 1
$$
State-transition probabilities is the three-argument function: $p:\cal{S}\times\cal{S}\times\cal{A}\rightarrow[0,1]$
$$
p(s^{'}|s, a) = Pr\\{S_t = s^{'} | S_{t-1}=s, A_{t-1}=a\\} = \sum_{r\in\cal{R}}p(s^{'}, r|s, a)
$$
The expected rewards for the state-action pairs as a two-argument function: $r:\cal{S}\times\cal{A}\rightarrow\mathbb{R}$
$$
r(s,a) = \mathbb{E}[R_t|S_{t-1}=s, A_{t-1}=a] = \sum_{r\in\cal{R}}r\sum_{s^{'}\in\cal{S}}p(s^{'},r|s,a)
$$
The expected reward for the state-action-next-state triples as a three-argument function: $r:\cal(S)\times\cal(A)\times\cal(S)\rightarrow\mathbb{R}$:
$$
r(s,a,s^{'}) = \mathbb{E}[R_t|S_{t-1}=s, A_{t-1}=a, S_t=s^{'}] = \sum_{r\in\cal{R}}r\frac{p(s^{'},r|s,a)}{p(s^{'}|s,a)}
$$

## Goal and Rewards

## Return and Episodes
$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2R_{t+3} + \cdots
$$
## Policies and Value Functions
A policy $\pi$ is a mapping from state to probabilities of selecting each possible action.  
State-value function for policy $\pi$:
$$
v_{\pi}(s) = \mathbb{E} _ \{\pi}[G_t | S_t = s] \\\\
= \mathbb{E} _ {\pi}[\sum_{k=0}^{\infty}\gamma^kR_{t+k+1} | S_t=s],  for \ all \ s \ \in \mathbb{S}
$$
Action-value function for policy $\pi$:
$$
\begin{align}
q_{\pi}(s, a) &= \mathbb{E} _ {\pi}[G_t | S_t=s, A_t=a] \\\\
&= \mathbb{E} _ {\pi}[\sum_{k=0}^\infty\gamma^kR_{t+k+1} | S_t= s, A_t = a]
\end{align}
$$

Exericise 3.12
$$
v_{\pi} = \sum_{a}\pi(a|s)q_{\pi}(s, a)
$$
Exericise 3.13
$$
q_{\pi}(s, a) = \sum_{s^{'}, r}p(s^{'}, r | s, a)(r + \gamma v_{\pi}(s^{'}))
$$
A foundational property of value function used thoughout reinforcement learning and dynamic programming is:
$$
\begin{align}
v_{\pi}(s) &= \mathbb{E} _ {\pi} [G_t|S_t=s] \\\\
&= \mathbb{E} _ {\pi}[R_t + \gamma G_{t+1}|S_t=s] \\\\
&= \sum_a\pi(a|s)\sum_{s^{'}}\sum_rp(s^{'}, r|s, a)[r + \gamma G_{t+1}|S_{t+1}=s^{'}]
\end{align}
$$


## Reference
* Reinforcement Learning An Introduction by Richard S. Sutton and Andrew G. Barto
