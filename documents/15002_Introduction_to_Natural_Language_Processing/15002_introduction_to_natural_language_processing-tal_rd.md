# Fundamentals in Information Retrieval 

## Information Retrieval

Definition : selection of documents relevant to a query in an unstructured collection of documents.

- unstructured: not produced with IR in mind, not a database.
- document: here, natural language text (but could also be video, audio or images)
- query: utterance in natural language (possibly augmented with commands, see later)


## Relevance? Content versus topic

**Semantic content:** what the document talks about (topic) vs what it says (content).

Example:

- Document 1: Note how misty the river banks are.
- Document 2 : She got misty by the river of bank notes falling on the table.
- Document 3: Money had never interested her.

Doc. 1 \& 2 have similar word content but are not topically related. Doc. 2 \& 3 have similar topics but opposite semantic content.

## How is IR done?

- have the computer represent documens (at the adequate level): preprocessing, indexing, ...
- represent the query, not necessarily the same way as documents (short queries, operators, $\ldots$ )
- define satisfying relevance measures between representations


## Simple example: Boolean model

- Documents are sets of terms (presence/absence)
- Queries are boolean expressions on terms

Steps:

- $V$, a finite vocabulary of indexing terms
- $R$ representation space
- $\mathscr{R}_{D}: V^{*} \rightarrow R$ representation function
- matching between query and documents

Example: Boolean representation of documents:

- Document 1: Come on, now, I hear you're feeling down. Well I can ease your pain Get you on your feet again.
- Document 2: There is no pain you are receding. A distant ship, smoke on the horizon.
$\rightarrow$ Doc1: feeling; ease; pain; feet
$\rightarrow$ Doc2: pain; ship; smoke; horizon
- Query: pain AND feeling
    - Doc1 matches
    - Doc2 does not match

Limitations :

- We might want to return Doc2 as a second best choice. The boolean model does not allow this.
- What happens with "pain OR feeling"? does not match common layman wisdom


## Indexing and represention of documents

- Representation: translating a document (words) into computable data (numbers).
- Indexing: selecting relevant elements (features) to support the representation


## Tokenisation

Tokenisation: splitting the text into words (Pre-requisite to choosing indexing terms)

## Word Entities

Semantic entity: compound word (group of words) bearing a semantic meaning

Example :

- "Information retrieval"
- "rendez-vous"
- "Singing Lily" (a type of pastry)
- "Dolphin striker" (a spar [part of boat])


## Choice of indexing terms

### Filtering

Automated choice of indexing terms using filters:

- on morpho-syntactic categories (e.g.: prepositions have no semantic content; nouns do)
- on stop-words
- on frequencies


### Stop words

Stop word: term explicitely to be excluded from indexing.

Example : the; a; 's; in; but; I; we; my; your; their; then

$\rightarrow$ Benefits:

- more informative indexes
- cheap way to remove classes of words without semantic content
- smaller indexes (tractability)


### Choice of indexing terms: frequencies

Zipf and Luhn : If $r$ is the rank of a term and $n$ is its number of occurences (frequency) in the collection:

- Zipf (1949): $n \sim 1 / r$
- Luhn (1958): mid-rank terms are the best indicators of topics


## Stemming and lemmatisation

Stem: morphological root of a word.
Stemming: Process of reducing words to their stem.

Example :
- prepaid,paid \longrightarrow paid
- interesting, uninteresting \longrightarrow interest

Benefits :

- Reduces lexical variability $\Rightarrow$ reduces index size increases information value of each indexing term.

Non-trivial process :

$$
\begin{gathered}
\text { factual } \longrightarrow \text { fact } \\
\text { equal } \longrightarrow \text { eq }
\end{gathered} \quad \text { wrong ("eq" is too short) }
$$

## Desequentialisation: bag of words model

Assumption : Positions of the terms are ignored. Term distribution is indicative enough of the meaning.

Model : A document is a multiset of terms

$$
\begin{aligned}
& d_{1}=\left\{\left(t_{1}, n\left(d_{1}, t_{1}\right)\right) ;\left(t_{2}, n\left(d_{1}, t_{2}\right)\right) ; \ldots\right\} \\
& d_{2}=\left\{\left(t_{1}, n\left(d_{2}, t_{1}\right)\right) ;\left(t_{2}, n\left(d_{2}, t_{2}\right)\right) ; \ldots\right\}
\end{aligned}
$$

Example: Now so long, Marianne ; it's time that we began to laugh and cry and cry; and laugh about it all again.
->([begin,1] [cry,2] [laugh,2] [long,1][Marianne,1] [time, 1])

## Conclusions on indexing

- Bad indexing can ruin the performances of an otherwise sophisticated IR system
- Good indexing is anything but trivial


## Vector Space model

Objective : Overcome the limitations of the Boolean model by representing documents with vector describing term distributions.

Principle :

- $V$, a finite vocabulary of indexing terms
- $R$ representation space
- $\mathscr{R}_{D}: V^{*} \rightarrow R$ representation function
- similarity: $\mathscr{M}_{\text {prox }}: R \times R \rightarrow \mathbb{R}^{+}$

Note: choose similarity measure well behaved for the representation (depends on the representation)

## Characterisation

characterisation: projection of the document into the representation space

## Weightings

Term Frequency: $\mathrm{tf}\left(w_{i}, d_{j}\right)=\mathrm{nb}$ of occurences of term $w_{i}$ in document $d_{j}$
Sometimes $1+\log \left(\mathrm{tf}\left(w_{i}, d_{j}\right)\right)$ is used in place of $\operatorname{tf}\left(w_{i}, d_{j}\right)$

Term Frequency - Inverse Document Frequency :

$$
\operatorname{tf}-\operatorname{idf}\left(w_{i}, d_{j}\right)=\operatorname{tf}\left(w_{i}, d_{j}\right) \cdot \operatorname{idf}\left(w_{i}\right)
$$

with

$$
\operatorname{idf}\left(w_{i}\right)=\log \left(\frac{|D|}{n b\left(d_{k} \supset w_{i}\right)}\right)
$$

$|D|:$ number of documents $n b\left(d_{k} \supset w_{i}\right)$ : number of documents which contain term $w_{i}$

Example

- Now so long, Marianne it's time that we began to laugh and cry and cry and laugh about it all again.
- $\mathscr{R}_{D}: V^{*} \rightarrow R$ representation function = term Frequency
$\longrightarrow$ ([aardvark, 0] [begin,1] [cry,2]
[information, 0] [laugh, 2] [long, 1] ..... [Marianne, 1]
[retrieval,0] [time,1])
$\longrightarrow$(012021101 ···)


## Vector space model

- indexing terms define axis
- documents are point in the vector space (representing directions)


### Proximity measure between documents

Cosine similarity:

$$
\cos \left(\mathbf{d}_{1}, \mathbf{d}_{2}\right)=\frac{\mathbf{d}_{1}}{\left\|\mathbf{d}_{1}\right\|} \cdot \frac{\mathbf{d}_{2}}{\left\|\mathbf{d}_{2}\right\|}=\frac{\sum_{j=1}^{N} d_{1 j} d_{2 j}}{\sqrt{\left[\sum_{j} d_{1 j}^{2}\right]\left[\sum_{j} d_{2 j}^{2}\right]}}
$$

$\rightarrow$ bounded $\left(0<\cos \left(\mathbf{d}_{\mathbf{1}}, \mathbf{d}_{\mathbf{2}}\right)<1, \forall \mathbf{d}_{\mathbf{1}}, \mathbf{d}_{\mathbf{2}}\right)$

- it is a similarity: the greater, the more similar the documents (as opposed to a metric)
- independent on the length of the document

Example:

- Document 1 : Now so long, Marianne, it's time that we began to laugh and cry and cry and laugh about it all again.
    - ..., [long,1] [Marianne,1] [time,1] [begin,1] [laugh,2] [cry, 2], ...
    - $d_{1}=(\ldots, 1,1,1,1,2,2, \ldots)$
- Document 2 : I haven't seen Marianne laugthing for some time, is she crying all day long
    - ..., [long,1] [Marianne, 1] [time,1] [begin,0] [laugh,1] [cry, 1], ...
    - $d_{2}=(\ldots, 1,1,1,0,1,1, \ldots)$
- Cosine similarity :

$$
\cos \left(\mathbf{d}_{1}, \mathbf{d}_{2}\right)=7 /(\sqrt{12} \cdot \sqrt{5})=0.904
$$

## Queries

Definition : Queries (or "topics") are "questions" asked to the system. Typically keywords, possibly augmented with operators

- Supposed unknown at indexing time (difference between IR and classification or clustering)
- Query representation is not necessarly trivial (not always the same as representation of documents).


## Problem of short queries

On the web,

- the average query length is under three words
- very few users use operators

Language being ambiguous, three-word queries are difficult to satisfy.

Solutions :

- query expansion: use knowledge about the query terms to associate them with other terms and improve the query.
- query term reweighting: weight the terms of the query as to obtain maximum retrieval performance.
- relevance feedback: User provides the system an evaluation of the relevance of its answers.


## Performances of IR systems

Precision is the proportion of the documents retrieved by the system that are relevant (according to the referential)

Recall is the proportion of the relevant documents which were retrieved by the system

- Precision can be cheated by returning no document
- Recall can be cheated by returning all documents

Given an IR system, a document collection and a referential; for a query $q$, the results returned by the system is evaluated with:

- Precision: $\operatorname{Pr}(q)=\frac{|R(q) \cap S(q)|}{|S(q)|}$
- Recall: $\operatorname{Rec}(q)=\frac{|R(q) \cap S(q)|}{|R(q)|}$

Precision at $n$ document:

$$
\operatorname{Pr}_{n}(q)=\frac{\left|R(q) \cap S_{n}(q)\right|}{\left|S_{n}(q)\right|}
$$

with $S_{n}(q)=n$ first documents to be retrieved

## R-Precision

precision obtained after retrieving as many documents as there are relevant documents, averaged over queries

$$
\text { R-Precision }=\frac{1}{N} \sum_{i=1}^{N} \operatorname{Pr}_{\left|R\left(q_{i}\right)\right|}\left(q_{i}\right)
$$

## Average Precision

Average of the precisions whenever all relevant documents below rank $\mathrm{rk}(d, q)$ are retrieved:

$$
\operatorname{Avg}(q)=\frac{1}{|R(q)|} \sum_{d \in R(q)} \operatorname{Pr}_{\mathrm{rk}(d, q)}(q)
$$

## Mean Average Precision

Mean over the queries of the Average Precisions

$$
\frac{1}{N} \sum_{i} \operatorname{Avg} \mathrm{P}\left(q_{i}\right)
$$

MAP measures the tendency of the system to retrieve relevant documents first.

## Probabilistic models

Idea : The best possible ranking returns documents sorted by probability to be relevent given a query.

## Sparck-Jones' model

- Estimate the probability that a given document $d_{i}$ is relevant $\left(d_{i} \in R(q)\right)$ to given query $q: P\left(d_{i} \in R(q) \mid d_{i}, q\right)$
- Invert the probability (here $R$ is a boolean variable, standing for $\left.d_{i} \in R(q)\right): P\left(d_{i} \mid R, q\right)$
- Write $P\left(d_{i} \mid R, q\right)$ as a function of the probabilities of occurence of the terms (assuming that terms are conditionally independant): $P\left(t_{i} \in d \mid R, q\right)$
- Document $d$ contains term $t_{i}$ (of the query)

$$
w\left(t_{i}, d\right)=\log \frac{p\left(t_{i} \in d \mid d \in R\right)}{p\left(t_{i} \in d \mid d \notin R\right)}
$$

- Document $d$ does not contain term $t_{i}$ (of the query)

$$
w\left(t_{i}, d\right)=\log \frac{p\left(t_{i} \notin d \mid d \in R\right)}{p\left(t_{i} \notin d \mid d \notin R\right)}=\log \frac{1-p\left(t_{i} \in d \mid d \in R\right)}{1-p\left(t_{i} \in d \mid d \notin R\right)}
$$

- Combining the two

$$
\begin{gathered}
w\left(t_{i}, d\right)=\log \frac{p\left(t_{i} \in d \mid d \in R\right)}{p\left(t_{i} \in d \mid d \notin R\right)}-\log \frac{\left.p\left(t_{i} \notin d \mid d \in R\right)\right]}{p\left(t_{i} \notin d \mid d \notin R\right)} \\
=\log \frac{p\left(t_{i} \in d \mid d \in R\right)\left[1-p\left(t_{i} \in d \mid d \notin R\right)\right]}{p\left(t_{i} \in d \mid d \notin R\right)\left[1-p\left(t_{i} \in d \mid d \in R\right)\right]}
\end{gathered}
$$

## Okapi BM25

Idea: Refine Sparck-Jones' model by including term frequencies

$$
w=\log \frac{p(\operatorname{freq}(t, d)=\operatorname{tf} \mid d \in R) p(t \notin d \mid d \notin R)}{p(\operatorname{freq}(t, d)=\operatorname{tf} \mid d \notin R) p(t \notin d \mid d \in R)}
$$

## BM25 weight for term $i$

$$
w_{i}^{\mathrm{BM} 25}=\frac{\mathrm{tf}_{i}\left(k_{1}+1\right)}{k_{1}\left((1-b)+b \frac{d l}{\text { avdl }}\right)+\mathrm{tf}_{i}} \cdot \mathrm{df}_{i}
$$

with $d l=$ document length avfl $=$ average document length

BM25 is a very good model and used as reference for comparison with new models

## Topic-based models

Idea : Apply a transformation to the representation space as to emphasise the most relevant features: index senses rather than mere words

## Latent Semantic Indexing

Idea: Reduction of dimensionality of the original representation space. Create a matrix close to the occurence matrix but of smaller rank

Reduction of dimensionality

- approximation of the occurence matrix
- filtering of the occurence matrix

Drawbacks :

- Out-performed by other models
- Too expensive to compute on large bases (requires iterative methods)
- Meaning of axis ??
- Query projection is problematic


## Distributional Semantics Information Retrieval

Idea : There is a high degree of correlation between the observable distributional caracteristics of a term and its meaning:

## Co-occurence profile

Definition: caracterisation of a word by its co-occurences with indexing terms

Example:

- Document 1 : Now so long, Marianne, it's time that we began to laugh and cry and cry and laugh about it all again.
- Document 2 : it seems so long ago, Nancy was alone looking at the Late Late show through a semi-precious stone.

$\rightarrow$ Co-occurence profile of long $=([$ cry, 2$]$ [begin, 1] [Marianne, 1] [Nancy,1] [time,1] [late,2] [laugh,2])

## Co-occurence matrix

Definition: words $\times$ terms matrix of the co-occurence profiles with terms

$f_{i j}$ : number of times that the word $w_{i}$ and the indexing term $t_{j}$ occur together.

## DSIR Document representation

$$
F_{D}=F_{\text {occurence }} \cdot F_{\text {co-occurence }}
$$

$\rightarrow$ ponderation of the words in documents by the co-occurences

