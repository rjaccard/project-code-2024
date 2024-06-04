# Part 1: Information Retrieval 

## Information Management Tasks

Since the central role of an information system is to support a model of a realworld phenomen based on data, the key information management tasks are related to the interplay between data and models. We can identify two directions for this interplay: from models to data, and from data to models. From models to data is commonly what we understand by retrieval, or information retrieval.

Given a model, we would like to learn about specific aspects of reality. If we have a model of the temperature distribution in the world, we would like to retrieve the temperature at a specific location or the global average temperature. For Web search we would use a model of how search terms provided by user to a Web search engine relate to documents considered as being relevant by the user, to retrieve the results of a user query.

Going from data to models is what is commonly called data mining. Often we find big data collections for which we do not have a proper or only incomplete interpretation. For example, we might have temperature measurements at given points, but do not understand the correlations among those measurements or the values at locations without measurements. If we have large document collections, we do not understand which are the topics that are covered by those documents. Data mining deals with the problem of providing algorithms that reveal hidden structures in data in order to create new models. Both information retrieval and data mining will be central topics that will be covered in this course.

## 1. INFORMATION RETRIEVAL

## What is Information Retrieval?

Information retrieval (IR) is the task of finding in a large collection of documents those that satisfy the information needs of a user

- Documents are mostly unstructured data
- Most of the time text documents are considered

Examples

- Searching documents in a library
- Searching the Web

Information retrieval deals with the problem of matching information needs of human users with information provided in large document collections. Important aspects of this definition are:

- Documents are largely unstructured data; documents can be based on different media, including text, images, videos
- Document collections are generally large, with the Web being a prime example of a very large document collection
- Information needs are user-driven; there exists no formal (mathematical) definition of the information retrieval task


## What are the Constituents of a Document?

Content consists of the text, and possibly other media, such as images, videos
Concepts are general ideas mentioned, they can be

- Explicitly annotated, e.g., hashtags, keywords
- Automatically extracted, e.g., entities, concepts

In general, there are three types of features that can be associated with a document:

1. The document content: depending on the media this is the characters of text, the pixels of an image, the images of a video. In information retrieval features extracted of the content are the main source of input for retrieval methods to create structured representations of the documents. It is important to note that these structured representations are only used internally to the retrieval system and not visible to the human user. We will first strongly focus on content-based information retrieval for text documents.
2. The authors of the document: documents are authored, referenced and consumed by people. This social context can provide very useful to enhance the performance of information retrieval algorithms
3. The concepts mentioned in document: concepts are general ideas that have a specific meaning to humans and thus are - different to content features - visible to human users. They can be either manually annotated or automatically extracted, and also help in the retrieval task. Since they are human-understandable, they can
be in fact explicitly used in order to perform structured searches for documents. We will see in the last part of the lecture (extracting knowledge from documents) how automated methods can extract concepts from documents.

## Relationships!

Documents share similar content:

SEARCH / CLUSTERING / TOPICS / CLASSIFICATION

Concepts have relationships: TAXONOMIES / ONTOLOGIES

Each type of the aforementioned features is used to create relationships:

- Content-based features are used to compute document similarity, one of the basic approaches in information retrieval, this part of the lecture. Document similarity allows to search, cluster or classify documents
- Social features are used to create social networks, which can then be analyzed for influence (used in information retrieval) or communities (we will see in the lecture part on data mining how to extract communities)
- Concept features can be organized through semantic relationships in taxonomies and ontologies, which allow to classify and search documents (we will see in the lecture part on knowledge extraction how to infer such relationships)


## Information Retrieval

An information retrieval system has to deal with the following tasks:

- Generating structured representations of information items: this process is called feature extraction and can include simple tasks, such as extracting words from a text as well as complex methods, e.g., for image or video analysis.
- Generating structured representations of information needs: often this task is solved by providing users with a query language and leave the formulation of structured queries to them. This is the case, for example, for simple keyword based query languages, as used in Web search engines. Some information retrieval systems also support the user in the query formulation, e.g., through visual interfaces.
- Matching of information needs with information items: this is the algorithmic task of computing similarity of information items and retrieval queries. The heart of this step is the information retrieval model. Similarity measures on the structured representations of queries and documents are used to model relevance of information for users. As a result, a selection of relevant information items or a ranked result can be presented to the user.

Since information retrieval systems deal usually with large information collections and/or large user communities, the efficiency of an information retrieval system is crucial. This imposes fundamental constraints on the retrieval model. Retrieval models that would capture relevance very well, but are computationally prohibitively expensive, are not suitable for an information retrieval system.

## Example: Text Retrieval

The most popular information retrieval system are Web search engines. To a large degree, they are text retrieval systems, since they exploit mainly the textual content of Web documents for retrieval. However, current Web search engines also exploit link information and even image information. The three tasks of a Web search engine for retrieval are:

1. extracting the textual features, which are the words or terms that occur in the documents. We assume that the web search engine has already collected the documents from the Web using a Web crawler.
2. support the formulation of textual queries. This is usually done by allowing the entry of keywords through Web forms.
3. computing the similarity of documents with the query and producing from that a ranked result. Here Web search engines use standard text retrieval methods, such as Boolean retrieval and vector space retrieval. We will introduce these methods in detail in this lecture later.

## Retrieval Model

The retrieval model determines

- the structure of the document representation
- the structure of the query representation
- the similarity matching function


## Relevance

- determined by the similarity matching function
- should reflect right topic, user needs, authority, recency
- no objective measure

The heart of an information retrieval system is its retrieval model. The retrieval model is used to capture the meaning of documents and queries, and determine from that the relevance of documents with respect to queries. Although there exist a number of intuitive notions of what determines relevance one must keep clearly in mind that it is not an objective measure.

## Evaluating a Retrieval Model

## Quality of a retrieval model depends on how well it matches user needs!

Comparison to database querying

- correct evaluation of a class of query language expressions
- can be used to implement a retrieval model

The quality of a retrieval system can principally only be determined through the degree of satisfaction of its users. This is fundamentally different to database querying, where there exist criteria for correct query answering that can be formally verified, e.g., whether a result set retrieved from a database matches the logical conditions specified in a query.

## Information Filtering

The roles of documents and queries can be swapped in an information retrieval system. As a result one obtains an information filtering system. Information filtering systems can be based on the same retrieval models as standard information retrieval systems for ad-hoc query access.

## Information Retrieval and Browsing

Retrieval

- Produce a ranked result from a user request
- Interpretation of the information by the system

Browsing

- Let the user navigate in the information set
- Relevance feedback by the human

Information retrieval is usually closely connected to the task of browsing. Browsing is the explorative access by users to large document collections. By browsing a user implicitly specifies his/her information needs through selection of documents. This feedback can be used by an information retrieval system in order to improve its query representation and thus the retrieval result. One example of such an approach we will see when introducing relevance feedback. On the other hand, results returned by information retrieval systems are usually large, and therefore browsing is needed by users in order to explore the results. Both activities, retrieval and browsing thus can be combined into an iterative process.

## Evaluating Information Retrieval

Test collections, where the relevant documents are identified manually are used to determine the quality of an IR system (e.g. TREC)

Since there exists no objective criterion whether an information retrieval query is correctly answered, other means for evaluating the quality of an information retrieval system are required. The approach is to compare the performance of a specific system to human performance in retrieval. For that purpose test collections of documents, such as TREC (http://trec.nist.gov/), are created and for selected queries human experts select the relevant documents. Note that this approach assumes that humans have an agreed-upon, objective notion of relevance, an assumption that can be easily challenged of course.

## Recall and Precision

Recall is the fraction of relevant documents retrieved from the set of total relevant documents collectionwide

Precision is the fraction of relevant documents retrieved from the total number retrieved (answer set)

|  | Relevant | Non-relevant |  |
| :---: | :---: | :---: | :---: |
| Retrieved | True positives <br> (tp) | False positives <br> (fp) | $R=\frac{t p}{t p+f n}=P($ retrieved $\mid$ relevant $)$ |
| Not Retrieved | False negatives <br> (fn) | True negatives <br> (tn) | $P=\frac{t p}{t p+f p}=P($ relevant $\mid$ retrieved $)$ |

The results of IR systems are compared to the expected result in two ways:

1. Recall measures how large a fraction of the expected results is actually found.
2. Precision measures how many of the results returned are actually relevant.

Important note: This measure evaluates an unranked result set. All elements of the result are considered as equally important.

## Recall and Precision - A Tradeoff

Suppose you search for "Theory of Relativity".

Optimizing recall: retrieve all pages mentioning "theory" and "relativ*"

- We will have probably most documents talking about the topic
- We might have results such as, "In theory, I feel relatively good", "Relative to the theory of evolution ..." etc.

Optimizing precision: retrieve all pages mentioning "relativity theory" and "expanding universe

- Most likely all results are relevant
- But we might miss "the theory of relativity by Einstein"

Thus high recall hurts precision and vice versa

This example expands upon the point that we made in the previous slide. Simply recalling all web pages that match the search query does not ensure precision-in other words relevance to user needs is not a simple matter.

## Combined Measures

Sometimes we want to characterize the performance of a retrieval system by one number F-Measure: weighted harmonic mean

$$
F=\frac{1}{\alpha \frac{1}{P}+(1-\alpha) \frac{1}{R}}, \quad \alpha \in[0,1]
$$

F1: balanced F-Measure with $\alpha=\frac{1}{2}: \quad F 1=\frac{2 P R}{P+R}$

Sometimes one wants to characterize the performance of a retrieval system by a single measures. Different types of means could be considered, e.g., the arithmetic mean or the accuracy measure, i.e. (tp $+\operatorname{tn}) /(\operatorname{tp}+\operatorname{tn}+\mathrm{fp}+\mathrm{fn})$. Accuracy, which is used in evaluating quality of classifiers could be considered, as retrieval can be understood as the problem of classifying into two sets, relevant and non-relevant. However, since the set of relevant documents is usually much smaller than the set of non-relevant documents, the measure could be optimized by declaring all documents non-relevant. Arithmetic mean is also no suitable, since when choosing $100 \%$ recall we would always have at least $50 \%$ of arithmetic mean between recall and precision. Therefore in practice the harmonic mean is used. It can be tuned by the parameter alpha. Larger values of alpha emphasize the importance of precision and smaller ones the importance of recall

## Precision/Recall Tradeoff in Ranked Retrieval

An IR system ranks documents by a similarity coefficient, allowing the user to trade off between precision and recall by choosing the cutoff level

One of the two measures of recall and precision can always be optimized. Recall can be optimized by simply returning the whole document collection, whereas precision can be optimized by returning only very few results. Important is the trade-off: the higher the precision for a specific recall, the better the information retrieval system. A hypothetical, optimal information retrieval system would return results with $100 \%$ percent precision always. If a system ranks the results according to relevance the user can control the relation between recall and precision by selecting a threshold of how many results he/she inspects.

## Evaluating Ranked Retrieval

Recall-Precision Plot

If we draw the Recall-Precision graph for a ranked retrieval result, we will find the following picture. The precision will always drop when non-relevant documents are returned and increase when relevant documents are returned. The green dots correspond to relevant documents and the red dots to non-relevant ones.

## Interpolated Precision

In order to convert the recall-precision plot into a monotonically decreasing function, interpolated precision is introduced, which returns always the highest level of precision achieved up to a given recall level.

## Mean Average Precision (MAP)

Given a set of queries $Q$

For each $q_{j} \in Q$ the set of relevant documents $\left\{d_{1}, \ldots d_{m_{j}}\right\}$

$R_{j k}$ the top $\mathrm{k}$ documents for query $q_{j}$

$P_{\text {int }}\left(R_{j k}\right)$ interpolated precision of result $R_{j k}$

$$
\operatorname{MAP}(Q)=\frac{1}{|Q|} \sum_{j=1}^{|Q|} \frac{1}{m_{j}} \sum_{k=1}^{m_{j}} P_{i n t}\left(R_{j k}\right)
$$

Mean Average Precision has been shown to be a robust measure for evaluating the quality of a ranked retrieval system for a query collection $\mathrm{Q}$. When a relevant document is not retrieved at all, the precision value in the MAP is 0 .

## Example 

Assume 4 results are returned for a query $q$ : <br> R N R N <br> $\mathrm{P} @ 1=1, \mathrm{P} @ 2=0.5, \mathrm{P} @ 3=2 / 3, \mathrm{P} @ 4=0.5$ <br> Then $\operatorname{MAP}(\{q\})=1 / 4(1+0.5+2 / 3+0.5)=2 / 3$

A simple example where the query set $\mathrm{Q}$ to be evaluated consists of a single query q. For multiple queries the results would be averaged.

## ROC Curve

Specificity S: $1-\mathrm{S}=\frac{f p}{f p+t n}=P$ (retrieved $\mid$ not relevant $)$

Specificity gives information about how many of the true negatives have been retrieved as false positives

- The steeper the curve rises at the beginning, the better
- The larger the area under the curve, the better

Another frequently used approach to globally evaluate ranked retrieval is the ROC curve. The ROC curve is frequently loosely called a recall-precision curve, which is not accurate (as the figure shows).

The ROC curve relates specificity (on the $x$-axis) to recall (on the $y$ axis). Specificity measures the fraction of true negatives that are detected in proportion to all negatives. Thus 1 - specificity is the rate of false positives that have been retrieved, the so-called false positive rate (FPR). In other words, it is the fraction of non-relevant documents among all non-relevant documents that occur in the result. The desired behavior of an IR system is that the curve raises quickly at the beginning, which means that many relevant results are retrieved without having a high fraction of non-relevant documents. This is also equivalent to saying that the area under the curve should be large. Therefore, the area under the ROC curve is sometimes considered similarly as an evaluation of the overall retrieval quality of a retrieval system, analogous to the MAP measure.

## Example:

- When the recall is at 0.5 then $1-\mathrm{S}$ is at 0.1 . This implies that $\mathrm{S}$ is 0.9 . Then we can conclude that $\mathrm{fp}=1 / 9 \mathrm{tn}$, or in other words when retrieving half of the relevant documents, then we have also retrieved about $10 \%$ of the non-relevant documents.


## 2. TEXT-BASED INFORMATION RETRIEVAL

## Text-based Information Retrieval

Most of the information needs and content are expressed in natural language

- Library and document management systems
- Web Search Engines

Basic approach: use the words that occur in a text as

features for the interpretation of the content

- This is called the "full text" retrieval approach
- Ignore grammar, meaning etc.
- Simplification that has proven successful
- Document structure, layout and metadata may be taken into account additionally (e.g. PageRank/Google)

Traditional information retrieval has been primarily concerned over many years with the problem of retrieving information from large bodies of documents with mostly textual content, as they where typically found in library and document management systems. The problems addressed were classification and categorization of documents, systems and languages for retrieval, user interfaces and visualization. The area was perceived as being one of narrow interest for a highly specialized user community, mainly librarians. The advent of the WWW changed this perception completely, as the web is a universal repository of documents with universal access.

Since nowadays most of the information content is still available in textual form, text is an important basis for information retrieval. Natural language text carries a lot of meaning, which still cannot fully be captured computationally. The research in cognitive science, especially linguistics suggests that perhaps this can never be done. Therefore information retrieval systems are based on strongly simplified models of text, ignoring most of the grammatical structure of text and reducing texts essentially to the terms they contain. This approach is called full text retrieval and is a simplification that has proven to be very successful. Nowadays, this approach is gradually
extended by taking into account other features of documents, such as the document or link structure.

## Architecture of Text Retrieval Systems

This figure illustrates the basic architecture with the different functional components of a text retrieval system. We can distinguish three main groups of components:

1. the feature extraction component: it performs text processing to turn queries and text documents into a keyword-based representation
2. the ranking system: it implements the retrieval model. In a first step user queries are potentially modified (in particular if user relevance feedback is used), then the documents required for producing the result are retrieved from the database and finally the similarity values are computed according to the retrieval model in order to compute the ranked result.
3. the data access system: it supports the ranking system by efficiently retrieving documents containing specific keywords from large document collections. The standard technique to implement this component is called inverted files.

In addition we recognize two components to interface the system to the user on the one hand, and to the data collection on the other hand.

## Pre-Processing Text for Text Retrieval 

## Feature Extraction 

In full text retrieval each document is represented by a set of representative keywords or index terms. Using index terms is an ancient concept that has been used in books. The earliest example of an index is from a temple library in Babylon, cataloging the subjects of the cuneiforms. An index term is a document word useful for capturing the document's main topics. Often, index terms are only nouns, because nouns carry meaning by themselves, whereas verbs express relationships between words. These relationships are more difficult to extract.

When using words as text features normally a stepwise processing approach is taken: in a first step, the document structure, e.g., from $\mathrm{XML}$, is extracted and if required stored for further processing. The remaining text is stripped of special characters, producing the full text of the document as a sequence of tokens. Then very frequent words which are not useful for retrieval, so-called "stopwords", are eliminated (e.g. "a", "and" etc.). As the same word can occur in natural language in different forms, usually stemming is used: Stemming eliminates grammatical variations of the same word by reducing it to a word root, e.g., the words connecting, connection, connections would be reduced to the same "stem" connect. This step
can be followed by a manual intervention, where humans can select or add index terms based on their understanding of the semantics of the document. The result of the process is a set of index terms which represents the document.

## Text Retrieval - Basic Concepts and Notations

Document d: $\quad$ expresses ideas about some topic in a natural language

Query q: $\quad$ expresses an information need for documents pertaining to some topic

Index term: a semantic unit, a word, short phrase, or potentially root of a word

Database DB: $\quad$ collection of $n$ documents $d_{j} \in D B, j=1, \ldots, n$

Vocabulary $T: \quad$ collection of $m$ index terms $k_{i} \in T, i=1, \ldots, m$

A document is represented by a set of index terms $k_{i}$

The importance of an index term $k_{i}$ for the meaning of a document $d_{j}$ is represented by a weight $w_{i j} \in[0,1]$; we write $d_{j}=\left(w_{1 j} \ldots, w_{m j}\right)$

The IR system assigns a similarity coefficient $\operatorname{sim}\left(q, d_{j}\right)$ as an estimate for the relevance of a document $d_{j} \in D B$ for a query $q$.

We introduce the precise terminology we will use in the following for text retrieval systems. Note that the way of how specific weights are assigned to an index term with respect to a document and of how similarity coefficients are computed are part of the definition of the text retrieval model.

## Term-Document Matrix

Matrix of weights $w_{i j}$

| Terms |  |  |  |  |  |  |  |  |  | Documents |  |  |  |  |  |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 | B11 | B12 | B13 | B14 | B15 | B16 | B17 |  |  |
| algorithms | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| application | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |
| delay | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |
| differential | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |  |  |
| equations | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |  |  |
| implementation | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| integral | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |  |
| introduction | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| methods | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |
| nonlinear | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |
| ordinary | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| oscillation | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |
| partial | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |
| problem | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |
| systems | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| theory | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |  |  |

- Vocabulary (contains only terms that occur multiple times, no stop words)
- all weights are set to 1 (equal importance)

In text retrieval we represent the relationship between the index terms and the documents in a term-document matrix. In this example only a selected vocabulary is used for retrieval, consisting of all index terms that occur in more than one document and only weights of 1 are assigned, indicating that the term occurs in the document.

## Boolean Retrieval

Users specify which terms should be present in the documents

- Simple, based on set-theory, precise meaning
- Frequently used in (old) library systems
- Still many applications, e.g., web harvesting

Example query

- "application" AND "theory" $\rightarrow$ answer: B3, B17

Retrieval Language

expr $::=$ term | (expr) | NOT expr | expr AND expr | expr OR expr

Weights for index terms appearing in documents

$w_{i j}=1$ if $k_{i} \in d_{j}$ and 0 otherwise

Early information retrieval systems (as well as many search systems in use today, such as spotlight and windows search) use the Boolean retrieval model. This model is actually more similar to database querying, as requests are specified as first order (Boolean) expressions. Term weights are set to 1 when a term occurs in a document, just as in the term-document matrix on the previous slide.

## "Similarity" Computation in Boolean Retrieval

## Step 1:

Determine the disjunctive normal form of the query $q$

- A disjunction of conjunctions
- Using distributivity and Morgans laws, e.g. NOT (s AND $t$ ) $\equiv$ NOT s OR NOTt
- Thus $q=c t_{1} O R \ldots O R c t_{l}$ where $c t=\underline{t}_{1} A N D \ldots A N D \underline{t}_{k}$ and $\underline{t} \in\{t, N O T t\}$


## Step 2:

For each conjunctive term ct create its query weight vector $\operatorname{vec}(c t)$

$-\operatorname{vec}(c t)=\left(w_{1} \ldots, w_{m}\right):$

$w_{i}=1 \quad$ if $k_{i}$ occurs in $c t$

$w_{i}=-1$ if NOT $k_{i}$ occurs in ct

$w_{i}=0 \quad$ otherwise

Computing the similarity of a document with a query reduces in Boolean retrieval to the problem of checking whether the term occurrences in the document satisfy the Boolean condition specified by the query. In order to do this in a systematic manner, a Boolean query is first normalized into disjunctive normal form. Using this equivalent representation, checking whether a document matches the query reduces to the problem of checking whether the document vector, i.e., the column of the term-document matrix corresponding to the document, matches one of the conjunctive terms of the query.

## Step 3:

If one weight vector of a conjunctive term $c t$ in $q$ matches the document weight vector $d_{j}=\left(w_{1 j}, \ldots, w_{m j}\right)$ of a document $d_{j}$, then the document $d_{j}$ is relevant, i.e., $\operatorname{sim}\left(d_{j}, q\right)=1$

- vec(ct) matches $d_{j}$ if:

$$
\begin{aligned}
& w_{i}=1 \wedge w_{i j}=1 \\
& w_{i}=-1 \wedge w_{i j}=0
\end{aligned}
$$

A match is established if the document vector contains all the terms of the query vector in the correct form, i.e., if the term occurs positively in the query the term has to occur in the document, if the term occurs in the negated form in the query the term must not occur, and if the term does not occur in the query it may or may not occur in the document.

## 3. VECTOR SPACE RETRIEVAL

Limitations of Boolean Retrieval

- No ranking: problems with handling large result sets
- Queries are difficult to formulate
- No tolerance for errors
- Queries either return far too many results, or none


## Key Idea of Vector Space Retrieval

- represent both the document and the query by a weight vector in the m-dimensional keyword space assigning non-binary weights
- determine their distance in the m-dimensional keyword space

The main limitation of the Boolean retrieval model is its incapability to rank the result and to match documents that do not contain all the keywords of the query. More complex requests become very difficult to formulate. Finally it is hard to predict for the user whether a query would produce a reasonably sized set of results. Often either no results are returned, if the query is too restrictive or very large numbers of results are produced in the opposite case.

The vector space retrieval model addresses these issues by supporting non-binary weights, i.e., real numbers in $[0,1]$, both for documents and queries, and producing continuous similarity measures in $[0,1]$. The similarity measure is derived from the geometrical relationship of vectors in the m-dimensional space of document/query vectors.

## Similarity Computation in Vector Space Retrieval

$$
\begin{aligned}
& \vec{d}_{j}=\left(w_{1 j}, w_{2 j}, \ldots, w_{m j}\right), w_{i j}>0 \quad \text { if } k_{i} \in d_{j} \\
& \vec{q}=\left(w_{1 q}, w_{2 q}, \ldots, w_{m q}\right), w_{i q} \geq 0 \\
& \operatorname{sim}\left(\vec{q}_{q}, \vec{d}_{j}\right)=\cos (\theta)=\frac{\vec{d}_{j} \bullet \vec{q}}{\left|\vec{d}_{j}\right||\vec{q}|}=\frac{\sum_{i=1}^{m} w_{i j} w_{i q}}{\left|\vec{d}_{j}\right||\vec{q}|} \\
& |v|=\sqrt{\sum_{i=1}^{m} v_{i}^{2}} \\
& \text { Since } w_{i j}>0 \text { and } w_{i q} \geq 0,0 \leq \operatorname{sim}\left(q, d_{j}\right) \leq 1
\end{aligned}
$$

The distance measure for vectors has to satisfy the following properties:

- If two vectors coincide completely their similarity should be maximal, i.e., equal to 1 .
- If two vectors have no keywords in common, i.e., if wherever the query vector has positive weights the document vector has weight 0 , and vice versa - or in other words if the vectors are orthogonal - the similarity should be minimal, i.e., equal to 0 .
- in all other cases the similarity should be between 0 and 1 .

The scalar product (which is equivalent to the cosine of the angle of two vectors) has exactly these properties and is therefore (normally) used as similarity measure for vector space retrieval.

## Vector Space Retrieval - Properties

## Properties

- Ranking of documents according to similarity value
- Documents can be retrieved even if they don't contain some query keyword


## Today's standard text retrieval technique

- Web Search Engines
- The vector model is the basis of most search engines, however they do not rely on it exclusively
- It is simple and fast to compute

The vector space retrieval model is the standard retrieval technique used both on the Web and for classical text retrieval.

## Example

We apply the same weighting scheme for the document and query vectors as in the case of Boolean retrieval, and show the results vector space retrieval produces. We observe that also documents containing only one of the two keywords occurring in the query, would show up in the result, although with lower similarity value.

Since in vector space retrieval no longer exclusively binary weights are used, a central question is of how to determine weights that more precisely determine the importance of a term for the document. Obviously not all terms carry the same amount of information on the meaning of a document. This was for example one of the reasons to eliminate stop words, as they normally carry no meaning at all.

## Term Frequency

Documents are similar if they contain the same keywords (frequently)

- Therefore use the frequency freq $(i, j)$ of the keyword $k_{i}$ in the document $d_{j}$ to determine the weight of the document vectors

(Normalized) term frequency of term $k_{i}$ in Document $d_{j}$

$$
t f(i, j)=\frac{\text { freq }(i, j)}{\max _{k \in T} f r e q(k, j)}
$$

An obvious difference that can be made among terms is with respect to their frequency of occurrence in a document. Thus a weighting scheme for documents can be defined by considering the (relative) frequency of terms within a document. The term frequency is normalized with respect to the maximal frequency of all terms occurring within the document.

## Example

Vocabulary $T=\{$ information, retrieval, agency $\}$ Query $q=($ information, retrieval) $=(1,1,0)$

This example illustrates the use of term frequency. Assume we form the query vector by simply setting the weight to 1 if the keyword appears in the query. Then we would obtain D1 and D2 as result. Actually, this result appears to be non-intuitive, since we would expect that D3 is much more similar to $\mathrm{q}$ than $\mathrm{D} 2$. What has gone wrong?

The problem is that the term "retrieval", since it occurs very frequently in $\mathrm{D} 2$, leads to a high similarity value for $\mathrm{D} 2$. On the other hand the term retrieval has very little power to disambiguate meaning in this document collection, since every document contains this term. From an information-theoretic perspective one can state, that the term "retrieval" does not reduce the uncertainty about the result at all.

## Inverse Document Frequency

We have not only to consider how frequent a term occurs within a document (measure for similarity), but also how frequent a term is in the document collection of size $\mathrm{n}$ (measure for distinctiveness)

Inverse document frequency of term $k_{i}$

$$
i d f(i)=\log \left(\frac{n}{n_{i}}\right) \in[0, \log (n)]
$$

$n_{i}$ number of documents in which term $k_{i}$ occurs

Inverse document frequency can be interpreted as the amount of information associated with the term $k_{i}$

Term weight (tf-idf) $\quad w_{i j}=t f(i, j) i d f(i)$

Thus we have to take into account not only the frequency of a term within a document, when determining the importance of the term for characterizing the document, but also the discriminative power of the term with respect to the document collection as a whole. For that purpose, the inverse document frequency is computed and included into the term weight.

We can see now from this weighting scheme that eliminating stop words is actually an optimization of computing similarity measures in vector space retrieval. Since stop words normally occur in every document of a collection, their term weights will normally be 0 and thus the terms do not play a role in retrieval. Thus it is of advantage to exclude them already from the retrieval process at the very beginning.

## Example

Vocabulary $T=\{$ information, retrieval, agency $\}$ Query $q=($ information, retrieval) $=(1,1,0)$

$$
idf(i)=\log \left(\frac{n}{n_{i}}\right) \in[0, \log (n)]
$$

$$
idf(information)=idf(agency)=log(2) idf(retrieval) =\log (1)=0
$$

We have now: $\mathrm{n}=4, \mathrm{n}_{\text {information }}=2, \mathrm{n}_{\text {retrieval }}=4, \mathrm{n}_{\text {agency }}=2$

The result corresponds much better to the "expectation" when using the inverse document frequencies.

## Query Weights

The same considerations as for document term weights apply also to query term weights

Query weight for query $q$

$$
w_{i q}=\frac{\operatorname{freq}(i, q)}{\max _{k \in T} \operatorname{freq}(k, q)} \log \left(\frac{n}{n_{i}}\right)
$$

Example: Query $q=$ (information, retrieval)

- Query vector: $(\log (2), 0,0)$
- Scores: $\operatorname{sim}(q, D 1)=0.569 \ldots$

$\operatorname{sim}(q, D 2)=0$

$\operatorname{sim}(q, D 3)=0.254$

$\operatorname{sim}(q, D 4)=0$

Finally, we have to look at the question of how to determine the weights for the query vector. One can apply the same principles as for determining the document vector, as is shown. In practice there exist a number of variations of this approach.

## The Role of Document Length

When computing cosine similarity, document vectors are normalized

For a long term the suspicion was that the standard vector space retrieval method favors short documents over long documents as a result of the normalization of document vectors. While normalizing document vectors in the longer a document a term that occurs in the query would receive a lower weight, as it has to share the total weigth of 1 with a larger number of documents, and thus the longer document is less likely to receive a high rank. In a seminal paper Singhal and co-authors provided empirical evidence for this phenomenon. The compared for a TREC dataset the likelihood of a document of a given length of being relevant (by relying on the manual evaluation) with the propobability that a document of that length would be retrieved using standard vector retrieval. The graph shows clearly that shorter documents have better chances to show up in the result, than longer ones, even when they are less relevant. The pivot point is the document length where the both probabilities match.

## Length Normalization

Different schemes for length normalization

Original scheme: $\frac{t f * i d f}{((1-s)+s * n)}$ $s=$ slope, $n=$ old normalization factor

## Advantage:

- Better retrieval performance

Disadvantage

- Normalization is collection specific

To correct for this phenomenon different normalization schemes accounting for document length have been proposed, such as the original one from Singhal. As this normalization schemes contain a parameter, like the slope parameter in Singhal schemes, this parameter needs to be chosen. The choice depends on the document collection and can be based on empirical evaluations.

## Variants of Vector Space Retrieval Model

The vector model with tf-idf weights is a good ranking strategy for general collection

- many alternative weighting schemes exist, but are not fundamentally different

| Term frequency |  | Document frequency |  | Normalization |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| n (natural) | $\mathrm{tf}_{t, d}$ | n (no) | 1 | n (none) | 1 |
| I (logarithm) | $1+\log \left(\mathrm{tf}_{t, d}\right)$ | t (idf) | $\log \frac{N}{d f_{t}}$ | c (cosine) | $\frac{1}{\sqrt{w_{1}^{2}+w_{2}^{2}+\ldots+w_{M}^{2}}}$ |
| a (augmented) | $0.5+\frac{0.5 \times \mathrm{tf}_{t, d}}{\max _{t}\left(\mathrm{tf}_{t, d}\right)}$ | p (prob idf) | $\max \left\{0, \log \frac{N-\mathrm{df}_{t}}{\mathrm{df}_{t}}\right\}$ | u (pivoted <br> unique) | $1 / u$ |
| b (boolean) | $\begin{cases}1 & \text { if } \mathrm{tf}_{t, d}>0 \\ 0 & \text { otherwise }\end{cases}$ |  |  | b (byte size) | $1 /$ CharLength $^{\alpha}$, <br> $\alpha<1$ |
| L (log ave) | $\frac{1+\log \left(\mathrm{tf}_{t, d}\right)}{1+\log \left(\operatorname{ave}_{t \in d}\left(\mathrm{tf}_{t, d}\right)\right)}$ |  |  |  |  |

Different variants of tf-idf weighting schemes have been developed and used over time. They can be combined with each other, also independently for the weighting of document and query terms. One important variant is the logarithmic weighting of term frequencies, which moderates the influence of very frequently occurring terms in documents.

## Discussion of Vector Space Retrieval Model 

We summarize here the main advantages of the vector space retrieval model. It has proven to be a very successful model for general text collections, i.e., if there exists no additional (context) information on the documents that could be exploited, e.g., from a specific application domain. Providing a ranked result improves the usability of the approach, as users can more easily distinguish more relevant documents from less relevant documents. The model inherently assumes that there exist no mutual dependencies in the occurrences of the terms, i.e., that certain terms appear together more frequently than others. Studies have however shown that taking such co-occurrence probabilities additionally into account, can actually HURT the performance of the retrieval system. The reason is that co-occurrence probabilities are often related to specific application domains and thus do not easily transfer to general-purpose retrieval.

One of the principal criticisms of the vector space model is the lack of theoretical explanation why it works. At the end, it is a heuristics. This drawback has been addressed with other models, in particular probabilistic retrieval models.

