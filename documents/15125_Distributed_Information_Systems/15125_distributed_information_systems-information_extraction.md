# Part 3: Knowledge Modeling <br> - Information Extraction 

## Populating Knowledge Bases

Manual creation of knowledge bases is expensive

Can we produce such knowledge automatically?

Idea: Extract knowledge from documents

Challenge: Knowledge is encoded in natural language

Objectives

- Automated or accelerated creation of knowledge bases
- Support for structured search on documents

Traditionally knowledge bases are created manually, either by experts (e.g., WordNet) or by crowd-sourcing (e.g., WikiData). This is expensive. In the case of WordNet, it took tens of years to construct the knowledge base, in the case of WikiData (resp. WikiPedia) we all know about the notorious difficulty to finance this endeavor. So an interesting problem is whether such knowledge bases could not be automatically constructed.

For automatic construction we can exploit all information that is digitally available, e.g., all documents accessible on the Web. These documents encode massive human knowledge in natural language. So the problem is to extract such knowledge by analyzing natural language text, which is not an easy problem.

The results would, however, be immensely useful. First, we could create massive knowledge bases in a nearly automated way, and furthermore these knowledge bases could be used to annotate documents, in particular the documents from which the
knowledge has been extracted, for supporting more expressive and precise searches and analysis.

## Knowledge Extraction

For extracting knowledge from textual content, we can consider the different constituents of a knowledge graph separately: entities, attributes and relationships.

## Basic Questions in Knowledge Extraction

For each of the three questions of generating the basic entities for a knowledge graph there exist specific problems that have been investigated.

Keyphrase extraction concerns the extraction of typical phrases in a document that could identify basic concepts.

Named entity extaction concerns the extaction and typing of text that represents names of real-world entities.

Information extraction concerns the automated extraction of relationships from text.

Taxonomy induction concerns the automated extraction of a specific relationship, namely generalization, from text.

## Knowledge Inference

From knowledge to more complete and precise knowledge

Once knowledge graphs have been extracted from text they can be further processed. This enables the inference of new knowledge from the existing knowledge, but as well the correction, completion and integration of existing knowledge bases.

Knowledge inference concerns a wide number of problems that have been studied in many different contexts. Some of the basic examples are:

Entity linking and disambiguation, which concerns the problem of identifying which entity names represent the same real-world entity, respective which entity is referred to in case of ambiguous entity names.

Schema integration, which concerns the problem which classes, attributes and relationships in one knowledge bases correspond to which in another one.

Collective classification, which concerns the problem of learning unknown attribute values from the available knowledge in a knowledge base.

Link prediction, which concerns the problem of learning unknown relationships from the available knowledge in a knowledge base.

## Knowledge Extraction

1. Keyphrase extraction
2. Named entity recognition
3. Information extraction
4. Taxonomy Induction

## 1. KEYPHRASE EXTRACTION

Idea: key phrase extraction concerns "the automatic selection of important and topical phrases from the body of a document" (Turney, 2000)

A first type of information extraction method is key phrase extraction. Key phrase extraction aims at identifying words and phrases (phrase $=$ sequence of words) that are particularly typical for the document and characterize important concepts that occur in the document. Key phrase extraction has been developed to support document summarization, where the key phrase give an overview of the key concepts of a document, and document search and indexing, where a distinctive vocabulary is being used in document searches. Moreover, key phrases can also provide useful features for document classification, i.e. they key phrase extraction can be considered as a feature selection method, and they support opinion mining, identifying distinctive expressions related to opinions. In the example text we see the possible outcome of key phrase extraction, with all key phrases identifies marked in bold.

## Keyphrase Extraction Methods

Approach: generate candidate phrases and rank them

Candidate phrases

- Remove stopwords
- Use word n-grams
- Consider part-of-speech tags (POS)

Baseline ranking approach

- rank candidate phrases of the document according to their tf-idf value

Advanced approaches

- Use of many structural, syntactic features of the documents
- Use of external resources, such as Wikipedia, Wordnet

The basic approach to key phrase extraction is based on principles well known from information retrieval. A first decision is what should be possible key phrases. As in IR stopwords are excluded and key phrase candidates could be all n-grams from the remaining text (where $n$ is typically in the range of 2 to 5 ). Furthermore part-of-speech tags could be used to further select the candidates, e.g., for excluding all verb phrases.

In order to assess whether a candidate phrase is characteristic for a document, basic tf-idf ranking is a possible approach. As in IR a candidate phrase is considered as relevant for the document if it is at the same time frequent and distinctive. Apart from that, many heuristics have been developed to refine this approach, taking into account additional features of the document. For example, a phrase in the title or a header could be considered as more relevant. Or, external knowledge bases could be used to check whether a phrase corresponds to a commonly known concept.

## Use of Keyphrase Extraction

Key phrase extraction can be used as an initial step to create a domain-specific thesaurus or taxonomy. In the example, we see a thesaurus that has been constructed for the food domain, based on a key phrase extraction. For the phrase "junk food" a large number of synonyms and near-synonyms have been identified. In practice a human expert would not be able to extract reliably all different types of mentions of such a concept.

As a result, this allows, among others, to retrieve documents that refer to this concept with higher recall, than would be possible with a simple keyword search just using the phrases "junk food", and possibly some alternative phrases found in an ad-hoc way.

## 2. NAMED ENTITY RECOGNITION

## Named Entity Recognition (NER)

Task: Find and classify names of people, organizations, places, brands etc. that are mentioned in documents

Named entity recognition is a more specific task than key phrase extraction. In NER the objective is to identify phrases that are names of specific types of entities, such as people, organizations or places. This, again, is very useful for document classification and search, but also a stepping stone to extract more complex pieces of knowledge, in particular statements, as we will see later.

- Named entities can be indexed, linked, etc.
- Sentiment can be attributed to companies or products
- Information extraction can use named entities as anchors

NER has in particular many commercial applications, e.g., for marketing or studying public perception, by linking volume of communication, sentiment and popularity to specific entities, such as products, companies or organizations. Thus, there exist a number of commercial tools that offer this type of service.

## NER as Sequence Labelling Task

Sequence of tags, indicating whether a word is inside (I) or outside of an entity ( 0 )

The occurrences of entities (can be) typed

EPFL is located in Lausanne in Switzerland, next to Lake Geneva

| I | 0 | 0 | 0 | I | 0 | I | 0 | 0 | 0 | I | I |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ORG |  |  |  | GEO |  | GEO |  |  | GEO | GEO |  |

A classification problem!

The basic task of NER is to detect whether a word belongs to an entity name or not. Furthermore, when a entity name is detected it can be classified according to the type of the entity, e.g. an organisation (ORG), a location (GEO), a person etc.

When analyzing a text entity, NER is thus a classification problem, where for each word it needs to be decided whether it is inside or outside of an entity name. More detailed classifications, in particular whether a word is the beginning or end of entity name, could also be done. Note that in this context also punctuation marks are considered as words, as they may carry important information on the presence of an entity.

Given that NER can be understood as a classification problem, we have to answer two questions, namely which are the input features for the classifier and which is the classification algorithm to be used. As for the input features, typically the neighborhood of a word is considered. In this neighborhood we find other words, which can be used as directly as features and from which a number of derived features can be produced. One additional type of feature that is specifically used in NER is the labels that have been produced by the classifier for the words preceding the word to be classified. Thus, the classifier classifies words while reading the words in the sequence they appear in the document. Thus, even though in principle any classifier could be applied, e.g. Naïve Bayes, which is used frequently in practice, specific sequence-oriented classifiers (HMM, MEMM, CRF) can have better performance.

## Features used in NER

- Word and neighboring words: Lausanne, in
- Part-of-speech tags (POS): $\quad$ POS(Lausanne) $=$ NN
- Prefixes and Suffixes: $\quad$ prefix(Lausanne, 3) $=$ Lau
- Word shape: $\quad$ WS(Lausanne) $=X x x x x x x x$
- Short wordshape: $\quad$ SWS(Lausanne) $=X x$

Here we see a list of typical features that are used in named entity recognition. Some of them are quite specific to the task. For example, part-of-speech tags can be helpful as they allows to distinguish noun phrases (NN) which are typical for entities. Pre- and suffixes are another interesting feature. For example, words ending in "land" would often be locations, thus learning this could help to generalize the classification to new terms that would contain such a suffix. For entities (in particular in English) also the word shape is a important features, as usually names start in capital letters, or acronyms consist of capital letters only.

## Exploiting Context

When deciding the entity type exclusively on local context, important information may be missed

- The release of Harry Potter and the Philosopher's Stone in 2001 was Watson's
- Although the system is primarily an IBM effort, Watson's

Idea: consider a model that takes into the account the sequential structure of language and exploits sentence context

## Generative Probabilistic Model

Sequence of words (known): $W=\left(w_{1}, w_{2}, w_{3}, \ldots, w_{n}\right)$

Sequence of states (unknown): $E=\left(e_{1}, e_{2}, e_{3}, \ldots, e_{n}\right)$

Assume the text is produced by a probabilistic process:

$P(E, W)$

Find the most probable model

$$
\underset{E}{\operatorname{argmax}} P(E \mid W)
$$

Bayes Law

$$
\underset{E}{\operatorname{argmax}} P(E \mid W)=\underset{E}{\operatorname{argmax}} P(E) P(W \mid E)
$$

We now will see a classifier that specifically takes advantage of the sequential nature of learning entities in natural language text. The approach is strongly related to probabilistic information retrieval and based on a generative probabilistic model for text.

The basic model assumes that there exists a (unknown) probability distribution $P(E, W)$ that connects sequences of words with the corresponding sequences of labels. The task of classification is then to identify for a given sequence of words, the most probable sequence of labels given the sequence of words. Using Bayes law we can reformulate this, by decomposing the conditional probability $P(E \mid W)$ into the product of two probability distributions. $\mathrm{P}(\mathrm{E})$ is a model of how the different labels interact with each other, and $\mathrm{P}(\mathrm{W} \mid \mathrm{E})$ is a model of how words interact with labels.

## Approximation

Label transition probabilities (bigram model)

$$
P(E)=P\left(e_{1}, \ldots, e_{n}\right) \approx \prod_{i=2, \ldots, n} P_{E}\left(e_{i} \mid e_{i-1}\right)
$$

Word emission probabilities

$$
P(W \mid E) \approx \prod_{i=1, \ldots, n} P_{W}\left(w_{i} \mid e_{i}\right)
$$

As we will not be able to estimate the complete probability distribution functions, we approximate them by making (sever) independence assumptions. We assume that the probability of a label to occur, depends only on the previous label. This corresponds to a bigram model (generalizing the unigram model we have assumed in probabilistic information retrieval). For words we assume that their probability depends only on the label that it received. Thus the two probability functions decompose into products of much simpler functions that we can estimate.

## Hidden Markov Model (HMM)

Assume the text is produced by a probabilistic process (with unknown transition probabilities)

We can represent approximate model of the probability distribution graphically as a Markov Model, where we indicate which probabilistic variables depend on which others. More precisely, we have here the case of a hidden Markov model since the labels $E$ are unknown and their probabilities need to be estimated from the known words.

The approach for HMM can be applied to any sequence labelling task. In particular it can be used to learn part-of-speech tags and the types of the entities.

## Learning the Model

$$
\begin{aligned}
& \text { Maximum Likelihood Estimation, e.g., } \\
& \qquad \mathrm{P}_{\mathrm{E}}(\mathrm{I} \mid \mathrm{O})=2 / 4, \mathrm{P}_{\mathrm{W}}(\text { in } \mid \mathrm{O})=2 / 5
\end{aligned}
$$

Requires only counting

Smoothing: Unseen words might only accidentally miss in the training set:

$$
P_{W S}\left(w_{i} \mid e_{i}\right)=\lambda P_{W}\left(w_{i} \mid e_{i}\right)+(1-\lambda) \frac{1}{n}
$$

For labels no smoothing is needed, as all labels occur in the training set

For estimating the basic probabilities $P_{E}\left(e_{i} \mid e_{i-1}\right)$ and $P_{W}\left(w_{i} \mid e_{i}\right)$ we use maximum likelihood estimation as in probabilistic information retrieval. For example, for estimating a probability $P_{E}\left(e_{i} \mid O\right)$ we count the total number of occurrences of $\mathrm{O}$, and then compute the ratio between the cases where the preceding label was I respectively $\mathrm{O}$ with the total number of occurrences.

As in probabilistic information retrieval we have the issue of sparsity of words in the training set. As a result it might occur that for a specific label no words appear as examples in the training data, whereas it is not excluded that such a word might be related to the label in general. With smoothing this is taken into account, where the smoothing parameter depends on the length of the word sequence.

For the labels no smoothing is required, as the number of labels is very small (in the case of untyped entity recognition it is 2 ) and thus all label combinations are extremely likely to occur.

## Using the Model

For a given sequence of words $W$ find the most probable model for the labels $E$

$$
\underset{E}{\operatorname{argmax}} P(E \mid W)
$$

Brute force search: compute for all possible sequences $\mathrm{E}=\left(\mathrm{e}_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}, \ldots, \mathrm{e}_{\mathrm{n}}\right)$ the probability $P(E \mid W)$ and then take the maximum

Complexity $\mathrm{O}\left(2^{\mathrm{n}}\right) \rightarrow$ unfeasible for longer sequences

For using the HMM Model the problem is of simply finding the sequence of labels that is the most probably one produced by the HMM for a giving sequence of words. In principle, this can be performed by brute-force search, but which does not scale for longer text due to a combinatorial growth in cost.

## Observation

$$
\begin{aligned}
& \underset{E}{\operatorname{argmax}} P(E \mid W) \\
& =\underset{E}{\operatorname{argmax}} \prod_{i=2, \ldots, n} P_{E}\left(e_{i} \mid e_{i-1}\right) \prod_{i=1, \ldots, n} P_{W}\left(w_{i} \mid e_{i}\right) \\
& =\underset{E}{\operatorname{argmax}} P_{E}\left(e_{n} \mid e_{n-1}\right) P_{W}\left(w_{n} \mid e_{n}\right) \\
& \underset{E}{\operatorname{argmax}} \prod_{i=2, \ldots, n-1} P_{E}\left(e_{i} \mid e_{i-1}\right) \prod_{i=1, \ldots, n-1} P_{W}\left(w_{i} \mid e_{i}\right) \\
& \quad \text { Independent of the choice of } e_{n}
\end{aligned}
$$

A simple observation is that the choice of the last label in a sequence that produces the largest probability can be made independently of the choices of the preceding labels that produce a maximal probability. Based on this observations the computation of the sequence with the maximal probability can be dramatically simplified.

## Viterbi Algorithm

Let $\pi(k, v)$ be the maximum probability a sequence of length $k$ can achieve with last label $v$

Then

$$
\begin{gathered}
\pi(k, v)=\max _{u} \pi(k-1, u) P_{E}\left(e_{k} \mid u\right) P_{W}\left(w_{k} \mid v\right) \\
\pi(0, *)=1
\end{gathered}
$$

This is a dynamic programming algorithm $\rightarrow$ Viterbi algorithm

It is just necessary to keep the information which is the sequence that produces the maximum value up to the last label, and then compute the label that maximizes this probability in the last step. In the case where the HMM model considers only the value of the previous label for predicting the next label this results in the aboce algorithm. In its generalized form, where labels can depend on multiple other labels (resp. random variables) the algorithm becomes a dynamic programming algorithm and it is called the Viterbi algorithm according to its inventor.

## 3. INFORMATION EXTRACTION

## Information Extraction (IE)

Task: Extract statements from text $\rightarrow$ creation of knowledge graphs

Taking the analysis of documents one step further, we now consider the extraction of statements from natural language text, as is illustrated in the example. Statements connect entities through relationships, for example, the first statement expresses that EPFL is part of a larger organization, the Swiss Federal Institutes of Technology. Thus the notion of statements we use here corresponds exactly to the notion of statements we introduced earlier with RDF.

## Typed Statements

$$
\begin{aligned}
& \text { EPFL - PART-OF - Swiss Federal Institute of Technology } \\
& \text { Type: ORG - PART-OF - ORG } \\
& \text { EPFL - RELATED-TO - ETHZ } \\
& \text { Type: ORG - RELATED-TO - ORG } \\
& \text { EPF Domain - PART-OF - FDEA } \\
& \text { Type: ORG - PART-OF - ORG } \\
& \text { EPFL - LOCATED-IN - Lausanne } \\
& \text { Type: ORG - LOCATED-IN - LOC } \\
& \text { EPFL - LOCATED-IN - Alps ? Lake Geneva - LOCATED-IN - Alps? } \\
& \text { Type: ORG - LOCATED-IN - LOC } \\
& \text { Type: LOC - LOCATED-IN - LOC }
\end{aligned}
$$

We can from the individual statements generalize to the statements with the type of entities, resulting in statement types. This implies that we may assume the existence of a schema for statements (in RDF an RDF schema) that specifies which types of entities can be connected by which types of relationships. Not every type of entity can be related in a meaningful way to another type of entity. For example, it would not make sense to have a statement expressing that a location is part of a person. Having these additional constraints, will be helpful to more precisely detect statements.

## Approaches to Information Extraction

1. Hand-written patterns
2. Supervised machine learning
3. Bootstrapping
4. Distant supervision
5. Matrix Factorization

## 1. Hand-Written Patterns

Advantages

- Rules tend to be high-precision
- Can be tailored to specific domains

Disadvantages

- Human patterns are often low-recall
- A lot of effort to think of all possible patterns

Hand-written patterns is in general a very reliable method for statement extraction. However, it suffers from low recall and it is very difficult to conceive all possible patterns by a human (expert). Therefore more automated methods are of interest, that we will discuss in the following.

## 2. Supervised Learning for IE

Approach: train a classifier on labeled data

Creating a training set

- Choose relevant named entities and their relations
- Hand-label relations among entities (positive examples)

The supervised learning approach for information extraction requires first a training set. Producing such a training set is labor-intensive and a major task. For example, for the domain of life sciences efforts have been undertaken. In the example shown, more than 2000 sentences have been manually annotated.

## Classifiers for Information Extraction

- A filtering classifier, to detect whether a relation exists among the entities
- A relation-specific classifier detecting the relation label

Training the classifiers

- Extract named entities in the document corpus using NER
- Detect pairs of entities, e.g., in the same sentence
- Use unlabeled entity pairs as negative examples

Once a manually annotated document collection is available, classifiers for information extraction can be trained. One approach is to train two types of classifiers, one that simply detects whether a relationship exists among two entities, and a second that detects the type of the relationship. The use of a filtering classifier can speed up the classification task and allows the use of distinct feature-sets for the two tasks.

For training the classifiers, one first extracts all entity pairs using NER that occur in the same context, for example, in the same sentence. If the pairs are not annotated they are taken as negative examples. Then the classifier is being trained using features extract from the context of the occurrences of the entities.

## Syntactic Features

The syntactic features, or part-of-speech tags can be exploited in various ways. In the simplest case only the sequence of POS tags in between the mentions is used. More complex features can be constructed as well, e.g. the navigation path between the mentions in the parse tree.

## 3. Bootstrapping

No training data, but a few high-precision patterns

## Approach:

- Find entity pairs that match the pattern
- Find sentences containing those entity pairs
- Generalize the entities in those sentences
- Generate new patterns

One of the big problems with supervised approaches to information extraction is the scarcity of training data. One way to approach this problem is called bootstrapping. The basic idea is that one may have a few high-precision patterns, such as the Hearst patterns, or simple a set of example statements that are manually extracted, and one tries to generalize these patterns by analyzing a large document corpus.

The approach is to first find entity pairs using the high precision patterns. Then using those entity pairs sentences containing the same entity pairs are searched. The assumption is that with large likelihood these sentences express the same type of relationship, just in a different syntactic representation. Thus such sentences can be considered as templates for expressing the relationship. By generalizing the occurrences of the entities in such a sentence, now patterns for identifying the relationship are produced.

## Example

Pattern: LOC is located in LOC

- Mumbai is located in India
- Adelaide is located in Southern Australia
- Sriharikota is located in Nellore

Search for entity pairs (Mumbai, India)

- Mumbai is India's top destination
- Mumbai hotels, India

New patterns

- LOC is LOC's top destination
- LOC hotels, LOC

This example illustrates the approach. We start with a simple, but precise pattern, LOC is located in LOC, with which we find occurrences of entity pairs. Then we search for those entity pairs, and find other sentences mentioning them. These are then generalized to patterns by replacing the entity occurrences by their types.

## Confidence

Assume we have a confirmed set of pairs of mentions $M$

- A new pattern should also match many of those

Hits $_{p}=$ number of pairs in $\mathrm{M}$ that a new pattern matches Find $_{p}=$ total number of pairs that a new pattern matches

Confidence that a new patterns finds many relevant mentions

$$
\operatorname{Conf}(p)=\frac{\text { Hits }_{p}}{\text { Finds }_{p}} \log \left(\text { Finds }_{p}\right)
$$

In order to contain the problem of inferring too many "wrong" patterns, a confidence metric can be used. With this metrics the confidence in a new template increases, whenever it retrieves more entity pairs that are already confirmed to be correct. However, this is balanced by measuring of how many entity pairs the new template matches in total. If in proportion it matches too many pairs, without creating confirmed entity pairs, the confidence in the template is lowered.

## 4. No Training Data? Distant Supervision

Idea: use existing knowledge bases to collect training data from which a classifier can be trained

- Combines advantages of bootstrapping with supervised learning

Example: learning PLACE-OF-BIRTH

Another idea to deal with the problem of lacking training data is based on the observation that large databases of known statements (also called facts) do exist. One example is WikiData. Thus, instead of producing confirmed statements from a training corpus by using high precision patterns, such statements are drawn from an existing knowledge base. In this way, large document collections can be searched for sentences that potentially express those facts, and these sentences can be used to train a classifier for information extraction.

## Distant Supervision: Approach

Here we illustrate the process of the distant supervision method. First, we start by running NER over a large document collection, such as WikiPedia. This produces a set of sentences s that contain entity pairs (e1,e2). Having those entity pairs, next we check in the existing knowledge base, in this example WikiData, whether relations among the entity pairs exist. For those entity pairs, for which a relation is confirmed in the knowledge base, we have identified an instance for the training data, and we extract all typical features used for information extraction from the sentence in which the entity pair has been found. This produces a training set for training a classifier to predict the relation. Finally this classifier can be used to predict relations for unseen documents, by extracting occurrences of entity pairs and feeding the classifier with the features of the sentence in which they are contained.

## Features for Distant Supervision

Use conjunctions of standard IE features as sentence features

- Match only if all individual features match
- High precision, but low recall features!
- Feasible, since training set is large

Complex features resemble to templates used in rulebased approaches

In distant supervision the features are constructed in a different way than in standard information extraction using supervised learning, due to the fact that the number of training examples is in generally much higher. Instead of producing a feature vector from combining all individual features, each feature combination is considered as a separate feature, which results in a much larger feature space. As a result, those more complex features are much more precise, but have low recall. This is, however, compensated by the fact that the training set is much larger.

## Example

Complex Features for "EPFL is located in Lausanne in Switzerland":

FO: M1=ORG and M2=LOC and betweenwords=\{is, located, in $\}$ and afterwords=\{\} and betweenPOS $=\{V P, V P, P P\}$

F1: M1=ORG and M2=LOC and betweenwords=\{is, located, in\} and afterwords=\{in\} and betweenPOS $=\{\mathrm{VP}, \mathrm{VP}, \mathrm{PP}\}$

$\rightarrow$ F0 matches "ETHZ is located in Zürich, Switzerland", F1 not

Individual features:

F1: M1=ORG, F2: M2=LOC, F3: betweenwords=\{is, located, in \}, F4: afterwords $0=\{\}$,

F5: afterwords1=\{in\}, F6: betweenPOS = \{VP, VP, PP $\}$

$\rightarrow$ only F5 is different

The example illustrates this point. We construct two complex features by computing the conjunction of several simple features, once considering a window of size 0 around the phrase containing the entities (resulting in feature F0) and once considering a window of size 1 around the phrase containing the entities (resulting in feature F1). As a result, the complex feature F1 does not match at all the sentence "ETHZ is located in Zürich, Switzerland".

If used a feature vector derived from the individual features, the two feature vectors derived for the two documents would be very similar for these feature set, since most of the features are identical. Only feature F5 would be different.

## 5. Matrix Factorization

Linking entity pairs from text to knowledge bases (as in distant supervision)

Create a matrix with

- Entity pairs as rows
- Relation types as columns

Distant supervision aims at generating classifiers for relations that are based on syntactic features. With the same information used for distant supervision we could also try to understand the intrinsic nature of relationships by mapping them to a lowdimensional representation, as we did earlier for words with word embeddings. This is the idea underlying to apply matrix factorization ot the entity-pairs / relation matrix.

## Relation Extraction with Matrix Factorization

Use matrix factorization to

- Link text patterns to relation types and identify similar text patterns
- Extract relations from text

The entity-pair/relation matrix is a sparse matrix (like in recommender systems)

By using matrix factorization the hope is to align similar text patterns and corresponding relationships in a latent space. This can help both in identifying text patterns that correspond to relationships and to extract those relationships from text.

The entity-pair/relation matrix is a sparse matrix is a sparse matrix. Thus situation is comparable to the one we had in recommender systems. Algebraix factorization methods would not work. On the other hand using matrix factorization based on SGD might help to "guess" new relationships (as in recommender systems it helps to guess unseen ratings). This idea we will alter exploit also for the problem of link prediction.

## Learning the Matrix Factorization

$R(i, j)$ positive examples of facts

$R^{\prime}(x, y)$ negative examples of facts

The matrix factorization will represent both entity pairs and relations as low-dimensional vectors in a latent space. The entries in the matrix will be the corresponding scalar products. The entries in the matrix are high probabilities if a relationship holds, and low probabilities if this is not the case.

From distant supervision and text analysis we have positive examples. For learning we also need negative examples.

## Bayesian Personalized Ranking

Idea: give observed true facts higher ranking then unobserved (true or false) facts

Approach: create ranked pairs $f^{+}$and $f^{-}$ Objective Function

$$
\sum_{f^{+}, f^{-}} \log \sigma\left(\theta_{f^{+}}-\theta_{f^{-}}\right)
$$

where

$$
\theta_{f}=\boldsymbol{p} \cdot \boldsymbol{r}
$$

Maximize with Stochastic Gradient Descent

For choosing negative examples of facts we encounter the problem that we can choose any fact that has not been observed in the data as such a negative example, but that we cannot be sure that the chosen example really is a negative example. It could simply be a relationship that holds, but has not been registered anywhere. This problem is similar to the one encountered in recommender systems where the absence of a rating does not imply a negative rating.

To better adjust to this situation an alternative method for matric factorization, called Baysian Personalized Ranking, is used. It is based on an alternative loss function is constructed that attempts to maintain the relative ranking among positive and negative examples.

## Relation Embeddings

The matric factorization obtained this way allows to map entity pairs and relationships in the same low-dimensional space. As illustrated in this example this should cluster together those that coorespond to similar relationships. This allows to infer new relationships for existing entity pairs, as well as syntactic forms of relationships.

## Summary

Information extraction

- Populating knowledge bases and fact databases
- Taxonomy induction

Pattern-based approaches

- High precision, low recall, work intensive

Supervised learning

- Low precision, high recall, work intensive

Hybrid methods: bootstrapping, distant supervision, matric factorization

No statement schema known: open information extraction

We have discussed the different variants of information extraction methods typically used, with their advantages and drawbacks. Another problem of information extraction is called open information extraction. It is typically used for extracting statements from large collections of documents, such as the Web, where no predefined schema of relations and entity types is known. Such methods have first of all to be able to identify that a statement is present. Such methods rely on significant syntactic preprocessing of the text, and use verbs as anchor points to detect statements.

