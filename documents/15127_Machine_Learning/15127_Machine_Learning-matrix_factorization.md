# Matrix Factorizations 

# Motivation 

In the Netflix prize, the goal was to predict ratings of users for movies, given the existing ratings of those users for other movies. We are going to study the method that achieved the best error (for a single method).

## The Movie Ratings Data

Given items (movies) d=1, 2, . . . , D and users n=1, 2, . . . , N, we define X to be the D × N matrix containing all rating entries. That is, x_{dn} is the rating of n-th user for d-th item.

Note that most ratings xdn are missing and our task is to predict those missing ratings accurately.

## Prediction Using A Matrix Factorization

We will aim to find W, Z s.t. X ≈ WZ^⊤.

So we hope to 'explain' each rating xdn by a numerical representation of the corresponding item and user - in fact by the inner product of an item feature vector with the user feature vector.

$$\operatorname*{min}_{\mathbf{W,Z}}\ {\mathcal{L}}(\mathbf{W},\mathbf{Z}):={\frac{1}{2}}\sum_{(d,n)\in\Omega}\left[x_{d n}-(\mathbf{WZ}^{\top})_{d n}\right]^{2}$$
where W ∈ R^{D×K} and Z ∈ R^{N×K} are tall matrices, having only K ≪ D, N columns.

The set Ω ⊆ [D] × [N] collects the indices of the observed ratings of the input matrix X.

Each row of those matrices is the feature representation of an item (row of W) or a user (row of Z) respectively.

## Choosing K

K is the number of *latent* features.
Recall that for K-means, K was the number of clusters.
Large K Facilitates Overfitting.

## Stochastic Gradient Descent (Sgd)

The training objective is a sum over $|\Omega|$ terms (one per rating): 
$$\sum_{(d,n)\in\Omega}\frac{\frac{1}{2}\left[x_{dn}-(\mathbf{WZ}^{\top})_{dn}\right]^{2}}{f_{d,n}}$$ 

Derive the stochastic gradient for $\mathbf{W},\mathbf{Z}$, given one observed rating $(d,n)\in\Omega$.

For one fixed element (d, n) of the sum, we derive the gradient entry (d′, k) for W :

$$\begin{array}{l l}{{\frac{\partial}{\partial w_{d^{\prime},k}}f_{d,n}(\mathbf{W},\mathbf{Z})}}\\ {{}}&{{=\left\{\begin{array}{l l}{-\left[x_{d n}-(\mathbf{W}\mathbf{Z}^{\top})_{d n}\right]z_{n,k}}&{{\mathrm{if~}}d^{\prime}=d}\\ {0}&{{\mathrm{otherwise}}}\end{array}\right.}}\end{array}$$

$$\begin{array}{l l}{{\frac{\partial}{\partial z_{n^{\prime},k}}f_{d,n}(\mathbf{W},\mathbf{Z})}}\\ {{}}&{{=\left\{\begin{array}{l l}{-\left[x_{d n}-(\mathbf{W}\mathbf{Z}^{\top})_{d n}\right]w_{d,k}}&{{\mathrm{if~}}n^{\prime}=n}\\ {0}&{{\mathrm{otherwise}}}\end{array}\right.}}\end{array}$$

## Alternating Least-Squares (Als)

For simplicity, let us first assume that there are no missing ratings, that is Ω = [D] × [N]. Then

$$\begin{array}{c}{{\frac{1}{2}\sum_{d=1}^{D}\sum_{n=1}^{N}\left[x_{d n}-(\mathbf{W}\mathbf{Z}^{\top})_{d n}\right]^{2}}}\\ {{=\frac{1}{2}\|\mathbf{X}-\mathbf{W}\mathbf{Z}^{\top}\|_{\mathrm{Frob}}^{2}\ .}}\end{array}$$

We can use coordinate descent to minimize the cost plus regularizer:
We first minimize w.r.t. Z for fixed W and then minimize W
given Z.

- Z^⊤ := (W^⊤ W + λ_z I_K)^{−1} W^⊤X
- W^⊤ := (Z^⊤ Z + λ_w I_K)^{−1} Z^⊤X^⊤
What is the computational complexity? How can you decrease the cost when N and D are large?
