# Lecture 18 Bis: Source Coding With Distortion

In this second part, we will return back to source coding introducing however the new concept of distortion, that can be understood better now that we have more tools.

## 1 Source Coding Using The Concept Of Distortion 1.1 Setup

The setup is very similar to the cases we studied earlier during the course. We pass an input U1, . . . , Un to a source encoder that spits out nR bits. These bits go into a decoder that will output V1, . . . , Vn which should hopefully be close to the Ui's. The random variables that form the source are iid of distribution pU. We are also given a function d : U × V → R. We wish to compute a new quantity called the average distortion. We denote it by D and it equals
$$D={\frac{1}{n}}\sum_{i=1}^{n}E[d(U_{i},V_{i})].$$

This can be seen as the per letter expected badness of our system. We now wish to understand the tradeoff between the rate R and D.

## 1.2 Examples

1. Let Ui and Vi be Bernoulli variables that take values in {0, 1} = U = V. The distortion of U and V is d(u, v) = 1{u̸=v}.
2. Now, if U = V = R and U *∼ N*(0, 1), if d(*u, v*) = (u − v)^2, the average distortion D will in turn be the mean squared error of our system.
