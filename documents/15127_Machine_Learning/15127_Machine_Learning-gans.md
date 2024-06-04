# Generative Models 

Generative models model a probability distribution over a set of random variables either explicitly or *implicitly*.

In the latter case, we do not have direct access to the underlying probability distribution, but we can sample according to it.

Generative Adversarial Networks (GANs, Goodfellow et al. [2014]) are a family of implicit generative algorithms that are fast to sample from. Contrary to single-objective minimization f: X → R, The optimization of a GAN is formulated as a differentiable two-player game where the generator G with parameters θ, and the discriminator D with parameters φ, aim at minimizing their own cost function L_θ and L_φ, respectively, as follows:

$$\begin{array}{l}{{\theta^{\star}\in\operatorname{arg\,min}_{\theta\in\Theta}{\mathcal{L}}^{\theta}(\theta,\varphi^{\star})}}\\ {{\varphi^{\star}\in\operatorname{arg\,min}_{\varphi\in\Phi}{\mathcal{L}}^{\varphi}(\theta^{\star},\varphi)\,.}}\end{array}$$ (2P-G)

When L_θ = −L_φ the game is called a zero-sum game and (2P-G) is a minmax problem.

## Generative Models

Given a data sample x, a discriminative model
aims at predicting its label y, hence it models the
posterior distribution p(y|x).

Generative models instead model the distribution p(x) defined
over the datapoints x. Depending on the type of
the generative model we can either evaluate the
probability assigned to each datapoint, or sample
according to it.

### Taxonomy.

The explicit density generative models explicitly
model the distribution that describes the proba-
bility that the model assigns to each datapoint,
controlled by parameters θ. These models can
be further categorized as: (i) exact or tractable,
and (ii) approximate models. Rather than cal-
culating the likelihood, implicit density models
instead provide a way to draw samples.

### Applications.

Due to the high dimensionality of the raw data of real-world tasks, a critical step for efficiency (memory & computa-
tion) is learning a semantically meaningful subspace. Generative models share the same underlying goal of learning representations. Other applications include: (i) planning in Reinforcement learning [Sutton and Barto, 2018]–where agents
simulate sequences of outcomes [e.g. Kurutach et al., 2018],
(ii) physics–e.g. generating plausible trajectory of a Hamiltonian particle [Greydanus et al., 2019], among many others.

## 2-Player Vs. Single-Objective Minimization

1. Standard supervised learning: convex objective
2. Minmax: convex–concave objective

We would like to converge to a point called Nash equilibrium (NE). In the context of game theory, NE is a combination of strategies from which, no player has an incentive to deviate unilaterally.

## Differential Nash Equilibrium

More formally, a Nash equilibrium for a continuous game is defined as a point (θ⋆, φ⋆) where:

$$L(θ⋆, φ) ≤ L(θ⋆, φ⋆) ≤ L(θ, φ⋆) ∀θ, φ$$. (NE) 

Such points are (locally) optimal for both players with respect to their own decision variable, *i.e.* no player has the incentive to unilaterally deviate from it. In machine learning we are interested in differential games where L is twice differentiable, in which case such NE needs to satisfy slightly stronger conditions. 

A point (θ⋆, φ⋆) is a Differential Nash Equilibrium (DNE) of a zero-sum game iff: 

$$∥∇_θL(θ⋆, φ⋆)∥ = ∥∇_φL(θ⋆, φ⋆)∥= 0$$, 
$$∇^2_θ L(θ⋆, φ⋆) ≻ 0, and ∇^2_φ L(θ⋆, φ⋆) ≺ 0$$, (DNE)

where A ≻ 0 and A ≺ 0 iff A is positive definite and negative definite, respectively.

## Generative Adversarial Networks

1. The discriminator "distinguishes" real vs. *fake* samples:
- pz known "noise" distribution, *e.g.* N(0, 1)
- pd the real data distribution
- D mapping D: x → y ∈ [0, 1], where y is an estimated probability that x ∼ p_d

2. The generator aims at fooling the discriminator that its samples are real:
- G mapping G: z → x, such that if z ∼ p_z, then hopefully x ∼ p_d
- p_g the "fake" data distribution

3. Objective
$$\operatorname*{min}_{G}\operatorname*{max}_{D}\ \mathbb{E}_{x\sim p_{d}}[\log D(x)]+\operatorname*{\mathbb{E}}_{z\sim p_{z}}[\log(1-D(G(z)))]$$

- Loss for D: distinguish between x ∼ p_g and x ∼ pd (binary classification):
$${\mathcal{L}}_{D}(G,D)=\operatorname*{max}_{D}\,\operatorname*{\mathbb{E}}_{x\sim p_{d}}\,[\log D(x)]+\,\operatorname*{\mathbb{E}}_{z\sim p_{z}}\,[\log(1-D(G(z)))]$$
- Loss for G: fool D that G(z) ∼ pd:
$$\begin{array}{l l}{{{\mathcal{L}}_{G}(G,D)=\operatorname*{min}_{G}\ \mathbb{E}\ [\log(1-D(G(z)))]}}\\ {{\qquad}}&{{\mathrm{:=(in\ practice)\ \operatorname*{max}_{G}\ \mathbb{E}\ [\log(D(G(z)))]}}}\end{array}$$


4. Theoretical Solution: The optimum is reached when p_g = p_d and the optimal value is −log 4 

## Kl And Js Divergences

Before proving that at the equilibrium of the above GAN framework p_g = p_d we need to define some measures of similarity between two probability distributions: The KL and JS divergences.

The Kullback–Leibler (KL) divergence is defined as:

$$\mathbb{D}_{K L}(p_{d}||p_{g}):=\int_{x}\log\left(\frac{p_{d}(x)}{p_{g}(x)}\right)p_{d}(x)\,\mathrm{d}x\;.$$
KL is also called *relative entropy*, as it measures how one probability distribution is different from a "reference" probability distribution, and it is asymmetric.

The Jenson-Shannon (JS) divergence is defined as:

$$\mathbb{D}_{J S}(p||q):=\frac{1}{2}\mathbb{D}_{K L}(p||\frac{p+q}{2})+\frac{1}{2}\mathbb{D}_{K L}(q||\frac{p+q}{2})$$
Note that contrary to the KL divergence defined above, the JS divergence is symmetric.

## The Gan Framework: Equilibrium At Pg = Pd

In the following, we'll assume the neural network models G and D have infinite capacity, so can represent any probability distribution. We will study the convergence of the loss function in the space of probability density functions.

The discriminator maximizes:

$$\mathcal{L}(G,D)=\int_{x}p_{d}(x)\log(D(x))\,\mathrm{d}x$$ $$\quad+\int_{z}p_{z}(z)\log(1-D(G(z)))\,\mathrm{d}z$$ $$=\int_{x}p_{d}(x)\log(D(x))+p_{g}(x)\log(1-D(x))\,\mathrm{d}x$$
Where we used x = G(z), and p_g is the distribution of x.

Hence, optimal discriminator D⋆ is:
$$D^{\star}(x)=\frac{p_{d}(x)}{p_{d}(x)+p_{g}(x)}$$

By replacing the optimal discriminator in the above objective, we obtain that the generator minimizes:

$$\mathcal{L}(G,D^{\star})=\mathbb{E}\left[\log D^{\star}(x)\right]+\mathbb{E}\left[\log(1-D^{\star}(x))\right]$$ $$=\mathbb{E}\left[\log\frac{p_{d}(x)}{p_{d}(x)+p_{g}(x)}\right]+\mathbb{E}\left[\log\frac{p_{g}(x)}{p_{d}(x)+p_{g}(x)}\right]$$ $$=-\log4+\mathbb{D}_{KL}\!\!\left(p_{d}\Big{\|}\frac{p_{d}+p_{g}}{2}\right)+\mathbb{D}_{KL}\!\!\left(p_{g}\Big{\|}\frac{p_{d}+p_{g}}{2}\right)$$ $$=-\log4+2\cdot\mathbb{D}_{JS}(p_{d}\|p_{g})$$

where to obtain the third expression we used the definition of logarithm:

$$p_{g}(x)+p_{d}(x)$$

$$\begin{array}{c}{{\log2+\log\left(\frac{p_{d}(x)}{p_{g}(x)+p_{\mathrm{\tiny~\cdots~}}}\right.}}\\ {{=\log\left(2\frac{p_{d}(x)}{p_{g}(x)+p_{d}(x)}\right)}}\\ {{=\log\left(\frac{p_{d}(x)}{\frac{p_{g}(x)+p_{d}(x)}{2}}\right).}}\end{array}$$
A
bove, D_{KL} and D_{JS} again denote the Kullback–Leibler and the Jenson-Shannon divergences
(see previous slides).

The optimum is reached when p_g = p_d (note D^⋆ = 1/2), and the optimal value is − log 4.

## Wasserstein Distance

The previous example motivates the use of the Wasserstein distance (aka Earth mover's distance) in the context of GANs, described next.

Wasserstein-1 distance is defined as:

$$\mathbb{D}_{W}(p_{d},p_{g})=\operatorname*{inf}_{\gamma\sim\Pi(p_{d},p_{g})}\mathbb{E}_{(x,y)\sim\gamma}[\|x-y\|],$$
where $Π(p_d, p_g)$ is the set of all possible joint probability distributions between p_d and p_g, whose marginals are p_d, p_g, resp.

## Wasserstein Gan

**Def.**$f:\mathbb{R}\to\mathbb{R}$ is called $k$-Lipschitz continuous if $\exists k\in\mathbb{R}$ s.t.

$|f(x_{1})-f(x_{2})|\leq k|x_{1}-x_{2}|,\quad\forall x_{1},x_{2}$.

The so called Wasserstein GAN [WGAN, Arjovsky et al., 2017, Gulrajani et al., 2017] replaces the JS divergence with the Wasserstein distance. As the Wasserstein distance is intractable for Deep Neural Nets, WGANs make use of the so called Kantorovich-Rubinstein duality principle, which tells us that:

$$\mathbb{D}_{W}(p_{d},p_{g})=\operatorname*{sup}_{\|f\|_{L\leq1}}\mathbb{E}_{x\sim p_{d}}[f(x)]-\mathbb{E}_{x\sim p_{g}}[f(x)]\,,$$
where the supremum is over 1-Lipschitz functions f : X → R.

In the context of GANs, f is the function represented by the discriminator (called critic in WGAN), yielding:

$$\operatorname*{min}_{G}\operatorname*{max}_{D\in{\mathcal{D}}}\mathbb{E}_{x\sim p_{d}}[D(x)]-\operatorname*{\mathbb{E}}_{x\sim p_{g}}[D(x)]\,,$$
where D is the set of 1-Lipschitz functions.


## Alternating–Gan Algorithm

In practice, G and D are parametrized models (typically neural networks), and are optimized with gradient based methods.
- G: deep neural network G(z; θ) with parameters θ
- D: deep neural network D(x; φ) with parameters φ

In most GAN implementations G and D have different losses L^θ and L^{φa}, resp. In the following, we present the most commonly used algorithm for training GANs.


## Conditional Gan - (Cgan)

Many applications require generative model of a conditional probability distribution (*e.g.* "in-painting", segmentation, predicting the next frame of a video *etc.*).

GANs can also generate samples of conditional distribution, called Conditional GAN (CGAN) [Mirza and Osindero, 2014]. In CGANs both the Generator and the Discriminator are conditioned during training by some additional information, typically the class labels (but could also be images e.g. auto-generated edges of an image, conditioning on non-occluded portion–so as to generate the occluded part of the image etc).

When conditioning on the class labels, typically one-hot vector representation of the class labels is used (empirically shown to perform better).

## Gan Architectures For Images

In the context of images synthesis, [Radford et al., 2015] propose specific architectures of the two models, named Deep Convolutional GANs - *DCGAN*. Notably, the generator uses transposed convolutional layer (a.k.a. fractionally strided convolutions), also informally called "Deconvolution layers" (wrongfully). Simlest way to explain these is that they "swap" the forward and the backward passes of a convolution layer: the forward transposed convolution operation can be thought of as the gradient of some convolution with respect to its input, which is usually how transposed convolutions are also implemented in practice.

## Diffusion Models

Diffusion models are another class of generative models that have gained popularity in recent years, both for their enhanced performance and implementation in AI image generators like DALL-E 2, Stable Diffusion, and Midjourney. Unlike GANs, which train two separate models for data generation and discrimination, Diffusion Models work by progressively adding noise to input data and training one single model to estimate the added noise and recover the data. The figure above from Ho et al. [2020] describes the steps of the diffusion process, where x1, . . . , xT are latent representations of the input data x0 that share its dimensions. 

The forward process (right to left in the image above) consists of a Markov chain that adds Gaussian noise q with a variance β_t to each latent x_{t−1}.

The reverse process (left to right in the image above) learns the transitions of the Markov chain through the noise distribution p, where:
$$pθ(xt−1|xt) = N(xt−1; µθ(xt, t), Σθ(xt, t))$$.

A model is trained to estimate the added noise at each step of the process, and a simple L2 loss function compares the predicted noise to the actual added noise. Then, data can be generated starting from random inputs by modeling the noise at each step and subtracting it from the image. Instead of starting from a purely random image, DALL-E 2 begins by embedding the inputted text and transforming it into an image, which is then decoded using a Diffusion model. The text embedding simply provides additional information to condition the input of the Diffusion model. Here are some examples of transformed text provided by Ramesh et al. [2022]:

## Applications Of Gans And Diffusion Models

- Generating images; - edges to realistic photos [Isola et al., 2017];
- old gray-scale images to RGB - Semi supervised learning; - Text–to–image generation; - Super resolution; - Image editing; - Image Inpainting (filling gaps);
- Adversarial examples (Defense Vs. Attack of
classifiers);
- Videos (generation/prediction); - Domain-transfer; - Audio; - Tabular data; - Also: physics, games...