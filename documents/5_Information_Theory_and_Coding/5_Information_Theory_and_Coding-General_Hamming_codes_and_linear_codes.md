# Lecture 22: General Hamming Codes And Linear Codes

In this lecture we will generalise the form of a Hamming code and introduce a few other interesting bounds including what we call linear codes.

## 1 General Hamming Codes 1.1 General Form

A Hamming code is generally of the form (2^m − 1, 2^m − m − 1, 3) for every m ≥ 3. The matrix H we introduced in last lecture will now contain m rows and 2m − 1 columns, each corresponding to one possible non-zero m-tuple. The matrix is essentially made of the m × m Identity matrix along with the remaining rows. Note that it has 2m − m − 1 free variables such that we can choose
(x_{m+1}, . . . , x_{2^m−1}) freely. Hx = 0 determines x1*, . . . , x*m. We have the following implications:

1. H has no 0-columns =⇒ d_min > 1.
2. All columns of H are distinct =⇒ d_min > 2.
3. By the sphere packing bound, d_min ≤ 3.
Hence, dmin can only be equal to 3, everytime.

## 1.2 Decoding Hamming Codes

Suppose we have Xn for which HX^n = 0 and Y^n = X^n ⊕ Z^n where Z_i says whether bit i has been flipped or not. Suppose furthermore that Z can flip at most one bit (i.e. there will be a total of n + 1 different choices of flip possible, no bits or only one of them). Given y_n, we can find Z^n as follows: compute

$\mathbf{H}Y^{n}=\mathbf{H}X^{n}\oplus\mathbf{H}Z^{n}=\mathbf{H}Z^{n}=\begin{cases}\vec{0}&\text{if}Z^{n}=\vec{0}\\ \text{the}i\text{'th column of}\mathbf{H}&\text{if}Z^{n}=e_{i},\end{cases}$
where ei is the vector with a 1 in position i and zeros elsewhere. Hence there are a total of n + 1
possible results for HY^n (which we call the "syndrome").

## 1.3 Varshamov-Gilbert Bound

Given $n$ and $d$, there is an encoder $enc:\{1,\ldots,M\}\to\{0,1\}^{n}$ with $d_{min}(enc)\geq d$ and

$$\sum_{i=0}^{d-1}\binom{n}{i}\geq2^{n}/M.$$
This means that there is approximately a factor of two difference with the sphere packing bound, which sums only half of the elements. To prove this bound, we use a greedy algorithm.

**Algorithm 1** Proof of the Varshamov-Gilbert bound: Let $A=\{0,1\}^{n}$ and $L=\{\}$.

```
while $N\neq0$ do
  if $A\neq\emptyset$ then
    Pick $x\in A$
    $L\gets L\cup\{x\}$
    $A\gets A\setminus Ball(x,d-1)$ 
return L
``` 

Here, Ball(x, d − 1) represents all objects up to distance d − 1 to x in an n-dimensional ball.
The collection L in fact contains all x's that are at least d-apart in distance. 

## 1.4 Singleton Bound

Suppose enc : {1, . . . , M*} → {*0, 1}n with *M >* 2k−1, then
$$d_{m i n}(e n c)\leq n-k+1.$$

In particular, an (n, k, d) code must have d + k ≤ n + 1. To prove this, we write the n-length sequences *enc*(1)*, . . . , enc*(m) as concatenations of two sequences of length k − 1 and n − k + 1
respectively. Since M > 2^{k−1}, by the pigeonhole principle, there must exist two encoders for which the first k − 1 bits are the same, meaning that for two messages m and m′,

$d_{min}\leq d_{H}(enc(m),enc(m^{\prime}))\leq n-k+1$
which concludes the proof.

## 2 Linear Codes

Definition 1 : A code e = {enc(1), . . . , enc(M)} is called linear if it is forms vector space over
{0, 1}.

Recall that V is a vector space over F means that:

1. F is a field.
2. There is scalar multiplication, i.e. av = w ∈ V where a ∈ F and v ∈ V . Note that if a = 1,
then av = v. We also have (a + b) · v = a · v + b · v for v *∈ {*0, 1}n. Additionally, for a, b ∈ F
and v ∈ V , (ab) · V = a · (b · V ).
3. There is vector addition, i.e. (u+v)∈V = w ∈ V , which is both associative and commutative.

The additions and multiplications are done component-wise, meaning that we have

$${\vec{u}}+{\vec{v}}={\begin{pmatrix}u_{1}\\ u_{2}\\ \vdots\\ u_{n}\end{pmatrix}}+{\begin{pmatrix}v_{1}\\ v_{2}\\ \vdots\\ v_{n}\end{pmatrix}}={\begin{pmatrix}u_{1}+v_{2}\\ u_{2}+v_{2}\\ \vdots\\ u_{n}+v_{n}\end{pmatrix}},$$
and

$$a\vec{v}=a\begin{pmatrix}v_{1}\\ v_{2}\\ \vdots\\ v_{n}\end{pmatrix}=\begin{pmatrix}av_{2}\\ av_{1}\\ \vdots\\ av_{n}\end{pmatrix},$$

for a real $a\in\mathbb{R}$ and two vectors $\vec{u}$ and $\vec{v}\in\mathbb{R}^{n}$. Note that the number of encodings must be a power of two. To summarize, $\{enc(1),\ldots,enc(m)\}$ forming a vector space over $\{0,1\}$ is equivalent to saying that $enc(i)+enc(j)=enc(k)$ for every $i,j\in[n]$ and some $k\in[n]$. In other words, **each encoder can be written as a linear combination of two others from the same vector space**.

