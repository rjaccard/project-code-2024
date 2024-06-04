# Text Representation Learning

## Motivation 

Finding numerical representations for words is fundamental for all machine learning methods dealing with text data.

**Goal:** For each word, find mapping (embedding)
$w_i → w_i ∈ R^K$

Representation should capture semantics of the word.
Constructing good feature representations (= representation learning) benefits all ML applications.

## The Co-Occurence Matrix 

A big corpus of un-labeled text can be represented as the co-occurrence counts.
-  n_{ij} := #contexts where word wi occurs together with word wj.

Needs definition of
- Context e.g. document, paragraph, sentence, window
- Vocabulary V := {w1, . . . , wD}

For words wd = 1, 2*, . . . , D* and context words wn = 1, 2*, . . . , N*, the co-occurence counts n_{ij} form a very sparse D × N matrix.

## Learning Word-Representations (Using Matrix Factorization)

Find a factorization of the cooccurence matrix! Typically uses log of the actual counts, i.e. x_{dn} := log(n_{dn}).

We will aim to find W, Z s.t. $X ≈ WZ^⊤$.

So for each pair of words (wd, wn), we try to 'explain' their co-occurence count by a numerical representation of the two words - in fact by the inner product of the two feature vectors W_{d:}, Z_{n:}.
$$\operatorname*{min}_{\mathbf{W,Z}}\ {\mathcal{L}}(\mathbf{W},\mathbf{Z}):={\frac{1}{2}}\sum_{(d,n)\in\Omega}f_{d n}\big[x_{d n}-(\mathbf{WZ}^{\top})_{d n}\big]^{2}$$

where W ∈ R^{D×K} and Z ∈ R^{N×K} are tall matrices, having only K ≪ D, N columns.

The set Ω ⊆ [D] × [N] collects the indices of non-zeros of the count matrix X.

Each row of those matrices forms a representation of a word (W) or a context word (Z) respectively.

## GloVe 

This model is called GloVe, and is a variant of word2vec.
- Weights f_{dn}: Give "importance" of each entry. Choosing f_{dn} := 1 is ok.
- GloVe weight function: $$f_{d n}:=\operatorname*{min}\left\{1,\left(n_{d n}/n_{\operatorname*{max}}\right)^{\alpha}\right\},\quad\alpha\in[0;1]\quad\mathrm{e.g.}\ \alpha=\frac{3}{4}$$

## Training

- Stochastic Gradient Descent (SGD)
- Alternating Least-Squares (ALS)

Open questions:
- Parallel and distributed training
- Does regularization help?

## Alternative: Skip-Gram Model (Original word2vec) 

Uses binary classification (logistic regression objective), to separate real word pairs (wd, wn) from fake word pairs. Same inner product score = matrix factorization.

Given w_d, a context word w_n is
- real = appearing together in a context window of size 5
- fake = any word wn′ sampled randomly: Negative sampling


## Learning Representations of Sentences & Documents 

- Supervised: For a supervised task (e.g. predicting the emotion of a tweet), we can use matrix factorization (below) or convolutional neural networks.

## Unsupervised:

- Adding or averaging (fixed, given) word vectors 
- Training word vectors such that adding/averaging works well
- Direct unsupervised training for sentences (appearing
together with context sentences) instead of words

## FastText 

Matrix factorization to learn document/sentence representations (supervised).

Given a sentence s_n = (w1, w2*, . . . , w*m), let x_n ∈ R^|V| be the bag-of-words representation of the sentence.

$$ min_{W,Z} L(W,Z) = \sum f(y_n W Z^⊤ x_n) $$

where W ∈ R^{1×K}, Z ∈ R^{|V|×K} are the variables, and the vector x_n ∈ R^{|V|} represents our n-th training sentence.

Here f is a linear classifier loss function, and yn ∈ {±1} is the classification label for sentence xn.