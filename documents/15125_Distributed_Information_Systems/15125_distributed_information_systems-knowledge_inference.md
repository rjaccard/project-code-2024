# Knowledge Inference 

##  Link prediction

Knowledge inference concerns a wide number of problems that have been studied in many different contexts. Some of the basic examples are:

Entity linking and disambiguation, which concerns the problem of identifying which entity names represent the same real-world entity, respective which entity is referred to in case of ambiguous entity names.

Schema integration, which concerns the problem which classes, attributes and relationships in one knowledge bases correspond to which in another one.

Collective classification, which concerns the problem of learning unknown attribute values from the available knowledge in a knowledge base.

Link prediction, which concerns the problem of learning unknown relationships from the available knowledge in a knowledge base.

## 1. ENTITY DISAMBIGUATION

Task: Link a text mention in a document to an entry in a knowledge base (e.g. WikiPedia or WikiData)

- Also called entity resolution and linking


## Challenge

Two problems

- Homonyms: entities with the same name
- Synonyms: different names for the same entity

Entity disambiguation can however be quite challenging to the homonymy and synonymy problem. Handling these problems is essential for every text analytics tasks. Not being able to handle homonymy usually results in the introduction of noise into the results (poor precision) whereas not properly handling synonymy risks to miss relevant documents (poor recall).

## Sources of Information

For performing entity disambiguation one can exploit two different sources of information. On the one hand local information extracted from the text mention, or its vicinity, can be exploited. This can be used to compare the text mention and its features with the representation in the knowledge base, in order to obtain evidence which entitities in the knowledge base are potentially matched. A second source of information is the knowledge base itself, when multiple entities are mentioned in the same text. Since these entities from the same text are likely to be in some form of relationship among each other, it is likely that such relationships are also discovered in the knowledge base. This can help in entity disambiguation.

## Entity Graph

Here we illustrate the basic model of how a knowledge base can be employed for entity disambiguation:

- $m$ are text mentions of entities (extracted using NER)
- For each mention there are candidates in $\mathrm{KB}$; these can be identified using local information from the text mention
- Each is a graph node; we can also associate a similarity measure to each node
- Edges between mention-candidate pairs are included if a link exists in the $\mathrm{KB}$ among the respective candidates

Since the same text mention can relate to several candidates, the problem of entity disambiguation is to determine which among the multiple candidates is the most likely to be correct.

To perform entity disambiguation, we pose the following question: given a node s in the entity graph, how well does it support the presence of another node e in the graph?

This question is actually related to a question that has been investigated in the context of personalized Web search: given a URL from the personal bookmark list of a user, how relevant is a page in the Web for this user. To answer this question a variation of the PageRank algorithm, which determines general relevance, has been proposed. It is called Personalized PageRank.

## Personalized PageRank

Same as PageRank, except that random jumps are always back to the same node (or same set of nodes)

- Original motivation: use personal bookmark list as source of rank

$$
\begin{aligned}
& \vec{p}=c(q R \cdot \vec{p}+(1-q) \vec{e}) \\
& \vec{e}=(1,0,0, \ldots, 0)
\end{aligned}
$$

Can be computed using Monte Carlo method

- Perform multiple independent random walks
- Compute distribution of end points of random walks

Personalized PageRank works almost the same as the original PageRank. The difference is that random jumps are not performed uniformly random to any other node of the graph, but to a selected subset of nodes. In the case of Web search this subset would be the personal bookmark list, and by jumping back to this subset nodes from that list will have a large influence on the ranking of a page, such that nodes that are well connected to the bookmarks will receive more ranking value.

PPR can be computed either like standard PageRank, or using a Monte Carlo method, by starting random walks independently and aggregate the distribution of the end points of those walks.

## Approach

Finding the concept candidate linked to a mention $m$ that is most likely to be valid

1. For all concept candidates $c$ compute total support received from other nodes

$$
\begin{aligned}
& e=(c, m), s=\left(c^{\prime}, m^{\prime}\right) \\
& \text { score }_{e}=\sum_{s \in \text { Contributors }_{e}} \operatorname{PPR}_{s}(e)
\end{aligned}
$$

## 1. Select the candidate with highest score

The procedure for selecting the best concept candidate for a text mention is straightforward. One computes the total support that the candidate receives from other nodes $\mathrm{s}$, by computing the PPR of e with the source node s a selected node. Which source nodes $s$ are contributing to this computation we need still to determine. At the end the candidate with the highest score is selected.

## Contributing Nodes

Only one interpretation $c$ for a mention $m$ is valid

- Competing nodes $s=\left(c^{\prime}, m\right)$ that have the same entity mention as $e=(c, m)$ cannot support $e$
- For multiple nodes $s$ that have the same entity mention $m$, only the one with highest contribution is considered

Thus

Contributors $_{e}=\left\{\left(m^{\prime}, \underset{c}{\operatorname{argmax}} P P R_{\left(m^{\prime}, c\right)}(e), m^{\prime} \neq m\right)\right\}$

Not every node should contribute as source node for a mention $\mathrm{m}$, if we assume that only one interpretation can be correct. First, we exclude nodes that are "competing" for the interpretation of the text mention. Second for multiple nodes related to the some other entity mention, we select only the contribution of the one that has the highest value. In this way we favor a unique interpretation for mentions.

## Considering Popularity

The method can furthermore consider popularity measures for nodes

- If information is insufficient, favor popular nodes

$$
\begin{aligned}
& \text { coherence }_{S}(e)=P P R_{S}(e) \text { popularity }(s) \\
& \operatorname{coherence}(e)=\sum_{s \in \text { Contributors }_{e}} \text { coherence }_{s}(e) \\
& \operatorname{score}(e)=\operatorname{coherence}(e)+P P R_{\text {avg }} \text { popularity }(e)
\end{aligned}
$$

To further improve the method, one can add a general popularity measure to weight the contributions of source nodes. This will favor popular nodes, which is beneficial if little information is available for disambiguation. Then it is better to choose a popular candidate since chances that this is correct are higher. One of possible choice of a popularity score could be the number of links a node has in the knowledge base.

## 2. LABEL PROPAGATION

## Inferring Attributes

A second inference task in knowledge bases, after entities have been disambiguated, is to assign to the entities correct attribute values. For discrete attributes this problem an be understood as a classification problem. This question has, for example, been studied for classifying users in a social network with respect to their stance or emotion towards a specific topic.

In the case of emotion analysis there exists typically indications of emotions, e.g., in the form of the use of emoticons or specific hashtags. However, only few users are using those.

## Propagating Attribute Values

In many cases nodes that are connected by edges in a knowledge graph or as well in a social network, share properties. In social networks this is quite apparent. People that are connected through social links (e..g follower, friend, retweet, reply etc) are in general more likely to share opinions than those that are not. Is it possible to exploit this property to predict the attributes (respectively class lables) for those users that have none?

## Model

Graph $G=(V, E)$ with vertices $V$ and Edges $E$

- Vertices $V$ have a label from a set $L \cup\{$ unknown $\}$ of size $n+1$
- Edges are undirected and unweighted

Probability distributions for vertices

- $\boldsymbol{l}_{\text {apriori }}(v)$ is a vector of size $n+1$

assigns weight 1 for label if known for $v \in V$

- $\boldsymbol{l}_{\text {inferred }}(v)$ is a vector of size $n+1$

assigns a probability distribution to vertices

- $\boldsymbol{l}_{\text {unknown }}$ is a vector of size $n+1$ assigns weight 1 for label unknown

We consider the following model. A graph with vertices that can have either a label from a set $L$, or a lable unknown. The edges are all undirected and unweighted. The model and approach can be extended for directed graphs with weighted edges.

We associate with vertices probability distributions that represent our knowledge about the assignment of a label. For some vertices we have an apriori assignment of labels (these are the vertices for which the label is known). For all vertices we will compute an inferred probability distribution. For vertices that have no apriori label assigned we have a vector to represent the unknown state.

Note that the aprioir distribution can also be a true probability distribution, if we are initially not sure about the label, but have some knowledge.

## Label Inference

We assume that all neighbors excert the same influence on a node

Thus we would require that

$$
\boldsymbol{l}_{\text {inferred }}(v)=\frac{1}{\operatorname{deg}(v)} \sum_{(v, w) \in E} \boldsymbol{l}_{\text {inferred }}(w)
$$

In this model we assume that all neighbors of a node in the graph are equally influencing it. Thus, we can compute its expected label distribution by averaging the distributions of the neighbors. The resulting equation is analogous to the formulation of the PageRank model. Thus the Label Inference can be interpreted as a random walk model.

The model can be extended to weighted graphs, in which case the edge weight would be considered in the aggregation of the distributions of the neighboring vertices.

## Label Propagation Algorithm

$\boldsymbol{l}_{\text {inferred }}(v)=\boldsymbol{l}_{\text {apriori }}(v)$ for nodes with known labels, otherwise $\boldsymbol{l}_{\text {unknown }}$ while not converged

$$
\begin{aligned}
& \boldsymbol{l}_{\text {inferred }}(v)=\frac{1}{\operatorname{deg}(v)} \sum_{(v, w) \in E} \boldsymbol{l}_{\text {inferred }}(w) \\
& \boldsymbol{l}_{\text {inferred }}(v)=p_{v}^{\text {inj }} \boldsymbol{l}_{\text {apriori }}(v)+\quad / / \text { inject apriori knowledge } \\
& p_{v}^{\text {continue }} \boldsymbol{l}_{\text {inferred }}(v)+/ / \text { infer from neighbors } \\
& p_{v}^{\text {abandon }} \boldsymbol{l}_{\text {unknown }} \quad / / \text { stop }
\end{aligned}
$$

The probabilities $p_{v}^{\text {inj }}, p_{v}^{\text {continue }}$ and $p_{v}^{\text {abandon }}$ can be interpreted as decisions in a random walk

The full label propagation model adds additional aspects to the propagation of labels to neighbors.

- For vertices with apriori labels, at every step the apriori distribution is injected with a certain probability $p_{v}^{\text {inj }}$ that depends on the vertice
- For all vertices the propogation process can also be abandoned with a certain probability $p_{v}^{\text {abandon }}$
- The propagation of the label distribution to neighbors occurs then with a (remaining) probability of $p_{v}^{\text {continue }}$

As in PageRank the process is iterated till convergence occurs.

## Determining the Probabilities

Entropy of transition probabilities $H(v)=-\log \frac{1}{\operatorname{deg}(v)}$

$$
\begin{aligned}
& c_{v}=\frac{\log 2}{\log (2+\operatorname{deg}(v))} \\
& d_{v}=\left(1-c_{v}\right) \sqrt{H(v)} \text { if } v \text { is labelled, } 0 \text { otherwise } \\
& z_{v}=\max \left(c_{v}+d_{v}, 1\right)
\end{aligned}
$$

$p_{v}^{\text {cont }}=\frac{c_{v}}{z_{v}}, \quad p_{v}^{\text {inj }}=\frac{d_{v}}{z_{v}}$ for labelled nodes, 0 otherwise $p_{v}^{\text {abandon }}=1-p_{v}^{\text {cont }}-p_{v}^{\text {inj }}$

The transition probabilities depend on the properties of the vertices. In our model, the only relevant property is its degree.

In a more general model with edge weights the probabilities would depend on the distribution of edge weights of the edges connected to the vertice (Fan-out entropy heuristics)

## Behavior of Probabilities: Labelled Nodes

- Injection probability increases with the degree of the nodes, while continuation probability decreases
- Abandoning probability positive for only very low degree nodes $(d=1,2)$

For labelled nodes the injection probability increases with the degree. Thus, well connected pre-labelled nodes have a lot of influence.

## Behavior of Probabilities: Unlabelled Nodes

- Abandon probability increases with degree
- Prevents algorithm from propogating information through unlabeled, high-degree nodes

For unlabeled nodes the behavior the abandon probability increases with the degree. Thus, high degree nodes have less influence.

## 3. LINK PREDICTION

## Knowledge Base Completion

In general, knowledge bases are incomplete. Thus there is a significant interest in completing in particular the relationships among entities. To do so one might exploit "patterns" that entities and relationships follow, and generalize them.

## Observation on Word Embeddings

In order to tackle this problem, we come back to an observation that we had made for word embeddings. We found that (in some cases) relationships seem to be encoded as linear transformations.

## Relations in Word Embeddings 

Idea: Find a vector

$v_{\text {is_capital_of }}$ such that $\boldsymbol{v}_{\text {Tokyo }}+\boldsymbol{v}_{\text {is_capital_of }}-\boldsymbol{v}_{\text {Japan }} \approx \mathbf{0}$

$\boldsymbol{v}_{\text {Berlin }}+\boldsymbol{v}_{\text {is_capital_of }}-\boldsymbol{v}_{\text {Germany }} \approx \mathbf{0}$

$\boldsymbol{v}_{\text {Rome }}+\boldsymbol{v}_{\text {is_capital_of }}-\boldsymbol{v}_{\text {Italy }} \approx \mathbf{0}$

$\boldsymbol{v}_{\text {Lisbon }}+\boldsymbol{v}_{\text {is_capital_of }}-\boldsymbol{v}_{\text {Portugal }} \approx \mathbf{0}$

This observation can be formally described in two different ways. We could say, that the differences of entity vectors that are in a relationship should result in similar values. Alternatively, we sould also say, that there must be some vector that represents the relationship and that the sum of this vector with the difference vector of the entities should be approximately zero. This second formulation of the properties gives rise to an idea of how link prediction could be performed using and embedding technique.

## Model

Knowledge graph $G$ consists of (correct) triples $(h, r, t)$ where $h, t \in E$ and $r \in R$

Define a plausibility score $\mathrm{f}(h, r, t)$

$$
\mathrm{f}(h, r, t)>\mathrm{f}\left(h^{\prime}, r^{\prime}, t^{\prime}\right)
$$

If $(h, r, t)$ is a plausible triple and $\left(h^{\prime}, r^{\prime}, t^{\prime}\right)$ is a implausible triple

To formulate the model we assume that we have a knowledge graph consisting of triples $(h, r, t)$. $h$ indicates the term "head" and $t$ the term "tail".

Then we introduce a function that measure how plausible a triple is (we can think of it as a probability). Clearly, the function should return higher values for plausible tuples than for implausible ones.

## Learning the Model

Minimize the loss function

$$
J(\theta)=\sum_{\substack{(h, r, t) \in G \\\left(h^{\prime}, r^{\prime}, t^{\prime}\right) \in G^{\prime}(h, r, t)}} \max \left(0, \gamma+\mathrm{f}(h, r, t)-\mathrm{f}\left(h^{\prime}, r^{\prime}, t^{\prime}\right)\right)
$$

where $G^{\prime}(h, r, t)$ is a set of incorrect triples, generated by corrupting the correct triple $(h, r, t)$

$\gamma$ is a hyperparameter

Using the plausibility function, we can formulate a loss function that should be minimized. The minimization will be performed as usual using $S G D$.

## TransE Model

One of the first emedding-based models for knowledge base completion

- Based on the intuition from text WE

$$
\mathrm{f}(h, r, t)=\left\|\boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\boldsymbol{v}_{t}\right\|_{1 / 2}
$$

Each entity and relationship is mapped to a lowdimensional vector, resulting in $\boldsymbol{v}_{h}, \boldsymbol{v}_{r}, \boldsymbol{v}_{t}$

With the generic model we can instantiate difference concrete approaches for link prediction, depending on the choice of f. One of the initial approaches that was strongly inspired by our initial observation on word embeddings from the beginning. It directly introduces a vector $\boldsymbol{v}_{r}$ that represents the linear transformation corresponding to a relationship, and mapping the head and tail into the same (low-dimensional) vector space.

The mappings from the entities and relationships to the latent space are performed (as in word embeddings) using embedding matrices, which constitute the model parameters that have to be learnt using $S G D$.

## Performing SGD

Initialize vectors with random values

- From interval $\left[-\frac{6}{\sqrt{k}}, \frac{6}{\sqrt{k}}\right]$ where $k$ is the embedding dimension
- In each iteration
- Sample a correct triple or batch
- Derive a corrupt triple from the correct one: replace $h$ or $t$ by a random entity
- Update embeddings by minimizing loss function
- Normalize all entity vectors to 1 (not relationship vectors!)

The SGD algorithm proceeds as follows. First the vectors are initialized with random values (the choice is motivated by empirical findings from neural network training). Then in every iteration a triple (or several triples are randomly chosen). Negative samples are generated by randomly replacing head or tail (not both). The update of the embeddings is performed as usual by computing the differential of the loss function. Entity vectors are normalized to 1 in every iteration (this avoids the model to find a trivial solution).

## Alternative Models

| Model | Score function $f(h, r, t)$ | Opt. |
| :---: | :---: | :---: |
| Unstructured | $\left\\|\boldsymbol{v}_{h}-\boldsymbol{v}_{t}\right\\|_{l_{1 / 2}}$ | SGD |
| SE | $\\| \mathbf{W}_{r, 1} \boldsymbol{v}_{h}-\mathbf{W}_{r, 2} \boldsymbol{v}_{t} \ell_{\ell_{12}} ; \mathbf{W}_{r, 1} \cdot \mathbf{W}_{r, 2} \in \mathbb{R}^{k \times k}$ | SGD |
| SME | $\left(\mathbf{W}_{1,1} \boldsymbol{v}_{h}+\mathbf{W}_{1,2} \boldsymbol{v}_{r}+\mathbf{b}_{1}\right)^{\top}\left(\mathbf{W}_{2,1} \boldsymbol{v}_{t}+\mathbf{W}_{2,2} \boldsymbol{v}_{r}+\mathbf{b}_{2}\right)$ <br> $\mathbf{b}_{1}, \mathbf{b}_{2} \in \mathbb{R}^{n} ; \mathbf{W}_{1,1}, \mathbf{W}_{1,2}, \mathbf{W}_{2,1} \cdot \mathbf{W}_{2,2} \in \mathbb{R}^{n \times k}$ | SGD |
| TransE | $\left\\|\boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\boldsymbol{v}_{t}\right\\| \epsilon_{1 / 2} ; \boldsymbol{v}_{r} \in \mathbb{R}^{k}$ | SGD |
| TransH | $\left\\|\left(\mathbf{I}-\boldsymbol{r}_{p} \boldsymbol{r}_{p}^{\top}\right) \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\left(\mathbf{I}-\boldsymbol{r}_{p} \boldsymbol{r}_{p}^{\top}\right) \boldsymbol{v}_{t}\right\\|_{\epsilon_{1 / 2}}$ <br> $\boldsymbol{r}_{p}, \boldsymbol{v}_{r} \in \mathbb{R}^{k} ; \mathbf{I}$ Identity matrix size $k \times k$ | SGD |
| TransR | $\left\\|\mathbf{W}_{r} \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\mathbf{W}_{r} \boldsymbol{v}_{t}\right\\|_{l_{1 / 2}}: \mathbf{W}_{r} \in \mathbb{R}^{n \times k} ; \boldsymbol{v}_{r} \in \mathbb{R}^{n}$ | SGD |
| TransD | $\left\\|\left(\mathbf{I}+\boldsymbol{r}_{p} \boldsymbol{h}_{p}^{\top}\right) \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\left(\mathbf{I}+\boldsymbol{r}_{p} t_{p}^{\top}\right) \boldsymbol{v}_{t}\right\\|_{\ell_{1 / 2}}$ <br> $\boldsymbol{r}_{p}, \boldsymbol{v}_{r} \in \mathbb{R}^{n} ; \boldsymbol{h}_{p}, \boldsymbol{t}_{p} \in \mathbb{R}^{k} ; \mathbf{I}$ : Identity matrix size $n \times k$ | AdaDelta |
| IppTransD | $\left\\|\left(\mathbf{I}+\boldsymbol{r}_{p, 1} \boldsymbol{h}_{p}^{\top}\right) \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\left(\mathbf{I}+\boldsymbol{r}_{p, 2} \boldsymbol{t}_{p}^{\top}\right) \boldsymbol{v}_{\\|}\right\\|_{\ell_{1 / 2}}$ <br> $\boldsymbol{r}_{p, 1}, \boldsymbol{r}_{p, 2}, \boldsymbol{v}_{r} \in \mathbb{R}^{n} ; \boldsymbol{h}_{p,}, \boldsymbol{t}_{p} \in \mathbb{R}^{k} ; \mathbf{I}$ : Identity matrix size $n \times k$ | SGD |
| STransE | $\left\\|\mathbf{W}_{r, 1} \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\mathbf{W}_{r, 2} \boldsymbol{v}_{t}\right\\|_{\varepsilon_{1 / 2}} ; \mathbf{W}_{r, 1}, \mathbf{W}_{r, 2} \in \mathbb{R}^{k \times k} ; \boldsymbol{v}_{r} \in \mathbb{R}^{k}$ | SGD |
| TranSparse | $\left\\|\mathbf{W}_{r}^{h}\left(\theta_{r}^{h}\right) \boldsymbol{v}_{h}+\boldsymbol{v}_{r}-\mathbf{W}_{r}^{t}\left(\theta_{r}^{t}\right) \boldsymbol{v}_{t}\right\\| \\|_{1 / 2} ; \mathbf{W}_{r}^{h}, \mathbf{W}_{r}^{t} \in \mathbb{R}^{n \times k} ; \theta_{r}^{h}, \theta_{r}^{t} \in \mathbb{R} ; \boldsymbol{v}_{r} \in \mathbb{R}^{n}$ | SGD |
| DISTMULT | $\boldsymbol{v}_{h}^{\top} \mathbf{W}_{r} \boldsymbol{v}_{t} ; \mathbf{W}_{r}$ is a diagonal matrix $\in \mathbb{R}^{k \times k}$ | AdaGrad |
| NTN | $\boldsymbol{v}_{r}^{\top} \tanh \left(\boldsymbol{v}_{h}^{\top} \mathbf{M}_{r} \boldsymbol{v}_{t}+\mathbf{W}_{r, 1} \boldsymbol{v}_{h}+\mathbf{W}_{r, 2} \boldsymbol{v}_{t}+\mathbf{b}_{r}\right)$ <br> $\boldsymbol{v}_{r}, \mathbf{b}_{r} \in \mathbb{R}^{n} ; \mathbf{M}_{r} \in \mathbb{R}^{k \times k \times k n} ; \mathbf{W}_{r, 1}, \mathbf{W}_{r, 2} \in \mathbb{R}^{n \times k}$ | L-BFGS |
| HolE | sigmoid $\left(\boldsymbol{v}_{r}^{\top}\left(\boldsymbol{v}_{h} \circ \boldsymbol{v}_{t}\right)\right): \boldsymbol{v}_{r} \in \mathbb{R}^{k}, \circ$ denotes circular correlation | AdaGrad |
| Bilinear-comp | $\boldsymbol{v}_{h}^{\top} \mathbf{W}_{r_{1}} \mathbf{W}_{r_{2}} \ldots \mathbf{W}_{r_{m}} \boldsymbol{v}_{t} ; \mathbf{W}_{r_{1}}, \mathbf{W}_{r_{2}}, \ldots, \mathbf{W}_{r_{r}} \in \mathbb{R}^{k \times k}$ | AdaGrad |
| TransE-comp | $\left\\|\boldsymbol{v}_{\mathrm{h}}+\boldsymbol{v}_{r_{1}}+\boldsymbol{v}_{r_{2}}+\ldots+\boldsymbol{v}_{r_{m}}-\boldsymbol{v}_{t}\right\\|_{\ell_{1 / 2}} ; \boldsymbol{v}_{r_{1}}, \boldsymbol{v}_{r_{2}}, \ldots, \boldsymbol{v}_{r_{m}} \in \mathbb{R}^{k}$ | AdaGrad |
| ConvE | $\boldsymbol{v}_{t}^{\top} g\left(\operatorname{vec}\left(g\left(\operatorname{concat}\left(\overline{\boldsymbol{v}}_{h}, \overline{\boldsymbol{v}}_{r}\right) * \boldsymbol{\Omega}\right)\right) \boldsymbol{W}\right) ; g$ denotes a non-linear function | Adam |
| ConvKB | $\mathbf{w}^{\top}$ concat $\left(g\left(\left[\boldsymbol{v}_{h}, \boldsymbol{v}_{r}, \boldsymbol{v}_{t}\right] * \boldsymbol{\Omega}\right)\right) ; *$ denotes a convolution operator | Adam |

The TransE method is only one example of very many methods that have been in the meanwhile proposed to tackle the link prediction problem.

## 4. DATA INTEGRATION

## Key Tasks in Distributed Information Management

This figure illustrates the problem of information starvation: there exist many information systems supplying data, but each having their own view on the world, which does not necessarily match the needs or understanding of a specific consumer. Every information system is interpreting its model differently with respect to the real world and relating to different views on the real world. Though there exists some relationships among all these views on the real world (let's denote it as $R$ ), and it surely implies some relationship R' among the different models used in the different information systems, the consumers of the information cannot easily understand the relationship $R$, and thus can also not easily relate their models to the models of others via the relationship R'. From the viewpoint of the data providers, introducing $R^{\prime}$ ' introduces a new interpretation of their data with respect to the model used by the data consumer.

## Schema Matching

Integration of heterogeneous data sources

- Every project on Big Data analysis first has to integrate data from different, heterogeneous data sources
- Different schemas, taxonomies, knowledge graphs
- One of the long-standing open problems in data management How to find good "matches"?

Schema matching is a long standindg problem, both in industry and research.

## Schema Matching Approaches

## Manual matching

- still common practice today


## Schema matching tools

- Based on structural and content features
- names, domains, structure, values, ...
- Establish correspondences and rank according to quality
- Errors are frequent and unavoidable
- Works well for small schemas


## Schema Matching Tools

The Problem: Given two (hierarchical) knowledge graphs D1, D2, a 1:1 matching of nodes (entities, classes) that have the same or similar "meaning"

Assumption: two nodes (classes) are considered similar, if they have the same or similar instances (entities)

In the following we will study the problem of integrating heterogeneous databases respectively knowledge graphs. We assume that we want to integrate data that are available in two knowledge graphs that are semantically related to each other.

We will make a few assumptions:

- the knowledge graph is hierarchical. It could also be a taxonomy.
- Some entities represent classes. We are in particular interested in matching those.
- Entities that represent classes share similar kinds of instances, which are entities.


## Universe of a Database

Universe $U$ is a finite set of possible instances

Example:

$\mathrm{U}=\{\mathrm{u}$, computer science, mathematics, life sciences, $A$, c1, c2, c3, information systems, aberer, signal processing, vetterli, databases, ailamaki, ...\}

![](https://cdn.mathpix.com/cropped/2024_05_18_ea14c8ea5227f48e463fg-43.jpg?height=371&width=629&top_left_y=796&top_left_x=1114)

One basic approach to assess whether two classes are similar, is to measure their level of similarity at the content level, i.e., to test to which extent the elements (=instances) of the two classes overlap.

## Similarity of Classes

A, B are classes, classes are subsets of $U$

Similarity measure (Jaccard similarity)

$$
\begin{aligned}
& \operatorname{sim}(A, B)=\frac{|A \cap B|}{|A \cup B|}=\frac{P(x \in A \text { and } x \in B)}{P(x \in A \text { or } x \in B)}=\frac{P(A, B)}{P(A, B)+P(\bar{A}, B)+P(A, \bar{B})} \\
& \text { where } P(A, B)=P(x \in A \text { and } x \in B) \text { and } \\
& P(A, \bar{B})=P(x \in A \text { and } x \notin B) \text { etc }
\end{aligned}
$$

The Jaccard measure is a standard approach to measure such a set similarity.

## Complex Features of Classes

Considering the instances (direct children) of classes is only an example of a simple class feature

Many complex features can be exploited (and have been exploited in schema matching)

- Names of attributes and relationships
- Structural relationships (data types)
- Distributional features (data values)
- Content features (e.g., text)

In database integration, many different features that can be associated with structural elements of a database have been considered for establishing semantic correspondences. For illustration, we will use in the following a simple feature: the set of atomic data values (strings) that can be reached from a node in the knowledge graph.

## Content Feature of Classes

We consider as content feature, the set of terms associated with the paths of an node $i$ to the leaves

$$
T_{i}=\left\{t_{1}, \ldots, t_{n}\right\} \text { with repeated occurrences (bag of words) }
$$

$$
\begin{aligned}
& -T_{A}=\{\text { aberer, } \\
& \text { information systems, signal processing, vetterli, ... }\}
\end{aligned}
$$

$-T_{c 1}=\{$ aberer, information systems $\}$

## Finding Corresponding Classes

If U1 and U2 are the universes of DB1 and DB2 we may assume

$$
U 1 \cap U 2=\varnothing
$$

Thus no way to compute $P(A, B)$ directly!

Given $i \in A$, the question is whether it would be likely that considering its features also $i \in B$, even if $i$ is not part of U2

Even if we have identified features that can help to spot correspondences between structurally different, but semantically equivalent elements of two databases, it might be the case that the coverage of a real-world aspect in two databases is different (e.g. courses in two different universities). Thus, directly comparing the features (e.g. the instances of a class) does not help to detect the correspondences.

## Probabilistic Approach

We want to construct a function the gives the probability for a given instance $i$ with feature $T_{i}$ to belong to a class $A$

$P\left(A \mid T_{i}\right)=P\left(T_{i} \mid A\right) P(A) P(d) \propto P\left(T_{i} \mid A\right) P(A)$ (Bayes law)

$P\left(A \mid T_{i}\right)$ is a Naïve Bayes classifier to determine whether $\mathrm{i}$ belongs to $\mathrm{A}$

Objective: determine $P\left(T_{i} \mid A\right)$ and $P(A)$

To tackle the problem, we will construct a model that determines (probabilistically) whether a given data instance with certain features is semantically related to a class.

## Naïve Bayes Classifier

We know $P(A)=\frac{|A|}{\left|U_{1}\right|}$

Independence assumption: $P\left(T_{i} \mid A\right)=P\left(t_{1} \mid A\right) \ldots P\left(t_{n} \mid A\right)$

With $T_{A}$ being the bag of all terms occurring in all instances of $A$ we have

$$
P(t \mid A)=\frac{\left|t \in T_{A}\right|}{\sum_{t},\left|t^{\prime} \in T_{A}\right|}
$$

Computing $\mathrm{P}(\mathrm{A})$ is straightforward. We have just to determine the relative frequency of instances of $A$ (how big $A$ is) in the set of all possible instances.

For computing $\mathrm{P}(\mathrm{Ti} \mid \mathrm{A})$ we first make an independence assumption: we assume that different terms occurring in the instance $i$ of a class $A$ are independent of each other. In practice this is not the case, but is a generally accepted assumption for simplicity. Then we have to compute the probability of a single term $t$ in class $A$ to occur.

By computing $\mathrm{P}(\mathrm{A})$ and $\mathrm{P}(\mathrm{Ti} \mid \mathrm{A}$ ) we obtain (up to a constant) the probability of for a (new) instance I to belong to class A.

## Example

Classifier for class $A=\{c 1, c 2, c 3\}$

$T_{A}=\{$ information systems, aberer, signal processing,... $\}$

New instance cn: $T_{c n}=\{$ information systems, vetterli $\}$

$P($ vetterl $i \mid A)=\frac{1}{6}, P($ vetterli $\mid U)=\frac{1}{9}$

$P\left(T_{c n} \mid A\right)=\frac{1}{36}, P\left(T_{c n} \mid U\right)=\frac{1}{81}$

$P(A)=\frac{3}{13}, P(U)=\frac{4}{13}$ (13 instances total)

$P\left(A \mid T_{c n}\right) \propto \frac{1}{36} \frac{3}{13}, P\left(U \mid T_{c n}\right) \propto \frac{1}{81} \frac{4}{13}$

Thus instance $c n$ is considered to correspond more likely to $A$ than to $U$

We show here a complete example of how for a new instance cn, the most likely corresponding class can be determined in the database. The Naïve Bayes classifier assigns a higher probability for $c n$ to belong to $\mathrm{A}$ than to $\mathrm{U}$ (which coincides with our intuition).

## Computing Similarity between Classes A and B

1. Take all instances of $U 1$ and train a classifier to decide whether an instance belongs to $A$ or not
2. Select all instances in $U 2$ belonging to $\mathrm{B}: U 2^{B}$
3. Apply the classifier trained with $U 1$ to all instances in $U 2^{B}$ to produce set $U 2^{A B}$
4. Do the same with roles of $A$ and $B$ exchanged
5. Compute $P(A, B)=\frac{\left|U 1^{A B}\right|+\left|U 2^{A B}\right|}{|U 1|+|U 2|}$
6. Compute similarly $P(A, \bar{B})$ etc
7. Then compute $\operatorname{sim}(A, B)=\frac{P(A, B)}{(P(A, B)+P(\bar{A}, B)+P(A, \bar{B}))}$

For computing Jaccard similarity between two classes $\mathrm{A}$ and $\mathrm{B}$ we need to know how many elements are contained in the intersection of $A$ and $B$ and the union of $A$ and $B$. To that end we can first separate in each of the two databases the elements that belong to the class present in the database (e.g. A in database D1 with universe U1), and then apply the classifier learnt from the other database, whether an element in each of those two sets belongs also to the other class, or not. We consider U2 ${ }^{\mathrm{AB}}$ as the set of elements of $B$ that are likely to belong to $A$, if they where part of database D1. In this way we determine (or better estimate) the sizes of the potential intersection of $A$ and $B$ and the union of $A$ and $B$ and can based on this compute an estimate for Jaccard similarity.

## Node Mapping

With the similarity values, alternative class mappings are possible Naïve approach

- Order matchings by probability
- Choose the most probable matching and produce a mapping among the classes
- Remove the mapped classes
- Choose the next most probable matching and repeat

Drawback

- Obvious consistency constraints may be violated, e.g., if all children of a class are mapped, then also their parent class should be mapped
- Solution: more sophisticated mapping algorithms that incorporate such general and domain-specific constraints (research problem)

Once the similarity values are computed the process of matching for establishing correspondences is completed. Now the problem of mapping remains, i.e. determine which classes should be considered as equivalent. This is in general not uniquely determined, since a class can be similar to several others. On the other hand we can assume that one class should only be mapped to exactly another class in the other database. This imposes a constraint on the mapping.

A simple approach to establish a mapping that observes this constraint is by proceeding in a greedy fashion. First the best matches are used to produce mappings, then the the mapped classes are removed (to assure that each class is mapped to a unique other class) and then the process continues.

