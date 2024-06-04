# Textual Data Analysis 

## Introduction: Data Analysis

Classification/clustering consists in regrouping several objects in categories/clusters (i.e. subsets of objects)

Vizualisation: display in a intelligible way the internal structures of data (documents here)

## Supervized/unsupervized

The classification can be

- supervized (strict meaning of classification) :
    - Classes are known a priori
    - They are usually meaningfull for the user
- unsupervized (called: clustering) : Clusters are based on the inner structures of the data (e.g. neighborhoods) Their meaning is really more dubious


## (Dis)Symilarity Matrix

Most of classification techniques use distance mesures or (dis)similaries: matrix of the distances between each data points: $\frac{N(N-1)}{2}$ values (symetric with null diagonal)

distance:

(1) $d(x, y) \geq 0 \quad$ and $\quad d(x, y)=0 \Longleftrightarrow x=y$

(2) $d(x, y)=d(y, x)$

(3) $d(x, y) \leq d(x, z)+d(z, y)$

dissimilarity: (1) and (2) only

## Some of the usual metrics/symilarities

- Euclidian:

$$
d(x, y)=\sqrt{\sum_{j=1}^{m}\left(x_{j}-y_{j}\right)^{2}}
$$

- generalized $(p \in[1 \ldots \infty[)$ :

$$
d_{p}(x, y)=\left(\sum_{j=1}^{m}\left(x_{j}-y_{j}\right)^{p}\right)^{1 / p}
$$

- $\chi^{2}$ :

$$
d(x, y)=\sum_{j=1}^{m} \lambda_{j}\left(\frac{x_{j}}{\sum x_{j^{\prime}}}-\frac{y_{j}}{\sum y_{j^{\prime}}}\right)^{2}
$$

where $\lambda_{j}=\frac{\Sigma_{i} \Sigma_{j} u_{i j}}{\Sigma_{i} u_{i j}}$ depends on some reference data $\left(u_{i}, i=1 \ldots N\right)$

## Some of the usual metrics/symilarities

- cosine (similarity):

$$
\mathscr{S}(x, y)=\frac{\sum_{j=1}^{m} x_{j} y_{j}}{\sqrt{\sum_{j} x_{j}^{2}} \sqrt{\sum_{j} y_{j}^{2}}}=\frac{x}{\|x\|} \cdot \frac{y}{\|y\|}
$$

- for probability distributions :
- KL-divergence:

$$
D_{K L}(x, y)=\sum_{j=1}^{m} x_{j} \log \left(\frac{x_{j}}{y_{j}}\right)
$$

- Jensen-Shannon divergence:

$$
J S(x, y)=\frac{1}{2}\left(D_{K L}\left(x, \frac{x+y}{2}\right)+D_{K L}\left(y, \frac{x+y}{2}\right)\right)
$$

- Hellinger distance:

$$
d(x, y)=d_{\text {Euclid }}(\sqrt{x}, \sqrt{y})=\sqrt{\sum_{j=1}^{m}\left(\sqrt{x_{j}}-\sqrt{y_{j}}\right)^{2}}
$$

## Bayesian approach

Probabilitic modeling: the classification is made according to $P\left(C_{k} \mid x\right)$ : an object $x^{(i)}$ is classified in category

$$
\underset{C}{\operatorname{argmax}} P\left(C \mid x=x^{(i)}\right)
$$

Discriminative: model $P\left(C_{k} \mid x\right)$ directly;

Generative: assume we know $P\left(C_{k}\right)$ and $P\left(x \mid C_{k}\right)$, then using Bayes formula:

$$
P\left(C \mid x=x^{(i)}\right)=\frac{P\left(x=x^{(i)} \mid C\right) \cdot P(C)}{P\left(x=x^{(i)}\right)}=\frac{P\left(x^{(i)} \mid C\right) \cdot P(C)}{\Sigma_{c}\left[P(C) \cdot P\left(x^{(i)} \mid C\right)\right]}
$$

$P(C): "$ prior"

$$
P(C \mid x): \text { "posterior" }
$$

$$
P(x \mid C) \text { : "likelihood" }
$$

In practice, those distributions are hardly known.

All the difficulty consists in "learning" (estimating) them from samples making several hypotheses.

## Naive Bayes

Supervised generative probabilistic (non overlaping) model:

Classification is made using the Bayes formula

$P(C)$ is estimated directly on a typical example

What is "naive" in this approach is the computation of $P(x \mid C)$

Hypothesis: feature independance:

$$
P(x \mid C)=\prod_{j=1}^{m} p\left(x_{j} \mid C\right)
$$

The $p\left(x_{j} \mid C\right)$ (a priori much fewer than the $P(x \mid C)$ ) are estimated on typical examples (learning corpus).

In the case of Textual Data: features $=$ indexing terms (e.g. lemmas)

This hypothesis is most certainly wrong but good enough in practice

## (multinomial) Logistic regression

Supervised discriminative probabilistic (non overlaping) model:

Directly model $P(C \mid x)$ as:

$$
P(C \mid x)=\prod_{j=1}^{m} f\left(x_{j}, C\right)=\frac{\exp \left(\sum_{j=1}^{m} w_{C, j} x_{j}\right)}{\sum_{C^{\prime}} \exp \left(\sum_{j^{\prime}=1}^{m} w_{C^{\prime}, j^{\prime}} X_{j^{\prime}}\right)}
$$

where $w_{C, j}$ is a parameter, the "weight" of $x_{j}$ for class $C$ ( $x_{j}$ being here some numerical representation of $j$-th indexing term: $0-1$, frequency, log-normalized, ...).

The parameters $w_{C, j}$ can be learned using various approximation algorithms (e.g. iterative or batch; IGS, IRLS, L-BGFS, ...), for instance:

$$
w_{C, j}^{(t+1)}=w_{C, j}{ }^{(t)}+\alpha\left(\delta_{C, \widehat{c}_{n}}-P\left(C \mid x_{n}\right)\right) x_{n j}
$$

with $\alpha$ a learning parameter (step strength/speed) and $\delta_{C, \hat{C}_{n}}$ the Kronecker delta function between class $\mathrm{C}$ and expected class $\widehat{C}_{n}$ for sample input $x_{n}$.

## $K$ nearest neighbors:

very simple:

classify a new object according to the majority class in its $K$ nearest neighbors (vote). (no learning phase)

## Parzen window:

same idea, but the votes are weighted according to the distance to the new object

![](https://cdn.mathpix.com/cropped/2024_05_17_a6b505ba329939b31ba0g-21.jpg?height=283&width=410&top_left_y=566&top_left_x=655)

## Dendrograms

It's a bottom-up hierachical clustering

Starts form a distance chart between the $N$ objects

(1) Regroup in one cluster the two closest "elements" and consider the new cluster as a new element

(2) compute the distances between this new element and the others

(3) loop in (1) while there are more than one element

- representation in the form of a binary tree
- Complexity: $\mathscr{O}\left(N^{2} \log N\right)$


## Dendrograms: "linkage" scheme

Goal : regroup the two closest elements" closest

Two questions:

1. How to define the distance between two clusters (two sets of elements)? (based on the distances between the elements)
2. How to (efficiently) compute distance between a former cluster and a (new) merge of two clusters?

Let $A$ and $B$ be two subclusters: what is their distance?

| method | definition | merging |
| :---: | :---: | :---: |
|  | $D(A, B)=$ | $D(A \cup B, C)=$ |
| single linkage: | $\min _{x \in A, y \in B} d(x, y)$ | $\min (D(A, C), D(B, C))$ |
| complete linkage: | $\max _{x \in A, y \in B} d(x, y)$ | $\max (D(A, C), D(B, C))$ |
| average linkage: | $\frac{1}{\|A\| \cdot\|B\|} \sum_{x \in A, y \in B} d(x, y)$ | $\frac{\|A\| \cdot D(A, C)+\|B\| \cdot D(B, C)}{\|A\|+\|B\|}$ |

## $K$-means

non hierachical non overlapping clustering

(1) choose a priori the number of clusters : $K$

(2) randomly draw $K$ objects as clusters' representatives ("clusters' centers")

(3) partition the objects with respect to the $K$ centers (closest)

(4) recompute the $K$ centers as the mean of each cluster

(5) loop in (3) until convergence (or any other stoping criterion).

Cluster representatives: mean (centre of gravity) -> $R_{k}=\frac{1}{N_{k}} \sum_{x \in C_{k}} x$

The algorithm is convergent because the intra-class variance can only decrease

$$
v=\sum_{i=1}^{K} \sum_{x \in C_{i}} p(x) d\left(x, R_{i}\right)^{2}
$$

$(p(x):$ probability of the objects)

BUT it converges to a local minimum.

## About Word Embedings

“Word embedding":

- numerical representation of words (see "Information Retrieval" lecture)
- a.k.a. "Semantic Vectors", "Distributionnal Semantics"
- objective: relative similarities of representations correlate with syntactic/semantic similarity of words/phrases.

$\rightarrow$ two key ideas:

1. representation(composition of words) = vectorial-composition(representations(word))

$$
\text { for instance: representation(document) }=\sum_{\text {word } \in \text { document }} \text { representation(word) }
$$

2. remove sparsness, compactify representation: dimension reduction

## Word Embedings: different techniques

Main techniques:

- co-occurence matrix; often reduced (LSI, Hellinger-PCA)
- probabilistic/distribution (DSIR, LDA)
- shallow (Mikolov) or deep-learning Neural Networks


## about Deep Learning

- there is NO need of deep learning for good word-embedding
- not all Neural Network models (NN) are deep learners
- models: convolutional NN (CNN) or recurrrent NN (RNN, incl. LSTM)
- still suffer the same old problems: overfitting and computational power


## Classification: evaluation

- classification (supervised): evaluation is "easy" $\rightarrow$ test corpus (some known samples kept for testing only)
- clustering (unsupervised): objective evaluation is more difficult: what are the criteria?


## Clustering (unsupervised learning) evaluation

There is no absolute scheme with which to evaluate clustering, but a variety of ad-hoc measures from diverse areas/point-of-view.

For $K$ non overlapping clusters (with objects having a probability $p$ ), standard measures include:

Intra-cluster variance (to be minimized): $\quad v=\sum_{k=1}^{K} \sum_{x \in C_{k}} p(x) d\left(x, \overline{\bar{x}_{k}}\right)^{2}$

$$
\text { Inter-cluster variance (to be maximized): } \quad V=\sum_{k=1}^{K} \underbrace{\left(\sum_{x \in C_{k}} p(x)\right)}_{=p\left(C_{k}\right)} d\left(\overline{x_{k}}, \bar{x}\right)^{2}
$$

usually: high intra-cluster similarity and low inter-cluster similarity

## "Visualization"

Visualize: project/map data in 2D or 3D

More generaly: techniques presented in this section are to lower the dimension of data go form $N$-D to $n$-D with $n<N$ or even $n \ll N$

usualy means: go from sparse to dense representation

## Principal Components Analysis (PCA)

Input: a matrix $\bar{M}$ objects (rows) - features (columns) (of size $N \times m$ with $N>m$ ) centered: $\bar{M}_{i \bullet}=x^{(i)}-\bar{x}$

Singular value decomposition (SVD) of $\bar{M}$ :

$$
\bar{M}=U \wedge V^{t}
$$

$\wedge$ diagonal, ordered: $\lambda_{1} \geq \lambda_{2} \geq \ldots \geq \lambda_{m} \geq 0$, $U$ of size $N \times m$ with orthogonal columns and $V$ orthogonal, of size $m \times m$

- Projection in a low dimension space:

$$
\widetilde{M}=U_{q} \wedge_{q} V_{q}^{t}
$$

with $q<m$ and $X_{q}$ matrices reduced to only the $q$ first singular values

- $\tilde{M}$ is the better approximation of rank $q$ of $\bar{M}$.
- "better approximation" w.r.t several criteria:
    - $L_{2}$ norm, biggest variance (trace and determinant of the corvariance matrix), Frobenius norm, $\ldots$
This means that the subspace of the first $q$ principal components is the best linear approximation of dimension $q$ of the data, "best" in the sense of the distance between the original data points and their projection.

How to choose dimension $q$ ?

- sometimes imposed by the application (e.g. for visualization $q=2$ or 3 )
- otherwise: make use of the spectrum:
- simple: choose $q$ where there is a "big step" in $\lambda_{i} / \Sigma_{j} \lambda_{j}$ plot (a.k.a. "Cattell's scree plot" or "explained variance"):

