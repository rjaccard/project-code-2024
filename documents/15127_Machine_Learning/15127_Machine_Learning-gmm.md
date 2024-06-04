# Gaussian Mixture Models 

## Motivation 

K-means forces the clusters to be spherical, but sometimes it is desirable to have *elliptical* clusters. Another issue is that, in K-means, each example can only belong to one cluster, but this may not always be a good choice, e.g. for data points that are near the "border". Both of these problems are solved by using Gaussian Mixture Models.

## Clustering With Gaussians

The first issue is resolved by using full covariance matrices Σk instead of *isotropic* covariances.

$$p(\mathbf{X}|{\boldsymbol{\mu}},\mathbf{\Sigma},\mathbf{z})=\prod_{n=1}^{N}\prod_{k=1}^{K}[{\mathcal{N}}(\mathbf{x}_{n}|{\boldsymbol{\mu}}_{k},\mathbf{\Sigma}_{k})]^{z_{n k}}$$

## Soft-Clustering

The second issue is resolved by defining zn to be a random variable.

Specifically, define z_n ∈ {1, 2, . . . , K} that follows a multinomial distribution.

$$p(z_{n}=k)=\pi_{k}{\mathrm{~where~}}\pi_{k}>0,\forall k{\mathrm{~and~}}\sum_{k=1}^{K}\pi_{k}=1$$

This leads to soft-clustering as opposed to having "hard" assignments.

## Gaussian mixture model 

Together, the likelihood and the prior define the joint distribution of Gaussian mixture model (GMM):

$$p(\mathbf{X},\mathbf{z}\, \mu, \Sigma,\pi) {{=\prod_{n=1}^{N}p(\mathbf{x}_{n}|z_{n} \mu, \Sigma)p(z_{n}|\pi)}}\\ {{=\prod_{n=1}^{N}K}}\\ {{=\prod_{n=1}^{N}\prod_{k=1}^{K}\left[\mathcal{W}(\mathbf{x}_{n}|\mu_{k},\Sigma_{k})\right]^{z_{n k}}\prod_{k=1}^{K}\left[\pi_{k}\right]^{z_{n k}}}}$$
Here, xn are observed data vectors, zn are latent unobserved variables, and the unknown parameters are given by $θ:={µ1, . . . , µK, Σ1*, . . . ,* ΣK, π}$.

## Marginal Likelihood

GMM is a latent variable model with zn being the unobserved (latent) variables.

An advantage of treating zn as latent variables instead of *parameters* is that we can *marginalize* them out to get a cost function that does not depend on zn, i.e. as if zn never existed.

Specifically, we get the following marginal likelihood by marginalizing zn out from the likelihood:
Deriving cost functions this way is good for *statistical efficiency*.

Without a latent variable model, the number of parameters grows at rate O(N).
After marginalization, the growth is reduced to O(D^2.K) (assuming *D, K* ≪ N).

## Maximum likelihood 

To get a maximum (marginal) likelihood estimate of θ, we maximize the following:

$$\operatorname*{max}_{\boldsymbol{\theta}}\sum_{n=1}^{N}\log\sum_{k=1}^{K}\pi_{k}{\mathcal{N}}({\mathbf{x}}_{n}|{\boldsymbol{\mu}}_{k},\,{\boldsymbol{\Sigma}}_{k})$$