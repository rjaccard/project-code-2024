## Machine Learning Methods for Many-Body Quantum Systems

Machine learning (ML) techniques are the modern answer to one of the most ancient desires of humanity: devising an Artificial Intelligence capable of independent thinking and problem solving. The applications of ML are ubiquitous, and you might have unconsciously made use of one of those. The tasks that can be solved are for example: language translation, face recognition, game playing. In this Chapter we will discuss the application of machine learning techniques (ML) as a tool to solve the many-body Schroedinger's equation.

### 9.1 Artificial Neural networks: the machine

There are several pure and applied problems in which the task to be solved whose solution can be expressed as a complex high-dimensional function. For example, let us take the case of identifying faces in a picture. To simplify, let us assume that the picture is monochromatic, and it can be seen, when digitalized, as a a set $\mathbf{x}=b_{1}, b_{2} \ldots b_{N}$ of bits $b_{1}=0,1$ (signaling if the given pixel should be black or white). Then, we can ask a machine to give the probability that in a given picture a certain person exists: this can be formulated as: find a function $F_{\text {image }}(\mathbf{x})=P_{\text {inthere }}(\mathbf{x})$. Analogously, other tasks can be written in this form, like in the case of game playing, where $f$ could be for example the game policy: given the current set of pieces on a board, call it $\mathbf{x}$, find the optimal move that will maximize the chance to win the game. The field of ML is mainly concerned then with the problem of finding compact approximations of such highly-dimensional functions. This goal is achieved through several learning paradigms, i.e. ways of using or generating relevant information to find the best functions.

In modern Deep Learning applications, artificial neural networks play a central role. An artificial neural network is nothing but a highly-dimensional function, composition of simple one-dimensional functions, and depending on internal parameters. Taking inspiration from the biology of the brain, the specific functions are taken to be for example of the logistic/sigmoidal form:

$$
\phi(x)=\frac{1}{1+\exp (-x)}
$$

In a feed-forward neural network we would start by taking a linear combination of the input, to define a new set of variables (which defines the first "layer" of the network):

$$
a_{j}^{(1)}=\phi\left(\sum_{i} w_{i j}^{(1)} x_{i}+b_{j}^{(1)}\right)
$$

where the matrix $w_{i j}^{(1)}$ and the bias vector $b_{j}^{(1)}$ are arbitrary parameters. Then, we can feed those variables into another layer:

$$
a_{j}^{(2)}=\phi\left(\sum_{i} w_{i j}^{(2)} a_{i}^{(1)}+b_{j}^{(2)}\right)
$$

and so on, until we reach the final layer:

$$
\begin{aligned}
a_{j}^{(D)} & =\phi\left(\sum_{i} w_{i j}^{(D)} a_{i}^{(D-1)}+b_{j}^{(D)}\right) \\
& \equiv[F(\mathbf{x})]_{j}
\end{aligned}
$$

In this sense, the full function can be seen as a nested composition of non-linear vector functions:

$$
\begin{equation*}
F\left(x_{1}, x_{2}, \ldots x_{N}\right)=\phi^{(D)} \circ W^{(D)} \cdots \circ \phi^{(2)} \circ W^{(2)} \phi^{(1)} \circ W^{(1)} \mathbf{x} \tag{9.1}
\end{equation*}
$$

The size of the matrices at each layer are commonly referred to as the widths of the neural network, whereas $D$ is referred to as the depth.

As a consequence of the Kolmogorov-Arnold representation theorem [1], it can be shown that it is possible to represent (almost) arbitrary high dimensional functions in the form above, provided that the width of the first layer is large enough or that, at fixed width, the depth $L$ is large enough. In the worst case scenario, the width or depth of the network can be exponentially large in $N$, however in most applications it is found that polynomially large networks constitute excellent approximations. Barron's Theorem further relates the number of nodes in the neural network to the Fourier properties of the function to be approximated. The number of units is of order

$$
N_{\text {units }}=O\left(\frac{C_{f}^{2}}{\epsilon}\right)
$$

where $\epsilon$ is the desired error on the functional approximation, and $C_{f}$ is a constant related to the smoothness of the function to be approximated. This also shows that if a function is smooth enough, a relatively small number of "neurons" (nodes in the network) is sufficient.

### 9.2 Supervised Learning

With the machine architecture specified by a set of parameters $\boldsymbol{\theta}=\theta_{1}, \ldots \theta_{M}$ (for example the weights and bias in the previous equations), the remaining task is to find
a convenient strategy to numerically determine the weights and the structure of the network. This task is the "learning" aspect of ML. The conceptually simplest approach to learning is the so-called "supervised learning".

In this context we assume that a collection of large, pre-existing data $\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots \mathbf{x}_{N_{s}}$ exists, such that it is known in advance what the desired output of the machine should be on those, i.e. we also know the associated labels: $y_{i} \equiv F_{\text {ideal }}\left(\mathbf{x}_{i}\right)$. Goal of the supervised learning is to find the best neural-network weights such as $F(\mathbf{x} ; \boldsymbol{\theta}) \simeq F_{\text {ideal }}(\mathbf{x})$, where the ideal function is known only at the points in the dataset.

In order to quantify the quality of the machine at doing his task, we can define a "loss function":

$$
\begin{equation*}
\mathcal{L}(\boldsymbol{\theta})=\frac{1}{N_{\mathrm{s}}} \sum_{i}^{N_{s}}\left|F\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right)-y_{i}\right|^{2} \tag{9.2}
\end{equation*}
$$

which attains a minimum value of zero for perfect reconstruction. The supervised learning problem is therefore a conceptually simple inference problem or, alternatively, a non-linear fitting problem.

Learning then amounts to minimizing the loss function with respect to the parameters $\boldsymbol{\theta}$, a task that is typically realized with iterative gradient descent techniques.

### 9.3 Neural-Network quantum states

Given the ability of artificial neural networks to represent complex high-dimensional functions, in recent years the idea of using them to represent variational wave functions has emerged. This representation is known as "Neural-Network quantum state" (NQS), as introduced in $[2]$.

Formally, we set:

$$
\begin{equation*}
\langle\mathbf{x} \mid \Psi(\boldsymbol{\theta})\rangle=F\left(\mathbf{x} ; \theta_{1}, \ldots \theta_{M}\right) \tag{9.3}
\end{equation*}
$$

where $F$ is the output of a suitably chosen artificial neural network, depending on a set of parameters $\boldsymbol{\theta}$. For example, in the case of spin $1 / 2$ particles previously introduced, we can choose a neural-network representation $\Psi\left(s_{1}, s_{2}, \ldots s_{N}\right)=F\left(s_{1}, s_{2}, \ldots s_{N}\right)$. The only requirement is that the output of the neural network is a (complex-valued, in general) scalar. This can be achieved for example by taking complex-valued weight matrices $W^{(i)}$ and constraining the network widths in such a way that the last layer has a single output.

In practical applications, the most commonly parameterization is not for the amplitudes themselves but rather for the logarithm of the amplitudes, such that:

$$
\begin{equation*}
\langle\mathbf{x} \mid \Psi(\boldsymbol{\theta})\rangle=\exp \left[F_{l}\left(\mathbf{x} ; \theta_{1}, \ldots \theta_{M}\right)\right] \tag{9.4}
\end{equation*}
$$

where $F_{l}(\boldsymbol{\theta})$ is a feed-forward network.

### 9.3.1 The loss function

Given the problem of finding the best variational approximation for the ground state of a given hamiltonian $\hat{H}$, we have seen in the previous chapter that the most natural
quantity to minimize is the expected valued of the energy, thus we can readily identify it as the loss function:

$$
\begin{equation*}
E(\boldsymbol{\theta})=\frac{\langle\psi(\boldsymbol{\theta})|\hat{H}| \psi(\boldsymbol{\theta})\rangle}{\langle\psi(\boldsymbol{\theta}) \mid \psi(\boldsymbol{\theta})\rangle} \tag{9.5}
\end{equation*}
$$

In the previous Chapter, we have discussed at length how this expectation value can be estimated using Monte Carlo methods, for example Markov-Chain Monte Carlo, generating $N_{s}$ samples according to the probability density

$$
\begin{equation*}
\Pi(\mathbf{x} ; \boldsymbol{\theta})=\frac{|\Psi(\mathbf{x} ; \boldsymbol{\theta})|^{2}}{\sum_{\mathbf{x}^{\prime}}\left|\Psi\left(\mathbf{x}^{\prime} ; \boldsymbol{\theta}\right)\right|^{2}} \tag{9.6}
\end{equation*}
$$

since

$$
\begin{align*}
E(\boldsymbol{\theta}) & =\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right]  \tag{9.7}\\
& \simeq \frac{1}{N_{s}} \sum_{i=1}^{N_{s}} E_{\mathrm{loc}}\left(\mathbf{x}^{(i)}\right) \tag{9.8}
\end{align*}
$$

### 9.4 Taking Gradients

An appealing feature of neural networks is that they can be combined with automatic differentiation (AD) techniques. These are approaches to automatically compute (numerically exact) gradients of high-dimensional functions.

### 9.4.1 The BackPropagation algorithm

In the case of feed-forward neural networks, this is typically achieved through the so called "back-propagation" algorithm.

Let us recall that in a deep network

$$
\begin{align*}
& a_{j}^{(l)}=\phi\left(z_{j}^{(l)}\right)  \tag{9.9}\\
& z_{j}^{(l)}=\sum_{i} w_{i j}^{(l)} a_{i}^{(l-1)}+b_{j}^{(l)} \tag{9.10}
\end{align*}
$$

with the "boundary" conditions

$$
\begin{align*}
z_{j}^{(0)} & =x_{j}  \tag{9.11}\\
a^{(D)} & =F(\mathbf{x}) \tag{9.12}
\end{align*}
$$

For simplicity, and since this is the case relevant for NQS, we are focusing here on artificial neural networks with a scalar output, thus the last width is equal to 1 and the index $j$ is omitted: $a_{j=1}^{(D)} \equiv a^{(D)}$.

We then define the sensitivity of the neural network output to a change in the weighted input as

$$
\begin{equation*}
\Delta_{j}^{(l)} \equiv \frac{\partial F}{\partial z_{j}^{(l)}} \tag{9.13}
\end{equation*}
$$

These sensitivity vectors can be efficiently computed in a recursive way, using the chain rule:

$$
\begin{align*}
\Delta_{j}^{(l)} & =\frac{\partial F}{\partial z_{j}^{(l)}}  \tag{9.14}\\
& =\sum_{k} \frac{\partial F}{\partial z_{k}^{(l+1)}} \frac{\partial z_{k}^{(l+1)}}{\partial z_{j}^{(l)}}  \tag{9.15}\\
& =\sum_{k} \Delta_{k}^{(l+1)} \frac{\partial z_{k}^{(l+1)}}{\partial z_{j}^{(l)}}  \tag{9.16}\\
& =\sum_{k} \Delta_{k}^{(l+1)} \frac{\partial}{\partial z_{j}^{(l)}}\left(\sum_{i} w_{i k}^{(l+1)} a_{i}^{(l)}+b_{k}^{(l+1)}\right)  \tag{9.17}\\
& =\sum_{k} \Delta_{k}^{(l+1)} \frac{\partial}{\partial z_{j}^{(l)}}\left(\sum_{i} w_{i k}^{(l+1)} \phi\left(z_{i}^{(l)}\right)+b_{k}^{(l+1)}\right)  \tag{9.18}\\
& =\sum_{k} \Delta_{k}^{(l+1)} w_{j k}^{(l+1)} \phi^{\prime}\left(z_{j}^{(l)}\right) \tag{9.19}
\end{align*}
$$

The key to the back-propagation algorithm is then the ability to compute these sensitivities efficiently, which can be realized also noticing that the sensitivity in the last layer is easy to compute:

$$
\begin{align*}
\Delta_{j}^{(D)} & =\frac{\partial F}{\partial z_{j}^{(D)}}  \tag{9.20}\\
& =\phi^{\prime}\left(z_{j}^{(D)}\right) \tag{9.21}
\end{align*}
$$

Thus the algorithm works in two passes:

1. Forward pass: compute and store both $a_{j}^{(0)}, a_{j}^{(1)} \ldots a_{j}^{(D)}$ and $z_{j}^{(1)}, z_{j}^{(2)} \ldots z_{j}^{(D)}$ using the feed-forward formula (9.1).
2. Backward pass: compute the sensitivities $\Delta_{j}^{(D)}, \Delta_{j}^{(D-1)} \ldots \Delta_{j}^{(1)}$ using the recursive formula (9.19)

Finally, the gradients of the neural-network output with respect to the parameters (weights and biases) are simply related to the sensitivities, since

$$
\begin{align*}
\frac{\partial F}{\partial b_{j}^{(l)}} & =\frac{\partial F}{\partial b_{j}^{(l)}} \frac{\partial b_{j}^{(l)}}{\partial z_{j}^{(l)}}  \tag{9.22}\\
& =\frac{\partial F}{\partial z_{j}^{(l)}}  \tag{9.23}\\
& =\Delta_{j}^{(l)} \tag{9.24}
\end{align*}
$$

and similarly for gradients with respect to the weights:

$$
\begin{align*}
\frac{\partial F}{\partial w_{i j}^{(l)}} & =\frac{\partial F}{\partial z_{j}^{(l)}} \frac{\partial z_{j}^{(l)}}{\partial w_{i j}^{(l)}}  \tag{9.25}\\
& =\Delta_{j}^{(l)} a_{i}^{(l-1)} \tag{9.26}
\end{align*}
$$

### 9.4.2 Computing gradients of the energy

The back-propagation algorithm can be readily combined with variational Monte Carlo. Restricting our attention to real-valued wave function, and using the results of the previous Chapter, we can write the gradient of the energy as

$$
\begin{aligned}
\frac{\partial}{\partial \theta_{k}} E(\boldsymbol{\theta}) & =\mathbb{E}_{\Pi}\left[G_{k}(\mathbf{x})\right] \\
& =2 \mathbb{E}_{\Pi}\left[\left(E_{\mathrm{loc}}(\mathbf{x})-\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right]\right) D_{k}(\mathbf{x})\right]
\end{aligned}
$$

with

$$
D_{k}(\mathbf{x})=\frac{\partial_{\theta_{k}} \Psi(\mathbf{x})}{\Psi(\mathbf{x})}
$$

If we now take a parameterization $\Psi(\mathbf{x})=\exp \left[F_{l}\left(\mathbf{x} ; \theta_{1}, \ldots \theta_{M}\right)\right]$, then

$$
D_{k}(\mathbf{x})=\frac{\partial}{\partial \theta_{k}} F_{l}(\mathbf{x} ; \boldsymbol{\theta})
$$

thus

$$
\frac{\partial}{\partial \theta_{k}} E(\boldsymbol{\theta}) \simeq \frac{2}{N_{s}} \sum_{i}\left(E_{\mathrm{loc}}\left(\mathbf{x}^{(i)}\right)-\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right]\right) \frac{\partial}{\partial \theta_{k}} F_{l}\left(\mathbf{x}^{(i)} ; \boldsymbol{\theta}\right)
$$

and the last term can be estimated efficiently using the back-propagation method.

