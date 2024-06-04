# 8. MINING SOCIAL GRAPHS 

# Analyzing Graphs 

- Objects have been described by attributes
- Relationships among objects inferred from distance measure on attributes

Use of explicit relationships: Graphs

- In many cases relationships are explicitly given
- Prime example: social network graphs
- Graph structure can be inferred from distance measure (e.g. for documents)

So far we have assumed that relationships among different objects in clustering are implicitly defined, using a distance measure that is based on the objects' attributes. In many applications such relationships are not implicitly given, but explicitly provided, notably in social network graphs. There the relationships among users are given by different friend relationships or interactions such as likes and retweets. The resulting graphs can be weighted or unweighted. In the following we will consider the case of unweighted graphs.

Of course, it would also be possible to derive a relationship graph by using a distance measure based on attribute values and using the distance as as an edge weight, respectively consider only edges above a distance threshold. In this way the following methods of clustering objects based on graphs could also be applied in this more traditional context.

## Graphs and Clustering

Networks often contain structure

- Clusters (also called communities, modules)

It is widely observed that natural networks contain structure. This is true for social networks (e.g. on social media platforms, citation networks), as well as for many natural networks as we find them in biology. Graph-based clustering aims at uncovering such hidden structures.

## Social Network Analysis

## Types of Community Detection Algorithms 

- Hierarchical clustering
- iteratively identifies groups of nodes with high
- similarity

Two strategies

- Agglomerative algorithms merge nodes and communities with high similarity
- Divisive algorithms split communities by removing links that connect nodes with low similarity

In general, community detection algorithms are based on a hierarchical approach. The idea is that within communities sub-communities can be identified, till the network decomposes into individual nodes. In order to produce such a hierarchical clustering, two approaches are possible: either by starting from individual nodes, by merging them into communities, and recursively merge communities into larger communities till no new communities can be formed (agglomerative algorithms), or by decomposing the network into communities, and recursively decompose communities till only individual nodes are left (divisive algorithms).

In the following we will present one representative of each of the two categories of algorihtms:

1. The Louvain Algorithm, an agglomerative algorithm
2. The Girvan-newman algorithm, a divisive algorithm

## Louvain Modularity Algorithm

Agglomorative Community Detection

- Based on a measure for community quality (Modularity)
- greedy optimization of modularity

Overall algorithm

- first small communities are found by optimizing modularity locally on all nodes
- then each small community is grouped into one new community node
- Repeat till no more new communities are formed

The Louvain algorithm is essentially based on a the use of a measure, modularity, that allows to assess the quality of a community clustering. The algorithm performs greedy optimization of this measure. It is fairly straightforward: initially every node is considered as a community. The communities are traversed, and for each community it is tested whether by joining it to a neighboring community, the modularity of the clustering can be improved. This process is repeated till no new communities form anymore.

## Measuring Community Quality

Communities are sets of nodes with many mutual connections, and much less connections to the outside

Modularity measures this quality: the higher the better

$\sum_{c \in \text { Communities }}(\# e d g e s$ within $c-$ expected \#edges within c)

In order to measure the quality of a community clustering, modularity compares simply the difference between the number of edges that occur within a community with the number of edges that would be expected if the edges in the graph would occur randomly. The random graph model is used as what is called the null model, a graph that has the same distribution of node degrees, but randomly assigned connections.

## Expected Number of Edges

Graph with unweighted edges
$-m=$ total number of edges
$-k_{i}=$ number of outgoing edges of node $i$ (degree) Observation: edges connect to $2 \mathrm{~m}$ nodes

Assumption: distributes weight $\mathrm{k}_{\mathrm{i}}$ uniformly to other nodes

Node $\mathrm{j}$ receives fraction of $\mathrm{k}_{\mathrm{j}} / 2 \mathrm{~m}$ (competes with all other nodes)

The model requires to determining the number of edges that we would expect among a set of nodes, of which we know the degrees, but not the connectivity in detail. Assume that for all nodes i in a community we would now their degree ki (number of edges leaving the node). How many edges would we then observe if the connections on the graph were generated randomly? To answer this question we reason as follows: select one of the nodes i with degree ki. What is now the probability (or fraction of weight) an arbitrary other node $\mathrm{j}$ with weight kj would receive? If there are a total of $m$ edges in the network, there are $2 \mathrm{~m}$ edge ends (since each edge ends in two nodes). If the edge ends of ki are uniformly distributed, node $\mathrm{j}$ would thus receive $\mathrm{ki} / 2 \mathrm{~m}$ edge ends. Thus the number of expected edges connecting nodes $\mathrm{i}$ and $\mathrm{j}$ would be ki times $\mathrm{kj} / 2 \mathrm{~m}$.

## Modularity

$$
\begin{aligned}
& \text { We define now the modularity measure } Q \\
& \qquad \begin{array}{l}
-A_{i j}=\text { effective number of edges between nodes } i \\
\text { and } j \\
-c_{i}, c_{j}=\text { communities of nodes } i \text { and } j \\
\text { Effective number of edges Expected number of edges } \\
\qquad Q=\frac{1}{2 m} \sum_{i, j}\left(A_{i j}-\frac{k_{i} k_{j}}{2 m}\right) \delta\left(c_{i}, c_{j}\right)
\end{array}
\end{aligned}
$$

## Modularity to Evaluate Community Quality

Modularity can also be used to evaluate the best level to cutoff of a hierarchical clustering

Apart from constructing the communities, the modularity measure can also be used to evaluate the quality of communities in hierarchical clustering. This can be done independently of how the clustering has been constructed. In fact, there is an optimal level of clustering when moving from one level of the hierarchy to the next. Initially increasing the number of communities increases their quality, by separating distinct communities. At a certain point, splitting of communities in smaller communities worsens the quality of the community structure. Thus there exists an optimum point of clustering that can be selected using modularity.

## Louvain Modularity - Discussion

Widely used in social network analysis and beyond

- Method to extract communities from very large networks very fast

Complexity: O(n $\log n)$

Louvain modularity clustering is today the method of choice for social network clustering, mainly because of its good computational efficiency. It runs in $n \log n$, which makes it applicable for very large networks, as they occur today, in particular for social networks resulting from large platforms, as social network sites, messaging services or telephony.

## Girvan-Newman Algorithm

## Divisive Community Detection

- Based on a betweenness measure for edges, measuring how well they separate communities
- Decomposition of network by splitting along edges with highest separation capacity

Overall algorithm

- Repeat until no edges are left
- Calculate betweenness of edges
- Remove edges with highest betweenness
- Resulting connected components are communities
- Results in hierarchical decomposition of network

We now introduce a second algorithm fro community detection, that belongs to the class of divisive algorithms. Also this algorithm is based on a measure, this time on a measure on edges. The betweenness measure gives an indication which edges are likely to connect different communities, and thus are good splitting points, to partition larger parts of the network in to communities. The algorithm recursively decomposes the network, by removing edges with the highest betweenness measure, till no edges are left. Also this algorithm results in a hierarchical clustering.

## Edge Betweenness

## Edge betweenness: fraction of number of shortest paths passing over the edge

$$
\operatorname{betweenness}(v)=\sum_{x, y} \frac{\sigma_{x y}(v)}{\sigma_{x y}}
$$

where
$\sigma_{x y}:$ number of shortest paths from $x$ to $y$ $\sigma_{x y}(v):$ number of shortest paths from $x$ to $y$ passing through $v$

Betweenness centrality is an indicator of a node's centrality in a network. It is equal to the number of shortest paths from all vertices to all others that pass through that node. A node with high betweenness centrality has a large influence on the transfer of items through the network, under the assumption that item transfer follows the shortest paths. The concept finds wide application, including computer and social networks, biology, transport and scientific cooperation.

Alternatively, there exist also the concept of random-walk betweenness. A pair of nodes $m$ and $n$ are chosen at random. A walker starts at $m$, following each adjacent link with equal probability until it reaches $n$. Random walk betweenness $x_{i j}$ is the probability that the link $i \rightarrow j$ was crossed by the walker after averaging over all possible choices for the starting nodes $m$ and $n$

## Computing Betweenness - BFS

We describe now the process of computing the betweenness values. The approach is to perform a breadth-first search (BFS) for every node in the graph. The nodes are arranged in increasing levels of distance of the starting node, e.g. node A.

## Computing Betweenness - Path Counting

In a first phase we count the number of shortest paths that are leading to each node, starting from node A. To do so we can simply reuse the data that has been computed at the previous level, summing up the number of paths that have been leading to each parent of a given node.

## Computing Betweenness - Edge Flow 

In a second phase we compute edge flow values (that are the betweenness values related to node A). We proceed in a bottom-up approach. The flow that arrives at every node is 1 . In addition, the node receives also all the flows that are passing on to the children. Thus, the total flow weight a node receives (or has to pass through) is 1 plus the flows to all of its children. This weight is distributed over the parents, proportionally to the number of paths that are leading to those parents (what has been computed in phase 1 ).

## Algorithm for Computing Betweenness

1. Build one BFS structure for each node
2. Determine edge flow values for each edge using the previous procedure
3. Sum up the flow values of each edge in all BFS structures to obtain betweenness value

- Flows are computed between each pairs of nodes $\rightarrow$ final values divided by 2

Once the flows specific to a node have been computed for every node, the last step is to aggregate for each edge all the flow values that have been computed for all the nodes. In this way we compute each flow twice (flow into both direction), therefore, the final betweenness value corresponds to the aggregate flow value divided by 2.

## Girvan-Newman Discussion 

## Complexity

- Computation of betweenness for one link: $O\left(n^{2}\right)$
- Computation of betweenness for all links: $O\left(L n^{2}\right)$
- Sparse matrix: $O\left(n^{3}\right)$

The Girvan-Newman algorithm is the classical algorithm for community detection. It's major drawback is its scalability. The flow computation for one link has quadratic cost in the number of nodes (it has to be computed for each pair of nodes). If we assume sparse networks, where the number of links is of the same order as the number of nodes, the total cost is cubic. This was also one of the motivations the inspired the development of the modularity based community detection algorithm

