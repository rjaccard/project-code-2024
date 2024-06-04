# Least Squares 

## Motivation 

In rare cases, one can compute the optimum of the cost function analytically. Linear regression using a mean-squared error cost function is one such case. Here the solution can be obtained explicitly, by solving a linear system of equations.

These equations are sometimes called the normal equations. This method is one of the most popular methods for data fitting.

It is called least squares. To derive the normal equations, we first show that the problem is convex.

We then use the optimality conditions for convex functions (see the previous lecture notes on optimization). I.e., at the optimum parameter, call it w⋆, it must be true that the gradient of the cost function is 0. I.e.,

$$\nabla{\mathcal{L}}(\mathbf{w}^{\star})=\mathbf{0}.$$
This is a system of D equations.

## Normal Equations

Recall that the cost function for linear regression with mean-squared error is given by

$$\mathcal{L}(\mathbf{w})=\frac{1}{2N}\sum_{n=1}^{N}\left(y_{n}-\mathbf{x}_{n}^{\top}\mathbf{w}\right)^{2}=\frac{1}{2N}(\mathbf{y}-\mathbf{X}\mathbf{w})^{\top}(\mathbf{y}-\mathbf{X}\mathbf{w}),$$

where

$$\mathbf{y}=\left[\begin{array}{c}y_{1}\\ y_{2}\\ \vdots\\ y_{N}\end{array}\right],\mathbf{X}=\left[\begin{array}{cccc}x_{11}&x_{12}&\ldots&x_{1D}\\ x_{21}&x_{22}&\ldots&x_{2D}\\ \vdots&\vdots&\ddots&\vdots\\ x_{N1}&x_{N2}&\ldots&x_{ND}\end{array}\right].$$

We claim that this cost function is _convex_ in the $\mathbf{w}$. There are several ways of proving this:

1. Simplest way: observe that L is naturally represented as the sum (with positive coefficients) of the simple terms $(y_n − x_n^⊤ \times w)^2$. Further, each of
these simple terms is the composition of a linear function with a convex function (the square function).
Therefore, each of these simple terms is convex and hence the sum is convex.

2. Directly verify the definition, that for any λ ∈ [0,1] and w, w′, 
$$L(λw + (1 − λ)w′) − (λL(w) + (1 − λ)L(w′)) ≤ 0.$$

Computation: 

$$LHS = -\frac{1}{2N}\lambda(1-\lambda)\|{\bf X}({\bf w}-{\bf w^{\prime}})\|_{2}^{2},$$
which indeed is non-positive.

3. We can compute the second derivative (the Hessian) and show that it is positive semidefinite (all its eigenvalues are non-negative).
For the present case a computation shows that the Hessian
has the form $${\frac{1}{N}}\mathbf{X}^{\top}\mathbf{X}.$$
This matrix is indeed positive semidefinite since its non-zero eigenvalues are the squares of the non-zero singular values of the matrix X.

Now where we know that the function is convex, let us find its minimum.

If we take the gradient of this expression with respect to the weight vector w we get

$$\nabla{\mathcal{L}}(\mathbf{w})=-{\frac{1}{N}}\mathbf{X}^{\top}(\mathbf{y}-\mathbf{X}\mathbf{w}).$$

If we set this expression to 0 we get the normal equations for linear regression,

$$\mathbf{X}^{\top}\underbrace{\left(\mathbf{y}-\mathbf{X}\mathbf{w}\right)}_{\mathrm{error}}=\mathbf{0}.$$

## Geometric Interpretation

The error is orthogonal to all columns of X.
The span of X is the space spanned by the columns of X.
Every element of the span can be written as u = Xw for some choice of w.

Which element of *span*(X) shall we take? The normal equations tell us that the optimum choice for u, call it u⋆, is that element so that y − u⋆ is orthogonal to *span*(X). In other words, we should pick u⋆ to be equal to the projection of y onto *span*(X).

## Least Squares

The matrix $X^⊤ \times X ∈ R^{D×D}$ is called the Gram matrix. If it is invertible, we can multiply the normal equation by the inverse of the Gram matrix from the left to get a closed-form expression for the minimum:
$$\mathbf{w}^{\star}=(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}.$$

We can use this model to predict a new value for an unseen datapoint (test point) x_m:

$$\hat{y}_{m}:={\bf x}_{m}^{\top}{\bf w}^{\star}={\bf x}_{m}^{\top}({\bf X}^{\top}{\bf X})^{-1}{\bf X}^{\top}{\bf y}.$$

## Invertibility And Uniqueness

Note that the Gram matrix $X^⊤ \times X ∈ R^{D×D}$ is invertible if and only if X has full column rank, or in other words *rank*(X) = D.

Proof: To see this assume first that rank(X) < D. Then there exists a non-zero vector u so that Xu = 0. It follows that X⊤Xu = 0, and so rank(X⊤X) *< D*. Therefore, X⊤X is not invertible.

Conversely, assume that $X^⊤ \times X$ is not invertible. Hence, there exists a non-zero vector v so that $X^⊤ \times X u = 0$. It follows that
$$\mathbf{0}=\mathbf{v}^{\top}\mathbf{X}^{\top}\mathbf{X}\mathbf{v}=(\mathbf{X}\mathbf{v})^{\top}(\mathbf{X}\mathbf{v})=\|\mathbf{X}\mathbf{v}\|^{2}.$$

This implies that Xv = 0, i.e., rank(X) < D.

## Rank Deficiency And Ill-Conditioning

Unfortunately, in practice, X is often rank deficient.

- If *D > N*, we always have rank(X) < D (since row rank = col. rank)
- If D ≤ N, but some of the columns x_{:d} are (nearly)
collinear, then the matrix is illconditioned, leading to numerical issues when solving the linear system.

Can we solve least squares if X is rank deficient? Yes, using a linear system solver.

## Summary Of Linear Regression

We have studied three types of methods:

1. Grid Search 
2. Iterative Optimization Algorithms : (Stochastic) Gradient Descent
3. Least squares : closed-form solution, for linear MSE