# Bias-Variance Decomposition 

## Motivation

Last time we saw how to assess if a given function was good.

In particular, we discussed how we can bound the difference between the true risk of the function and the empirical risk. We then used the same ideas and discussed how to choose the "best" out of a finite number of models. This led us to the idea of splitting the data into a *train* set and a *test* set.

Our motivation for the model selection problem was that typically we need to optimize hyper-parameters. E.g., in the ridge regression problem the hyper-parameter was λ. These hyper-parameters often control the "complexity" of the class of models that we allow. Today we will focus on how the risk (true or empirical) behaves as a function of the complexity of the model class. This will lead to the important concept of the bias - variance trade-off when we perform the model selection. It will help us to decide how "complex" or "rich" we should make our model.

Let us discuss a very simple example. Consider linear regression with a one-dimensional input and using polynomial feature expansion.

The maximum degree d regulates the complexity of the class. We will see that the following is typically true.

Assume that we only allow simple models, i.e., we restrain the degree to be small:

- We then typically will get a large bias, i.e., a bad fit. - On the other hand the variance of LD(fS) as a function
of the random sample S is typically small.
We say that we have high bias but low variance.

Assume that we allow complex models, i.e., we allow large degrees:

- We then typically will find a model that fits the data
very well. We will say that we have small bias.
- But we likely observe that the variance of LD(fS) as a
function of the random sample S is large.
We say that we have low bias but high variance.

## Data Generation Model

Assume that the data is generated as $$y=f(\mathbf{x})+\varepsilon,$$. 
where f is some (arbitrary and unknown) function and ε is additive *noise* with distribution D_ε that is independent from sample to sample and independent from the data. Assume the noise has zero mean (otherwise this constant can be absorbed into f). Note that f is in general not *realizable*, i.e., it is in general not in our model class.

We further assume that x is generated according to some fixed but unknown distribution Dx. Finally, we assume that the loss function ℓ(·, ·) is the square loss. Let D denote the joint distribution on pairs (x, y).

## Error Decomposition

As always, we have given some training data $S_{train}$, consisting of i.i.d. samples according to D. Given our learning algorithm A, we compute the prediction function $f_{S_{train}} = A(S_{train})$. We are ultimately interested in how the true error

$$\mathbb{E}_{\mathbf{x}\sim{\mathcal{D}}}[\left(f(\mathbf{x})+\varepsilon-f_{S_{\mathrm{train}}}(\mathbf{x})\right)^{2}]$$
behaves as a function of the training set S_{train} and the complexity of the model class. But the decomposition we will discuss already applies "pointwise", i.e., for a single sample x. It is therefore simpler if we fix x0, and only consider

$$(f({\bf x}_{0})+\varepsilon-f_{S_{\mathrm{train}}}({\bf x}_{0}))^{2}.$$

We imagine that we are running the experiment many times:
we create $S_{train}$, we learn the model $f_{S_{train}}$, and then we evaluate the performance by computing the square loss for this fixed element x0.

So let us look at the expected value of this quantity:

$$\mathbb{E}_{S_{\mathrm{train}}\sim\mathcal{D},\,\varepsilon\sim\mathcal{D}_{\varepsilon}}[\left(f(\mathbf{x}_{0})+\varepsilon-f_{S_{\mathrm{train}}}(\mathbf{x}_{0})\right)^{2}].$$


## Interpretation Of Decomposition

Each of the three terms is non-negative. Hence each of them is a lower bound on the true error for the input x0.

The noise imposes a strict lower bound on what error we can achieve. This contribution is given by the term Var_{ε∼Dε}[ε].

The bias term is the square of the difference between the actual value f(x0) and the expected prediction E_{S′∼D}[f_{S'}(x0)], where the expectation is over the training sets. (E.g. simple models can not fit well, so have a large bias) The variance term is the variance of the prediction function. If we consider very complicated models then small variations in the data set can produce vastly different models and our prediction for an input x0 will vary widely.