# Lecture 23: Linear Codes With Examples

The goal of this lecture is to recall the definition of a linear code and give multiple examples of some important linear codes that are often used in practice.

## 1 Linear Codes 1.1 Definitions

Recall that we define a code enc : {1, . . . , M} → F^n to be linear if the range of encoders {enc(i) :
i ∈ [M]} forms a vector space. To check that a given code is linear, we must show the following two conditions:

1. ∀i, j, *enc*(i) + *enc*(j) = *enc*(k) for some k ∈ [M], i.e. an encoder must be written as a linear
combination of two others.
2. ∀α ∈ F and ∀i, *αenc*(i) = *enc*(j) for some j ∈ [M].

## 1.2 Example

Recall the (7, 4, 3)-Hamming code, the following definitions of which are equivalent:

$$\begin{pmatrix}1&0&0&0&1&1&1\\ 0&1&0&1&0&1&1\\ 0&0&1&1&1&0&1\end{pmatrix}\begin{pmatrix}x_{1}\\ x_{2}\\ \vdots\\ x_{7}\end{pmatrix}=\begin{pmatrix}0\\ 0\\ 0\end{pmatrix}\equiv\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\end{pmatrix}=\begin{pmatrix}0&1&1&1\\ 1&0&1&1\\ 1&1&0&1\end{pmatrix}\begin{pmatrix}x_{4}\\ x_{5}\\ x_{6}\\ x_{7}\end{pmatrix}$$

$$\equiv\begin{pmatrix}x_{1}\\ x_{2}\\ \vdots\\ x_{7}\end{pmatrix}=\begin{pmatrix}0&1&1&1&1\\ 1&0&1&1&1\\ 1&1&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&0\\ 0&0&0&1\end{pmatrix}\begin{pmatrix}x_{4}\\ x_{5}\\ x_{6}\\ x_{7}\end{pmatrix}=\boldsymbol{G\alpha}_{\leq4},$$

where $G$ in the theory of linear codes is called the generator matrix (in a more linearly algebraic way, it is the matrix that contains our basis vectors) and $\alpha_{\leq4}$ is the vector of the known coordinates of $x$. The above shows that Hamming codes are linear!

## 1.3 Distances

Theorem 1: Suppose V ⊆ Fn is a vector space. Then,

$$\operatorname*{min}_{v,v^{\prime}\in V:v\neq v^{\prime}}d_{H}(v,v^{\prime})=\operatorname*{min}_{v\in V:v\neq0}w_{H}(v).$$

Corollary 2 : d_min = w_min for linear codes.