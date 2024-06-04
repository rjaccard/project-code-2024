# Generalization, Model Selection, And Validation 

## Motivation

Assume that your friend has trained a model on some data and now claims to have found the "perfect" regression function f. How can you verify this claim and have confidence that f will have good performance? This leads us to the question of *generalization* and *validation*.

As a second motivation consider the following problem. We have seen in ridge regression that the regularization parameter λ > 0 can be tuned to reduce overfitting by reducing model complexity,

$$\operatorname*{min}_{\bf w}\quad\frac{1}{2N}\sum_{n=1}^{N}(y_{n}-{\bf x}_{n}^{\top}{\bf w})^{2}\quad+\quad\lambda\|{\bf w}\|^{2}$$

The parameter λ is a *hyper*-parameter.

In a similar manner, we can enrich the model complexity, by augmenting the feature vector x. E.g., consider a polynomial feature expansion. Here the degree d is a hyperparameter.

To see a final example consider neural nets. Here we have tens or hundreds of hyperparameters: architecture, width, depth, type of the network etc. In all these cases we are faced with the same problem: how do we choose these hyperparameters?

This is the model selection problem.

## Data Model And Learning Algorithm

In order to give a meaningful answer to the above questions we first need to specify our data model.

We assume that there is an (unknown) underlying distribution $\mathcal{D}$, with range $\mathcal{X}\times\mathcal{Y}$. The data set we see, call it $S$, consists of independent samples from $\mathcal{D}$:

$$S=\left\{(\mathbf{x}_{n},y_{n})\text{i.i.d.}\sim\mathcal{D}\right\}_{n=1}^{N}.$$

The *learning algorithm* takes the data and outputs a model within the class of models that it is given.

Often this is done by optimising a cost function. We have seen that we can use e.g. (stochastic) gradient descent or least-squares for the ridge-regression model as an efficient way of implementing this learning. Write f_S = A(S), where A denotes the learning algorithm.

If we want to indicate that fS also depends on parameters of the model, e.g., the λ in the ridge regression model, we can add a subscript to write f_{S,λ}.

## True Error, Empirical Error, And Training Error

Given a model f, how can we assess if f is any good? We should compute the *expected* error over all samples chosen according to D, i.e., we should compute $L_D(f) = E_D[ℓ(y, f(x))]$, where ℓ(·, ·) is our loss function. 
E.g., for ridge regression 

$$ℓ(y, f(x)) = \frac{1}{2}(y − f(x))^2$, 

The quantity L_D(f) has many names: (true/expected)
(risk/loss/error). This is the quantity we are fundamentally interested in, but we cannot compute it since D is not known.

But we are given some data S. It is therefore natural to compute the equivalent *empirical* quantity

$$L_{S}(f)=\frac{1}{|S|}\sum_{(\mathbf{x}_{n},y_{n})\in S}\ell(y_{n},f(\mathbf{x}_{n})).\tag{1}$$

This is called the _(empirical) (risk/loss/error)_. There is one added complication. Assume that we are given the data $S$. If we first learn the model from $S$, i.e., we compute $f_{S}=\mathcal{A}(S)$ and then we compute the empirical risk of $f_{S}$ using the _same data_$S$ then in fact we are computing

$$L_{S}(f_{S})=\frac{1}{|S|}\sum_{(\mathbf{x}_{n},y_{n})\in S}\ell(y_{n},f_{S}(\mathbf{x}_{n})).$$

This is called the *training (risk/loss/error)* and we have already discussed in previous lectures that this training error might not be representative of the error we see on "fresh" samples.

The reason that L_S(f_S) might not be close to L_D(f_S) is of course overfitting.

So let us summarize. If somebody hands us a function f then there is the true risk L_D(f) associated to f, but we cannot in general compute it. If we have some data S that was not used to determine f then we can compute the empirical risk of f with respect to S. This is denoted by L_S(f). We will shortly discuss the relationship between L_D(f) and L_S(f).

And if S was used to learn f, then we denote it by f_S and call the resulting empirical error the training error, L_S(f_S).

## Splitting The Data And Test Error

Before we go on and explore the relationship between the true risk and the empirical risk, let us first see how we can address the potential overfitting problem that occurs if we train and test the model on the same data.

Problem: Validating model on the same data subset we trained it on!

Fix: Split the data into a *training* and a *test* set (a.k.a. validation set), call them S_{train} and S_{test}, respectively.

We apply the learning algorithm A to the training set Strain and compute the function fStrain. We then compute the error on the test set, i.e.,

$$L_{S_{\mathrm{test}}}(f_{S_{\mathrm{train}}})=\frac{1}{|S_{\mathrm{test}}|}\sum_{(y_{n},{\bf x}_{n})\in S_{\mathrm{test}}}\ell(y_{n},f_{S_{\mathrm{train}}}({\bf x}_{n})).$$

This is called the *(test/validation) (risk/loss/error)*. Since Stest is a "fresh" sample we can hope that $L_{S_{test}}(f_{S_{train}})$ is close to the quantity $L_D(f_{S_{train}})$.

But we payed a price. We had to split the data and now have less data both for the learning as well as the validation (test) task. "Cross validation" as described below is more efficient in using data, but hard to analyze.

## True Error, Test Error, And Generalization Error

We now get back to our original question. Assume that we have a model f, and that our loss function ℓ(·, ·) is bounded, lets say in [a, b]. We are given a test set S_{test} chosen i.i.d. from the underlying distribution D (and this test set was not used to train the model). The test/empirical error is

$$L_{S_{\mathrm{test}}}(f)=\frac{1}{|S_{\mathrm{test}}|}\sum_{({\bf x}_{n},y_{n})\in S_{\mathrm{test}}}\ell(y_{n},f({\bf x}_{n})).$$

The true error is
$$L_{\mathcal{D}}(f)=\mathbb{E}_{(y,\mathbf{x})\sim\mathcal{D}}[\ell(y,f(\mathbf{x}))].$$

How far are these apart? This is called the generalization error and it is given by
$$|L_{\mathcal{D}}(f)-L_{S_{\mathrm{test}}}(f)|.$$

First note that in expectation they are the same, i.e.,
$$L_{\mathcal{D}}(f)=\mathbb{E}_{S_{\mathrm{test}}\sim{\mathcal{D}}}[L_{S_{\mathrm{test}}}(f)],\qquad\qquad(2)$$
where the expectation is over the samples of the test set.

But we need to worry about the variation. We claim that
$$\mathbb{P}\bigg{[}\ |L_{\mathcal{D}}(f)-L_{S_{\mathrm{test}}}(f)|\geq\sqrt{\frac{(b-a)^{2}\ln(2/\delta)}{2|S_{\mathrm{test}}|}}\ \bigg{]}\leq\delta.\tag{3}$$

_Inights:_ The error decreases as $\mathcal{O}(1/\sqrt{|S_{\mathrm{test}}|})$ with the number test points. The more data points we have therefore, the more confident we can be that the empirical loss we measure is close to the true loss. If we want $\delta$ to be smaller we only need to increase the size of the test set slightly.

_Proof of (3):_
Since we assumed that each data sample (xn, yn) in the test set S_{test} is chosen independently, the associated losses ℓ(yn, f(xn)), given a fixed model f, are also i.i.d. random variables, taking values in [a, b] by assumption. Call each such loss Θn. The expected value of Θn = ℓ(yn, f(xn)) is equal to the true loss
$$L_{\mathcal{D}}(f)=\mathbb{E}[\ell(y_{n},f(\mathbf{x}_{n}))].$$

The empirical loss on the other hand is equal to the average of |S_{test}| such i.i.d. values.

We want to know the chance that the empirical loss $L_{S_{test}}(f)$ deviates from its true value by more than a given constant. This is a classical problem addressed in the following lemma.

**Lemma 0.1 (Hoeffding's inequality).** Let Θ1, . . . , ΘN be a sequence of i.i.d. random variables with mean E[Θ] and range [a, b]. Then, for any ε > 0,

$$\mathbb{P}\bigg{[}\bigg{|}\frac{1}{N}\sum_{n=1}^{N}\Theta_{n}-\mathbb{E}[\Theta]\bigg{|}\geq\varepsilon\bigg{]}\leq2e^{-2N\varepsilon^{2}/(b-a)^{2}}.$$


## How To Use This Bound

Let us summarize. Assume at first that somebody hands you a function f and you have a data set S. Then you can assert that

$$\mathbb{P}\bigg{[}\ L_{\mathcal{D}}(f)>L_{S}(f)+\sqrt{\frac{(b-a)^{2}\ln(2/\delta)}{2|S|}}\ \bigg{]}\leq\delta.$$

In words, we can compute a probabilistic upper bound on the true risk since both $L_{S}(S)$ as well as the error term can be computed with the data at hand.

In the more general case, we are given a data set $S$ and we want to first learn a function and then compute an upper bound on the true risk of the learned function. In this case we should split $S$ into $S=S_{\mathrm{train}}\cup S_{\mathrm{test}}$. We then let $f_{S_{\mathrm{train}}}=\mathcal{A}(S_{\mathrm{train}})$. Then we can assert that

$$\mathbb{P}\bigg{[}L_{\mathcal{D}}(f_{S_{\mathrm{train}}})>L_{S_{\mathrm{test}}}(f_{S_{\mathrm{train}}})+\sqrt{\frac{(b-a)^{2}\ln(2/\delta)}{2|S_{\mathrm{test}}|}}\ \bigg{]}\leq\delta.$$

So also in this case do we get a a computable probabilistic upper bound. In the second case we pay a price for splitting the data and the bound will in general be less tight.

## Model Selection

Let us now get to our second, related, problem. We are looking for a way to select the hyperparameters of our model, like the parameter λ for the ridge regression problem.

We split our data into a training set Strain and a test set Stest and we think of them as having been generated independently and sampled according to the underlying but unknown distribution D. We have in addition a set of values for a parameter of the model, e.g., the parameter λ in the ridge regression problem. Let these values be λ_k, k = 1, . . . , K.

To keep things simple we assume that K is some finite value. We run the learning algorithm K times on the same training set Strain to compute the K prediction functions $f_{S_{train}, λ_k}$.

For each such prediction function we compute the test error LStest(fStrain,λk). We then choose that value of the parameter λ which gives us the smallest such test error.

The same procedure can is applied to select other model hyperparameters, such as the degree in case of a polynomial feature expansion.

## Model Selection Based On Test Error

If for all models $f_{S_{train}, λ_k}$ the test error was exactly equal to the true error then it makes sense that we pick the best of these models. But we have seen that even if we compare the test to the true error of a single function in general there is a difference (the generalization error). And in the model selection problem we use the same test set K times to compute the test error for each of the K models. How confident can we be that the suggested procedure gives us meaningful results? This is a slight extension of our previous analysis.

Assume hence that we have K models fk given as candidates, k = 1, . . . , K. Again assume that our loss function ℓ(·, ·) is bounded in [a, b]. Given a test set S_{test} chosen i.i.d. from D. what is the maximum generalization error, i.e., what is the maximum difference between the true error and the test error? 

Similarly as in the case of a single model (3), we claim that we can now bound the maximum deviation for all K candidates, by

$$\mathbb{P}\bigg{[}\max_{k}\big{|}L_{\mathcal{D}}(f_{k})-L_{S_{\mathrm{test}}}(f_{k})\big{|}\geq\sqrt{\frac{(b-a)^{2}\ln(2K/\delta)}{2|S_{\mathrm{test}}|}}\ \bigg{]}\leq\delta.\tag{4}$$

Inights: The error decreases as $\mathcal{O}(1/\sqrt{\|S_{test}}$ number test points. Now that we test K hyper-parameters, our error only goes up by a very small factor which is proportional to $\sqrt{ln(K)}$. So we can test many different models without incurring a large penalty. 

The proof of this statement follows (3), which has answered the special case of K = 1. 

For a general K, if we check the deviations for K models and ask for the probability that for at least one such model we get a deviation of at least $\varepsilon$ then by the union bound this probability is at most $K$ times as large as in the case where we are only concerned with a single instance. I.e., the upper bound becomes $2Ke^{-2|S_{\rm test}|\varepsilon^{2}/(b-a)^{2}}$.

Hence, equating now $2Ke^{-2|S_{\rm test}|\varepsilon^{2}/(b-a)^{2}}$ with $\delta$ we get that $\varepsilon=\sqrt{\frac{(b-a)^{2}\ln(2K/\delta)}{2|S_{\rm test}|}}$ as stated.

Let $$k^{*}=\mbox{argmin}_{k}L_{\cal D}(f_{k}).$$
In words, f_k∗ is that function that has the smallest *true* risk. Further, let

$$\hat{k}=\mbox{argmin}_{k}L_{S_{\rm test}}(f_{k}).$$

In words, $f_{\hat{k}}$ is that function that has the smallest _empirical_ risk. Then a little thought shows that

$$\mathbb{P}\bigg{[}\ L_{\mathcal{D}}(f_{\hat{k}})>L_{\mathcal{D}}(f_{k^{*}})+2\sqrt{\frac{(b-a)^{2}\ln(2K/\delta)}{2|S_{\rm test}|}}\ \bigg{]}\leq\delta.\tag{5}$$

In words, if we choose the "best" function according to the empirical risk then its true risk is not too far away from the true risk of the optimal choice.

## Cross-Validation

Splitting the data once into two parts (one for training and one for testing) is not the most efficient way to use the data.

Cross-validation is a better way: K-fold cross-validation is a popular variant. Randomly partition the data into K groups. Now train K times. Each time leave out exactly one of the K groups for testing and use the remaining K −1 groups for training. Average the K results. 

Note: Have used all data for training, and all data for testing, and used each data point the same number of times.

Cross-validation returns an unbiased estimate of the generalization error and its variance.