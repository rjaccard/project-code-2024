# Modern Neural-Networks approaches to NLP 

## Word Embedings

“Word embedding":

- numerical representation of "words"("tokens")
- a.k.a. "Semantic Vectors", "Distributionnal Semantics"
- objective: relative similarities of representations correlate with syntactic/semantic similarity of words/phrases.
- two key ideas:

1. representation(composition of words) $=$ vectorial-composition(representations(word)) for instance: representation(phrase) $=\sum_{\text {word } \in \text { phrase }}$ representation(word)
2. remove sparsness, compactify representation: dimension reduction

## Word Embedings: different techniques

Main techniques:

- co-occurence matrix; often reduced (LSI, Hellinger-PCA (2013), GloVe (2014))
- probabilistic/distribution (DSIR, LDA)
- shallow (Mikolov et al. 2013) or deep Neural Networks (ELMo)

Popular word embeding are not from Deep Learning but can then serve as input to Deep Learners

## Word embedding "geometry"

- The geometry of embeddings should account for desired properties (e.g. syntactic, semantics, synonymy, word classes, ...)

e.g. predict new word representation (embedding) from the sum of embeddings of words around it

- Word embedding indeed exhibit some semantic compositionality


## word2vec (Mikolov et al. 2013)

Predict new word representation (embedding) from the sum of the embeddings of the words around it

context $=(2 k+1)$-gram around (not including) word:

$$
w_{i-k} \cdots w_{i-1}\left(\mathbf{w}_{\mathbf{i}}\right) w_{i+1} \cdots w_{i+k}
$$

word2vec comes with 2 flavors:

- CBoW (Continuous Bag-of-Words): predicts the current "word" based on its context
- Skip-gram: predict the context from the current "word"


## word2vec key ideas

- idea \#1:

unsupervised co-learning of context $c$ representation and word $w$ representation so as to maximize either $P(c \mid w)$ (skip-gram model) or $P(w \mid c)$ (CBoW model).

- idea \#2 ("negative sampling"): minimize as well $P\left(w^{\prime} \mid c\right)$ for $w^{\prime}$ not having $c$ as context

Actual other key simplification:

- turn word prediction $(P(w \mid c))$ into binary classification $(P(y=1 \mid w, c))$ Example:

Turn $P(X \mid$ black cat $\boldsymbol{X}$ the white) (for all words $X$ ) into : $P(O k \mid$ black cat ate the white) (1 number)

## word2vec method

More formally: the "word embeddings" (i.e. vectors) $h_{i}=h\left(w^{(i)}\right) \in \mathbb{R}^{d}$ (for each word $\left.w^{(i)} \in \mathscr{L}\right)$ are optimized at the same times as "reverse projection" $m_{j} \in \mathbb{R}^{d}$ (i.e. matrix $M=\left(m_{j}\right)$ projects "word embeddings" back to input space; this corresponds to the weight of the output layer) such that the context log-likelihood

$$
L=-\sum_{w \in \text { corpus }} \log Q(c, w)
$$

is minimized, where:

- in CBoW, using a softmax output layer, $Q(c, w)=P(w \mid c)$ could be modeled as

$$
P\left(w^{(i)} \mid c\right)=\frac{\exp \left(m_{i} \cdot h(c)\right)}{\sum_{w^{(k)} \in \mathscr{L}} \exp \left(m_{k} \cdot h(c)\right)}
$$

(for a context $c$ of word $w^{(i)}, h(c)=\sum_{w \in c} h(w)$ )

- and in skipgram $Q(c, w)=P(c \mid w)$ modeled similarly.


## word2vec actual loss

In fact, softmax is too expensive too compute (and less stable, it seems) so, rather than softmax, the output is directly $\sigma\left(m_{i} \cdot h(c)\right)$ with $\sigma()$ the sigmoïd function.

This in fact replaces $Q(c, w)=P(w \mid c)$ with $Q(c, w)=P(y=1 \mid w, c)$ the probability of genuine co-occurrence (i.e. simplifies a word-prediction task into a binaray classification task)...

...which then leads to the idea of learning $P\left(y=0 \mid w^{\prime}, c\right)$ as well (for some other words $w^{\prime}$ ).

To do this, word2vec draws $R$ negative random samples from the words distribution loss function then becomes:

$$
\sum_{w \in \text { corpus }}\left(\log \left(1+\exp \left(-m_{i} \cdot h(c)\right)\right)+\sum_{r=1}^{R} \log \left(1+\exp \left(+m_{j(r)} \cdot h(c)\right)\right)\right)
$$

(where $c$ is the context of $w, i$ is the index of $w$ in the lexicon (i.e. $\left.w=w^{(i)}\right)$ and $j(r)$ is drawn at random)

## GloVe (Pennington et al. 2014)

GloVe (Global Vectors) is another famous (non NN) "word" embedding method which works directly on the word co-occurrence matrix

- normalizing the co-occurrence counts,
- log-smoothing them,
- then factorizing the matrix to get lower dimensional representations by minimizing some "reconstruction loss" (difference between the dot-product of word embeddings and the log of the probability of co-occurrence)

GloVe embeddings work better on some data sets, while word2vec embeddings work better on others

## In practice

In practice, you can either:

- construct your own embeddings

CBoW: for corpus with short sentences but high number of samples

Skip-gram: for corpus with long sentences and low number of samples (infrequent words)

or GloVE, fastText, ELMo

$\checkmark$ use existing word embeddings word embeddings provide generally helpful features without the need for a lengthy training (for NN)

## From "words" to sentences/documents

word2vec: how to go from tokens to compound words, phrases, sentences, documents?

Compounds/Name Entities/Phrases: idioms like "hot potato" or named entities such as "Boston Globe" does not represent the combination of meanings of individual words.

One solution to this problem, as explored by Mikolov et al. (2013), is to identify such phrases based on word co-occurrence and train embeddings for them separately. More recent methods have explored directly learning $n$-gram embeddings from unlabeled data

How to represent a document: average/sum of its word vectors?

Solution: effective feature function that extracts higher-level features from constituting tokens-grams: CNN and RNN

Convolutional Neural Nets (CNN; Fukushima (1980), Le Cun (1998)) original key idea (inspired from visual cortex): share weights

Recurrent Neural Networks (Elman 1990): Designed to deal with sequences (of vectors) by composing former intermediate representations (= outputs), output is a function of input an previous output

$\vec{x}_{i}$ : "word" embedding for $i$-th word/token

$\vec{y}$ : output = probability distribution; e.g. $y_{j} \simeq$ $P\left(\right.$ Class $\left._{j} \mid w_{1} \ldots w_{i}\right)$ "Classif.": a MLP

$\mathrm{RNN}$ are generalized to

- bidirectional RNN
- RNN with gates:
- Long Short-Term Memory (LSTM; Hochreiter and Schmidhuber (1997))
- Gated recurrent unit (GRU; Cho et al. (2014))


## Limitations of classical RNNs:

- vanishing gradients: addressed with gate neuron/vector: learning to forget some parts of the memory
- exploding gradients: addressed by gradient clipping

Gate neuron: a $0 / 1$ selection (elementwise product) of input component input/memory information filter(= gate)

$$
\begin{aligned}
z_{t} & =\sigma\left(W_{z} \cdot\left[h_{t-1}, x_{t}\right]\right) \\
r_{t} & =\sigma\left(W_{r} \cdot\left[h_{t-1}, x_{t}\right]\right) \\
\tilde{h}_{t} & =\tanh \left(W \cdot\left[r_{t} * h_{t-1}, x_{t}\right]\right) \\
h_{t} & =\left(1-z_{t}\right) * h_{t-1}+z_{t} * \tilde{h}_{t}
\end{aligned}
$$

## Conclusion

Modern approach to NLP heavily emphasizes "Neural Networks" and "Deep Learning"

Two key ideas (which are, in fact, quite independant):

- "word embeddings":
- go from sparse (\& high-dimensional) to dense (\& less high-dimensional) representation of documents
- make use of (“deep") neural networks (= trainable non-linear functions)

Models:

- word embeddings: word2vec (CBoW, Skip-gram), GloVe, fastText, ELMo
- neural networks: CNN, LSTM, GPU

(software: spaCy, Keras, Torch/PyTorch, TensorFlow, scikit-learn, DarkNet)

## Pros and Cons

- Best performances, but lots of data (unsupervised for word embeddings, supervised for taks-oriented NN) and lot of CPU(/GPU)
- word embeddings are dependent on the applications in which it is used.

Labutov and Lipson ("word re-embedding", 2013) proposed task specific embeddings which retrain the word embeddings to align them in the current task space.

- Traditional word embedding algorithms assign a distinct vector to each word. This makes them unable to account for polysemy.

Several approaches address this issue :

e.g. Upadhyay et al. (2017), ELMo (E. P. Matthew et al. (2018))

- discussions on the relevance of word embeddings in the long run have cropped up recently

e.g. Lucy and Gauthier (2017) has recently tried to evaluate how well the word vectors capture the necessary facets of conceptual meaning. The authors have discovered severe limitations in perceptual understanding of the concepts behind the words, which cannot be inferred from distributional semantics alone.

