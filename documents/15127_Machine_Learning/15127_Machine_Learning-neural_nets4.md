# Neural Nets - Some Popular Activation Functions

## Motivation

There are many activation functions that are being used in practice. Let us list here some of them and briefly discuss their merits.

## Sigmoid

We start with the sigmoid φ(x), which we have encountered already several times. Just to summarize, it is defined by
$$\phi(x)=\frac{1}{1+e^{-x}},$$

Note that the sigmoid is always positive (not really an issue) and that it is bounded.

Further, for |x| large, φ′(x) ∼ 0. This can cause the gradient to become very small (which is known as the "vanishing gradient problem"), sometimes making learning slow.

## Tanh

Very much related to the sigmoid is tanh(x). It is defined by
$$\operatorname{tanh}(x)={\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}}=2\phi(2x)-1,$$

Note that tanh(x) is "balanced" (positive and negative) and that it is bounded. But it has the same problem as the sigmoid function, namely for |x| large, tanh′(x) ∼ 0. As mentioned, this can cause the gradient to become very small, sometimes making learning slow.

## Rectified Linear Unit - Relu

Very popular is the rectified linear unit (ReLU) (x)+ that we have also seen already. To recall, it is defined by
$$(x)_{+}=\operatorname*{max}\{0,x\},$$. 

Note that the ReLU is always positive and that it  is unbounded. One nice property of the ReLU is that its derivative is 1 (and does not vanish) for positive values of x (it has 0 derivative for negative values of x though).

## Leaky Relu

In order to solve the 0-derivative problem of the ReLU (for negative values of x) one can add a very small slope α in the negative part. This gives rise to the leaky rectified linear unit (LReLU). It is defined by
$$f(x)=\operatorname*{max}\{\alpha x,x\}$$. 

The constant α is of course a hyper-parameter that can be optimized.

## Maxout

The maxout generalizes ReLU and LReLU. It is defined by
$$f(x)=\operatorname*{max}\{{\bf x}^{\top}{\bf w}_{1}+b_{1},\cdot\cdot\cdot\ ,{\bf x}^{\top}{\bf w}_{k}+b_{k}\}$$. 

The constants in this function are of course parameters that can be chosen for the particular application. Note that this activation function is quite different from the previous cases. In the previous cases we computed a weighted sum and then applied the activation function to it, whereas here we compute two or more different weighted sums and then choose the maximum.