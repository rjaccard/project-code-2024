# Logistic Regression 

## Logistic Regression

Recall that in the previous lecture we discussed what happens if we treat binary classification as regression with lets say y = 0 and y = 1 as the two possible (target) values and then decide on the label by looking if the predicted value is smaller or larger than 0.5.

We have also discussed that it is tempting to interpret the predicted value as probability. But there are problems: (i) the predicted values are in general not in [0, 1]; further, (ii) very large (y ≫ 1) or very small (y ≪ 0) values of the prediction will contribute to the error if we use the squared loss, even though they indicate that we are very confident in the resulting classification.

It is therefore natural that we *transform* the predictions that take values in (−∞, ∞) into a true probability by applying an appropriate function.

There are several possible such functions. The logistic function
$$\sigma(z):=\frac{e^{z}}{1+e^{z}}$$

is a natural and popular choice, see the next figure.1
Consider the binary classification case and assume that our two class labels are {0, 1}. We proceed as follows. Given a training set Strain we learn a weight vector w (we will discuss how to do this shortly)
and a "shift" (scalar) w0. Given a "new" feature vector x, we predict the (posterior) *probability* of the two class labels given x by means of

$${{p(1\mid\mathbf{x},\mathbf{w})=\sigma(\mathbf{x}^{\top}\mathbf{w}+w_{0}),}}\\ {{p(0\mid\mathbf{x},\mathbf{w})=1-\sigma(\mathbf{x}^{\top}\mathbf{w}+w_{0}).}}$$

Note that we predict a real value (a probability) and not a label. This is the reason it is called logistic *regression*. But typically we use logistic regression as the first step of a classifier. In the second step we quantize the value to a binary value, typically according to whether the predicted probability is smaller or larger than 0.5.

So very large and very small (large negative) values of $x^⊤w+w_0$ correspond to probabilities p(1 | x, w)
very close to 1 and 0, respectively. 

It is easy to see what the roles of w and w0 are. The vector w is orthogonal to the "surface of transition"
and the w0 allows us to shift the transition point along the vector w. E.g., if w = (1, 0) and w0 = 0
then the transition between the two levels happens at the x1 = 0 plane. By scaling w we can make the transition faster or slower and by changing w0 we can shift the decision region along the w vector.

At this point it is hopefully clear how we use logistic regression to do classification. To repeat, given the weight vector w we predict the probability of the class label 1 to be p(1 | x, w) = σ(x^⊤ w + w0) and then quantize. What we need to discuss next is how we learn the model, i.e., how we find a good weight vector w given some training set S_{train}.

## Training

As always we assume that we have our training set Strain, consisting of iid samples {(xn, yn)}_n, sampled according to a fixed but unknown distribution D.

Exploiting that the samples (xn, yn) are independent, the probability of y (vector of all labels) given X
(matrix of all inputs) and w (weight vector) has a simple product form:

$$p(\mathbf{y}\,|\,\mathbf{X},\mathbf{w})=\prod_{n=1}^{N}p(y_{n}|\mathbf{x}_{n})$$ $$=\prod_{n:y_{n}=1}^{N}p(y_{n}=1|\mathbf{x}_{n})\prod_{n:y_{n}=0}^{N}p(y_{n}=0|\mathbf{x}_{n})$$ $$=\prod_{n=1}^{N}\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})^{y_{n}}[1\,-\,\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})]^{1-y_{n}}.$$

It is convenient to take the logarithm of this probability to bring it into an even simpler form. In addition we add a minus sign to the expression. In this way our objective will be to minimize the resulting cost function (rather than maximizing it). This is consistent with our previous examples, where we always minimized the cost function. We call the resulting cost function L(w),

$$\mathcal{L}(\mathbf{w})=-\frac{1}{N}\sum_{n=1}^{N}y_{n}\ln\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})+(1-y_{n})\ln[1-\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})]$$ $$=\frac{1}{N}\sum_{n=1}^{N}\ln[1+\exp(\mathbf{x}_{n}^{\top}\mathbf{w})]-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w}.$$

In the last step we have used the specific form of the logistic function σ(x) to bring the cost function into a nice form.

Before we continue note the following. In principle we should have written down the likelihood of the data (y, X) given the parameter w, i.e., p(y, X | w). But

$$\begin{array}{c}{{p({\bf y},{\bf X}\,|\,{\bf w})=p({\bf X}\,|\,{\bf w})p({\bf y}\,|\,{\bf X},{\bf w})}}\\ {{=p({\bf X})p({\bf y}\,|\,{\bf X},{\bf w}),}}\end{array}$$

where in the second step we have made the natural assumption that the X data does not depend on the parameter we choose in our model. Note that this is an assumption and part of our model. But now note that the factor p(X) is a constant wrt to the choice of w, and hence plays no role when we apply the maximum likelihood criterion.

## Maximum Likelihood Criterion

Recall what we did so far. Under the assumption that the samples are independent we have written down the likelihood of the data given a particular choice of weights w. We then choose the weights w that maximize this likelihood.

Equivalently, we choose the weights that maximize the *log*-likelihood. This is called the maximumlikelihood criterion. In a final reformulation, we added a negative sign to bring the cost function to our standard form and called it L(w). In this form, we are looking for the weights w that minimize L(w). In formulae, we choose the weight w⋆, so that w⋆ = argmin_w L(w).

As we discussed in that context of the probabilistic interpretation of the least squares problem, one justification of the maximum-likelihood criterion is that, under some mild technical conditions, it is consistent. I.e., if we assume that the data was generated according to a model in this class and we have i.i.d. samples and we use this procedure to estimate the underlying parameter, then our estimate will converge to the true parameter if we get more and more data. Of course, in practice the data is unlikely being generated in this way and there might not be *any* probabilistic model underlying it. But nevertheless, this gives our method a theoretical justification.

## Conditions Of Optimality

As we want to minimize L(w), let us look at the stationary points of this function by computing the gradient, setting it to zero, and solving for w. Note
$$\partial\ln[1+\exp(x)]=\sigma(x).$$

Therefore

$$\begin{split}\nabla\mathcal{L}(\mathbf{w})&=\frac{1}{N}\sum_{n=1}^{N}\mathbf{x}_{n}(\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})-y_{n})\\ &=\frac{1}{N}\mathbf{X}^{\top}\,[\sigma(\mathbf{X}\mathbf{w})-\mathbf{y}].\end{split}$$

Recall that by our convention the matrix X has N rows, one per input sample. Further, y is the column vector of length N which represents the N labels corresponding to each sample.

Therefore, Xw is a column vector of length N. The expression σ(Xw) means that we apply the function σ to each of the N components of Xw.

In this manner we can express the gradient in a compact manner. 

There is no closed-form solution for this equation. Let us therefore discuss how to solve this equation in an iterative fashion by using gradient descent or the Newton method.

## Convexity

Since we are planning to iteratively minimize our cost function, it is good to know that this cost function is convex.

### Lemma. The Cost Function

$${\mathcal{L}}(\mathbf{w})={\frac{1}{N}}\sum_{n=1}^{N}\ln[1+\exp(\mathbf{x}_{n}^{\top}\mathbf{w})]-y_{n}\mathbf{x}_{n}^{\top}\mathbf{w}$$

is convex in the weight vector w. 

## Gradient Descent

As we have done for other cost functions, we can apply a (stochastic) gradient descent algorithm to minimize our cost function.

E.g. for the batch version we can implement the update equation
$${\bf w}^{(t+1)}:={\bf w}^{(t)}-\gamma^{(t)}\nabla{\mathcal{L}}({\bf w}^{(t)}),$$

where γ^{(t)} > 0 is the step size and w^{(t)} is the sequence of weight vectors.

## Newton's Method

The gradient method is a *first-order* method, i.e., it only uses the gradient (the first derivative). We get a more powerful optimization algorithm if we use also the second order terms. Of course there is a trade-off. On the one hand we need fewer steps to converge if we use second order terms, on the other hand every iteration is more costly. Let us describe now a scheme that also makes use of second order terms. It is called *Newton's method*.

## Hessian Of The Log-Likelihood

Let us compute the *Hessian* of the cost function L(w), call it H(w). What is the Hessian? If w has D components then this is the D × D symmetric matrix with entries

$${\bf H}_{i,j}=\frac{\partial^{2}{\mathcal{L}}({\bf w})}{\partial w_{i}\partial w_{j}}.$$

Recall that the cost function L(w) is a sum of N
terms, all of the same form. So let us first compute the Hessian corresponding to one such term. We already computed the *gradient* of one such term and got
$$\mathbf{X}_{n}(\sigma(\mathbf{x}_{n}^{\top}\mathbf{w})\,-\,y_{n}).$$

Recall, that this gradient is a vector of length D
(the dimension of the feature vector x and hence also the dimension of the weight vector) where the i-th component is the derivative of L(w) with respect to wi. If you look at the above expression you see that this gradient is equal to x (a vector) times the scalar $(σ(x_n^T \times w) − y_n)$. Note that x does not depend on w and neither does yn. The only dependence on w is in the term $σ(x_n^T \times w)$. Therefore, the Hessian associated to one term will be
$$\mathbf{X}_{n}\bigl(\nabla\sigma\bigl(\mathbf{x}_{n}^{\top}\mathbf{w}\bigr)\bigr)^{\top}.$$

We have already seen that σ′(x) = σ(x)(1−σ(x)).

Therefore, by the chain rule one such term gives rise to the Hessian
$${\bf x}_{n}{\bf x}_{n}^{\top}\sigma({\bf x}_{n}^{\top}{\bf w})(1-\sigma({\bf x}_{n}^{\top}{\bf w})).$$

It remains to do the sum over all N samples. Rather than just summing, let us put this again in a compact form by using the data matrix X. We get
$$\mathbf{H}(\mathbf{w})={\frac{1}{N}}\mathbf{X}^{\top}\mathbf{S}\mathbf{X},$$
where S is a N ×N diagonal matrix with diagonal entries
$$S_{n n}:=\sigma({\bf x}_{n}^{\top}{\bf w})[1-\sigma({\bf x}_{n}^{\top}{\bf w})].$$

Note that the diagonal entries of S are non-negative.
Hence H(w) is non-negative definite. This gives us an alternative proof that our original cost function is convex.

## Newton'S Method

Gradient descent uses only first-order information and takes steps in the direction opposite to the gradient. This makes sense since the gradient points in the direction of increasing function values and we want to *minimize* the function.

Newton's method uses second-order information and takes steps in the direction that minimizes a quadratic approximation.

More precisely, it approximates the function locally by a quadratic form and then moves in the direction where this quadratic form has its minimum. The update equation is of the form

$${\bf w}^{(t+1)}={\bf w}^{(t)}-\gamma^{(t)}({\bf H}^{(t)})^{-1}\nabla{\mathcal L}({\bf w}^{(t)}).$$
Where does this update equation come from? Recall that the Taylor series approximation of a function (up to second order terms) around a point w⋆ has the form

$$\begin{array}{c}{{{\mathcal L}({\bf w})\approx{\mathcal L}({\bf w}^{\star})+\nabla{\mathcal L}({\bf w}^{\star})^{\top}({\bf w}-{\bf w}^{\star})}}\\ {{\qquad\qquad+\frac{1}{2}({\bf w}-{\bf w}^{\star})^{\top}{\bf H}({\bf w}^{\star})({\bf w}-{\bf w}^{\star}).}}\end{array}$$

The right-hand side is a *local approximation* of L(w). Assume that we take the right-hand side to be an exact representation of our cost function. We want to minimize this function. So let us look where the right-hand side takes its minimum value. If we think that this approximation is reasonably good, then it makes sense to move the new weight vector to the position of this minimum. Let us take the gradient of the right hand side and set it to zero. We get

$$\nabla{\mathcal{L}}(\mathbf{w}^{\star})+\mathbf{H}(\mathbf{w}^{\star})(\mathbf{w}-\mathbf{w}^{\star})=\mathbf{0}.$$

Solving for w gives us $w = w⋆ − H(w⋆)^{−1} ∇L(w⋆)$.

This corresponds exactly to the stated update equation, except that in this update we have an extra step size γ. Why do we need this factor?

Recall that the right-hand side is only an approximation. Caution therefore dictates that we only move part of the way to the indicated minimum.

## Regularized Logistic Regression

Although the cost-function for logistic regression is lower bounded by 0 we get issues if the data is linearly separable. In this case there is no finiteweight vector w which gives us this minimum cost function and if we continue to run the optimization the weights will tend to infinity. To avoid this problem, as for standard regression problems, we can add a penalty term.

E.g., we consider the cost function
$$\operatorname{argmin}_{\mathbf{w}}-{\frac{1}{N}}\sum_{n=1}^{N}\ln p(y_{n}\,|\,\mathbf{x}_{n}^{\top}\mathbf{w})+{\frac{\lambda}{2}}||\mathbf{w}||^{2}.$$

When the data is linearly separable, even if the gradient descent algorithm is not converging to a finite-weight vector, the direction in which the iterates are diverging to infinity is still very informative: the predictor converges to the direction of the max-margin solution. 