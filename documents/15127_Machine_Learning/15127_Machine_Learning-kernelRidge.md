# Kernel Ridge Regression And The Kernel Trick


## Motivation

In our last lecture we formulated the optimization problem corresponding to SVMs.

We then derived an alternative formulation using duality. We saw that in this alternative formulation the data only enters in the form of a "kernel" K = XX^⊤.

The aim of today is the following.

First, we will discuss a second problem, namely ridge regression, that admits an alternative formulation that is "kernelized," i.e., the alternative formulation depends on the data only via the kernel K = XX⊤.

Second, we will see that for any kernelized problem we can apply the *kernel trick*. This trick will allow us to use a significantly augmented feature vector without incurring extra costs. We will discuss what kernel functions are *admissible* for this trick and how to construct new kernel functions from old ones. Even though we present the kernel trick in the context of ridge regression it will hopefully be clear by the end that the same trick can be applied to any problem that can be brought into kernelized form.

## Alternative Formulation Of Ridge Regression

Recall that ridge regression corresponds to the following optimization problem:

$$\operatorname*{min}_{\bf w}\quad\frac{1}{2N}\|{\bf y}-{\bf X}{\bf w}\|^{2}\,+\,\frac{\lambda}{2}\|{\bf w}\|^{2}.$$

It has the solution
$${\bf w}^{\star}=\frac{1}{N}(\frac{1}{N}{\bf X}^{\top}{\bf X}+\lambda{\bf I}_{D})^{-1}{\bf X}^{\top}{\bf y}.$$

We claim that this solution can be written alternatively as
$$\mathbf{w}^{\star}={\frac{1}{N}}\mathbf{X}^{\mathsf{T}}({\frac{1}{N}}\mathbf{X}\mathbf{X}^{\mathsf{T}}+\lambda\mathbf{I}_{N})^{-1}\mathbf{y}.\qquad\qquad(1)$$

This second formulation can be proved using the following identity: let P be an N × M matrix and Q be an M × N
matrix. Then, trivially,

$$\mathbf{P}(\mathbf{Q}\mathbf{P}+\mathbf{I}_{M})=\mathbf{P}\mathbf{Q}\mathbf{P}+\mathbf{P}=(\mathbf{P}\mathbf{Q}+\mathbf{I}_{N})\mathbf{P}.$$

If we now assume that (QP + I_M) and (PQ + I_N) are invertible we have the identity
$$({\bf P Q}+{\bf I}_{N})^{-1}{\bf P}={\bf P}({\bf Q P}+{\bf I}_{M})^{-1}.$$

To derive from this general statement our alternative representation, let P = X^⊤ and Q = \frac{1}{λN}X.

Why is this alternative representation useful?

1. The original formulation involves computation of order
O(D^3 + ND^2), while the second can be computed in
time O(N^3 + DN^2). Hence it depends on the size of
D and N which of the two is more efficient.
2. We will see that (1) and (2) are the crucial ingredients for the kernel trick to work.

## The Representer Theorem

The representer theorem generalizes this result: for a w⋆
minimizing the following function for any Ln,

$$\operatorname*{min}_{\mathbf{w}}\ \frac{1}{N}\sum_{n=1}^{N}\mathcal{L}_{n}(\mathbf{x}_{n}^{\top}\mathbf{w},\,y_{n})+\frac{\lambda}{2}\|\mathbf{w}\|^{2}$$

there exists $\boldsymbol{\alpha}^{\star}$ such that $\mathbf{w}^{\star}=\mathbf{X}^{\top}\boldsymbol{\alpha}^{\star}$.


## Kernelized Ridge Regression

Let us go back to ridge regression. The representer theorem allows us to write an equivalent optimization problem in terms of α:

$$\begin{array}{l l}{{{\bf w^{\star}=\operatorname*{arg\,min}}}}&{{{\frac{1}{2N}}||{\bf y}-{\bf X w}||^{2}\,+\,{\frac{\lambda}{2}}||{\bf w}||^{2}}}\\ {{}}&{{}}\\ {{{\boldsymbol{\alpha^{\star}=\operatorname*{arg\,min}}}}}&{{{\frac{1}{2}}{\boldsymbol{\alpha}}^{\top}({\frac{1}{N}}{\bf X X^{\top}}+\lambda{\bf I}_{N}){\boldsymbol{\alpha}}-{\frac{1}{N}}{\boldsymbol{\alpha}}^{\top}{\bf y}\,.}}\end{array}$$
To see that these two problems have equivalent solutions, note that if we take the gradient of the second expression we get (XX^⊤ + λI_ N)α − y. Setting this to 0 and solving for α results in

$$\mathbf{\alpha}^{\star}={\frac{1}{N}}({\frac{1}{N}}\mathbf{X}\mathbf{X}^{\top}+\lambda\mathbf{I}_{N})^{-1}\mathbf{y}.$$

If we combine this with the representer theorem $w^⋆ = X^⊤ \times α⋆$,  we find back the solution (1).

As we discussed previously, depending on the D, the dimension of the feature space, and N, the number of samples, one or the other of the two formulations might be more efficient.

But there is an arguably even more important reason why the second expression is of interest. In this second expression the data only enters in terms of the kernel matrix K = XX^⊤.

## The Kernel Trick

The big advantage of using kernels is that rather than first augmenting the feature space and then computing the kernel, we can do both steps together, and we can do it more efficiently. Let us discuss how this works.

Let us define a "kernel function" κ(x, x′) and let us compute the (*i, j*)-th entry of K as K_{ij} = κ(x_i, x_j). For the right choice of kernel κ it turns out to be equivalent to first augmenting the features to some suitable φ(x) and then computing the inner product $φ(X)^⊤ φ(X′)$ in the augmented space. In other words, for the right choices we have $κ(x, x′) = φ(x)^⊤ φ(x′)$.

This is probably best seen by looking at examples:

1. To start trivially, if we pick the linear kernel $κ(x, x′) = x^⊤ x′$, then the corresponding feature map is of course φ(x′) = x′.
2. Assume that x ∈ R, i.e., x is a scalar. The kernel
κ(x, x′) = (xx′)^2 corresponds to φ(x) = x^2.
3. Assume that ${\bf x}\in\mathbb{R}^{3}$, i.e., ${\bf x}$ is a vector of dimension 3. The kernel $\kappa({\bf x},{\bf x}^{\prime})=(x_{1}x_{1}^{\prime}+x_{2}x_{2}^{\prime}+x_{3}x_{3}^{\prime})^{2}$ corresponds to

$\mathbf{\phi(x)}^{\top}=\left[\begin{array}{cc}x_{1}^{2},&x_{2}^{2},&x_{3}^{2},&\sqrt{2}x_{1}x_{2},&\sqrt{2}x_{1}x_{3},&\sqrt{2}x_{2}x_{3}\end{array}\right].$

This is an example of what is called a polynomial kernel.

4. The kernel $κ(x, x′) = exp  −(x − x′)^⊤ (x − x′)$
corresponds to an infinite feature map! It is called the the *radial basis function* (RBF) kernel. In order to look at this more in detail, consider the simple case where the x and x′ are scalars. 

5. Building new kernels from old kernels.
- κ(x, x′) = aκ_1(x, x′) + bκ_2(x, x′) for all a, b ≥ 0.

Proof. By assumption κ1 and κ2 are valid kernels.

Hence there exist feature maps φ1 and φ2 so that
κ1(x, x′) = φ1(x)^⊤ φ1(x′),
κ2(x, x′) = φ2(x)^⊤ φ2(x′).

Hence,
$$\kappa({\bf x},{\bf x^{\prime}})=a\phi_{1}({\bf x})^{\top}\phi_{1}({\bf x^{\prime}})+b\phi_{2}({\bf x})^{\top}\phi_{2}({\bf x^{\prime}}).$$

This can be represented as an inner product via the feature map
$$(\sqrt{a}\phi_{1}(\cdot),\sqrt{b}\phi_{2}(\cdot)).$$

- κ(x, x′) = κ1(x, x′)κ2(x, x′).

- κ(x, x′) = κ1(f(x), f(x′)) for any f from the domain to itself.

- κ(x, x′) = f(x)f(x′) for any real-valued f. Clearly,
φ(x) = f(x) will be the corresponding feature map.

## Classifying With The Kernel K

We have seen so far how we can compute the optimal parameter vector α using only the kernel (and not having to go to the extended feature space). We have also discussed that in some cases the feature space is in fact infinite. All this would not be useful if there was not also a way to do the prediction using only the kernel. Indeed this is possible.

Recall that the classifier predicts $y = φ(x)^⊤ \times w∗$ which, using (2), can be expressed as

$$y=\phi(\mathbf{x})^{\top}\phi(\mathbf{X})^{\top}\alpha=\sum_{n=1}^{N}\kappa(\mathbf{x},\mathbf{x}_{n})\alpha_{n}.$$

I.e., we can express the prediction in terms of the kernel function applied to the new feature vector and the data vector in the original space and do not need to go into the augmented space. From this expression we can also clearly see that although the classifier in the extended space φ(x) is linear, if we look at the decision regions in the original space x it is non-linear.

## Properties Of Kernels: Mercer'S Condition

A natural question is the following: how can we ensure that there exists a φ corresponding to a given kernel function κ?

I.e., how do we ensure that the kernel function is an innerproduct in some feature space? Mercer's condition states that this is true if and only if the following two conditions are fulfilled. In the following, given the kernel function κ and some arbitrary input set {xn}_n, let K be the associated kernel matrix, K_{i,j} = κ(x_i, x_j).

1. The kernel function κ must be symmetric, i.e. κ(x, x′) = κ(x′, x); equivalently, the kernel matrix K must be
symmetric for all possible input sets.
2. The kernel matrix K must be positive semi-definite for
all possible input sets.