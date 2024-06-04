# Expectation-Maximization Algorithm

## Motivation
Computing maximum likelihood for Gaussian mixture model is difficult due to the log outside the sum.

$$\operatorname*{max}_{\boldsymbol{\theta}}\ {\mathcal{L}}({\boldsymbol{\theta}}):=\sum_{n=1}^{N}\log\sum_{k=1}^{K}\pi_{k}{\mathcal{N}}({\mathbf{x}}_{n}\mid{\boldsymbol{\mu}}_{k},\,{\boldsymbol{\Sigma}}_{k})$$

Expectation-Maximization (EM) algorithm provides an elegant and general method to optimize such optimization problems. It uses an iterative two-step procedure where individual steps usually involve problems that are easy to optimize.

## Em Algorithm: Summary

Start with θ(1) and iterate:

1. Expectation step: Compute a lower bound to the cost such that it is tight at the previous θ(t):
$$ L(θ) *≥ L*(θ, θ(t)) and L(θ(t)) = L(θ(t), θ(t)).$$

2. Maximization step:

Update θ:
$$\mathbf{\theta}^{(t+1)}=\arg\operatorname*{max}_{\mathbf{\theta}}{\underline{{{\mathcal{L}}}}}(\mathbf{\theta},\mathbf{\theta}^{(t)}).$$

## Concavity Of Log

Given non-negative weights $q$ s.t. $\sum_{k}q_{k}=1$, the following holds for any $r_{k}>0$:

$$\log\left(\sum_{k=1}^{K}q_{k}r_{k}\right)\geq\sum_{k=1}^{K}q_{k}\log r_{k}$$

## The Expectation Step

$$\log\sum_{k=1}^{K}\pi_{k}{\mathcal{N}}({\mathbf{x}}_{n}\,|\,{\boldsymbol{\mu}}_{k},{\boldsymbol{\Sigma}}_{k})\geq\sum_{k=1}^{K}q_{k n}\log{\frac{\pi_{k}{\mathcal{N}}({\mathbf{x}}_{n}\,|\,{\boldsymbol{\mu}}_{k},{\boldsymbol{\Sigma}}_{k})}{q_{k n}}}$$
with equality when,

$$q_{k n}=\frac{\pi_{k}\mathcal{N}(\mathbf{x}_{n}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})}{\sum_{k=1}^{K}\pi_{k}\mathcal{N}(\mathbf{x}_{n}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})}$$

This is not a coincidence.

## The Maximization Step

Maximize the lower bound w.r.t. θ.

$$\operatorname*{max}_{\pmb{\theta}}\;\sum_{n=1}^{N}\sum_{k=1}^{K}q_{k n}^{(t)}\left[\log\pi_{k}+\log{\mathcal{N}}({\bf x}_{n}|{\pmb{\mu}}_{k},\Sigma_{k})\right]$$

Differentiating w.r.t. µk, Σ_k{−1} , we can get the updates for µ_k and Σ_k.

$${{\mu_{k}^{(t+1)}:=\frac{\sum_{n}q_{k n}^{(t)}\mathbf{x}_{n}}{\sum_{n}q_{k n}^{(t)}}}}\\ {{\sum_{k}q_{k n}^{(t)}(\mathbf{x}_{n}-\mu_{k}^{(t+1)})(\mathbf{x}_{n}-\mu_{k}^{(t+1)})^{\top}}}\\ {{\sum_{n}q_{k n}^{(t)}}}$$

For $\pi_{k}$, we use the fact that they sum to 1. Therefore, we add a Lagrangian term, differentiate w.r.t. $\pi_{k}$ and set to 0, to get the following update:

$${l}{{\pi_{k}^{(t+1)}:=\frac{1}{N}\sum_{n=1}^{N}q_{k n}^{(t)}}}$$

## Summary Of Em For Gmm

Initialize µ^(1), Σ^(1), π^(1) and iterate between the E and M
step, until L(θ) stabilizes.

1. E-step: Compute assignments $q_{kn}^(t)$
$$q_{k n}^{(t)}:=\frac{\pi_{k}^{(t)}\mathcal{N}(\mathbf{x}_{n}\mid\boldsymbol{\mu}_{k}^{(t)},\boldsymbol{\Sigma}_{k}^{(t)})}{\sum_{k=1}^{K}\pi_{k}^{(t)}\mathcal{N}(\mathbf{x}_{n}\mid\boldsymbol{\mu}_{k}^{(t)},\boldsymbol{\Sigma}_{k}^{(t)})}$$

2. Compute the marginal likelihood (cost).
$$\mathcal{L}(\boldsymbol{\theta}^{(t)})=\sum_{n=1}^{N}\log\sum_{k=1}^{K}\pi_{k}^{(t)}\mathcal{N}(\mathbf{x}_{n}\mid\boldsymbol{\mu}_{k}^{(t)},\boldsymbol{\Sigma}_{k}^{(t)})$$

3. M-step: Update $µ_k^{(t+1)}, Σ_k^{(t+1)}, π_k^{(t+1)}$.

$$\begin{array}{l}{{\mu_{k}^{(t+1)}:=\frac{\sum_{n}q_{k n}^{(t)}{\bf x}_{n}}}}\\ {{\sum_{n}q_{k n}^{(t)}}}\\ {{\sum_{k}^{(t+1)}:=\frac{\sum_{n}q_{k n}^{(t)}({\bf x}_{n}-\mu_{k}^{(t+1)})({\bf x}_{n}-\mu_{k}^{(t+1)})^{\top}}}}\\ {{\sum_{n}q_{k n}^{(t)}}}\\ {{\pi_{k}^{(t+1)}:=\frac{1}{N}\sum_{n}q_{k n}^{(t)}}}\end{array}$$
If we let the covariance be diagonal i.e. Σk := σ2I, then EM
algorithm is same as K-means as σ2 → 0.

## Posterior Distribution

We now show that $q_{kn}^(t)$ is the posterior distribution of the latent variable, i.e. $q_{kn}^(t) = p(z_n = k | x_n, θ^(t))$

$$p(x_n, z_n|θ) = p(x_n|z_n, θ)p(z_n|θ) = p(z_n|x_n, θ)p(x_n|θ)$$

## Em In General

Given a general joint distribution p(xn, zn|θ), the marginal likelihood can be lower bounded similarly: The EM algorithm can be compactly written as follows:

$$\pmb{\theta}^{(t+1)}:=\arg\operatorname*{max}_{\pmb{\theta}}\sum_{n=1}^{N}\mathbb{E}_{p(z_{n}|\mathbf{x}_{n},\pmb{\theta}^{(t)})}\big[\log p(\mathbf{x}_{n},z_{n}|\pmb{\theta})\big]$$
Another interpretation is that part of the data is missing, i.e. (xn, zn) is the "complete" data and zn is missing.

The EM algorithm averages over the "unobserved" part of the data.