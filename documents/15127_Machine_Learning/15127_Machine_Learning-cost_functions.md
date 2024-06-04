# Cost Functions Sept 22, 2022

## Motivation Consider The Following Models.

1-parameter model: $y_n ≈ w_0$
2-parameter model: $y_n ≈ w_0 + w_1 \dot x_{n1}$
How can we estimate (or guess) values of w given the data D?

## What is a cost function?

A cost function (or energy, loss, training objective) is used to learn parameters that explain the data well.

The cost function quantifies how well our model does - or in other words how costly our mistakes are.

## Two Desirable Properties Of Cost Functions

When the target y is real-valued, it is often desirable that the cost is symmetric around 0, since both positive and negative errors should be penalized equally. Also, our cost function should penalize "large" mistakes and "very large" mistakes similarly.

## Statistical Vs Computational Trade-Off

If we want better statistical properties, then we have to give-up good computational properties.

## Mean Square Error (Mse)

MSE is one of the most popular cost functions.

$$\mathrm{MSE}(\mathbf{w}):={\frac{1}{N}}\sum_{n=1}^{N}\left[y_{n}-f_{\mathbf{w}}(\mathbf{x}_{n})\right]^{2}$$

Does this cost function have both mentioned properties?

## Outliers 

Outliers are data examples that are far away from most of the other examples.

Unfortunately, they occur more often in reality than you would want them to! MSE is not a good cost function when outliers are present. 

## Mean Absolute Error (Mae)

$$\left|y_{n}-f_{\mathbf{w}}(\mathbf{x}_{n})\right|$$

## Convexity

Roughly, a function is convex iff a line segment between two points on the function's graph always lies above the function.

A function h(u) with u ∈ R^D is convex, if for any u, v ∈ R^D and for any 0 ≤ λ ≤ 1, we have: 
$$h(λu + (1 − λ)v) ≤ λh(u) + (1 − λ)h(v)$$
A function is strictly convex if the inequality is strict.

## Importance Of Convexity

A strictly convex function has a unique global minimum w⋆.

For convex functions, every local minimum is a global minimum. Sums of convex functions are also convex. Therefore, MSE combined with a linear model is convex in w.

Convexity is a desired computational property.

## Computational Vs Statistical Trade-Off

So which loss function is the best?

If we want better statistical properties, then we have to give-up good computational properties.

## Additional Reading Other Cost Functions

### Huber loss

$$Huber(e):=\left\{\begin{array}{l l}{{\frac{1}{2}e^{2}}}&{{,\mathrm{if~}|e|\leq\delta}}\\ {{\delta|e|-\frac{1}{2}\delta^{2}}}&{{,\mathrm{if~}|e|>\delta}}\end{array}\right.\eqno(1)$$

Huber loss is convex, differentiable, and also robust to outliers. However, setting δ is not an easy task.

### Tukey's bisquare loss (defined in terms of the gradient)

$${\frac{\partial{\mathcal{L}}}{\partial e}}:={\left\{\begin{array}{l l}{e\{1-e^{2}/\delta^{2}\}^{2}}&{{,\mathrm{if~}|e|\leq\delta}}\\ {0}&{{,\mathrm{if~}|e|>\delta}}\end{array}\right.}\qquad\qquad(2)$$
Tukey's loss is non-convex, but robust to outliers.