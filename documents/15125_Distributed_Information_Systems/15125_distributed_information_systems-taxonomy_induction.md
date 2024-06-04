# 4. TAXONOMY INDUCTION 

## 1. Taxonomy Induction

Information extraction

- Extract isolated facts from documents, e.g., lion ISA animal

Taxonomy induction

- Extract related facts from documents, e.g., classification of animals

Information extraction concerns the extraction of isolated facts, such as ISA relationships. Taxonomy induction aims at extracting related facts and organizing them in a structured knowledge basis, e.g. a hierarchical taxonomy. It is a special case of the more general ontology induction, which organizes knowledge using arbitrary relationships.

## Use of Taxonomies

Hyponyms (subordinate terms) can inherit properties from hypernyms (more general terms)

- Due to transitivity of ISA, no need to learn inferred facts No unique taxonomies
- Depending on the perspective and application different taxonomies may be useful:

A tiger and a puppy are both Mammals and hence belong close together in a typical taxonomy, but tiger is a WildAnimal (in the perspective of Animal-Function) and a JungleDweller (in the perspective of Habitat), while a puppy is a Pet (as function) and a HouseAnimal (as habitat), which would place them relatively far from one another

One of the advantages of taxonomy induction (and more generally ontology induction) is the possibility to perform inferences on the extracted knowledge. For example, in a ISA hierarchy, lower nodes in the hierarchy can inherit properties from higher nodes, thus these extra facts need not to be learnt separately.

One of the challenges in taxonomy induction is the fact that there is no notion of "correct" taxonomy. A taxonomy strongly depends in its intended use and on the specific perspective of the user on the domain. Integrating all possible perspectives into one single global taxonomy would not be feasible and useful, as the resulting taxonomy would potentially be too complex to be used.

## Taxonomy Induction Task

1. Learn relevant terms and their hypernym / hyponym relationships
2. Filter out erroneous terms and relations
3. Induce a taxonomy structure

We present in the following one specific approach to taxonomy induction, which was one of the first approaches proposed in the field. It starts from the assumption that one general concept (e.g. animals) and at least on basic concept of the taxonomy (e.g. lion) are provided as input. From this starting point the task is to identify more relevant concepts (represented as terms), establish the hypernym and hyponym relationships, filter out erronous terms and relations and finally induce an overall taxonomy structure. The figure illustrates the process: at the bottom level first more related terms are identified. Then intermediate concepts, more abstract than the basic concepts are identified. From this data finally the taxonomy will be induced.

## Learning Terms

## Template approach

- Given a root concept c (e.g. animal) and a seed s (e.g. lion)
- Hyponym pattern: $P_{i}(c, s, X)=c$ such as $s$ and $X$
- Hypernym pattern: $P_{c}\left(t_{1}, t_{2}, X\right)=X$ such as $t_{1}$ and $t_{2}$

The basic idea is to learn terms and relationships by querying a Web search engine. As patterns language template capturing hypernym relationships are used. This is analogous to the approach with Hearst patterns for extracting ISA relationships. However, as in a first phase on has to detect more relevant terms, so-called double anchored patterns are used, that relate one (known) term to another (unknown) term of the same class of concepts. One example of such a pattern would be "c such as s and X", where $\mathrm{c}$ and $\mathrm{s}$ would be known and from the result the term at position $X$ would be a new term from the same class of concepts as c. Using such patterns new terms can be harvested by recursively applying the pattern to the terms known so far.

## Finding Hyponyms

Recursively harvest new terms using a Web search engine

$\mathrm{T}=\{\mathrm{s}\} ; \mathrm{w}(\mathrm{t})=0$

while $T$ changes

for all $t$ in $T$ : submit $P_{i}(c, t, X)$ to search engine

add to $T$ all new terms $t_{\text {new }}$ found in position $X$ in a result $\mathrm{w}(\mathrm{t})++$

## Finding Hypernyms

$$
C=\{c\}
$$

for all $t_{1}, t_{2}$ in $T$ with $w\left(t_{i}\right)>0$ :

submit $P_{c}\left(t_{1}, t_{2}, X\right)$ to search engine add new term $h$ found in position $X$ to $C$ add $t_{1} I S A h$ and $t_{2} I S A h$ to the hypernym relations $\mathrm{H}$ $w\left(\mathrm{t}_{1}, \mathrm{t}_{2}, \mathrm{~h}\right)++$

## Filtering

- rank concepts $h$ by $\sum_{t_{1} t_{2}} w\left(t_{1}, t_{2}, h\right)$
- keep top concepts

Once the search for terms is completed, hypernyms can be searched by using the same patterns, but now be putting a variable $\mathrm{X}$ in the place of the concept, and using the basic terms found so far. In this search only terms that have been leading to the discovery of other basic concepts are being used, which is expressed by the condition $\mathrm{w}(\mathrm{t})>0$.

Once the search for higher level concepts is completed, a filtering step is performed. The concepts found are ranked by the number of times they have been discovered starting from different term pairs and only the highest ranked concepts are retained.

## Inducing Hypernym Graph

Many possible relationships among concepts and terms have likely not been discovered

For each pair $t_{1}, t_{2}$ in TUC

Construct query $q_{1}=h\left(t_{1}, t_{2}\right)$ and $q_{2}=h\left(t_{2}, t_{1}\right)$

with Hearst pattern $h(X, Y)$, e.g., $h(X, Y)=$ " $X$ such as $Y$ "

Submit query to search engine and count number of results If \#results $\left(q_{1}\right)>\#$ results $\left(q_{2}\right)$

then add $t_{1} I S A t_{2}$ to $\mathrm{H}$

else add $t_{2} I S A t_{1}$ to $\mathrm{H}$

Result: A directed hypernym graph $\mathrm{H}$

In the steps performed so far, many possible relationships among higher level concepts and basic concepts and higher level concepts may not have been discovered. For discovering those again queries against a search engine are performed, testing the two possible directions of a hypernym relationship for each pair of terms. The alternative that produces more results in the search is considered as being the correct one. As templates we can use any of the Hearst patterns, such as " $X$ such as $Y$ ", " $X$ are $Y$ that", " $X$ including $Y$ ", " $X$ like $Y$ ", "such $X$ as $Y$ " etc

## Cleaning the Hypernym Graph

1. Determine all basic concepts

- Not hypernym of another concept

2. Determine all root concepts

- Have no hypernyms

3. For each basic concepts - root concept pair:

- Select all hypernym paths that connect them

4. Choose the longest hypernym paths for the final taxonomy

For cleaning up the taxonomy graph, first the basic and root concepts are identified, which are the ones that are not hypernym of another concept, resp. have no hypernym. Then for every possible pair of a root concept and a basic concept all paths between the two are extracted, and only the longest one (or the longest ones) is retained.

## Taxonomy Induction: 7 years later

We will present now a more advanced technique for automated taxonomy induction that we recently developed. It takes advantage of different advances in the available tools, but also incorporates some very fundamental ideas that have not been taken into account in the literature and largely help to improve the quality of results. The main ideas are the following:

1. Instead of starting from a clean predefined set of seed terms, the method starts from a document corpus and uses keyphrase extraction to generate an initial vocabulary. This vocabulary may be noisy, but the method will help to clean it up while generating the taxonomy.
2. Instead of querying the Web, the method uses a Hypernym database that has been generating from analyzing a Web corpus.
3. Instead of performing simple statistics, the method uses various machine learning techniques for inducing the taxonomy.

## Key Observations

Current approaches in the literature make two main assumptions

1. The vocabulary is free of noise

- Requires manual cleaning step before taxonomy induction

2. The quality of the taxonomy by estimating the probability of correctness of individual hypernym relationships

- There is evidence that this works not well for more general terms

In particular the second assumption is important. Considering only individual hypernym relationships for assessing correctness means that contextual knowledge, i.e., the other relationships the terms have, is not considered and thus important information is lost.

## Semantic Drift in Generalization

| TopEdge | 2 <br> 3 <br> 4 <br> 5 <br> 6 | blintz $\rightarrow$ goody <br> blintz $\rightarrow$ goody $\rightarrow$ thing <br> blintz $\rightarrow$ goody $\rightarrow$ ulead $\rightarrow$ editor <br> blintz $\rightarrow$ goody $\rightarrow$ ulead $\rightarrow$ social networking $\rightarrow$ networking $\rightarrow$ part <br> blintz $\rightarrow$ goody $\rightarrow$ ulead $\rightarrow$ editor $\rightarrow$ storyliner $\rightarrow$ role |
| :---: | :---: | :---: |
|  | 2 <br> 3 <br> 4 <br> 5 <br> 6 | oat $\rightarrow$ food <br> oat $\rightarrow$ crop $\rightarrow$ thing <br> oat $\rightarrow$ crop $\rightarrow$ total loss $\rightarrow$ partial loss $\rightarrow$ loss <br> oat $\rightarrow$ cereal grain $\rightarrow$ grain $\rightarrow$ balanced diet $\rightarrow$ diet $\rightarrow$ factor <br> oat $\rightarrow$ cereal $\rightarrow$ industry $\rightarrow$ field of life $\rightarrow$ other carrier $\rightarrow$ carrier |

Considering only individual hypernym relationships frequently results in semantic drift, in particular at the higher levels of the taxonomy.

## Key Ideas

1. Allow noisy vocabulary, but clean the resulting taxonomy after induction

- After taxonomy induction more information is available to identify noisy terms

2. Estimate the probability of correctness of a complete path of hypernym relationships!

- More contextual information is exploited in assessing the correctness of hypernym relationships

Based on the two key observations, two key ideas are applied in order to achieve better performance in taxonomy induction. Both ideas are based on the approach of exploiting more contextual information when performing the taxonomy induction task.

## Approach

## Find a DAG of generalizations

- Starting from one seed term in the vocabulary, e.g., “apple"
- Only one path for each hypernym of the seed term

| Candidate hypernym | Freq. |
| :---: | :---: |
| company | 5536 |
| fruit | 3898 |
| apple | 2119 |
| vegetable | 928 |
| orange | 797 |
| tech company | 619 |
| brand | 463 |
| hardware company | 460 |
| technology company | 427 |
| food | 370 |

Graph G

The basic approach of the method is to induce for each term in the vocabulary a DAG that consists of hypernym paths from the term to a root concept. In the approach it is assumed that for every hypernym of the term only a single path is generated. Each of the paths can correspond to a different sense of the term.

## Probabilistic Model

Ideally: given the evidence E, find the most probable Graph G $\operatorname{argmax}_{G} P(G / E)$ (not feasible)

Aproximation: $\operatorname{argmax}_{G} P(G \mid E)=\operatorname{argmax}_{G} \Pi_{i} P\left(E / S_{i}\right) \times P\left(S_{i}\right)$ where $S_{\mathrm{i}}$ subsequence from seed term to a root

An independence assumption

- But weaker than assuming all hypernym edges are independent of each other!

Need to estimate $P\left(E / S_{i}\right)$ and $P\left(S_{i}\right)$

Ideally, we would find the most likely graph structure, given the evidence $E$ provided in the hypernym database. Since it is not feasible to explore the complete space of all possible graphs, we will apply an independence assumption. We assume that the different paths from a leaf to the root of a hypernym graph are independent of each other (which is of course not correct, since the paths are in general overlapping). But in this way we need no more to estimate the probability of a graph, but only those of path. Note that this is still a weaker independence assumption than the one being made when assuming that al hypernym edges are independent of each other.

## Solution Strategy

1. Estimation of probabilities of subsequences
2. Search strategy for subsequences
3. Optimizing the resulting DAG

## Probability Estimation: $\mathbf{P ( S )}$

For $S=t \rightarrow h_{1} \rightarrow h_{2} \rightarrow h_{3} \rightarrow \ldots \rightarrow h_{n}$

$$
P(S)=P\left(t, h_{1}\right) \times P\left(h_{1}, h_{2}\right) \times \ldots \times P\left(h_{n-1}, h_{n}\right)
$$

$P(a, b)$ - edge probability

## Edge Probability

$P(a, b) \propto \exp (\mathbf{w} \cdot f(a, b))$

Edge features $f(a, b)$

- Normalized count, $n(a, b)=$ freq $(a, b) / \max _{c}(f r e q(a, c))$
- Normalized difference
- String-based features (prefix, suffix, substring, length)
- Generality based features

Weights w obtained from a classifier trained on a manually annotated set of edges

## Probability Estimation: $\mathbf{P ( E | S )}$

For $S=t \rightarrow h_{1} \rightarrow h_{2} \rightarrow h_{3} \rightarrow \ldots \rightarrow h_{n}$ $P(E \mid S)=\sum_{j} P\left(E_{j} \mid S\right)$

$P\left(E_{j} \mid S\right) \propto \max \left(\operatorname{sim}\left(E_{j}, h_{i}\right)\right)$ for all $h_{i}$

$\operatorname{sim}(a, b)=\max (P(a, b), P(b, a))$

Why maximum (and not, e.g., sum)?

- Consider $S=$ apple $\rightarrow$ fruit $\rightarrow$ food $\rightarrow$ substance $\rightarrow$ matter $\rightarrow$ entity
- For the term $\mathrm{E}_{\mathrm{j}}=$ fruit, the hypernyms matter and entity occurring in the sequence should not hurt, even when unrelated


## Intuitive Interpretation

$\operatorname{Pr}(\mathrm{S})$ promotes subsequences, which consist of individual edges with a larger probability of hypernymy

$\operatorname{Pr}(E \mid S)$ promotes subsequences, which contain a larger number of candidate hypernyms from $E$

