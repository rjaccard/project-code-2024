# Svd And Pca

## Motivation

Principal component analysis (PCA) is a popular method for *dimensionality reduction*. The idea is simple. Given the data matrix, we are looking for a linear mapping of the D-dimensional input into a K-dimensional space, K ≤ D, that "best" represents the original data. In other words, we "compress" the data with as small as possible distortion.

There is also a second interpretation of the PCA. We are looking for a linear transformation of the D-dimensional input into a K-dimensional space, K ≤ D, that has maximum variance. This can also be phrased probabilistically, as asking for a linear transform that "decorrelates" the input data. We will see that all these questions lead to the same answer and that this answer can be computed from the data matrix X via the so-called singular value decomposition (SVD).

PCA has strong connections to matrix factorizations, some of which we've already seen.

In all our subsequent discussion, X is the D × N data matrix, whose N columns represent the input datapoints in D-dimensional space.

## Svd

We start with the singular value decomposition (SVD).

Recall that any D ×N matrix X can be written in the form
$ X = Usv^⊤$.

This decomposition is depicted graphically in Figure 1. For simplicity in the following we assume that *D < N*. This is an arbitrary choice, but by consistently sticking with this convention it will make it easier to tell the dimensions apart.

Here, U is of size D × D and V is of size N × N and both matrices are unitary,1 i.e.,

$$\begin{array}{l}{{{\bf U U}^{\top}={\bf U}^{\top}{\bf U}={\bf I}_{D\times D},}}\\ {{{\bf V}{\bf V}^{\top}={\bf V}^{\top}{\bf V}={\bf I}_{N\times N}.}}\end{array}$$

Recall that the condition UU^⊤ = I_{D×D} means that the matrix U has orthonormal (i.e., orthogonal and norm 1)
rows and that U^⊤ = U^{−1}. But if UU^⊤ = I_{D×D} then also U^⊤U = U−1U = I_{D×D}, so that also the columns of U are orthonormal. Therefore, requiring that a square matrix is unitary, is the same as requiring that it has orthonormal rows, or requiring that it has orthonormal columns. One useful property of a unitary matrix is that the linear transform it represents can be interpreted as a "rotation", i.e., it does not change the length of the vector that is being transformed:

$$\|\mathbf{Ux}\|_{2}^{2}=\mathbf{x}^{\top}\mathbf{U}^{\top}\mathbf{Ux}=\mathbf{x}^{\top}\mathbf{x}=\|\mathbf{x}\|_{2}^{2}.\qquad\qquad(1)$$

The matrix S is a diagonal matrix of size D × N with nonnegative entries along the diagonal. These diagonal entries are called the singular values. The columns of U and V are called the left and right singular vectors, respectively. By convention, the singular values appear in a descending order in S, i.e., we have s1 ≥ s2 ≥ s3 *. . .* ≥ sD ≥ 0, where sj is the j-th singular value.

We will see that this transform plays a key role in our discussion. We will take this representation for granted and not give a proof of the SVD. But we will show how to perform an optimal dimensionality reduction given this representation.

## Svd And Dimensionality Reduction

We want to "compress" the data matrix X from dimension D
to lets say dimension K, 1 ≤ K ≤ D. More precisely, we are looking for a linear transform given by the K ×D matrix C (the compression) and a second linear transform given by the D × K matrix R (the reconstruction) so that

$$\|\mathbf{X}-\mathbf{R}\mathbf{C}\mathbf{X}\|_{F}^{2}$$
is minimized over all choices of C and R.

In words, we want to compress the D × N data matrix X
into the K × N matrix CX in such a way that the data is represented "as faithful as possible".

How do we measure the quality of the representation? We ask that the reconstruction **RCX** differs from the original matrix X as little as possible in the sense that the Frobenius norm of their difference is small, where
$$\|A\|_{F}^{2}:=\sum_{i,j}|A_{i,j}|^{2}.$$

Note that there are other natural ways of measuring the quality of a reconstruction but for simplicity we stick to this one measure.

**Lemma.** For any D×N matrix X and any D×N rank-
K *matrix* ˆX

$$\|\mathbf{X}-\hat{\mathbf{X}}\|_{F}^{2}\geq\|\mathbf{X}-\mathbf{U}_{K}\mathbf{U}_{K}^{\top}\mathbf{X}\|_{F}^{2}=\sum_{i\geq K+1}s_{i}^{2},$$

_where $\mathbf{X}=\mathbf{U}\mathbf{S}\mathbf{V}^{\top}$ is the SVD of $\mathbf{X}$, the $s_{i}$ are the singular values of $\mathbf{X}$, and $\mathbf{U}_{K}$ is the $D\times K$ matrix consisting of the first $K$ columns of $\mathbf{U}$._

Recall that the columns of U are called the left singular vectors of X. What the lemma tell us is that we should compress the data by projecting it onto these left singular vectors. 

More precisely, the most important information about the data is contained in the projection onto the first left singular vector, the second most important information is contained in the projection onto the second left singular vector etc. So the components are ordered in terms of importance, with the most important one being the first. In other words, our analysis/processing of the data uses the principal/most important components. This is why the above scheme is called the principal component analysis (PCA).

The expression $U_KU_K^TX has$ a very simple interpretation.
Let S^{(K)} be the D × N diagonal matrix that is equal to S
for the first K diagonal entries but is 0 thereafter.

We claim that
$$\mathbf{U}_{K}\mathbf{U}_{K}^{\mathsf{T}}\mathbf{X}=\mathbf{U}_{K}\mathbf{U}_{K}^{\mathsf{T}}\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}=\mathbf{U}\mathbf{S}^{(K)}\mathbf{V}^{\mathsf{T}}.\qquad(2)$$

With this interpretation, the lemma states that the best rank-K approximation to a matrix X is obtained by computing the SVD and by setting all the singular values sj, j ≥ K + 1 to zero.

The claim (2) is easily seen by checking that
$$\mathbf{U}_{K}^{\top}\mathbf{U}=(\mathbf{I}_{K\times K};\mathbf{0})\in\mathbb{R}^{K\times D}$$
is a D ×D matrix whose first K columns are the K identity and whose remaining columns are 0.

## Example Application.

Let us now discuss the implications of the SVD. One way to visualize the usefulness of this statement is to consider a particular compression problem.

For a set of images, we take the vector of D pixels that represent each image. We can then compress an image by running Some images of faces are depicted on the top-left side of Figure 23.2. Using SVD and compress the picture with the scheme above, projecting the image onto the first K columns of U. To see how well this works we can then reconstruct this image back to the original image space R^D and visualize it next to its original. This is shown in Figure 2 above.

Note that this is a slightly different application of what we had in mind when we started - as here we care about the compression, not so much about the lower-dimensional representations in R^D. But it gives a good intuition why this is a useful method. The compression aspect can also be visualized nicely. 

## Using Svd And Matrix Factorization

In previous lectures we have seen already several applications of matrix factorizations. Let us now discuss how the SVD relates to this problem.

Assume that we are given the data matrix X. Use the SVD
to write it as X = **USV**⊤.

$$\mathbf{X}=\mathbf{USV}^{\top}=\underbrace{\mathbf{U}}_{\mathbf{W}}\underbrace{\mathbf{SV}^{\top}}_{\mathbf{Z}^{\top}}=\mathbf{WZ}^{\top}.$$

So we have achieved a perfect factorization of our data matrix.
There are two differences compared to matrix factorization problems.

First, in the matrix factorization problem we typically restrict $\mathbf{W}$ and $\mathbf{Z}$ to have few columns only, lets say $K$, where  in SVD we can control the rank at any time later, and can let it range up to min{D, N}. Of course, in the low-rank case we cannot hope for a perfect factorization but we are looking for the best possible approximation. 

This difference can be easily addressed as we have already seen. Let 1 ≤ K ≤ min{*D, N*}. Let S(K) be the matrix that is equal to S except that all singular values sj for j ≥ K +1 are set to zero. We have seen this matrix already in our discussion of the SVD.

This gives us the rank-K approximation $X_K := US^{(K)}V^⊤$, and indeed, as we have discussed, it is the *best* rank-K approximation that we can find in the sense that the Frobenius norm of the difference is the smallest possible.

We can again write the above approximation in a factorized form. Again, let UK be the matrix consisting of the first K
columns of U. Similar to before we can now write

$$\mathbf{X}_{K}=\mathbf{U}_{K}\mathbf{S}^{(K)}\mathbf{V}^{\top}=\underbrace{\mathbf{U}_{K}}_{\mathbf{W}}\underbrace{\mathbf{S}^{(K)}\mathbf{V}^{\top}}_{\mathbf{Z}^{\top}}=\mathbf{WZ}^{\top},$$

where $\mathbf{W}$ is an $D\times K$ matrix and $\mathbf{Z}^{\top}$ is a $K\times N$ matrix.

The second difference is that in general matrix factorization problems we can have data matrix X that can have many missing entries. Indeed, one can construct a low-rank factorization that was close in the known values in order to predict the missing values, as we will see in the next lecture. The method using the SVD on the other hand starts with a complete data matrix. There does not seem to be an easy fix to adapt the SVD to the case of missing values. And so we see that despite some similarities between these problems there are also some significant differences.

## Pca And Decorrelation

There is another, probabilistic, view-point that gives insight why the PCA is a good idea. Assume that the D-dimensional data points are generated in an i.i.d. fashion according to some unknown distribution Dx. These N data points form the columns of our D × N matrix X. Let us compute the empirical/sample mean and co-variance: We have

$$\bar{\mathbf{x}}:=\frac{1}{N}\sum_{n=1}^{N}\mathbf{x}_{n}\quad,\quad\mathbf{K}:=\frac{1}{N}\sum_{n=1}^{N}(\mathbf{x}_{n}-\bar{\mathbf{x}})(\mathbf{x}_{n}-\bar{\mathbf{x}})^{\top}$$

If indeed the data comes from i.i.d. samples then the sample mean will converge to the true mean and the sample covariance matrix will converge to the true covariance matrix as $N\to\infty$.

Assume that we have pre-processed the data matrix $\mathbf{X}$ by subtracting the mean from each row. Using the SVD, the empirical covariance matrix can be written as

$$N\mathbf{K}=\sum_{n=1}^{N}\mathbf{x}_{n}\mathbf{x}_{n}^{\top}$$ $$=\mathbf{X}\mathbf{X}^{\top}=\mathbf{U}\mathbf{S}\mathbf{V}^{\top}\mathbf{V}\mathbf{S}^{\top}\mathbf{U}^{\top}=\mathbf{U}\mathbf{S}\mathbf{S}^{\top}\mathbf{U}^{\top}=\mathbf{U}\mathbf{S}_{D}^{2}\mathbf{U}^{\top},$$
where SD is the D × D diagonal matrix consisting of the D
first columns of S.

Now consider instead the transformed data ˜X = U⊤X. It has a sample co-variance matrix of

$$N\tilde{\bf K}=\tilde{\bf X}\tilde{\bf X}^{\sf T}={\bf U}^{\sf T}{\bf X}{\bf X}^{\sf T}{\bf U}={\bf U}^{\sf T}{\bf U}{\bf S}_{D}^{2}{\bf U}^{\sf T}{\bf U}={\bf S}_{D}^{2}.$$

This means, we have linearly transformed the data in such a way that the empirical co-variance matrix is diagonal, i.e., the various components are uncorrelated. This gives us some intuition why it is perhaps useful to first linearly transform the data via the "rotation" U^⊤X.

More is true. Note that by definition of the SVD, the first singular value, s1, is the largest of all singular values. And the empirical variance of the first feature component is equal to s_1^2 according to our calculation. This means that of all the components in our feature vector ˜X, the first component has the largest variance.

Assume that we are doing classification. It is then intuitive that it is easier to classify features that have a large variance than those that have a small variance. To see this, consider the extreme case where the variance is 0 in a particular component, i.e., the data is constant in this component. This component is then not useful for classification. From this point of view, it is then intuitive why it is good to keep the first K rows of ˜X when we perform a dimensionality reduction. These are the components that have the highest variance and they are uncorrelated.

To make sure that we understand the probabilistic interpretation of PCA, let us consider the following example. Let xj be i.i.d. samples from a D-dimensional Gaussian of mean zero and with covariance matrix
$$\mathbf{K}=\mathbf{Q}\Lambda\mathbf{Q}^{\top},$$
where Q is a D × D unitary matrix and Λ is a diagonal matrix with strictly non-zero entries.

Let X be the resulting D ×N data matrix. Assume that we run a PCA on this matrix without any preprocessing. Under the assumption that all eigenvalues are distinct and that N
tends to infinity what do you expect U to be? What could happen if some of the eigenvalues are equal?

## How To Compute U And S Efficiently 

We Start Again With The Svd

$\mathbf{X}=\mathbf{USV}^{\top}$.

We have seen in our discussion that for applications we need to compute $\mathbf{U}$ and $\mathbf{S}$. Let us see how we can do this efficiently.

Consider the $D\times D$ matrix $\mathbf{X}\mathbf{X}^{\top}$. We have

$$\mathbf{X}\mathbf{X}^{\top}=\mathbf{U}\mathbf{S}^{\top}\mathbf{U}^{\top}=\mathbf{US}_{D}^{2}\mathbf{U}^{\top}.$$

Let uj, j = 1*, . . . , D*, denote the columns of U. Then
$${\bf X X}^{\sf T}{\bf u}_{j}={\bf U S}_{D}^{2}{\bf U}^{\sf T}{\bf u}_{j}=s_{j}^{2}{\bf u}_{j}.$$

So we see that the j-th column of U is an eigenvector of XX^⊤ with eigenvalue s_j^2. Therefore, solving the eigenvector/value problem for the matrix XX^⊤ gives us a way to compute U and S.

There is a subtle point here. If uj is an eigenvector of XX^⊤ then so is −u_j. So the signs of the columns of U are not determined by this procedure. If we just want to compute X_K in order to project X onto its columns (PCA) then this sign does not matter since U_K U_K^⊤ is invariant to sign changes of columns of UK.

And what do we do if we want to determine the SVD? In this case the sign of the columns of U is also not determined uniquely, it just has to be matched to the sign of the columns of V.

Therefore, solve the above eigenvalue/eigenvector problem and fix some choice of signs to determine a D × D
matrix U consisting of eigenvectors of XX^⊤. To find now the matching V just compute U^⊤X. This is equal to SV^⊤, but we know that the entries of S are non-negative, so we can easily compute the matching V. In the exercise you will see that you can *either* solve the eigenvector problem for XX^⊤ or the one for X^⊤X. This comes in handy since we can then always work with the smaller of the two dimensions D and N.

## Pitfalls Of Pca

At this point it might seem that the PCA is a miracle cure.

Just take the data, compute the SVD, and compress. But note that the SVD is *not* invariant under scalings of the features in the original matrix X. I.e., the final representation we get *does* depend on how we scale our individual features vectors and so there is a large degree of arbitraryness. It therefore remains very important that the data is normalized properly. Experience shows that it is a good idea to remove the mean of each feature and to normalize the variance to one.