# Support Vector Machines 

## Motivation

Let us re-consider binary classification with data pairs (xn, ˜yn), ˜yn ∈ {0, 1}. We use here the notation ˜yn to denote variables that take values in {0, 1} since soon we will transform our labels to take values in {±1} and we want to avoid confusion.

As we had discussed, if we use least squares (not recommended!) and ignore right now any potential regularization term this lead us to the minimization

$$\operatorname*{min}_{\mathbf{w}}{\frac{1}{N}}\sum_{n=1}^{N}({\tilde{y}}_{n}-\mathbf{x}_{n}^{\top}\mathbf{w})^{2}.$$

If instead we use logistic regression and optimize the loglikelihood, we solve
$$\operatorname*{min}_{\mathbf{w}}{\frac{1}{N}}\sum_{n=1}^{N}\log(1+e^{\mathbf{x}_{n}^{\mathsf{T}}\mathbf{w}})-{\tilde{y}}_{n}\mathbf{x}_{n}^{\mathsf{T}}\mathbf{w}.$$

In the following it will be slightly more convenient to assume that yn ∈ {±1}, where we have the mappings 0 ↔ −1 and 1 ↔ 1. We can write this compactly as yn = 2˜yn − 1, or equivalently, ˜yn = 1 2(yn + 1).

Consider first the least squares problem. Assume, as always, that the feature vector contains the constant feature 1 and that this is component 0. Define ˜w = 1
2(w + e0), where e0 is the vector of length D (the dimension of the feature vector) that has a 1 at component 0 and 0 at all other components.

Note that this defines a one-to-one mapping between w and
˜w. We then have
$$4\sum_{n=1}^{N}(\tilde{y}_{n}-\mathbf{x}_{n}^{\top}\tilde{\mathbf{w}})^{2}=4\sum_{n=1}^{N}(\frac{1}{2}(y_{n}+1)-\frac{1}{2}\mathbf{x}_{n}^{\top}(\mathbf{w}+e_{0}))^{2}$$ $$=\sum_{n=1}^{N}((y_{n}+1)-\mathbf{x}_{n}^{\top}(\mathbf{w}+e_{0}))^{2}$$ $$=\sum_{n=1}^{N}(y_{n}-\mathbf{x}_{n}^{\top}\mathbf{w})^{2}$$ $$\stackrel{{(a)}}{{=}}\sum_{n=1}^{N}(1-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w})^{2}$$ $$=\sum_{n=1}^{N}\operatorname{MSE}(\mathbf{x}_{n}^{\top}\mathbf{w},y_{n}),$$
where MSE(z, y) = (1 − yz)^2.

In step (a) we have used the fact that yn{±1} so that y_n^2 = 1.

In a similar manner, for logistic regression we have
$$\sum_{n=1}^{N}\log(1+e^{\mathbf{x}_{n}^{\top}\mathbf{w}})-\tilde{y}_{n}\mathbf{x}_{n}^{\top}\mathbf{w}=\sum_{n=1}^{N}\log(1+e^{-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w}})$$ $$=\sum_{n=1}^{N}\text{LogisticLoss}(\mathbf{x}_{n}^{\top}\mathbf{w},\,y_{n}),$$
where LogisticLoss(z, y) = log(1 + exp(−yz)).

This is most easily seen by checking the two cases ˜yn = 0 ↔ yn = −1 and ˜yn = 1 ↔ yn = 1 separately.

Note that above, z is the prediction based on the given data point and y is the label associated to the data point. We get support vector machines (SVMs), if instead we use the loss Hinge(z, y) = [1 − yz]+ = max{0, 1 − yz}, and add a regularization term.

## Support Vector Machine

As just mentioned, SVMs correspond to the following optimization problem:
$$\operatorname*{min}_{\bf w}\;\frac{1}{N}\sum_{n=1}^{N}\left[1-y_{n}{\bf x}_{n}^{\top}{\bf w}\right]_{+}+\frac{\lambda}{2}\|{\bf w}\|^{2}.$$

Note that for least squares we incur a cost whenever we fail to represent the desired value exactly and the cost is symmetric around the target value. For logistic regression we always incur a cost but the cost is asymmetric - it becomes smaller the further we are "on the right side" and it becomes larger the further we are "on the wrong side." The hinge loss acts differently. Once we are "sufficiently far" on the right side we no longer pay a cost. But if we are not yet far enough on the correct side or if we are on the wrong side we do pay a cost and the cost increases linearly the further we are away.

In the figure below you see a region in pink. This region is called the "margin." It is defined as follows: Take the normal vector w that defines the hyperplane. Look at all feature vectors x so that |x^⊤w| ≤ 1. This is the margin.

Note that the margin does not only depend on the direction of the vector w but also its norm. In fact the total width of the margin is equal to 2/∥w∥.

If you are looking for an interpretation: It is the region where our prediction is not yet sufficiently "confident" (assuming that we get the sign right). The intuition is strongest if we look at the case of separable data.

This is shown in the following two figures (left with a large margin and therefore small ∥w∥, and right with small margin that corresponds A glance at Figure 9.6 reveals that αi is linked with yi (and therefore with w, b)
to a large ∥w∥). Assume that λ is small so that the cost function is dominated by the sum over the hinge losses on the left. What will the optimal w look like in this case? It is clear that we want the following:

1. A separating hyperplane.
2. A scaling of w so that no point of the data is in the
margin.
3. That separating hyperplane and scaling for which the
margin is the largest.

Conditions (1) and (2) ensure that there is no cost incurred in the first expression.
Since by assumption that λ is small this is the dominant term, we cannot hope to do better than having this term to be 0. The condition (3) ensures that we have the minimum possible cost associated for the regularization term, i.e.
the minimal possible normed squared ∥w∥^2.

Geometrically, this corresponds to a hyperplane with maximal "spacing" to the left and right, i.e., a hyperplane with maximal margin (corresponding to the figure on the left).

NOTE: We have introduced our formulation of SVMs for the general case where the data is not necessarily linearly separable. This is sometimes called the *soft-margin* formulation.

The *hard-margin* formulation concerns the case where the data is linearly separable and where we insist that the decision region is given in terms of a separating hyperplane. In this case the formulation would require us to find a separating hyperplane with minimal ∥w∥2. In other words, the optimal solution is a separating hyperplane with maximal margins. And in this case there must be some feature vectors which lie exactly on the boundaries (otherwise we could enlarge the margin, contradicting optimality). These feature vectors "support" the boundaries and hence the name "support vector." For the soft-margin case this interpretation is only approximately true as we have explained in the previous paragraphs.


## Optimization

Now where we have established *what function* we are optimizing, let us look at the question *how* we can optimize it efficiently. 

Note that the function is convex and and has a subgradient
(in w):
$$\min_{\mathbf{w}}\ \frac{1}{N}\sum_{n=1}^{N}\left[1-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w}\right]_{+}+\frac{\lambda}{2}\|\mathbf{w}\|^{2}$$

We can therefore use SGD with subgradients. This is good news!

## Duality: The Big Picture

We have just seen that we can use SGD in order to find the optimal parameters for the SVM. We will now discuss an alternative but equivalent formulation via the concept of duality. In some cases this leads to a more efficient implementation. But perhaps more importantly, once we have derived this alternative representation it will point us naturally to a more general formulation. This is called the kernel trick. We will explicitly discuss this technique in a separate lecture.

Let us say that we are interested in minimizing a function L(w).

Assume that we can define an auxiliary function G(w, α) so that
$${\mathcal{L}}(\mathbf{w})=\operatorname*{max}_{\boldsymbol{\alpha}}\;G(\mathbf{w},\boldsymbol{\alpha}).$$

We can therefore solve our original problem by solving
$$\operatorname*{min}_{\mathbf{w}}\operatorname*{max}_{\mathbf{\alpha}}G(\mathbf{w},\mathbf{\alpha}).$$

We call this the *primal* problem. In some cases it might be much easier to find
$$\operatorname*{max}_{\boldsymbol{\alpha}}\operatorname*{min}_{\boldsymbol{w}}G(\mathbf{w},{\boldsymbol{\alpha}}).$$

We call this the *dual* problem. This leads us naturally to the following questions:

1. How do we find a suitable G(w, α)?
2. When is it OK to switch min_w and max_α ?
3. When is the dual easier to optimize than the primal?

Q1: How do we find a suitable G(w, α)? There is a general theory on this topic (see e.g., Bertsekas' "Nonlinear Programming" for more formal details). But rather than talk about this in the abstract, let us look at our specific problem. We have
$$[z]_{+}=\operatorname*{max}\{0,z\}=\operatorname*{max}_{\alpha\in[0,1]}\alpha z.$$

Therefore,
$$[1-y_{n}{\bf x}_{n}^{\top}{\bf w}]_{+}=\operatorname*{max}_{\alpha_{n}\in[0,1]}\alpha_{n}(1-y_{n}{\bf x}_{n}^{\top}{\bf w}).$$

So we can rewrite the SVM problem as:
$$\min_{\mathbf{w}}\max_{\mathbf{\alpha}\in[0,1]^{N}}\ \underbrace{\frac{1}{N}\sum_{n=1}^{N}\alpha_{n}(1-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w})+\frac{\lambda}{2}\|\mathbf{w}\|^{2}}_{G(\mathbf{w},\mathbf{\alpha})}$$

Note that $G(\mathbf{w},\mathbf{\alpha})$ is convex in $\mathbf{w}$ and linear, hence concave, in $\mathbf{\alpha}$.

**Q2:** When is it OK to switch max and min?
Note that it is always true that
$$\operatorname*{max}_{\boldsymbol{\alpha}}\operatorname*{min}_{\boldsymbol{w}}G(\mathbf{w},\boldsymbol{\alpha})\leq\operatorname*{min}_{\boldsymbol{w}}\operatorname*{max}_{\boldsymbol{\alpha}}G(\mathbf{w},\boldsymbol{\alpha}).$$

This is easy to see:
$$\operatorname*{min}_{{\bf w}^{\prime}}G({\bf w}^{\prime},{\boldsymbol{\alpha}})\leq G({\bf w},{\boldsymbol{\alpha}})\;\;\forall{\bf w},{\boldsymbol{\alpha}},\Leftrightarrow$$
$$\operatorname*{max}_{{\boldsymbol{\alpha}}}\operatorname*{min}_{{\bf w}^{\prime}}G({\bf w}^{\prime},{\boldsymbol{\alpha}})\leq\operatorname*{max}_{{\boldsymbol{\alpha}}}G({\bf w},{\boldsymbol{\alpha}})\;\;\forall{\bf w}\Leftrightarrow$$
$$\operatorname*{max}_{{\boldsymbol{\alpha}}}\operatorname*{min}_{{\bf w}^{\prime}}G({\bf w}^{\prime},{\boldsymbol{\alpha}})\leq\operatorname*{min}_{{\boldsymbol{w}}}\operatorname*{max}_{{\boldsymbol{\alpha}}}G({\bf w},{\boldsymbol{\alpha}}).$$

We get equality if G(w, α) is a continuous function that is convex in w, concave in α, and the domain of w and α are both compact and convex. I.e., in this case we have
$$\operatorname*{min}_{\mathbf{w}}\operatorname*{max}_{\mathbf{\alpha}}G(\mathbf{w},\mathbf{\alpha})=\operatorname*{max}_{\mathbf{\alpha}}\operatorname*{min}_{\mathbf{w}}G(\mathbf{w},\mathbf{\alpha}).$$

In other words, we get equality if we have functions that look like saddles as in the previous figure. For SVMs the condition is fulfilled and we can switch the min and max. This leads to the following formulation
$$\operatorname*{max}_{\mathbf{\alpha}\in[0,1]^{N}}\operatorname*{min}\ {\frac{1}{N}}\sum_{n=1}^{N}\alpha_{n}(1-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w})+{\frac{\lambda}{2}}\|\mathbf{w}\|^{2}.\qquad(1)$$

Taking the derivative w.r.t. w we get
$$\nabla_{\mathbf{w}}\,G(\mathbf{w},\mathbf{\alpha})=-{\frac{1}{N}}\sum_{n=1}^{N}\alpha_{n}y_{n}\mathbf{x}_{n}+\lambda\mathbf{w}.$$

Equating this to 0, we can explicitly solve for w for any given α. We get
$$\mathbf{w}(\alpha)={\frac{1}{\lambda N}}\sum_{n=1}^{N}\alpha_{n}y_{n}\mathbf{x}_{n}={\frac{1}{\lambda N}}\mathbf{X}^{\top}\mathbf{Y}\alpha,$$
where Y := diag(y).

Plugging this w = w(α) back into the saddle-point formulation (1), gives rise to the following dual optimization problem:
$$\begin{array}{c}{{\operatorname*{max}_{\mathbf{\alpha}\in[0,1]^{N}}\frac{1}{N}\sum_{n=1}^{N}\alpha_{n}(1-\frac{1}{\lambda N}y_{n}\mathbf{x}_{n}^{\top}\mathbf{X}^{\top}\mathbf{Y}\mathbf{\alpha})+\frac{\lambda}{2}\|\frac{1}{\lambda N}\mathbf{X}^{\top}\mathbf{Y}\mathbf{\alpha}\|^{2}}}\\ {{=\operatorname*{max}_{\mathbf{\alpha}\in[0,1]^{N}}\frac{1}{N}\mathbf{\alpha}^{\top}\mathbf{1}-\frac{1}{2\lambda N^{2}}\mathbf{\alpha}^{\top}\mathbf{Y}\mathbf{X}\mathbf{X}^{\top}\mathbf{Y}\mathbf{\alpha}.}}\end{array}$$

Q3: When is the dual easier to optimize than the primal, and why?
- The dual is a differentiable (but constrained) quadratic
problem.
$$\operatorname*{max}_{\boldsymbol{\alpha}\in[0,1]^{N}}\ {\boldsymbol{\alpha}}^{\top}\mathbf{1}-{\frac{1}{2\lambda N}}{\boldsymbol{\alpha}}^{\top}\mathbf{Q}{\boldsymbol{\alpha}},$$
where Q := diag(y)XX^⊤diag(y).

Optimization is easy by using coordinate descent, or more precisely coordinate ascent since this is a maximization problem.

Crucially, this method will be changing only one αn variable a time.

- Note that in the dual formulation the data only enters
in the form K := XX^⊤. This product XX^⊤ is called
the "kernel." We hence often say that this formulation
is *kernelized*. As we will discuss in the next lecture,
this has a very pleasing consequence.

- The solution α is typically sparse, and is non-zero only
for the training examples that are instrumental in determining the decision boundary.
Recall the how the parameters αn were introduced:
$$[1-y_{n}{\bf x}_{n}^{\top}{\bf w}]_{+}=\operatorname*{max}_{\alpha_{n}\in[0,1]}\alpha_{n}(1-y_{n}{\bf x}_{n}^{\top}{\bf w})$$

From this formulation we can see that there are three distinct cases we should consider:

    - Examples that lie on the correct side and outside the margin. For those 1 − y_n x_n^T w < 0. Hence, α_n = 0.
    - Examples that lie on the correct side and just "on the margin". I.e., for those we have 1 − y_n x_n^T w = 0. Therefore αn ∈ [0, 1].
    - Examples that lie strictly inside the margin, or on the wrong side. I.e., for those we have 1 − y_n x_n^T w > 0. Therefore αn = 1.

We call the $\mathbf{x}_{n}$ for which $\alpha_{n}=0$ _non-support vectors_, the $\mathbf{x}_{n}$ for which $\alpha_{n}\in(0,1)$ _essential support vectors_ and _bound support vectors_ when $\alpha_{n}=1$. The above consideration explains why we expect most $\alpha_{n}$ to be zero.

## Coordinate Descent

**Goal:** Find α⋆ ∈ RN maximizing or minimizing g(α).
Yet another optimization algorithm?

**Idea:** Update one coordinate at a time, while keeping others fixed.

initialize α^{(0)} ∈ R^N
for t = 0:maxIter do
    - sample a coordinate $n$ randomly from $1\ldots N$.
    - Optimize $g$ w.r.t. that coordinate:
    $u^{*}\ \leftarrow\ \arg\min^{1}{}_{u\in\mathbb{R}}\ g\big{(}\alpha_{1}^{(t)},\ldots,\alpha_{n-1}^{(t)},\boldsymbol{u},\alpha_{n+1}^{(t)},\ldots,\alpha_{N}^{(t)}\big{)}$
    - update 
        - $\alpha_{n}^{(t+1)}\ \leftarrow\ u^{*}$
        - $\alpha_{n^{\prime}}^{(t+1)}\ \leftarrow\ \alpha_{n^{\prime}}^{(t)}$ for $n^{\prime}\neq n$ (_unchanged_)

## Issues With Svm

- There is no obvious probabilistic interpretation of SVM.
- Extension to multi-class is non-trivial 