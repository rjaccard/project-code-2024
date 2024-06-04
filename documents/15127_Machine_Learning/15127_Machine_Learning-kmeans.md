# K-Means Clustering 

## Clustering

Clusters are groups of points whose inter-point distances are small compared to the distances outside the cluster. The goal is to find "prototype" points µ1, µ2,. . . , µK and cluster assignments zn ∈ {1, 2, . . . , K} for all n = 1, 2, . . . , N data vectors x_n ∈ R^D.

## K-Means Clustering

Assume K is known.

$\begin{array}{c}\min\limits_{\mathbf{z},\mu}\mathcal{L}(\mathbf{z},\mu)=\sum\limits_{n=1}^{N}\sum\limits_{k=1}^{K}\mathcal{Z}_{nk}\left\|\mathbf{x}_{n}-\mu_{k}\right\|_{2}^{2}\\ \text{s.t.}\ \mu_{k}\in\mathbb{R}^{D},\ \mathcal{Z}_{nk}\in\{0,1\},\ \sum\limits_{k=1}^{K}\mathcal{Z}_{nk}=1,\\ \text{where}\ \mathbf{z}_{n}=\left[\mathcal{Z}_{n1},\mathcal{Z}_{n2},\ldots,\mathcal{Z}_{nk}\right]^{\top}\\ \mathbf{z}=\left[\mathbf{z}_{1},\mathbf{z}_{2},\ldots,\mathbf{z}_{N}\right]^{\top}\\ \boldsymbol{\mu}=\left[\boldsymbol{\mu}_{1},\boldsymbol{\mu}_{2},\ldots,\boldsymbol{\mu}_{K}\right]^{\top}\end{array}$


## Algorithm: 

Initialize µ_k ∀k, then iterate:

1. For all n, compute z_n given µ.
2. For all k, compute µ_k given z.

### Step 1: For All n, Compute z_n Given \mu.

$$z_{n k}=\left\{\begin{array}{l l}{{1\;\;\mathrm{if}\;k=\arg\operatorname*{min}_{j=1,2,\dots K}\|\mathbf{x}_{n}-\mu_{j}\|_{2}^{2}}}\\ {{0\;\;\mathrm{otherwise}}}\end{array}\right.$$

## Step 2: For All k, Compute \mu_k Given z. Take Derivative W.R.T. \mu_k To Get:

$$\mu_{k}=\frac{\sum_{n=1}^{N}z_{n k}\mathbf{X}_{n}}{\sum_{n=1}^{N}z_{n k}}$$

Hence, the name 'K-means'.

## Summary Of K-Means

Initialize µ_k ∀k, then iterate:

1. For all $n$, compute $\mathbf{z}_{n}$ given $\mu$.

$$z_{nk}=\left\{\begin{array}{ll}1&\mbox{if$k=\arg\min_{j}||\mathbf{x}_{n}-\mu_{j}||_{2}^{2}$}\\ 0&\mbox{otherwise}\end{array}\right.$$

2. For all k, compute µk given z.

$\mu_{k}=\frac{\sum_{n=1}^{N}\tilde{z}_{nk}\mathbf{X}_{n}}{\sum_{n=1}^{N}\tilde{z}_{nk}}$

Convergence to a local optimum is assured since each step decreases the cost (see Bishop, Exercise 9.1).

## Coordinate descent 

K-means is a coordinate descent algorithm, where, to find min_{z,µ} L(z, µ), we start with some µ^(0) and repeat the following:

- z^(t+1) := arg min_z L(z, µ^(t))
- µ^(t+1) := arg min_µ L(z^{(t+1)}, µ)

## K-Means As A Matrix Factorization 

Recall The Objective

$$\begin{array}{r l}{{\operatorname*{min}_{\mathbf{z},\boldsymbol{\mu}}\,\mathcal{L}(\mathbf{z},\boldsymbol{\mu})=\sum_{n=1}^{N}\sum_{k=1}^{K}z_{n k}\|\mathbf{x}_{n}-\boldsymbol{\mu}_{k}\|_{2}^{2}}}\\ {{}}&{{=\|\mathbf{X}^{\top}-\mathbf{M}\mathbf{Z}^{\top}\|_{\mathrm{Frob}}^{2}}}\\ {{}}&{{\mathrm{s.t.}\ \boldsymbol{\mu}_{k}\in\mathbb{R}^{D},}}\\ {{}}&{{z_{n k}\in\{0,1\},\,\sum_{k=1}^{K}z_{n k}=1.}}\end{array}$$

## Issues With K-Means

1. Computation can be heavy for large *N, D* and K.
2. Clusters are forced to be spherical (e.g. cannot be elliptical).
3. Each example can belong to only one cluster ("hard" cluster assignments).