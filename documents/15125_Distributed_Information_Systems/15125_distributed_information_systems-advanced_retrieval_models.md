# 7. LATENT SEMANTIC INDEXING 

Vector space retrieval is vague and noisy

- Based on index terms
- Unrelated documents might be included in the answer set
- apple (company) vs. apple (fruit)
- Relevant documents that do not contain at least one index term are not retrieved
- car vs. automobile


## Observation

- The user information need is more related to concepts and ideas than to index terms

Despite its success and widespread use the vector space retrieval model suffers from some problems. The important insight is that terms may indicate a concept a user is interested in, but there does not necessarily exist a one to one correspondence between terms and concepts. As a consequence retrieval results may contain irrelevant documents, and relevant documents may be missed.

## The Problem

Vector Space Retrieval handles poorly the following two situations

1. Synonymy: different terms refer to the same concept, e.g. car and automobile

- Result: poor recall

2. Homonymy: the same term may have different meanings, e.g. apple, model, bank

- Result: poor precision

These problems are related to the fact that the same concepts can be expressed through many different terms (synonyms) and that the same term may have multiple meanings (homonyms). Studies show that different users use the same keywords for expressing the same concepts only $20 \%$ of the time.

## Example: 3 documents

Let's illustrate the problem resulting from synomyms and homonyms by an example. Among these three documents at the level of terms doc 1 and doc 2 are (seem) highly related, whereas doc3 has no similarity with the other two documents. With human background knowledge it is however easy to see that in reality doc2 and doc3 are closely related, as they talk about mobile communications, whereas doc 1 is completely unrelated to the others as it is about health and nutrition.

## Key Idea

Map documents and queries into a lower-dimensional space composed of higher-level concepts

- Each concept represented by a combination of terms
- Fewer concepts than terms
- Vehicle $=\{$ car, automobile, wheels, auto car, motor car\}


## Dimensionality reduction

- Retrieval (and clustering) in a reduced concept space might be superior to retrieval in the high-dimensional space of index terms

Thus it would be an interesting to base information retrieval methods on the use of concepts, instead of terms. To that end it is first necessary to define a "concept space" to which documents and queries are mapped, and compute similarity within that concept space. This idea is developed in the following. The concept space should ideally have much lower dimension than the term space, whose dimensionality is determined by the size of the vocabulary.

## Using Concepts for Retrieval

This figure illustrates the approach: rather than directly relating documents $\mathrm{d}$ and terms $t$, as in vector space retrieval, there exists an intermediate layer of concepts $\mathrm{c}$ to which both queries and documents are mapped. The concept space can be of a smaller dimension than the term space. In this small example we can imagine that the terms $\mathrm{t} 1$ and $\mathrm{t} 2$ are synonyms and thus related to the same concept c1. If now a query t2 is posed, in the standard vector space retrieval model only the document $\mathrm{d} 1$ would be returned, as it contains the term t2. By using the intermediate concept layer the query $\mathrm{t} 2$ would also return the document d2.

## Example: Concept Space

Applying this idea to our example before, we can imagine to have a concept space consisting of four concepts, two related to health, two related to mobile communication. When we consider now doc 2 and doc3 we can already recognize much better the close conceptual relationship the two documents have.

## Similarity Computation in Concept Space

Concept represented by terms, e.g.

$$
\begin{aligned}
\text { device }= & \{\text { iOS, iPad, RIM, mobile, handy, } \\
& \text { tablet, apple, blackberry }\}
\end{aligned}
$$

Document represented by concept vector, counting number of concept terms, e.g.

$$
\begin{aligned}
& d o c_{1}=(4,3,3,1) \\
& \operatorname{doc}_{3}=(0,0,5,2)
\end{aligned}
$$

Similarity computed by scalar product of normalized concept vectors

We may consider concepts as being represented by sets of terms, and documents by concept vectors that count how many concept terms occur in the document. Using this approach we would obtain the non-normalized concept vectors doc $1=(4,3,3,1)$, doc $2=(3,1,3,3)$ and doc $3=(0,0,5,2)$.

## Result

$$
\text { Similarity }\left(\text { doc }_{1}, \text { doc }_{2}\right)=0.245 \quad \text { Similarity }\left(\text { doc }_{2}, \text { doc }_{3}\right)=0.3
$$

Similarity $\left(\right.$ doc $_{1}$, doc $\left._{3}\right)=0.22$

After normalizing these vectors we compute the cosine similarities among the resulting concept vectors and obtain:

$\operatorname{Sim}(2,3)=0.3$

$\operatorname{Sim}(1,2)=0.245$

$\operatorname{Sim}(1,3)=0.22$

This result shows that indeed documents 2 and 3 are the more related ones, though still some confusion remains due to the high number of synonyms occurring in these documents.

## Basic Definitions

Problem: how to identify and compute "concepts" ?

Consider the term-document matrix

- Let $M_{i j}$ be a term-document matrix with $m$ rows (terms) and $\mathrm{n}$ columns (documents)
- To each element of this matrix is assigned a weight $\mathrm{w}_{\mathrm{ij}}$ associated with $\mathrm{t}_{\mathrm{i}}$ and $\mathrm{d}_{\mathrm{j}}$
- The weight $\mathrm{w}_{\mathrm{ij}}$ can be based on a tf-idf weighting scheme

The problem is to identify a method that identifies and characterizes important concepts in document collections. One approach would be to perform this task manually, e.g. by using a predefined ontology and let users annotate documents using terms of the ontology. This is an approach that his been used in libraries, but is labor intensive. Thus we will now present a method that performs the task of concept identification and document classification by concepts automatically. Starting point for the method is the term-document matrix that we have introduced for vector space retrieval with weigths based on a tf-idf weighting scheme.

## Computing the Ranking Using M

We can understand the process of producing a retrieval results in vector space retrieval as a matric operation. This is illustrated in this figure. The ranking is the result of computing the product of a query vector $q$ with the term-document matrix $\mathrm{M}$. We assume that all columns in $\mathrm{M}$ and 1 are normalized to 1 .

## Identifying Top Concepts

Key Idea: extract the essential features of $\mathrm{M}^{\mathrm{t}}$ and approximate it by the most important ones

One way to understand of how concepts can be extracted from a document collection is to consider the effect of the term-document matric on data. If we apply this matrix to a (high-dimensional) unit ball it will distort this ball into an ellipsoid. This ellipsoid will have one direction with the strongest distortion. We may think of this direction as corresponding to a particularly important concept of the document collection.

## Singular Value Decomposition (SVD)

Represent Matrix $M$ as $M=K . S . D^{t}$

- $K$ and $D$ are matrices with orthonormal columns

$$
\text { K. } K^{\mathrm{t}}=\mathrm{I}=\mathrm{D} . \mathrm{D}^{\mathrm{t}}
$$

- S is an $r \times r$ diagonal matrix of the singular values sorted in decreasing order where $r=\min (m, n)$, i.e. the rank of $M$
- Such a decomposition always exists and is unique (up to sign)

To extract this particularly important directions of a matrix mapping, a standard mathematical construction from linear algebra is used, the singular value decomposition (SVD). SVD decomposes a matrix into the product of three matrices. The middle matrix $S$ is a diagonal matrix, where the elements of this matrix are the singular values of the matrix $\mathrm{M}$.

## Construction of SVD

$K$ is the matrix of eigenvectors derived from M.M

$D$ is the matrix of eigenvectors derived from $M^{t} . M$

Algorithms for constructing the SVD of a $m \times n$ matrix have complexity $O\left(n^{3}\right)$ if $m \leq n$

Formally the SVD can be computed by constructing eigenvectors of matrices derived from the original matrix M. This computationg can be performed in $\mathrm{O}\left(\mathrm{n}^{\wedge} 3\right)$. Note that the complexity is considerable, which makes the approach computationally expensive. There exist however also approximation techniques to perform this decomposition more efficiently.

## Interpretation of SVD

We can write $M$ as sum of outer vector products

$$
M=\sum_{i=1}^{r} s_{i} k_{i} \otimes d_{i}^{t}
$$

The $\mathrm{s}_{\mathrm{i}}$ are ordered in decreasing size

By taking only the largest ones we obtain a good

"approximation" of $M$ (least square approximation)

The singular values $s_{i}$ are the lengths of the semi-axes of the hyperellipsoid $\mathrm{E}$ defined by

$$
E=\left\{M x \mid\|x\|_{2}=1\right\}
$$

One way to understand of how the SVD extracts the important concepts from the term-document matrix is the following: the decomposition can be used to rewrite the original matrix as the sum of components that are weighted by the singular values. Thus we can obtain approximations of the matrix by only considering the larger singular values. The SVD after eliminating less important dimensions (smaller singular values) can be interpreted as a least square approximation to the original matrix. The symbol $\otimes$ denotes the outer product of two vectors, $d_{i}$ is the $i$-th row of $D$.

The singular values have also a geometrical interpretation, as they tell us how a unit ball $(\|x\|=1)$ is distorted when the linear transformation defined by the matrix $M$ is applied to it. We can interpret the axes of the hyperellipsoid $\mathrm{E}$ as the dimensions of the concept space.

## Latent Semantic Indexing

In the matrix S, select only the $s$ largest singular values

- Keep the corresponding columns in $\mathrm{K}$ and $\mathrm{D}$

The resultant matrix is called $M_{s}$ and is given by

- $M_{s}=K_{s} \cdot S_{s} \cdot D_{s}{ }^{t}$ where $s, s<r$, is the dimensionality of the concept space

The parameter s should be

- large enough to allow fitting the characteristics of the data
- small enough to filter out the non-relevant representational details

Using the singular value decomposition, we can now derive an "approximation" of $M$ by taking only the s largest singular values in matrix $S$. The choice of $s$ determines on how many of the "important concepts" the ranking will be based on. The assumption is that concepts with small singular value in $S$ are rather to be considered as "noise" and thus can be neglected. The resulting method is called Latent Semantic Indexing.

## Answering Queries

Documents can be compared by computing cosine similarity in the concept space, i.e., comparing their columns $\left(D_{s}{ }^{t}\right)_{i}$ and $\left.\left(D_{s}\right)^{t}\right)_{j}$ in matrix $D_{s}{ }^{t}$

A query $q$ is treated like one further document

- it is added as an additional column to matrix $\mathrm{M}$
- the same transformation is applied as for mapping $M$ to $D$

After performing the SVD the similarity of different documents can be determined by computing the cosine similarity measure among their representation in the concept space (the columns of matrix $D_{s}{ }^{t}$ ). Queries are considered like documents that are added to the document collection. Answering queries then corresponds then to computing the similarity between the query considered as a document and the documents in the collection.

## Mapping Queries

## Mapping of $M$ to $D$

$$
M=K . S . D^{t}
$$

$S^{-1} \cdot K^{t} \cdot M=D^{t} \quad\left(\right.$ since $\left.K \cdot K^{t}=1\right)$

$\mathrm{D}=\mathrm{M}^{\mathrm{t}} \cdot \mathrm{K} \cdot \mathrm{S}^{-1}$

Apply same transformation to q:

$$
q^{*}=q^{t} \cdot K_{s} \cdot S_{s}^{-1}
$$

Then compare transformed vector by using the standard cosine measure

$$
\operatorname{sim}\left(q^{*}, d_{i}\right)=\frac{q^{*} \bullet\left(D_{s}^{t}\right)_{i}}{\left|q^{*}\right|\left|\left(D_{s}^{t}\right)_{i}\right|}
$$

This construction works as follows: when a new column (the query) is added to $\mathrm{M}$, we have to apply the same transformation to this new column, as to the other columns of $M$, in order to produce the corresponding column in the matrix $D_{s}{ }^{t}$, representing documents in the concept space. We exploit the fact that $\mathrm{K}_{s}{ }^{t} \cdot \mathrm{K}_{s}=1$.

Since $\mathrm{M}_{\mathrm{s}}=\mathrm{K}_{\mathrm{s}} \cdot \mathrm{S}_{\mathrm{s}} \cdot \mathrm{D}_{\mathrm{s}}{ }^{t}$ we obtain $\mathrm{S}_{\mathrm{s}}{ }^{-1} \cdot \mathrm{K}_{\mathrm{s}}{ }^{t} \cdot \mathrm{M}_{\mathrm{s}}=\mathrm{D}_{\mathrm{s}}{ }^{t}$ or $\mathrm{D}_{\mathrm{s}}=\mathrm{M}_{\mathrm{s}}{ }^{\mathrm{t}} \cdot \mathrm{K}_{\mathrm{s}} \cdot \mathrm{S}_{\mathrm{s}}{ }^{-1}$.

This is the transformation that is applied to the query vector $q$ to obtain a query vector $q^{*}$ in the concept space. After that step, the similarity of the query to the documents in the concept space can be computed. (( $\left.D_{s}{ }^{t}\right)_{\text {i }}$ idenotes the i-th column of matrix $D_{s}{ }^{t}$ )

## Discussion of Latent Semantic Indexing

Latent semantic indexing provides an interesting conceptualization of the IR problem

Advantages

- It allows reducing the complexity of the underlying concept representation
- Facilitates interfacing with the user

Disadvantages

- Computationally expensive
- Poor statistical explanation

From a modelling perspective LSI suffers from poor explanatory power. For example, the least squares approximation concept is related to the assumption that term frequencies are normally distributed, which is in contradiction with the observation that term frequencies are power law distributed.

## Alternative Techniques

Probabilistic Latent Semantic Analysis

- Based on Bayesian Networks


## Latent Dirichlet Allocation

- Based on Dirichlet Distribution
- State-of-the-art method for concept extraction


## Same objective of creating a lower-dimensional concept space based on the term-document matrix

- Better explained mathematical foundation
- Better experimental results

The conceptual problems of LSI have triggered significant efforts in developing better suited models for concept extraction. The most recent and successful result of this has been the development of a method based on the use of Dirichlet distributions. Like LSI it produces a concept space, where concepts are represented as term vectors. The method has better theoretical foundations and empirically it produces better results, and is nowadays considered as the golden standard. The approach is mathematically more involved than LSI, and therefore we will not be able to develop this method in this course.

## Latent Dirichlet Allocation (LDA)

Idea: assume a document collection is (randomly) generated from a known set of topics (probabilistic generative model)

This illustration shows the basic idea underlying LDA: it is assumed that there exist topics that are represented as mixtures of words. In the example we see words that are related to two meanings of "bank", the financial institution and the river bank, and are represented by different related works. Then, documents are supposed to be generated from a mixture of topics, where the mixture is defined by some weights, as indicated in the figure. As a result each document contains terms form its associated topics in the right proportion.

Similar to the probabilistic language model used in information retrieval, we have here another example of a probabilistic generative model.

## Document Generation using a Probabilistic Process

For each document, choose a mixture of topics

For every word position, sample a topic from the topic mixture

For every word position, sample a word from the chosen topic

Given the underlying model we can define a probabilistic process for generating documents.

## LDA: Topic Identification

Approach: Inverting the process: given a document collection, reconstruct the topic model

The challenge is to determine the probabilistic model. The situation we consider in practice is that a set of documents is given, and we intend to reconstruct the (most likely) probabilistic process that has generated this document collection. This is a difficult problem to solve.

## Latent Dirichlet Allocation

Topics are interpretable unlike the arbitrary dimensions of LSI

Distributions follow a Dirichlet distribution Construction of topic model is mathematically involved, but computationally feasible Considered as the state-of-the art method for topic identification

We do not present the details of LDA here, as the method is mathematically fairly involved. However, it is important to note that it is considered today as the stateof-the-art method of topic detection.

## Use of Topic Models

Unsupervised Learning of topics

- Understanding main topics of a topic collection
- Organizing the document collection

Use for document retrieval: use topic vectors instead of term vectors to represent documents and queries

Document classification (Supervised Learning): use topics as features

Topic models provide a representation of documents at a conceptual level. Therefore they are applied in many different contexts, including document retrieval and classification.

## 8. WORD EMBEDDINGS

With latent semantic indexing we have exploited the idea that words that occur together in documents have a likelihood to have also some shared meaning. This idea is actually quite old, and has been already expressed, for example, by Firth in 1957. We will now exploit this idea in a slightly different way, by focusing on a much smaller context of a word than its document. We will just consider the local neighborhood of the work within a phrase. Typically we will consider all the neighborhoods that we can find in all documents of a large document collection.

For each word $\mathrm{w}$ we can identify its neighboring words, which will call its context and denote by $\mathrm{C}(\mathrm{W})$. The context can be determined by choosing a certain number of preceding and succeeding words, e.g. a typical number used is 5.

## Similarity-Based Representation

One of the most successful ideas in natural language processing

- Two words are considered as similar, when they have similar contexts
- Context captures both syntactic and semantic similarity
- Syntactic: e.g. king - kings
- Semantic: e.g. king - queen
- Implicitly used with the term-document matrix M
- Less localized context
- No distinction between context and word

This idea is one of the main ideas used (successfully) in natural language processing. The neighborhood captures not only semantic relationships among words (as would also co-occurrence in the same document).It can at the same time also capture syntactic relationships. This is a main difference to methods based on document co-occurrence like LSI.

A second important difference is that methods based on this idea distinguish between a word occurring as the center of a context and as a member of context. For example, it is very unlikely the word "dog" would have in its context a second occurrence of the word "dog". Thus dog as a "context word" needs to be treated differently from dog as the word of interest. This distinction is not made in purely co-occurrence based methods.

## Idea: Word Embeddings

Try to model how likely a word and a context occur together

Approach:

- Map words into a low-dimensional space (e.g., $d=200$ )
- Map context words into the same low-dimensional space
- A different mapping as before for the same words
- Interpret the vector distance (product) as a measure for how likely the word and its context occur together
- Due to projection in low-dimensional space, similar words and contexts should be close

The basic idea for word embeddings is simple. Both words and context words are mapped into the same low-dimensional space. Their representations in that space should be similar, if the word and the context word occur often together. Thus we capture the information on word context in a low-dimensional representation. Through the dimensionality reduction the expectation is that words and contexts that play similar roles would also move together, and thus we could capture syntactic and semantic similarity.

Dimensionality reduction is helpful, since vocabularies can become very large, in particular if not only words but also short phrases are included (e.g. tens of millions of entries). Thus data would be very sparse in these spaces and it would be difficult to model similarity. The low-dimensional spaces have on the other hand typically a few hundred dimensions.

## Overview of the Model

Columns represent words of the vocabulary in concept space of dimension d

## Parameters of model $(\theta)$

We introduce the basic notations we will use in the following. Note that the size of the vocabulary $m$ is typically very large (e.g. millions), whereas the size of the low-dimensional space $d$ is typically in the hundreds. The model will be fully specified by the two matrices $\mathrm{W}^{(\mathrm{w})}$ and $\mathrm{W}^{(c)}$ used to map words and context words. For convenience we will denote in the following the coefficients of these two matrices by $\theta$.

## Learning the Model from the Data

Consider a pair $(w, c)$

Model this as a probability (sigmoid)

$P(D=1 \mid w, c, \theta)=\frac{1}{1+e^{-\boldsymbol{c} \cdot \boldsymbol{w}}}=\sigma(\boldsymbol{c} \cdot \boldsymbol{w}) \quad f(x)=\frac{1}{1+e^{-\boldsymbol{w}}}$

Intuition: convert similarity value in vector space into a probability

Differently to LSI, where the (parameters of the) model have been derived by a mathematical operation (SVD), the idea in word embeddings is to learn the parameters directly from the data. To start with, we consider a word-context pair $(w, c)$ and ask the question whether it comes from the data. We would like that (ideally) the model gives us a probability of 1 if this is the case. In order to derive a probability from the model (the embedding into a low-dimensional space), we proceed as follows: we first take the scalar product of the embedded word and the context word vectors (this is where the parameters are hidden). This product will be large positive when the vectors are similar and large negative when they are opposite. In order to turn those values into a quantity that can be interpreted as probability (i.e. a value in $[0,1]$ ) we apply the sigmoid function It produces values close to 0 for large negative arguments, and values close to 1 for large positive arguments. The use of the sigmoid function in this model is for exactly the same reasons as it is for its use in binary logistic regression, converting a similarity value into a probability. Apart from mapping the values to $[0,1]$ it also is insensitive to large outliers.

## Problem: finding $\boldsymbol{\theta}$

Here we illustrate the embedding of words and context words in the same lowdimensional space. The idea is that the context words that typically co-occur together with a word, have similar embedding vectors, whereas others (like monkey, which is rarely occurring together with bank) have very different ones. The sigmoid function then converts the similarity values obtained from the scalar products of the embedding vectors into the interval $[0,1]$.

## Finding Parameters

- Assume we have positive examples $D$ for $(w, c)$, as well as negative examples $\widetilde{D}$, not occurring in the document collection
- Find $\theta$ such that the overall probability is maximized

$$
\begin{gathered}
\theta=\underset{\theta}{\operatorname{argmax}} \prod_{(w, c) \in D} P(D=1 \mid w, c, \theta) \prod_{(w, c) \in \tilde{D}} P(D=0 \mid w, c, \theta)= \\
\underset{\theta}{\operatorname{argmax}} \sum_{(w, c) \in D} \log \sigma(\boldsymbol{c} \cdot \boldsymbol{w})+\sum_{(w, c) \in \widetilde{D}} \log \sigma(-\boldsymbol{c} \cdot \boldsymbol{w})
\end{gathered}
$$

Now we assume that we do not only know positive examples of word-context occurrences, but also negative ones, i.e. pairs that do not occur together. We can similarly model this case as a probability $P(D=0 \mid w, c, \theta)$. If we have now a (big) collection of positive and negative samples $D$ and $\widetilde{D}$, the overall probability of such a collection to occur can be expressed as the product of all individual probabilities. Given this overall probability, the problem we would like to solve is to find parameters $\theta$ that maximize this probability. This is then the best model we can obtain under the assumptions that have been made.

## Loss Function

Define a loss function (to be minimized)

$$
\begin{aligned}
& J(\theta)=\frac{1}{s} \sum_{t=1}^{s} J_{t}(\theta) \\
& J_{t}(\theta)=-\log \left(\sigma\left(\boldsymbol{c} \cdot \boldsymbol{w}_{t}\right)\right)-\sum_{k=1}^{K} \log \left(\sigma\left(-\boldsymbol{c}_{k} \cdot \boldsymbol{w}_{t}\right)\right)
\end{aligned}
$$

$\boldsymbol{c}_{k}$ are negative examples of context words taken from a set $P_{n}\left(w_{t}\right)$

Following the previous derivation we can define a loss function $\mathrm{J}$ that optimizes the probabilities if minimized. (We transform the maximization problem into a minimization problem by defining a loss function $J(\theta)$ ) The loss function is defined over all terms in the vocabulary. For each term w it consists of a first component corresponding to a positive example, a (w,c) pair that occurs in the document collection, and a couple of negative examples for the same word. The question is how to obtain the negative examples.

## Obtaining Negative Samples

Negative samples are taken from

$P_{n}(w)=V \backslash C(w)$

Empirical approach

- If $p_{w}$ is the probability of word $w$ in collection, choose the word with probability $p_{w}{ }^{3 / 4}$
- Less frequent words are sampled more often
- Practically: approximate the probability by sampling a few non-context words

The method for learning the model relies on having negative samples. How to obtain them? We can choose any word from the vocabulary $\mathrm{V}$ that is not contained itself in the context. In order to model the occurrences we do this by considering the frequency at which the words occur in the document collection. Doing so, experience shows that high frequency words (e.g. stopwords) would however be favored to much, reducing the quality of the model. Thus the probability of word occurrence used for sampling is moderated by an exponent (in practice $3 / 4$ ). Also for obtaining the statistics on word probabilities for practical purposes not the whole data collection is used, but just a small sample of words not occurring in the context.

## Stochastic Gradient Descent 

For every $\left(w_{t}, c\right)$ in $D$, update $\theta$

$$
\theta^{\text {new }}=\theta^{\text {old }}-\alpha \nabla_{\theta} J_{t}\left(\theta^{\text {old }}\right)
$$

For $J_{t}$ updates only affect rows in $W^{(w)}$ and $W^{(c)}$ that correspond to $\boldsymbol{w}_{t}, \boldsymbol{c}$ and $\boldsymbol{c}_{k}$, e.g.,

$$
\boldsymbol{w}_{t}^{\text {new }}=\boldsymbol{w}_{t}^{\text {old }}-\alpha \frac{\partial}{\partial \boldsymbol{w}_{t}} J_{t}\left(\boldsymbol{w}_{t}^{\text {old }}, \boldsymbol{c}^{\text {old }}, \boldsymbol{c}_{t}^{\text {old }}, \ldots, \boldsymbol{c}_{t}^{\text {old }}\right)
$$

Finally, given the loss function, finding the optimal parameters $\theta$ can then be done using standard methods from machine learning. Then $\theta$ can be determined using gradient descent, i.e. standard search for minima using derivatives. More precisely, we will apply stochastic gradient descent. We update the parameters for each sample, separatly. Standard gradient descent would update the values of data only after having seen all samples, which would take extremely long given the very large number of samples. When stochastic gradient descent is used, only rows that contain the word or some context word in the loss function need to be updated. This implies that the data has to be organized that these rows can be efficiently accessed (e.g. using hashing).

## Computing the Derivative

Then

$$
\begin{gathered}
x=\mathbf{c} \cdot \boldsymbol{w}, \mathrm{p}=\sigma(x), z_{k}=-\mathbf{c}_{k} \cdot \boldsymbol{w}, q_{k}=\sigma\left(z_{k}\right) \\
J_{t}\left(\boldsymbol{w}, \mathbf{c}, \mathbf{c}_{1}, \ldots, \mathbf{c}_{k}\right)=-\log (p)-\sum_{k=1}^{K} \log q_{k} \\
\frac{\partial J_{t}}{\partial \boldsymbol{w}}=\frac{\partial J_{t}}{\partial p} \frac{\partial p}{\partial x} \frac{\partial x}{\partial \boldsymbol{w}}+\sum_{k=1}^{K} \frac{\partial J_{t}}{\partial q_{k}} \frac{\partial q_{k}}{\partial z_{k}} \frac{\partial z_{k}}{\partial \boldsymbol{w}} \\
\frac{\partial J_{t}}{\partial p}=-\frac{1}{p}, \frac{\partial p}{\partial x}=\mathrm{p}(1-\mathrm{p}), \frac{\partial x}{\partial \boldsymbol{w}}=\mathbf{c} \\
\frac{\partial J_{t}}{\partial \boldsymbol{w}}=-(1-\mathrm{p}) \mathbf{c}+\sum_{k=1}^{K}\left(1-q_{k}\right) \mathbf{c}_{k}
\end{gathered}
$$

Computing the derivative reveals that the updates to the parameters of the word embedding model are very simple computations. They involve the computation of the probability values for the words and context words and multiplying them with the existing embedding vectors. This (incomplete) computation shows how the weights of the embedding vector $\mathrm{w}$ of the word are updated.

## Result

Matrices $W^{(w)}$ and $W^{(c)}$ that capture information on word similarity

- Words appearing in similar contexts generate similar contexts and vice versa
- Hence, mapped to similar representations in lower dimensional space
- Use $W=W^{(w)}+W^{(c)}$ as the low-dimensional representation

As a result we obtain two models mapping words into a low dimensional space for different reasons. In practice, the final model is constructed as the sum of the two matrices. Though, there exists no theoretical insight, why exactly this models work well, practice shows that they are organizing words in interesting ways, capturing many semantic and syntactic relationships.

## A word embedding ...

1. depends only on the dimension $d$
2. depends on the dimension $d$ and number of iterations in gradient descent
3. depends on the dimension $d$, number of iterations and chosen negative samples
4. there are further factors on which it depends

## CBOW (Continuous Bag of Words Model)

- Predict word from context

GLOVE: exploits the following observation

|  | $\mathrm{x}=$ solid | $\mathrm{x}=$ gas | $\mathrm{x}=$ water | $\mathrm{x}=$ random |
| :---: | :---: | :---: | :---: | :---: |
| $P(x \mid$ ice $)$ | large | small | large | small |
| $P(x \mid$ steam $)$ | small | large | large | small |
| $\frac{P(x \mid \text { ice })}{P(x \mid \text { steam })}$ | large | small | $\sim 1$ | $\sim 1$ |

## Technically similar

The model we have discussed is one variant of a number of similar models that have been proposed recently. One interesting model is GLOVE, which is based on the observation that ratios of probabilities can be used to capture semantic relationships among terms. For example, the term solid is much more likely to cooccur with ice, than with water, and similarly steam co-occurs much more likely with gas than with ice. On the other hand, water co-occurs frequently with both. So the ratio of probabilities captures semantics on the meaning of solid and gas, beyond co-occurrence.

Technically most of these models follow similar approaches, first modeling some observation on how co-occurrence can capture semantic relationship, and then using gradient descent methods to learn the parameters.

## Properties of Word Embeddings

1. Similar terms are clustered
2. Syntactic and semantic relationships encoded as linear mappings
3. Dimensions can capture meaning

Word Embeddings have received recently a lot of attention as they exhibit fascinating capacity to capture different types of relationships among words. We will illustrate some of those in the following.

## Syntactic Relationships

Word embeddings also capture syntactic relationships, like singular-plural or comparative and superlative, as shown here. This type of visualizations is obtained by projecting from the d-dimensional word embedding space (appropriately) into a 2-dimensional space.

## Word Analogies: semantic relationships

Even more interestingly, word embeddings enable "computing" with relationships (this is called the word analogy task). Analogies translate into linear mappings!

## Use of Word Embedding Models

Document Search

- Use word embedding vectors as document representation

Thesaurus construction and taxonomy induction

- Search engine for semantically analogous / related terms

Document classification

- Use of word embedding vectors of document terms as features

