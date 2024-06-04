# Regularization: Ridge Regression And Lasso

## Motivation 

We have seen that by augmenting the feature vector we can make linear models as powerful as we want. Unfortunately this leads to the problem of overfitting. *Regularization* is a way to mitigate this undesirable behavior.

We will discuss regularization in the context of linear models, but the same principle applies also to more complex models such as neural nets.

## Regularization

Through regularization, we can penalize complex models and favor simpler ones:
$$\operatorname*{min}_{\bf w}\quad\quad{\mathcal L}({\bf w})+\Omega({\bf w})$$

The second term Ω is a regularizer, measuring the complexity of the model given by w.

## L2-Regularization: Ridge Regression

The most frequently used regularizer is the standard Euclidean norm (L2-norm), that is
$$\Omega({\bf w})=\lambda\|{\bf w}\|_{2}^{2}$$

where $\|{\bf w}\|_{2}^{2}=\sum_{i}w_{i}^{2}$. Here the main effect is that large model weights $w_{i}$ will be penalized (avoided), since we consider them "unlikely", while small ones are ok. When ${\cal L}$ is MSE, this is called ridge regression:
$$\min_{{\bf w}}\frac{1}{2N}\sum_{n=1}^{N}\left[y_{n}-{\bf x}_{n}^{\top}{\bf w}\right]^{2}+\lambda\|{\bf w}\|_{2}^{2}$$

_Least squares_ is a special case of this: set $\lambda:=0$.

## Explicit Solution For W: 

Differentiating And Setting To Zero:
$$\mathbf{w}_{\mathrm{ridge}}^{\star}=(\mathbf{X}^{\top}\mathbf{X}+\lambda^{\prime}\mathbf{I})^{-1}\mathbf{X}^{\top}\mathbf{y}$$
(here for simpler notation λ′/2N = λ)

## Ridge Regression To Fight Ill-Conditioning

The eigenvalues of (X^⊤X+λ′I) are all at least λ′ and so the inverse always exists. This is also referred to as lifting the eigenvalues.

Proof: Write the Eigenvalue decomposition of X^⊤X as USU^⊤.

We then have
$$\begin{array}{c}{{{\bf X}^{\top}{\bf X}+\lambda^{\prime}{\bf I}={\bf U}{\bf S}{\bf U}^{\top}+\lambda^{\prime}{\bf U}{\bf I}{\bf U}^{\top}}}\\ {{={\bf U}[{\bf S}+\lambda^{\prime}{\bf I}]{\bf U}^{\top}.}}\end{array}$$

We see now that every Eigenvalue is "lifted" by an amount λ′.

Here is an alternative proof. Recall that for a symmetric matrix A we can also compute eigenvalues by looking at the so-called Rayleigh ratio,
$$R(\mathbf{A},\mathbf{v})={\frac{\mathbf{v}^{\top}\mathbf{A}\mathbf{v}}{\mathbf{v}^{\top}\mathbf{v}}}.$$

Note that if v is an eigenvector with eigenvalue λ then the Rayleigh coefficient indeed gives us λ. We can find the smallest and largest eigenvalue by minimizing and maximizing this coefficient. But note that if we apply this to the symmetric matrix X^⊤X + λ′I then for any vector v we have
$$\mathbf{v}^{\top}(\mathbf{X}^{\top}\mathbf{X}+\lambda^{\prime}\mathbf{I})\mathbf{v}\geq{\frac{\lambda^{\prime}\mathbf{v}^{\top}\mathbf{v}}{\mathbf{v}^{\top}\mathbf{v}}}=\lambda^{\prime}.$$

## L1-Regularization: The Lasso

As an alternative measure of the complexity of the model, we can use a different norm. A very important case is the L1-norm, leading to L1- regularization. In combination with the MSE cost function, this is known as the Lasso:
$$\operatorname*{min}_{\mathbf{w}}\quad{\frac{1}{2N}}\sum_{n=1}^{N}[y_{n}-\mathbf{x}_{n}^{\top}\mathbf{w}]^{2}\ +\ \lambda\,\|\mathbf{w}\|_{1}$$
where
$$\|\mathbf{w}\|_{1}:=\sum_{i}|w_{i}|.$$