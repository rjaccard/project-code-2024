# Exponential Families And Generalized Linear Models


## Motivation

Let us go back to regression. Consider the very simple onedimensional example in Fig. 1. The horizontal axis represents the input x and the vertical axis the output y. Our aim is to find a model for this data. It is very natural in this case that we try a linear model: $y = x \dot w_1 +w_0 +Z$. I.e., we model the data as a line plus noise. Perhaps the most natural choice for the noise is a zero-mean Gaussian with some variance σ2. As we discussed, this leads to least squares, assuming that we think of the data samples as independent and that we maximize the likelihood. This is what is typically meant when people talk about linear models (of course the data could be higher dimensional). Now consider the data given in Fig. 2. In this case a linear model would not be a good fit. We have seen how we can get around this problem. Just add some additional features, e.g., x2 and x3. If we now use again a linear model, but in the extended feature space then we should be able to model the data well. So the idea was to augment or transform the feature space. But this is not the only option we have. Note that in the example above the linear model predicts the *mean* of a distribution from which we then assume the data was sampled.

Explicitly, we had $y = x \dot w_1 +w_0 +Z$, where $x \dot w_1 +w_0$ is the prediction of the linear model and represents the mean (i.e., the putatively "true" value for this data point) and then we get a noisy version as a sample. Here is now the extra degree of freedom we have: Instead of using the linear model to predict the mean of the distribution we can use it to predict a different quantity. We have already seen an example when we talked about logistic regression. Consider the data given in Fig 3, where all the y values are in {0, 1}. This might correspond to a binary classification problem. Recall that in logistic regression we model the probability of the two classes {0, 1} given the data x by

$$\begin{array}{l}{{p(y=1|\eta)=\sigma(\eta),}}\\ {{p(y=0|\eta)=1-\sigma(\eta),}}\end{array}$$
where η as a shorthand for $x^⊤ \dot w$. This can be written compactly as

$$p(y|\eta)=\frac{e^{\eta y}}{1+e^{\eta}}=\exp\left[\eta y-\log(1+e^{\eta})\right],$$
where y ∈ {0, 1}. Note that linear model predicts η, η =
$x^⊤ \dot w$, and that η is *not* the mean of the distribution. Rather, η is related to the mean µ by the non-linear relation $η = ln(\frac{µ}{1−µ})$ or µ = σ(η). This relation between the parameter we predict by the linear model and the mean is called the link function. It is exactly this nonlinear link function that makes it possible to use a linear model in this context.

## Outline

As you can see, we rewrote this distribution used in logistic regression in a very specific form. Our aim for today will be to generalize this form. We will see that there are many other distributions that can be written in this form. This will lead us to the class of distributions known as exponential families. We will first spend some time to talk about this family. We will see that many distributions (but not all) fit into this framework and that distributions in this family have many nice properties. We will only discuss some of these properties. Exponential families are also those distributions that have maximum entropy given some moment constraints and they are extremal also in other contexts. You are likely going to come across this family in other courses, and you will definitely see them if later on you will work in this area. As a second step we then discuss how exponential families can be used in the context of ML. In essence, by using different families we use different link functions, i.e., different relationships between the parameter η that the linear model predicts and the mean of the distribution. And this degree of freedom can be useful when we are trying to find a good model for a given set of data. In the subsequent discussion we consider various exponential families and then compute the corresponding link functions.

But conceptually it can also be fruitful to think in the reverse way. What should the relationship be between the parameter that the linear model predicts and the mean of the distribution in order to fit the data well. I.e., perhaps we start with a desired link function and then find the exponential family that gives us this relationship.

## Exponential Family - Definition

Let y be a scalar and η be a vector. We will say that a distribution belongs to the *exponential family* if it can be written in the form

$$p(y|\mathbf{\eta})=h(y)\exp\left[\mathbf{\eta}^{\top}\mathbf{\phi}(y)-A(\mathbf{\eta})\right].\tag{1}$$

$\mathbf{\zeta}$ at the various components of this distribution.

Let us look at the various components of this distribution.

The parameter vector, η is often referred to as the natural or canonical parameter. The quantity φ(y) is in general a vector and it is called a *sufficient statistics*. Why is φ(y) called a sufficient statistics? Assume that we are given independent samples from this distribution. We do know φ(y) and h(y) but we do not know the parameter η. It turns out that in order to optimally estimate η given these samples all we need is the empirical average of the φ(y). In other words, φ(y) contains all the relevant information.

Note that the expression in (1) is non-negative if h(y) ≥ 0.

So we only need to ensure that it is properly normalized, i.e., we require that
$$\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)-A(\boldsymbol{\eta})\right]dy]=1.$$

Rewriting this we see that
$$\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\right]dy]=e^{A(\boldsymbol{\eta})}.\tag{2}$$

We see from the last expression that the only role of A(η) is to ensure a proper normalization. A(η) is sometimes called the *cumulant* and some times it is called the log partition function. We will see shortly that despite the fact that A(η) is *only* there for normalization purposes it plays a crucial role and contains valuable information. If you look at the definition of the exponential family, you will see that we have several "degrees of freedom" to define an element of the family. We can choose the factor h(y), we can choose the vector φ(y), and we can choose the parameter η. For every choice we will get an element of the exponential family. The term A(η) is then determined for each such choice and ensures that the expression is properly normalized as discussed. Of course it can happen that for some parameters η, $h(y)exp[η^⊤ \times φ(y)]$ is such that we cannot normalize the expression because the integral is infinity.

E.g., set h(y) = 1, φ(y) = y^2 and η = 1. We will exclude such parameters by only looking at the set of parameters

$$M:=\{\eta:\int_{y}h(y)\exp\left[\eta^{\top}\phi(y)\right]d y\}<\infty\}.$$ 

As a final remark concerning $A(\boldsymbol{\eta})$ note that from (2) we have
$$A(\boldsymbol{\eta})=\ln\Big{[}\int_{y}h(y)\exp\big{[}\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\big{]}\,dy\Big{]}.\tag{3}$$

## Exponential Family - Examples

Let us look at a few examples which are probably familiar to you but you might not have seen them written in this form.

Example: We claim that the Bernoulli distribution is a member of the exponential family. We write

$$\begin{array}{c}{{p(y|\mu)=\mu^{y}(1-\mu)^{1-y},\mathrm{~where~}\mu\in(0,1)}}\\ {{=\exp\left[(\ln\frac{\mu}{1-\mu})y+\ln(1-\mu)\right]}}\\ {{=\exp\left[\eta\phi(y)-A(\eta)\right].}}\end{array}$$

Mapping this to (1) we see that
$$\begin{array}{c}{{\phi(y)=y,}}\\ {{\eta=\ln\frac{\mu}{1-\mu},}}\\ {{A(\eta)=-\ln(1-\mu)=\ln(1+e^{\eta}),}}\\ {{h(y)=1.}}\end{array}$$

In this case φ(y) is a scalar, reflecting the fact that this family only depends on a single parameter. In fact, we have a 1-1 relationship between η and µ,

$$\eta=g(\mu)=\ln\frac{\mu}{1-\mu}\iff\mu=g^{-1}(\eta)=\frac{e^{\eta}}{1+e^{\eta}}.$$ 

As we mentioned in the very beginning, this function $g$ is known as the _link_ function (it links the mean of $\boldsymbol{\phi}(y)$ to the parameter $\eta$.)

Note that this is _exactly_ the same distribution that we encountered when we discussed _logistic regression_.

_Example_: Consider the Poisson distribution with mean $\mu$. We have, for $y\in\mathbb{N}$,

$$p(y|\mu)=\frac{\mu^{y}e^{-\mu}}{y!}$$ $$=\frac{1}{y!}e^{y\ln(\mu)-\mu}$$ $$=h(y)e^{\eta\phi(y)-A(\eta)},$$
where h(y) = 1/y!, φ(y) = y, η = g(µ) = ln(µ), and
µ = g−1(η) = eη. Here again, g(µ) *links* the mean to the parameter η.

Example: The Gaussian distribution with mean µ and variance σ2 as parameters is also a member of the exponential family. We write

$$p(y|\mu)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{(y-\mu)^{2}}{2\sigma^{2}}},\mu\in\mathbb{R},\sigma^{2}\in\mathbb{R}^{+}$$ $$=\exp\left[(\mu/\sigma^{2},-1/(2\sigma^{2}))(y,y^{2})^{\top}-\frac{\mu^{2}}{2\sigma^{2}}-\frac{1}{2}\ln(2\pi\sigma^{2})\right].$$

Mapping this again to (1) we see that
$$\begin{array}{c}{{\phi(y)=(y,y^{2})^{\top}}}\\ {{\eta=(\eta_{1}=\mu/\sigma^{2},\eta_{2}=-1/(2\sigma^{2}))^{\top},}}\\ {{A(\eta)=\frac{\mu^{2}}{2\sigma^{2}}+\frac{1}{2}\ln(2\pi\sigma^{2}),}}\\ {{=-\frac{\eta_{1}^{2}}{4\eta_{2}}-\frac{1}{2}\ln(-\eta_{2}/\pi),}}\\ {{h(y)=1.}}\end{array}$$

Note that this time φ(y) is a vector of length two, reflecting the fact that the distribution depends on two parameters.
In fact, we have the 1-1 relationship between η = (η1, η2)
and (µ, σ^2).

$$\eta_{1}=\frac{\mu}{\sigma^{2}};\eta_{2}=-\frac{1}{2\sigma^{2}}\iff\mu=-\frac{\eta_{1}}{2\eta_{2}};\sigma^{2}=-\frac{1}{2\eta_{2}}.$$

## Basic Properties Convexity Of A(Η)

Lemma. The cumulant A(η) is convex as a function of η
on M (the set of parameters η where the cumulant is finite).

## Derivatives Of A(Η) And Moments

Another useful property is that the gradient and Hessian
(first and second derivatives) of A(η) are related to the mean and the variance of φ(y).

## Lemma.

$$\begin{array}{l}{{\nabla A(\mathbf{\eta})=\mathbb{E}[\mathbf{\phi}(y)],}}\\ {{\nabla^{2}A(\mathbf{\eta})=\mathbb{E}[\mathbf{\phi}(y)\mathbf{\phi}(y)^{\top}]-\mathbb{E}[\mathbf{\phi}(y)]\mathbb{E}[\mathbf{\phi}(y)]^{\top}.}}\end{array}$$
Note that this in particular shows that the Hessian of A(η) is a covariance matrix and hence is positive semi-definite. This gives us a second proof that A(η) is convex.

Before we prove this, let us check this for our two running examples. Recall that for the Bernoulli distribution φ(y) is a scalar, namely y. So in this case the first derivative should be the mean of the Bernoulli distribution and the second derivative the variance. Let us verify this. We get

$$\begin{array}{l}{{{\frac{d A(\eta)}{d\eta}}={\frac{d\ln(1+e^{\eta})}{d\eta}}={\frac{e^{\eta}}{1+e^{\eta}}}=\sigma(\eta)=\mu,}}\\ {{d^{2}A(\eta)}}\\ {{{\frac{d^{2}A(\eta)}{d\eta^{2}}}={\frac{d\sigma(\eta)}{d\eta}}=\sigma(\eta)(1-\sigma(\eta))=\mu(1-\mu),}}\end{array}$$
which confirms the claim.

For the Gaussian distribution our vector φ(y) is of the form (y, y^2)^⊤. So the first derivative (gradient) should give us the mean and the second moment of the Gaussian. The second derivative should give us the variance of various moments of y. We get

$$\begin{array}{l}{{\frac{\partial A(\mathbf{\eta})}{d\eta_{1}}=\frac{\partial(-\frac{\eta_{1}^{2}}{4\eta_{2}}-\frac{1}{2}\ln(-\eta_{2}/\pi))}{\partial\eta_{1}}=-\frac{\eta_{1}}{2\eta_{2}}=\mu,}}\\ {{\frac{\partial A(\mathbf{\eta})}{d\eta_{2}}=\frac{\partial(-\frac{\eta_{1}^{2}}{4\eta_{2}}-\frac{1}{2}\ln(-\eta_{2}/\pi))}{\partial\eta_{2}}=(\frac{\eta_{1}^{2}-2\eta_{2}}{4\eta_{2}^{2}})=\mu^{2}+\sigma^{2},}}\end{array}$$
which are exactly the expected value and the second moment of y, as claimed. To do one more computation, let us compute

$$\partial^{2}\frac{A(\eta)}{d\eta_{1}^{2}}=\frac{\partial(-\frac{\eta_{1}}{2\eta_{2}})}{\partial\eta_{1}}=-\frac{1}{2\eta_{2}}=\sigma^{2},$$
which is the variance of y, again as expected.

Proof.: Let us just write down the proof regarding the first derivative. The proof for the second derivative proceeds in a similar fashion. We have

$$\nabla A(\boldsymbol{\eta})=\nabla\ln[\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\right]\,dy]$$ $$=\frac{\int_{y}\nabla h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\right]\,dy}{\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\right]\,dy}$$ $$=\frac{\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)\right]\,\boldsymbol{\phi}(y)dy}{\exp(A(\boldsymbol{\eta}))}$$ $$=\int_{y}h(y)\exp\left[\boldsymbol{\eta}^{\top}\boldsymbol{\phi}(y)-A(\boldsymbol{\eta})\right]\,\boldsymbol{\phi}(y)dy$$ $$=\mathbb{E}[\boldsymbol{\phi}(y)].$$
In the second step we have exchange the derivative with the integral. Note that the exchange of differentiation and integration is permitted if the resulting integral is finite (which it is in our case).

## Link Function

As we have seen already in two specific cases (Bernoulli and Poisson), there is a relationship between the "mean" µ := E[φ(y)] and η defined using a so-called *link function* g.
$$η = g(µ) ⇐⇒ µ = g^{−1}(η).$$

For the Gaussian, we started with the parameters (µ, σ^2) and we have seen that there is a 1-1 relationship to the vector (η1, η2). But we could have started with the parameters (µ, µ^2+σ^2) (which now corresponds to E[φ(y)] = E[(y, y^2)^⊤] instead). And again we would have found that there is a 1-1 relationship between E[φ(y)] and the vector η.

For a list of such link functions for various distributions see the chapter on "Generalized Linear Model" in the KPM book.

## Applications In Ml

Let us now look at two applications of exponential families in ML.

## Maximum Likelihood Parameter Estimation

Assume that we have a set of samples {y_n}_n. We assume that these are independent samples from some distribution. Further, we assume that they come from some exponential family with a given h(y) and sufficient statistics φ(y) but unknown parameter η (or we simply want to find that element of this family of distributions that is closest). Our aim is to estimate the parameter η. We use our maximum likelihood principle to find this parameter.

We see that this is a convex function in η since A(η) is a convex function. Further, if we assume that we can determine the link function we can derive the solution in an explicit form by taking the gradient and setting it to zero:

This equation makes sense intuitively. It says that we should pick η in such a way that the expected value of the sufficient statistics is equal to its empirical value! In formula,

We now see the justification for why we called φ(y) a sufficient statistics.

## Generalized Linear Models

Given an element from the exponential family with a scalar
φ(y), we can construct from this a data model by assuming that a sample (x, y) follows the distribution

$$p(y\mid\mathbf{x},\mathbf{w})=h(y)e^{\mathbf{x}^{\top}\mathbf{w}\phi(y)-A(\mathbf{x}^{\top}\mathbf{w})}.$$

We call such a model a *generalized linear model*. Just note: If we had chosen w to be a matrix instead of a vector then we could build generalized linear models using exponential families with non-scalar parameters. Not much changes. To keep things simple we stick to the scalar case. It is a generalization of the data model we used for logistic regression. As we will now discuss, for such a model the maximum likelihood problem is particularly easy to solve.

Assume that we have given a training set Strain consisting of N independent samples (xn, yn). Assume further that we fit a generalized linear model to this data. This means that we assume that samples obey a distribution of the form

$$p(y_{n}\mid\mathbf{x}_{n},\mathbf{w})=h(y_{n})e^{\eta_{n}\phi(y_{n})-A(\eta_{n})}$$
with $η_n = x_n^⊤ \dot w$. Given S_{train}, we then write down the likelihood and look for that weight vector w that maximizes this likelihood. In more detail, we consider the cost function

$$\begin{array}{l l}{{{\mathcal{L}}(\mathbf{w})=-\frac{1}{N}\sum_{n=1}^{N}\ln p(y_{n}|\mathbf{x}_{n}^{\top}\mathbf{w})}}\\ {{}}&{{=-\frac{1}{N}\sum_{n=1}^{N}\ln(h(y_{n}))+\mathbf{x}_{n}^{\top}\mathbf{w}\phi(y_{n})-A(\mathbf{x}_{n}^{\top}\mathbf{w}).}}\end{array}$$
We want to minimize this cost function (we added a minus sign). First, note that this cost function is convex, hence a greedy algorithm should work well.

Let us take the gradient of this expression. We get

$$\nabla_{\bf w}{\cal L}({\bf w})=-\frac{1}{N}\sum_{n=1}^{N}{\bf x}_{n}\phi(y_{n})-{\bf x}_{n}g^{-1}({\bf x}_{n}^{\top}{\bf w}).$$

where we used the fact that
$$\nabla A(\eta)=g^{-1}(\eta).$$

If we set this equation to zero we get the condition of optimality. In particular, if we rewrite this sum by using our matrix notation we get

$$\nabla{\cal L}({\bf w})=\frac{1}{N}{\bf X}^{\top}\left[g^{-1}({\bf X}{\bf w})-\phi({\bf y})\right]=0,$$
where, as before, the scalar functions $(g^{-1}$ and $\phi)$ are applied to each vector component-wise.

To compare, for the case of the logistic regression we got the equation

$$\nabla{\cal L}({\bf w})=\frac{1}{N}{\bf X}^{\top}\left[\sigma({\bf X}{\bf w})-{\bf y}\right]=0.$$
As we have discussed, for the logistic case (Bernoulli distribution) we have the relationship g−1 = σ, which confirms that our previous derivation was just a special case.

Note also that we have already shown that A(x⊤w) is a convex function (A is convex and A(x⊤w) is the composition of a linear function with a convex function). Therefore L(w) is convex (the other terms are constant or linear), just as we have seen this for the logistic regression. As a consequence, greedy iterative algorithms (like gradient descent) to find the optimum weight vector w are expected to work well in this context.