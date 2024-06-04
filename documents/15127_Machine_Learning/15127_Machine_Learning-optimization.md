# Optimization

## Learning / Estimation / Fitting

Given a cost function L(w), we wish to find w⋆ which minimizes the cost:
$$min_w L(w)$$ subject to w ∈ R^D

This means the *learning* problem is formulated as an optimization problem. We will use an optimization algorithm to solve the problem (to find a good w).

## Grid Search 

Grid search is one of the simplest optimization algorithms. We compute the cost over all values w in a grid, and pick the best among those.

This is brute-force, but extremely simple and works for any kind of cost function when we have very few parameters and the cost is easy to compute.

For a large number of parameters D, however, grid search has too many "for-loops", resulting in an exponential computational complexity: If we decide to use 10 possible values for each dimension of w, then we have to check 10D points.

This is clearly impossible for most practical machine learning models, which can often have D ≈ millions of parameters.

Choosing a good range of values for each dimension is another problem.

Other issues: No guarantee can be given that we end up close to an optimum.

## Optimization Landscapes

A vector w⋆ is a local minimum of L if it is no worse than its neighbors; i.e. there exists an ϵ > 0 such that, L(w⋆) ≤ L(w), ∀w with ∥w − w⋆∥ < ϵ.

A vector w⋆ is a global minimum of L if it is no worse than all others, L(w⋆) ≤ L(w), ∀w ∈ R^D

A local or global minimum is said to be strict if the corresponding inequality is strict for w ̸= w⋆.

## Smooth Optimization

Follow the Gradient A gradient (at a point) is the slope of the tangent to the function (at that point).

It points to the direction of largest increase of the function.

**Definition of the gradient:**

$$\nabla{\mathcal{L}}(\mathbf{w}):=\left[{\frac{\partial{\mathcal{L}}(\mathbf{w})}{\partial w_{1}}},\ldots,{\frac{\partial{\mathcal{L}}(\mathbf{w})}{\partial w_{D}}}\right]^{\top}$$

This is a vector, ∇L(w) ∈ RD.

# Gradient Descent 

To minimize the function, we iteratively take a step in the (opposite) direction of the gradient $w^{(t+1)} := w^{(t)} − γ∇L(w^{(t)})$, where *γ >* 0 is the step-size (or learning rate).

Then repeat with the next t.

**Example:**
Gradient descent for 1- parameter model to minimize MSE:

$$w_{0}^{(t+1)}:=(1-\gamma)w_{0}^{(t)}+\gamma\bar{y}$$

where $\bar{y}:=\sum_{n}y_{n}/N$. When is this sequence guaranteed to converge?

## Gradient Descent For Linear Mse

For linear regression

$$\mathbf{y}={\left[\begin{array}{l}{y_{1}}\\ {y_{2}}\\ {\vdots}\\ {y_{N}}\end{array}\right]}\,,\mathbf{X}={\left[\begin{array}{l l l l}{x_{11}}&{x_{12}}&{\cdot\cdot\cdot}&{x_{1D}}\\ {x_{21}}&{x_{22}}&{\cdot\cdot\cdot}&{x_{2D}}\\ {\vdots}&{\vdots}&{\cdot\cdot\cdot}&{\vdots}\\ {x_{N1}}&{x_{N2}}&{\cdot\cdot\cdot}&{x_{N D}}\end{array}\right]}$$

We define the error vector $\mathbf{e}$: $e = y − Xw$ 

and MSE as follows:
$$\begin{array}{c}{{{\mathcal L}(\mathbf{w}):=\frac1{2N}\sum_{n=1}^{N}\left(y_{n}-\mathbf{x}_{n}^{\top}\mathbf{w}\right)^{2}}}\\ {{=\frac1{2N}\mathbf{e}^{\top}\mathbf{e}}}\end{array}$$

then the gradient is given by
$$\nabla{\mathcal{L}}(\mathbf{w})=-{\frac{1}{N}}\mathbf{X}^{\top}\mathbf{e}$$


## Variant with offset.

Recall: Alternative trick when also incorporating an offset term for the regression:

$$\mathbf{y}={\left[\begin{array}{l}{y_{1}}\\ {y_{2}}\\ {\vdots}\\ {y_{N}}\end{array}\right]}\qquad{\widetilde{\mathbf{X}}}={\left[\begin{array}{l l l l l}{1}&{x_{11}}&{x_{12}}&{\cdot\cdot\cdot}&{x_{1D}}\\ {1}&{x_{21}}&{x_{22}}&{\cdot\cdot\cdot}&{x_{2D}}\\ {\vdots}&{\vdots}&{\vdots}&{\ddots}&{\vdots}\\ {1}&{x_{N1}}&{x_{N2}}&{\cdot\cdot\cdot}&{x_{N D}}\end{array}\right]}$$


## Stochastic Gradient 

### Descent Sum Objectives.

In machine learning, most cost functions are formulated as a sum over the training examples, that is

$${\mathcal L}({\bf w})=\frac{1}{N}\sum_{n=1}^{N}{\mathcal L}_{n}({\bf w})\ ,$$

where Ln is the cost contributed by the n-th training example.

### The SGD Algorithm.

The stochastic gradient descent (SGD) algorithm is given by the following update rule, at step t:

$${\bf w}^{(t+1)}:={\bf w}^{(t)}-\gamma\,\nabla{\cal L}_{n}({\bf w}^{(t)})\ .$$

### Theoretical Motivation.

Idea: Cheap but unbiased estimate of the gradient!

In expectation over the random choice of n, we have
$$\mathbb{E}\left[\nabla{\mathcal{L}}_{n}(\mathbf{w})\right]=\nabla{\mathcal{L}}(\mathbf{w})$$
which is the true gradient direction.

### Mini-batch SGD.

There is an intermediate version, using the update direction being

$${\bf g}:=\frac{1}{|B|}\sum_{n\in B}\nabla{\mathcal L}_{n}({\bf w}^{(t)})$$
again with
$${\bf w}^{(t+1)}:={\bf w}^{(t)}-\gamma\,{\bf g}\ .$$

In the above gradient computation, we have randomly chosen a subset B ⊆ [N] of the training examples. For each of these selected examples n, we compute the respective gradient ∇Ln, at the same current point w^{(t)}.

The computation of g can be parallelized easily.

This is how current deep-learning applications utilize GPUs (by running over |B| threads in parallel).

Note that in the extreme case B := [N], we obtain (batch) gradient descent, i.e. g = ∇L.

## Non-Smooth Optimization

An alternative characterization of convexity, for differentiable functions is given by
$${\mathcal{L}}(\mathbf{u})\geq{\mathcal{L}}(\mathbf{w})+\nabla{\mathcal{L}}(\mathbf{w})^{\top}(\mathbf{u}-\mathbf{w})\quad\forall\mathbf{u},\mathbf{w}$$
meaning that the function must always lie above its linearization.

## Subgradients

A vector g ∈ RD such that
$${\mathcal{L}}(\mathbf{u})\geq{\mathcal{L}}(\mathbf{w})+\mathbf{g}^{\top}(\mathbf{u}-\mathbf{w})\quad\forall\mathbf{u}$$
is called a subgradient to the function L at w.

This definition makes sense for objectives L which are not necessarily differentiable (and not even necessarily convex).

If L is convex and differentiable at w, then the only subgradient at w is g = ∇L(w).

## Subgradient Descent

Identical to the gradient descent algorithm, but using a subgradient instead of gradient. Update rule

$$\mathbf{w}^{(t+1)}:=\mathbf{w}^{(t)}-\gamma\,\mathbf{g}$$
for g being a subgradient to L at the current iterate w(t).

## Stochastic Subgradient Descent

Same, g being a subgradient to the randomly selected Ln at the current iterate w^{(t)}.

## Constrained Optimization

Sometimes, optimization problems come posed with additional constraints:
$$min_w L(w)$$, subject to w ∈ C.

The set C ⊂ R^D is called the constraint set.

## Solving Constrained Optimization Problems

A) Projected Gradient Descent
B) Transform it into an unconstrained problem

## Convex Sets

A set C is convex iff the line segment between any two points of C lies in C, i.e., if for any u, v *∈ C* and any θ with 0 ≤ θ ≤ 1, we have

## Properties Of Convex Sets

- Intersections of convex sets are convex
- Projections onto convex sets are *unique*.
- Formal definition: $P_C(w′) := arg min_{v∈C} ∥v − w′∥$.

Roughly speaking, a set is convex if every point in the set can be seen by every other point, along an unobstructed straight path between them, where unobstructed means lying in the set. Every affine set is also convex, since it contains the entire line between any two distinct points in it, and therefore also the line segment

## Projected Gradient Descent

Idea: add a projection onto C after every step:

$$P_{\mathcal{C}}(\mathbf{w}^{\prime}):=\arg\operatorname*{min}_{\mathbf{v}\in\mathcal{C}}\left\|\mathbf{v}-\mathbf{w}^{\prime}\right\|\,.$$

Update rule:
$${\bf w}^{(t+1)}:=P_{\cal C}\big[{\bf w}^{(t)}-\gamma\;\nabla{\cal L}({\bf w}^{(t)})\big]\ .$$

### Projected SGD.

Same SGD step, followed by the projection step, as above.

Same convergence properties. Computational cost of projection? Crucial!

### Turning Constrained into Unconstrained Problems
(Alternatives to projected gradient methods)

Use penalty functions instead of directly solving $min_{w∈C} L(w)$.

* "_brick wall_" (indicator function) $\mathbf{w}\in\mathcal{C}$ $\mathbf{L}(\mathbf{w}):=\begin{cases}0&\mathbf{w}\in\mathcal{C}\\ \infty&\mathbf{w}\notin\mathcal{C}\end{cases}$ $\mathbf{w}\in\mathbb{R}^{D}$ (disadvantage: non-continuous objective)
* $\mathbf{P}$ penalize error. $\mathbf{L}$ $\mathbf{w}=\mathbf{b}$ $\mathbf{C}=\{\mathbf{w}\in\mathbb{R}^{D}\mid A\mathbf{w}=\mathbf{b}\}$ $\mathbf{w}\in\mathbb{R}^{D}$
- Linearized Penalty Functions (see Lagrange Multipliers)

## Implementation Issues For gradient methods

1. Stopping criteria:
When ∇L(w) is (close to) zero, we are (often) close to the optimum value.

2. Optimality:
If the second-order derivative is positive (positive semidefinite to be precise), then it is a (possibly local) minimum.
If the function is also convex, then this condition implies that we are at a global optimum. 

3. Step-size selection:
If γ is too big, the method might diverge. If it is too small, convergence is slow. Convergence to a local minimum is guaranteed only when γ < γmin where γmin is a fixed constant that depends on the problem.

4. Line-search methods:
For some objectives L, we can set step-size automatically using a line-search method.

5. Feature normalization and preconditioning:
Gradient descent is very sensitive to ill-conditioning. Therefore, it is typically advised to normalize your input features. In other words, we pre-condition the optimization problem.
Without this, step-size selection is more difficult since different "directions" might converge at different speed.

## Non-Convex Optimization

Real-world problems are not convex! All we have learnt on algorithm design and performance of convex algorithms still helps us in the nonconvex world.