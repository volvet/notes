# Introduction

### Exercise 1.1
Consider the sum-of-sequares error function given by (1.2) in which the function $y(x, w)$ is given by the polynomial (1.1). Show that the coefficients $w = \\{ \omega_i \\}$ that minimize the error function are given by the solution to the following set of linear equations:
$$
\sum_{j=0}^{M}A_{ij}\omega_{j} = T_i
$$
where
$$
A_{ij} = \sum_{n=0}^{N}x_n^{i+j} \\\\
T_i = \sum_{n=1}^Nx_n^it_n
$$
Here a suffix $i$ or $j$ denotes the index of a component, whereas $(x)^i$ denotes x raised to the power of $i$


### Exercise 1.2
Write down the set of coupled linear equations, analogous to $ \sum_{j=0}^{M}A_{ij}\omega_{j} = T_i $, satisfied by the coefficients $\omega_i$ which minimize the regularized sum-of-squares error function given by (1.4)
