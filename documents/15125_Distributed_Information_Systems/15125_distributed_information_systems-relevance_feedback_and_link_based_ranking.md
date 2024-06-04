# 9. QUERY EXPANSION 

## Motivation

If the user query does not contain any relevant term, a corresponding relevant document will not show up in the result

## Idea: System adds query terms to user query!

Users cannot predict or imagine all possible ways of how the concepts they are interested to find in their search can be expressed in natural language. This may have as a consequence, even under the vector space retrieval model, that relevant results are missed. This is, for the example, the case when there exist different synonyms (different terms with the same meaning). In the following we will see one possible approach to deal with this problem, namely extending the user query automatically by the system with additional terms.

## Two Methods for Extending Queries

1. Local Approach:

- Use information from current query results: user relevance feedback

2. Global Approach:

- Use information from a document collection: query expansion

In the following we will present two types of approaches to query extension, which are distinguished by the source of information used to identify new additional query terms. In the local approach the source of information is the current user query, respectively results produced by answering the user query. In the global approach the source of information is a existing document collection, either the documents that make up the corpus that is being queried by the user, or another, external collection of documents.

## 1. User Relevance Feedback

In general, a user does not necessarily know what is his information need and how to appropriately formulate a query. BUT usually a user can well identify relevant documents. Therefore the idea of user relevance feedback is to reformulate a query by taking into account feedback of the user on the relevance of already retrieved documents.

The advantages of such an approach are the following:

-The user is not involved in query formulation, but just points to interesting data items.

-The search task can be split up in smaller steps.

-The search task becomes a process converging to the desired result.

## Feedback from Users

The general situation when receiving feedback from users can be depicted as follows: the retrieval system returns some result set $R$ that is presented to the user. This result set overlaps with the set of relevant documents $\left(\mathrm{C}_{r}\right)$. The user can the identify within the result set both documents that are relevant and nonrelevant. This gives the two feedback sets $D_{r}$ and $D_{n}$.

## Rocchio Algorithm

Rocchio algorithm: find a query that optimally separates relevant from non-relevant documents

$$
\vec{q}_{\text {opt }}=\underset{\vec{q}}{\arg \max }\left[\operatorname{sim}\left(\vec{q}, \mu\left(D_{r}\right)\right)-\operatorname{sim}\left(\vec{q}, \mu\left(D_{n}\right)\right)\right]
$$

## Centroid of a document set

$$
\mu(D)=\frac{1}{|D|} \sum_{d \in D} \vec{d}
$$

The basic idea for user relevance feedback was introduced by Rocchio. It is based on the observation, that the centroid of all document vectors of a document set $D$ can be considered as the most characteristic representation of the document set. Then one could attempt to construct a query $\mathrm{q}_{\text {opt }}$ that optimally separates relevant from non-relevant documents. In order to achieve this, the query to be constructed has to have maximal similarity with the set of relevant documents, respectively its centroid, and maximal dissimilarity with the set of non-relevant documents, respectively its centroid. This can be achieved by finding a query that maximizes the difference among these two similarity values.

We now motivate of how the optimal query vector can be found with an illustration. Assume that the relevant documents are marked by circles, and the non-relevant documents are marked by crosses, and that the vector space has (only) 2 dimensions. When we consider the centroid of the relevant documents (which could be a potential query based on user relevance feedback) as a potential search query, then we see that we cannot achieve optimal precision and recall at the same time.

We therefore consider also the centroid of the non-relevant documents as part of the user relevance feedback. We compute the difference vector among the two centroids, and we will use this difference vector to "move away" the query from the non-relevant documents.

We add the difference vector to the centroid for the relevant documents. The resulting optimal query vector now can include all relevant documents in its result, without including non-relevant ones. In practice, such a clear separation will not always be possible, but it has been shown that under some additional assumptions, this method is the optimal way to constructing the optimal query vector.

## Identifying Relevant Documents

Following the previous reasoning the optimal query is

$$
\begin{gathered}
\vec{q}_{\text {opt }}=\mu\left(D_{r}\right)+\left[\mu\left(D_{r}\right)-\mu\left(D_{n}\right)\right] \\
\vec{q}_{\text {opt }}=\left[\mu\left(D_{r}\right)-\mu\left(D_{n}\right)\right] \text { (under cosine similarity) }
\end{gathered}
$$

## Practical issues

- User relevance feedback is not complete
- Users do not necessarily identify non-relevant documents
- Original query should continued to be considered

Constructing an optimal query vector as described before is only theoretically possible, since the complete information on relevant and non-relevant documents is lacking in practice. Therefore, the theoretical considerations put forward so far, serve as an intuition to devise a practical scheme, that is approximating the theoretical construction of an optimal query vector.

## SMART: Practical Relevance Feedback

## Approximation scheme for the theoretically optimal query vector

If users identify some relevant documents $D_{r}$ from the result set $R$ of a retrieval query $q$

- Assume all elements in $R \backslash D_{r}$ are not relevant, i.e., $D_{n}=R \backslash D_{r}$
- Modify the query to approximate theoretically optimal query

$$
\vec{q}_{\text {approx }}=\alpha \vec{q}+\frac{\beta}{\left|D_{r}\right|} \sum_{\vec{d}_{j} \in D_{r}} \vec{d}_{j}-\frac{\gamma}{\left|R \backslash D_{r}\right|} \sum_{\vec{d}_{j} \notin D_{r}} \vec{d}_{j}
$$

$-\alpha, \beta, \gamma$ are tuning parameters, $\alpha, \beta, \gamma \geq 0$

- Example: $\alpha=1, \beta=0.75, \gamma=0.25$

The approximation scheme for user relevance feedback is called SMART. It starts from the assumption that users have identified some relevant documents. Then the scheme assumes that all other documents should be considered as non-relevant. This results in a modification of the original query that is controlled by 3 tuning parameters.

Since this is of course not correct, two mechanisms are used to moderate the impact of this wrong assumption:

1. The original query vector is maintained, in order not to drift away too dramatically from the original user query.
2. The weight given for the modification using the centroid of non-relevant documents is generally kept lower than the weight for the centroid of the relevant documents, as their non-relevance is just an assumption made, and not based on real user relevance feedback.

## Example

Query $q=$ "application theory"

Result

$$
\begin{aligned}
& \qquad \begin{array}{l}
\text { 0.77: B17 The Double Mellin-Barnes Type Integrals and Their Applications to Convolution Theory } \\
\text { 0.68: B3 Automatic Differentiation of Algorithms: Theory, Implementation, and Application } \\
\text { 0.23: B11 Oscillation Theory for Neutral Differential Equations with Delay } \\
\text { 0.23: B12 Oscillation Theory of Delay Differential Equations }
\end{array} \\
& \text { Query reformulation } \quad \vec{q}_{\text {approx }}=\frac{1}{4} \vec{q}+\frac{1}{4} \overrightarrow{d_{3}}-\frac{1}{12}\left(\overrightarrow{d_{17}}+\overrightarrow{d_{12}}+\overrightarrow{d_{11}}\right), \alpha=\beta=\gamma=\frac{1}{4}
\end{aligned}
$$

Result for reformulated query

$$
\text { 0.87: B3 Automatic Differentiation of Algorithms: Theory, Implementation, and Application }
$$

$$
\begin{aligned}
& \text { 0.61: B17 The Double Mellin-Barnes Type Integrals and Their Applications to Convolution Theory } \\
& \text { 0.29: B7 Knapsack Problems: Algorithms and Computer Implementations }
\end{aligned}
$$

0.23: B5 Ideals, Varieties, and Algorithms: An Introduction to Computational Algebraic Geometry and Commutative Algebra

This example shows how the query reformulation works. By identifying document $\mathrm{B} 3$ as being relevant and modifying the query vector it turns out that new documents ( $B 5$ and $B 7$ ) become relevant. The reason is that those new documents share terms with document B3, and these terms are newly considered in the reformulated query.

## Discussion

## Underlying assumptions of SMART algorithm

1. Original query contains sufficient number of relevant terms
2. Results contain new relevant terms that co-occur with original query terms
3. Relevant documents form a single cluster
4. Users are willing to provide feedback (!)

All assumptions can be violated in practice

Practical considerations

- Modified queries are complex $\rightarrow$ expensive processing
- Relevance Feedback consumes user time $\rightarrow$ could be used in other ways

Concerning the first assumption, if the initial query of the user does not contain sufficient information to retrieve at least a few documents that are relevant to the true interest of the user, the relevance feedback system will not be able to produce sufficient relevant documents with additional terms.

Concerning the second assumption, new terms can only be included as part of the modified query, if they co-occur at least in some documents together with original query terms. Otherwise, these terms could never be part of relevant documents in the result of the original query (why?).

Concerning the third assumption, implicitly the SMART algorithm assumes that all relevant documents are part of one cluster in the vector space. If they form multiple clusters, it is not able to correctly produce a query that can retrieve the relevant documents.

## Pseudo-Relevance Feedback

If users do not give feedback, automate the process

- Choose the top-k documents as the relevant ones
- Apply the SMART algorithm

Works often well

- But can fail horribly: query drift


## 2. Query Expansion

Query is expanded using a global, query-independent resource

- Manually edited thesaurus
- Automatically extracted thesaurus, using term cooccurrence
- Query logs

Global methods for expanding user queries can rely on a variety of resources. These may include thesauri (a thesaurus is a database that contains (near-) synonyms) that are manually constructed or automatically derived, or the automated analysis of query logs.

## Manually Created Thesaurus

Performing query expansion using a manually thesaurus requires the (expensive) effort of creating and maintaining such a thesaurus. This task is mainly performed in highly specialized technical fields in science and engineering. One prominent example of such a Thesaurus is maintained by Pubmed, the biggest publication database for medical literature maintained by the NIH, the National Institute of Health in the US. When using its search engine, you will find a window "Search details" that shows how the user query is automatically expanded using the Pubmed thesaurus. In this example we see that the search system identifies that "cancer" is an entry on the concept "neoplasms", and thus extends the query with all entries that it finds associated in the thesaurus (e.g. it would also search for "tumor").

## Automatic Thesaurus Generation

Attempt to generate a thesaurus automatically by analyzing the distribution of words in documents

Fundamental notion: similarity between two words

Definition 1:

Two words are similar if they co-occur with similar words.

"switzerland" $\approx$ "austria" because both occur with words such as

"national", "election", "soccer" etc., so they must be similar.

Definition 2:

Two words are similar if they occur in a given grammatical relation with the same words. "live in *", "travel to *", "size of *" are all phrases in which both "switzerland" or "austria" can occur

In order to avoid the effort of manually creating a thesaurus one can attempt to create it automatically by studying large numbers of documents and the distribution of words in those. This leads to the concept of similarity of words. There exists two basic methods to study this similarity, either purely statistically, by observing which words occur together in documents, or in a more accurate way by identifying whether the words occur in the same grammatical relationships.

We will later in the course study both types of methods. For the first approach we will study so-called "word embeddings". For the second approach we will learn about methods of "information extraction".

This example illustrates of how such automatic thesaurus generation based on statistical analysis looks in practice. A statistical analysis would allow to compute similarity of words. With such a similarity measure it is possible to search for related words (just like searching for documents with an information retrieval system). As the example shows, such a search reveals immediately many terms directly related with the original word, which was "cat".

## Epxansion using Query Logs

## Main source of query expansion at search engines

- Exploit correlations in user sessions

Example 1: users extend query

- After searching “Obama”, users search “Obama president"
- Therefore, "president" might be a good expansion

Example 2: users refer to same result

- User A accesses URL epfl.ch after searching "Aebischer"
- User B accesses URL epfl.ch after searching "Vetterli"
- "Vetterli" might be a potential expansion for the query “Aebischer" (and vice versa)

Query logs contain potentially rich information for query expansion. There a numerous ways of how such knowledge can be exploited. We show here two possible examples. Other methods rely on mining query logs using various techniques, including clustering and association rule mining, that we will encounter in the later part on data mining.

## 10. LINK-BASED RANKING

## Web is a Hypertext

## Web documents are connected through hyperlinks

1. Anchor text describes content of referred document
2. Hyperlink is a quality signal

Beyond the textual contents, Web documents consist also of hyperlinks. A hyperlink can be exploited for information retrieval in two ways:

1. The link is surrounded by some textual information that presumably refers to the content of the document the link is pointing to. Thus this text can complement the content of the referred document.
2. The link can also be considered as an endorsement of the referenced document by the author of the referring document. Thus the link can be used as a signal for quality and importance of the referred document.

## Indexing Anchor Text

Anchor text is loosely defined as the text surrounding a hyperlink

Example: "You can find cheap cars here." Anchor text: "You can find cheap cars here"

Anchor text may contain a lot of additional content on the referred page

- It might be a better description of the page than the page content itself

Anchor text can be defined in different ways. In general, it is considered as the text that is surrounding the link, and not only the text contained as part of the link tag (in the example, this text would simply be "here".) This text can contain valuable information on the referred page and thus be very helpful in retrieval.

## Example

When indexing a document $D$, include (with some weight) anchor text from links pointing to $D$

This example illustrates the use of anchor text in retrieval. Typically a home page is very graphical and contains often very little relevant content. If we consider a home page, such as the EPFL home page, we would probably found many pages that very well characterize EPFL, such as pages mentioning topics related to research and technology transfer. Typically this links would point to the EPFL home page. Thus it would also let the home page stand out from other EPFL pages (such as pages on the laws and ordonnances of EPFL).

Assume that a malicious Internet user would create a fake EPFL home page. Then chances that such a page is referred by reputed organizations, such as SNF, is very low. On the other hand pages listing spam pages might point to such a page and indicate its true character.

Therefore it makes a lot of sense to include such anchor text in the representation of the document. This is usually done by adding it with a given weight.

## Scoring of Anchor Text

Score anchor text with a weight depending on the authority of the anchor page' s website

- E.g., if we were to assume that content from cnn.com or yahoo.com is authoritative, then trust (more) the anchor text from them


## Score anchor text from other sites (domains) higher than text from the same site

- non-nepotistic scoring

To fight spam, on can adapt the weighting function to the reputation of the page that is referring. This could be done by having a directory of highly reputed sites and to give high weights to its members. A more fundamental of producing such reputation scores we will see in the following part on link-based ranking.

In order to avoid self-promotion, another method to fight link spamming is to give lower weights to links within the same site (nepotistic scoring = promoting your own family members).

## Indexing Anchor Text

One of the risks of including anchor text is that it makes pages spammable. Malicious users could create spam pages that point to web pages and try to relate it to contents that serve their interests (e.g., higher the quality of preferred pages by adding links, lower the quality of the undesired page by attaching negative anchor text). That this is happening can be seen from analyzing the indegree distribution of Web pages. The figure shows a standard log-log representation of the in-degree vs. the frequency of pages. Normally this relationship should follow a power-law, which shows in a log-log representation as a linear dependency. In real Web data, we see that this power law is violated, and that certain levels of in-degrees are over-represented. This can be attributed to link spamming, which does create moderate numbers of additional links on Web pages.

## Link-based Ranking: Idea

The fundamental idea of link-based scoring while attempting to fight spam is based on the concept of a random walker on the Web. Assume a random walker would visit a Web page. Then it would follow each $f$ the outgoing links with equal probability. If walking for a very long time in the Web, it would have a certain fraction of visits it passes by every page.

One of the consequences of this model would be that pages that have few inlinks, would be relatively infrequently visited. Since link farms usually have not many links pointing to them, in this way their influence in terms of link spamming would be moderated.

## Random Walker Model

$$
P\left(p_{i}\right)=\sum_{p_{j} \mid p_{j} \rightarrow p_{i}} \frac{P\left(p_{j}\right)}{C\left(p_{j}\right)}
$$

$N$ is the number of Web pages

$C(p)$ is the number of outgoing links of page $p$

$P\left(p_{i}\right)$ probability to visit page $p_{i}$, where page $p_{i}$ is pointed to by pages $p_{1}$ to $p_{N}=$ relevance

## Result

- If a random walker visits a page more often it is more relevant
- takes into account the number of referrals AND the relevance of referrals

Here we describe the random walker model more formally. The long term probability of visiting a page, depends on the long-term probability of having visited a page that is referring to the page. Thus the formulation of the random walker model becomes recursive.

## Transition Matrix for Random Walker

The definition of $P\left(p_{i}\right)$ can be reformulated as matrix equation

$$
\begin{aligned}
& R_{i j}=\left\{\begin{array}{c}
\frac{1}{C\left(p_{j}\right)}, \text { if } p_{j} \rightarrow p_{i} \\
0, \text { otherwise }
\end{array}\right. \\
& \vec{p}=\left(P\left(p_{1}\right), \ldots, P\left(p_{n}\right)\right) \\
& \vec{p}=R \cdot \vec{p}, \quad \overrightarrow{\|p\|_{1}}=\sum_{i=1}^{n} p_{i}=1
\end{aligned}
$$

The vector of page relevance values is an Eigenvector of the matrix $R$

In order to determine the solution to the recursive formulation of the probabilities of a random walker to visit a page, we introduce a transition probability matrix $R$, which captures the probability of transitioning from one page to another. We also require that the long-term probabilities of visiting a page add up to 1 . With this representation the long-term visiting probabilities become the Eigenvector of matrix R. More precisely, they are the Eigenvector with the largest Eigenvalue.

## Source of Rank: Teleporting

## Assumption

- random walker jumps with probability 1-q to an arbitrary node
- thus it can leave dead ends and nodes without incoming links are reached


## PageRank method

To avoid the previously described problem, we add a "source of rank". The idea is that a random walker in each step can, rather than following a link, jump to any page with probability $1-\mathrm{q}$. Therefore the random walker can leave pages that have no outgoing links and also pages without incoming links can be reached by the random walk and give weight to other pages. In the mathematical formulation of the random walk this is resulting in an additional a term for the source of rank. Since at each step the random walker makes a jump with probability $1-q$ and any of the $N$ pages is reached with the same probability the additional term is $(1-q) / N$. Reformulating this again as matrix equation requires adding a NxN Matrix E with all entries being $1 / \mathrm{N}$. This is equivalent to saying that with probability $1 / \mathrm{N}$ transitions among any pairs of nodes (including transition from a node to itself) are performed. Since the vector $p$ has norm 1, i.e., the sum of the components is exactly 1 , E.p=e, where $e$ is the unit vector, the matrix equation can be reformulated in the second form shown below. The method described is called PageRank and is used by Google. By modifying the values of the matrix $E$ also a priori knowledge about the relative importance of pages can be added to the algorithm.

## Practical Computation of PageRank

Iterative computation $\quad \vec{p}_{0} \leftarrow \vec{s}$

$$
\begin{aligned}
& \text { while } \delta>\varepsilon \\
& \qquad \vec{p}_{i+1} \leftarrow q R \bullet \vec{p}_{i} \\
& \vec{p}_{i+1} \leftarrow \vec{p}_{i+1}+\frac{(1-q)}{N} \vec{e} \\
& \delta \leftarrow\left\|\vec{p}_{i+1}-\vec{p}_{i}\right\|_{1}
\end{aligned}
$$

$\varepsilon$ termination criterion

s arbitrary start vector, e.g. $s=e$

For the practical computation of the PageRank ranking an iterative approach can be used. It is derived from the second form of the formulation of the visiting probabilities of the random walker that we have given. The vector e used to add a source of rank has not necessarily to assign uniform weights to all pages, but might reflect itself a ranking of Web pages.

## Web Search

PageRank is part of the ranking method used by Google

- Compute the global PageRank for all Web pages
- Given a keyword-based query retrieve a ranked set of documents using
standard text retrieval methods
- Merge the ranking with the result of PageRank to both achieve high
precision (text retrieval) and high quality (PageRank)
- Google uses also many other methods to improve ranking
Technical challenges
- Crawling the Web
- Efficient computation of Page Rank for large link databases
- Combination with other ranking methods (text)

PageRank is used as one metrics to rank result documents in Google. Essentially Google uses text retrieval methods to retrieve relevant documents and then applies PageRank to create a more appropriate ranking. Google uses also many other methods to improve ranking, e.g., by giving different weights to different parts of Web documents and user relevance feedbacks. For example, title elements are given higher weight. The details of the ranking methods are trade secrets of the Web search engine providers.

Other issues that Web search engines have to deal with, are crawling the Web, which requires techniques that can explore the Web without revisiting pages too frequently. Also the enormous size of the document and link database poses implementation challenges in order to keep the ranking computations scalable. One of the outcomes of solving these challenges are the recent "cloud computing" infrastructures, which are large-scale computing clusters constructed from commodity hardware.

## LINK-BASED RANKING: HITS

## Hyperlink-Induced Topic Search (HITS)

Key Idea: in response to a query, instead of an ordered list of pages, find two sets of inter-related pages:

- Hub pages are good lists of links on a subject
- e.g., "World top universities"
- Authorative pages are referred recurrently on good hubs on the subject
- e.g., "EPFL"

Best suited for "broad topic" queries rather than for page-finding queries

- Understand common perception of quality

Hub-Authority ranking identifies not only pages that have a high authority, as measured by the number of incoming links, but also pages that have a substantial "referential" value, having many outgoing links (to pages of high importance). Different to the PageRank algorithm this technique has been originally proposed to post-process query results (rather than to rank pages from the complete Web graph). It can be used as a add-on to existing search engines, but as well as an alternative to the PageRank method.

## Hub-Authority Ranking

## Approach

- Hubs are pages that point to many/relevant authorities
- Authorities are pages that are pointed to by many/relevant hubs

In order to realize the idea of distinguish authorities from hubs a simple approach is taken. Hub pages are consider as those that are referred a lot by authority pages and vice versa. The example illustrates of how this would ideally separate authority pages, in the case of universities well known universities, from hub pages, such as university ranking and portal sites.

## Computing Hubs and Authorities

Repeat the following updates, for all $p$

$$
\begin{aligned}
& H\left(p_{i}\right)=\sum_{p_{j} \in N \mid p_{i} \rightarrow p_{j}} A\left(p_{j}\right) \\
& A\left(p_{i}\right)=\sum_{p_{j} \in N \mid p_{j} \rightarrow p_{i}} H\left(p_{j}\right)
\end{aligned}
$$

Normalize values (scaling)

$$
\sum_{p_{j} \in N} A\left(p_{j}\right)^{2}=1 \quad \sum_{p_{j} \in N} H\left(p_{j}\right)^{2}=1
$$

More precisely, the scores are recomputed by simply adding the scores of all incoming edges. For computing authority scores this is the hub scores and for hub scores the authority scores. In order to avoid that the scores grow continuously, they are rescaled to in each step, by normalizing the score vectors to one.

## HITS algorithm

$n:=|N| ;\left(a_{0}, h_{0}\right):=\frac{1}{n^{2}}((1, \ldots, 1),(1, \ldots, 1))$

while $l<k$

$l:=l+1$

$a_{l}:=\left(\sum_{p_{i} \rightarrow p_{1}} h_{l-1, i}, \ldots, \sum_{p_{i} \rightarrow p_{n}} h_{l-1, i}\right)$

$h_{l}:=\left(\sum_{p_{1} \rightarrow p_{i}} a_{l, i}, \ldots, \sum_{p_{n} \rightarrow p_{i}} a_{l, i}\right)$

$\left(a_{l}, h_{l}\right):=\left(\frac{a_{l}}{\left|a_{l}\right|}, \frac{h_{l}}{\left|h_{l}\right|}\right)$

In practice, 5 iterations sufficient to converge!

As for PageRank the Hub/Authority values can be iteratively computed. $\mathrm{x}$ corresponds to the authority weight and $y$ to the hub weight. At each iteration the values are renormalized to length 1.

## Convergence of HITS

We can interpret the iterative algorithm for computing HITS in terms of computing Eigenvectors for the link matrix. If $L$ is the link matrix then the computation of a from $h$ is defined as $a=L h$ and the computation of $h$ from a is defined as $h=L^{t} a$. Therefore $a^{*}$, the authority vector obtained after convergence, is the principal Eigenvector of Matrix $L^{t}$ and $\mathrm{h}^{*}$, the hub vector obtained after convergence, is the principal Eigenvector of matrix $L^{\mathrm{t}} \mathrm{L}$.

Remains the question whether this algorithm always converges. The algorithm is a particular algorithm for computing eigenvectors: the power iteration method. It is proven to converge against the principal Eigenvalue.

## HITS Conclusions

## Potential issues

- Topic Drift: off-topic pages can cause off-topic "authorities" to be returned
- Mutually Reinforcing Affiliates: clusters of affiliated pages/sites can boost each others' scores

Social Network Analysis

- PageRank and HITs are examples of SN Analysis algorithms
- SNs contain a lot of other interesting structure (see later)

Implementation

- How to efficiently obtain the base set?

Similarly as for PageRank, the HITS algorithm is also vulnerable structural anomalies of the link structure, be it caused by conscious manipulation or by chance. Topic drift would imply that the set of base pages refers to a topic that is different from the original intended one, expressed by a search query. For example, if we would search for top European universities, it could well happen that the topic would drift to top US universities, when ranking hubs come into play that strongly refer to those. We could have also clusters of related pages, that in the iterative computation mutually boost each others scores, and thus give too high weight to pages that would not merit it. This problem is similar to the one of link spamming with link farms.

In terms of implementation, link-based ranking algorithms require the capability to efficiently retrieve the link graph for the Web. This problem is addressed by so-called connectivity servers that we will introduce next.

## 11. LINK INDEXING

## Connectivity Server

Support for fast queries on the web graph

- Which URLs point to a given URL?
- Which URLs does a given URL point to?

Stores mappings in memory from

- URL to outlinks, URL to inlinks

Applications

- Link analysis (PageRank, HITS)
- Web crawl control
- Web graph analysis
- Connectivity, crawl optimization

In order to efficiently analyze the Web graph the Web links need to stored in a database, respectively index. A connectivity server is such an index. In essence, it stores for each URL all the URLs that the Web page at the URL is pointing to, and the URLs of other Web pages that point to this URL. Apart from link-based ranking algorithms as described before the applications are manifold.

## Adjacency Lists

The set of URLs a node is pointing to (or pointed to) sorted in lexicographical order

A connectivity server has to store all outgoing (and incoming) links to a web page. For example, the home page of EPFL contains a large set of outgoing links, some of which are shown here. As a first step, the lists of links are sorted in lexicographical order. As a result we obtain the adjacency list, which is similar to the posting list of a document.

## Representation of Adjacency Lists

Assume each URL represented by an integer

- For a 4 billion page web, we need 32 bits per node
- Naively, this demands 64 bits to represent each hyperlink (source and destination node); on average 10 links per page
- For the current Web: $320 \mathrm{~GB}$
- Can we do better (for main memory storage)?

| Node | Outdegree | Successors |
| :--- | :--- | :--- |
| $\cdots$ | $\cdots$ | $\cdots$ |
| 15 | 11 | $13,15,16,17,18,19,23,24,203,315,1034$ |
| 16 | 10 | $15,16,17,22,23,24,315,316,317,3041$ |
| 17 | 0 |  |
| 18 | 5 | $13,15,16,17,50$ |
| $\cdots$ | $\cdots$ | $\cdots$ |

As a first means to optimize the representation of adjacency lists, we represent each URL by one integer, instead of storing its textual form. From this we can estimate that for the current Web, we need $320 \mathrm{~GB}$ to represent all links:

- The current (crawled) Web has about 4 billion pages (http://www.worldwidewebsize.com/)
- It is estimated that a page contains on average 10 links
- We need 32 bits for each URL, which demands 64 bits for the storage of a single link.

Even with large memories this still a significant index size. In the following, we will show how to get this down to approximately $\sim 3$ bits/link which makes the index much more manageable. This will be achieved by systematically compressing the adjacency lists.

## Properties of Adjacency Lists

## Locality (within lists)

- Most links contained in a page have a navigational nature, thus their indices are close in lexicographical order
- E.g. for
- futuretudiant.epfl.ch/en
- futuretudiant.epfl.ch/mobility

Similarity (between lists)

- Either two lists have almost nothing in common, or they share large segments of their successor lists
- Pages that occur close to each other in lexicographic order tend to have similar lists
- E.g. futuretudiant.epfl.ch/en and futuretudiant.epfl.ch/mobility

For compressing adjacency lists we base ourselves on the following observations:

Locality. Most links contained in a page have a navigational nature: they lead the user to some other pages within the same host (as we can see clearly from the example of the EPFL home page). If we compare the source and target URLs of these links, we observe that they share often a long common prefix. Thus, if URLs are sorted lexicographically, the index of source and target are close to each other. Locality is a property of a list, thus addresses intra-list similarity.

Similarity. Pages that occur close to each other (in lexicographic order) tend to have many common successors. This is because many navigational links are the same within the same local cluster of pages, and even non-navigational links are often copied from one page to another within the same host. Similarity is a property concerning different lists, thus addresses inter-list similarity.

## Exploiting Locality

## Use Gap Encoding (as in inverted files)

$-S(x)=\left(s_{1}, \ldots, s_{k}\right)$ will be represented as

$$
\left(s_{1}-x, s_{2}-s_{1}-1, \ldots, s_{k}-s_{k-1}-1\right)
$$

- Use of varying length encoding

Locality can be exploited in a way analogous of how compression of posting lists for text indexing has been performed. Instead of storing the absolute values of the URL identifiers, differences are stored. In other words, we perform gap encoding. The resulting differences are then encoded using a varying length compression scheme, such as gamma coding.

## Exploiting Similarity

## Copy data from similar lists

- Reference list: reference to another list
- Searched in a neighboring window of nodes
- Copy list: indicate which node is copied from reference list
- Extra nodes: additional nodes not in reference list

| Node | Outdegree | Successors | Node | Outd. | Ref. | Copy list | Extra nodes |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ |
| 15 | 11 | $3,1,0,0,0,0,3,0,178,111,718$ | 15 | 11 | 0 |  | $13,15,16,17,18,19,23,24,203,315,1034$ |
| 16 | 10 | $\\| 1,0,0,4,0,0,290,0,0,2723$ | 16 | 10 | 1 | 01110011010 | $22,316,317,3041$ |
| 17 | $\mathbf{0}$ |  | 17 | 0 |  |  |  |
| 18 | 5 | $9,1,0,0,32$ | 18 | 5 | 3 | 11110000000 | 50 |
| $\ldots$ | $\cdots$ | $\cdots$ | $\cdots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ |

## Result: about 3 bytes / link (with some further compression)

For exploiting similarity we apply a similar idea as gap encoding, but now applied to the differences among different adjacency lists. If we consider a reference list (in the example the list of Node 15), subsequent adjacency lists can story a bitlist that indicates which nodes of the reference lists are retained in the subsequent adjacency list, and which are not. 0 indicates that the node in the reference lists is not retained, and 1 indicates that it is retained. Since the subsequent adjacency list can also contain other nodes, that are not stored in the reference list, those extra nodes are stored explicitly.

Candidates for potential reference lists are searched among neighboring lists using a window of predefined size. The choice of the window size is critical, as larger windows increase chances of finding good candidates, but also increase the cost of compression

Together with some further compression applied to the copy lists and the extra nodes, this index compression achieves about 3 Bytes/link cost in the representation of the Web graph.

