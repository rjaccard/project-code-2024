# Data Viz 

## Heavy-tailed

- With the log scale on the $y$ axis : you multiply instead of additioning
- Very large values are rare BUT they are not very rare
- If you plot this kind of data on log-x axis and log-y axis, you get a linear function
- Exponential : concave curve
- $\quad$ The CCDF is also a power law (Still the same shape but it is more monotone)
- Use robust statistics


## Statistics

## Robust statistic

A statistic is said to be robust if it is not sensitive to outliers.

- min, max, mean, std are not robust
- median, quartiles, geometric mean are robust


## P-value

Used to indicate whether the results obtained after conducting a test are statistically significant or not. It indicates the probability of making an error in rejecting or not rejecting the null hypothesis. It is in a way the probability of observing an extreme value.

The alpha level can be defined as the acceptable risk rejecting the null hypothesis even if it is true. The alpha level is usually chosen between $1 \%$ to $5 \%$ (common values : $5,1,0.5,0.1$ )

$\rightarrow$ It controls false-positive rate (probability of rejecting $\mathrm{H}_{0}$ although it is true).

$\rightarrow \alpha$ big $=$ high false-positive rate

| 1 | If $P=.05$, the null hypothesis has only a $5 \%$ chance of being true. |
| :---: | :--- |
| 2 | A nonsignificant difference (eg, $P \geq .05$ means there is no difference between groups. |
| 3 | A statistically significant finding is clinically important. |
| 4 | Studies with $P$ values on opposite sides of .05 are conflicting. |
| 5 | Studies with the same $P$ value provide the same evidence against the null hypothesis. |
| 6 | $P=.05$ means that we have observed data that would occur only $5 \%$ of the time under the null hypothesis. |
| 7 | $P=.05$ and $P \leq .05$ mean the same thing. |
| 8 | $P$ values are properly written as inequalities (eg, " $P \leq .02$ " when $P=.015$ ) |
| 9 | $P=.05$ means that if you reject the null hypothesis, the probability of a type I error is only $5 \%$. |
| 10 | With a $P=.05$ threshold for significance, the chance of a type I error will be $5 \%$. |
| 11 | You should use a one-sided $P$ value when you don't care about a result in one direction, or a difference in |
| 12 | that direction is impossible. |

## Test statistic

A measurement made on the data that is likely to be large under $\mathbf{H}_{\mathbf{1}}$ but small under $\mathbf{H}_{0}$

## Cl

Confidence Interval = a range of estimates ( estimations) for the parameter of interest (ex : mean)

that seems reasonable given the observed data

Bootstrap resampling : same size + replacement

## Multiple hypothesis testing

## Bonferroni Correction

- Just divide by the number of hypotheses

Šidák Correction

$$
\alpha_{c}=\frac{\alpha}{k}
$$

- Asserts independence

$$
\begin{aligned}
\alpha & =1-\left(1-\alpha_{c}\right)^{k} \\
\alpha_{c} & =1-(1-\alpha)^{\frac{1}{k}}
\end{aligned}
$$

## Coefficient of determination - $\mathrm{R}^{2}$

Close to 1 : les points sont proches de la prédiction

Close to 0 : les points sont dispersés autour de la prédiction

$\rightarrow$ goodness of fit

## Linear Regression

Goal : compare average outcomes y across subgroups of data

Regression can deal with correlation between predictors.

- Null hypothesis : The true coefficient is 0
- p-value $<0.05 \rightarrow$ coefficient is significant for the prediction


## Binary predictor / Continuous outcome

- Intercept $\beta_{1}=78$

$\rightarrow$ mean outcome for data points $i$ with $\boldsymbol{X}_{\boldsymbol{i}}=\mathbf{0}$

- Slope $\beta_{2}=12$

$\rightarrow$ difference in mean outcomes between data points with $\boldsymbol{X}_{\boldsymbol{i}}=\mathbf{1}$ and data points with $\boldsymbol{X}_{\boldsymbol{i}}=\mathbf{0}$ (just look the difference on the $y$-axis on the two means)

- The prediction function captures the mean in each subgroup


## Continuous predictor / Continuous outcome

- Same logic as before : For a given X, the model gives the mean outcome for all the points with the abscise $X$.
- Intercept $\beta_{1}$ : estimated mean outcome for data points with $X_{i}=0$
- Slope $\beta_{2}$ : difference in estimated mean outcomes between data points whose $X_{i}^{\prime}$ 's differ by 1 $\rightarrow$ difference between the mean of points where $X_{i}=0$ and $X_{j}=1$, etc.


## Continuous predictor + Categorical predictor / Continuous outcome

- Gives us two different regression models with two different intercepts and same slopes : one for each category of the categorical feature


## Mean centering of predictors

- The mean of outcomes $Y_{i}$ is easily found for the mean of features $X_{i}$ :
ordinate $Y_{i}$ of the prediction line taken at abscisse $X_{i}=0$.
- Intercept : estimated mean outcome when each predictor has its mean value
- The other coefficients (slope coefficient) $B_{k}$: estimated average increase in outcome $y$ for each unit increase in $X_{i k}$.

-> If all the features take their average value (0) except the one studied, how much does it cost to change the predictor value?

# After standardisation: 

The distance is seen as the number of standard deviations I am away from the mean.

## Logarithmic output

When the outcome $y$ follows a heavy-tailed distribution, when the outcomes are non-negative.

$\rightarrow$ Turns the additive model into a multiplicative one.

$$
\log y_{i}=b_{0}+b_{1} X_{i 1}+b_{2} X_{i 2}+\cdots+\epsilon_{i}
$$

Exponentiating both sides yields

$$
\begin{aligned}
y_{i} & =e^{b_{0}+b_{1} X_{i 1}+b_{2} X_{i 2}+\cdots+\epsilon_{i}} \\
& =B_{0} \cdot B_{1}^{X_{i 1}} \cdot B_{2}^{X_{i 2}} \cdots E_{i}
\end{aligned}
$$

- An additive increase of 1 in predictor $X_{1}$ is associated with a multiplicative increase of $B_{1}=$ $\exp \left(b_{1}\right)$ in the outcome


## Machine Learning

## Feature selection

Offline feature selection :

- Goal = select the best features according to their individual predictive power
- Criterias = Pearson coefficient, Mutual information, Chi-squared method

Online feature selection :

- Forward feature selection, Backward feature selection


## Feature normalization

- $\quad$ Some models don't manage well features with different scales
- Features with large values dominate the others, and the classifier tends to over-optimize for them

| Logarithmic <br> scaling | $x^{\prime}=\log (x)$ <br> Consider order of magnitude | Good for heavy-tailed features |
| :---: | :---: | :---: |
| Min-max scaling | $x_{i}^{\prime}=\left(x_{i}-m_{i}\right) /\left(M_{i}-m_{i}\right)$ <br> $m_{i}:$ min value <br> $M_{i}:$ max value <br> The new feature lies in the interval $[0,1]$ <br> Map the lowest value to 0 and the <br> largest to 1 | Not good if you have outliers <br> $\rightarrow$ very large will go to 1 <br> $\rightarrow$ very small will be shrink towards 0 |
| Standardization | $x_{i}^{\prime}=\left(x_{i}-\mu_{i}\right) / \sigma_{i}$ <br> To compare features with different <br> units <br> You measure in units of standard <br> deviation from the mean! | Not good if features are not symmetrical! <br> Normally, used for normal distributions. <br> Doesn't make sense if the data is skewed! |

## Scores : TP/FN

| Accuracy | $\frac{T P+T N}{A L L}$ |  | How many data points do you classify correctly? <br> Good if dataset is balanced <br> Not good is skewed |
| :---: | :---: | :---: | :---: |
| Precision | $\frac{T P}{T P+F P}$ <br> Look tl | $\frac{T N}{T N+F N}$ <br> row predicted $=1$ | What fraction of positive predictions are actually positive? <br> If I predict cancer, how many person actually have cancer? <br> Pourcentage de good classified parmis les classifiés comme 1. <br> Lot of FP $\Rightarrow$ Small precision |
| Recall | $\frac{T P}{T P+F N}$ <br> Look a <br> True p | $\frac{T N}{T N+F P}$ <br> he column real $=1$ <br> tive rate $=$ recall | What fraction of actually positive are predicted as positive? <br> How many people did I predict cancer from all the people who <br> have cancer? <br> Pourcentage de good classified parmis ceux qui ont vraiment <br> ce label. <br> Lot of FN $\Rightarrow$ Small Recall |
| Z-score | $2 \cdot \frac{\text { recal }}{\text { recall }}$ | recision <br> recision | Harmonic mean of the two! |


| False <br> positive <br> rate | $\frac{F P}{F P+T N}$ <br> Look at the column real $=\mathbf{0}$ | Probability type I error $($ label $=1 /$ true $=0)$ |
| :--- | :--- | :--- |


| Recall : $45 / 50=90 \%$ <br> Precision $45 / 65=70 \%$ | Recall : $40 / 50=80 \%$ <br> Precision $40 / 50=80 \%$ |
| :--- | :--- |
| Classifier 1 : Il y a plus de FP (precision) Mais il y a moins de FN (recall) $\Rightarrow$ Pick this one for cancer ! |  |

ROC Curve

When we decrease the threshold, we get more positive values thus it increases the true positive rate and decreases the true negative rate.

$\rightarrow$ worst : no discrimination capacity to distinguish between positive class and negative class

ROC AUC : area under the curve, captures the overall quality of the classifier

- $\quad$ Between 0.5 (random classifier - worst case) and 1 (perfect classifier)
- $\quad A \cup C=70 \% \Rightarrow$ there is a $70 \%$ chance that the model will be able to distinguish between positive class and negative class

| Threshold close to 0 | Most of labels <br> are 1 | Bad precision (lot of FP) <br> High recall (as almost all classified as 1) |
| :--- | :--- | :--- |
| Threshold close to 1 | Most of labels <br> are O | Good precision (among those classified as 1) <br> Low recall (as almost all classified as 0 $\rightarrow$ lot of FN) |

## Bias/Variance trade off

Plot learning curves : training set size VS training/testing errors (error as a function of the size)

$\rightarrow$ The complexity of the model is fixed!

## Supervised learning

## Distances (opposite of similarity)

- Euclidean Distance: Simplest, fast to compute

$$
d(x, y)=\|x-y\|
$$

- Cosine Distance: Good for documents, images, etc.

$$
d(x, y)=1-\frac{x \cdot y}{\|x\|\|y\|}
$$

- Jaccard Distance: For set data:

$$
d(X, Y)=1-\frac{|X \cap Y|}{|X \cup Y|}
$$

- Hamming Distance: For string data:

$$
d(x, y)=\sum_{i=1}^{n}\left(x_{i} \neq y_{i}\right)
$$

- Manhattan Distance: Coordinate-wise distance

$$
d(x, y)=\sum_{i=1}^{n}\left|x_{i}-y_{i}\right|
$$

- Edit Distance: for strings, especially genetic data.


## Decision trees

- Nodes are tests on a single attribute
- Branches are attribute values of parent node
- Leaves are marked with class labels
- At the beginning, all training samples belong to the root
- Examples are partitioned recursively based on selected "most discriminative" attributes
- All samples belong to the same class $\rightarrow$ assign the class label to the leaf

Which attribute we split on ?

$H(P, N)=-\frac{P}{P+N} \log _{2} \frac{P}{P+N}-\frac{N}{P+N} \log _{2} \frac{N}{P+N}$

## Attribute selection

$$
\mathrm{H}_{\mathrm{s}}=\mathrm{H}(9,5)=0.94
$$

| age | income | student | credit_rating | buys_computer |
| :--- | :--- | :---: | :--- | :---: |
| $=30$ | high | no | fair | no |
| $<=30$ | high | no | excellent | no |
| $31 \ldots 40$ | high | no | fair | yes |
| $>40$ | medium | no | fair | yes |
| $>40$ | low | yes | fair | yes |
| $=>40$ | low | yes | excellent | no |
| $31 . .40$ | low | yes | excellent | yes |
| $=-30$ | medlium | no | falr | no |
| $=-30$ | low | yes | fair | yes |
| $>40$ | medium | yes | frair | yes |
| $<-30$ | medium | yes | excellent | yes |
| $31 \ldots 40$ | medium | no | excellent | yes |
| $31 \ldots 40$ | high | yes | fair | yes |
| $>40$ | medium | no | excellent | no |
|  |  |  |  |  |

Income $[$ high] $\mathrm{H}(2,2)=1$

Income $[\mathrm{med}] \mathrm{H}(4,2)=0.92$

Income [low] $\mathrm{H}(3,1)=0.81$

Student [yes] $H(6,1)=0.59$

Student [no] $\quad H(3,4)=0.98$
Rating [fair] $\mathrm{H}(6,2)=0.81$

Rating [exc] $\mathrm{H}(3,3)=1$

## Attribute selection

| age | income | student | credit_rating | buys_computer |
| :---: | :---: | :---: | :---: | :---: |
| $<=30$ | high | no | fair | no |
| $<=30$ | high | no | excellent | no |
| $31 \ldots 40$ | high | no | fair | yes |
| $>40$ | medium | no | fair | yes |
| $=40$ | low | yes | fair | yes |
| $=40$ | low | yes | excellent | no |
| $31 \ldots 40$ | low | yes | excellent | yes |
| $<-30$ | medium | no | tair | no |
| $<-30$ | low | yes | tair | yes |
| $>40$ | medium | yes | tair | yes |
| $<=30$ | medium | yes | excellent | yes |
| $31 \ldots 40$ | medium | no | excellent | yes |
| $31 \ldots 40$ | high | yes | fair | yes |

$$
H_{S}=H(9,5)=0.94
$$

$H_{\text {Age }}=p([<=30]) \cdot H(2,3)+p([31 \ldots 40]) \cdot H(4,0)+p([>40]) \cdot H(3,2)=$ $=5 / 14 \cdot 0.97+4 / 14 \cdot 0+5 / 14 \cdot 0.97=0.69$

$H_{\text {Income }}=p([$ high $]) \cdot H(2,2)+p([$ med $]) \cdot H(4,2)+p([$ low $]) \cdot H(3,1)=$

$=4 / 14 \cdot 1+6 / 14 \cdot 0.92+4 / 14 \cdot 0.81=0.91$

$\mathrm{H}_{\text {student }}=\mathrm{p}([$ yes $]) \cdot \mathrm{H}(6,1)+\mathrm{p}([$ no] $) \cdot \mathrm{H}(3,4)=7 / 14 \cdot 0.59+7 / 14 \cdot 0.98=0.78$

$H_{\text {Rating }}=p([$ fair $]) \cdot H(6,2)+p([e x c]) \cdot H(3,3)=8 / 14 \cdot 0.81+6 / 14 \cdot 1=0.89$

The information gain obtained by splitting $S$ using $\mathrm{A}$ is

$$
\begin{aligned}
& \operatorname{Gain}(A)=H(P, N)-H(A) \\
& \text { Gain(Age) }=0.94-0.69=0.25 \\
& \text { Gain }(\text { Income })=0.94-0.91=0.03 \\
& \text { Gain(Student) }=0.94-0.78=0.16 \\
& \text { Gain(Rating) }=0.94-0.89=0.05
\end{aligned}
$$

## Ensemble methods

- Bagging: train learners in parallel on different samples of the data, then combine by voting (for discrete output) or by averaging (for continuous output).
- Stacking: combine outputs from various models using a second-stage learner (e.g., linear regression).
- Boosting: train learner again, but after filtering/weighting samples based on output of previous train/test runs.


## Random forests

- Random forests use 10 's of deep, large trees:


## Boosted trees

Bias reduction through boosting - variance already low

## Unsupervised learning

## Cluster bias :

- Usually people assume an underlying domain has discrete class in it (ex: personality types)
- In reality, the underlying data is often continuous !
- Use continuous models (ex: matrix factorisation, soft clustering)
- Or other methods (ex: dimensionality reduction)


## Clustering - def

Methods of clustering

| Hierarchical <br> methods | Agglomerative <br> (bottom up) | Initially, each point is a cluster <br> Repeatedly combine the two "nearest" clusters into one |
| :--- | :--- | :--- |


|  | Divisive (top <br> down) | Start with one cluster and recursively split it |
| :--- | :--- | :--- |
| Flat methods | Point <br> assignment <br> methods | Maintain a set of clusters <br> Assign points to "nearest" cluster; recompute clusters; repeat |

## K-means

## How to choose $\mathbf{k}$ ?

## For $\mathrm{k}=1,2,3, \ldots$

- Run $k$-means with $\mathrm{k}$ clusters
- For each data point i, compute "silhouette width" s(i)
- $S=$ average of $s(i)$ over all $i$
- Plot $S$ against $k$
- Pick $k$ for which $S$ is greatest

$$
s(i)=\frac{b(i)-a(i)}{\max \{a(i), b(i)\}} \begin{gathered}
\text { b(i): avg. distance to points in closest } \\
\text { other cluster }
\end{gathered}
$$

a(i): avg. distance to points in own cluster

## DBSCAN

| Core points | At least minPts neighbors in a sphere of diameter $\varepsilon$ around them <br> $\rightarrow$ They can directly reach neighbors in their $\varepsilon$-sphere <br> Ex : red points = core points with at least minPts $=3$ neighbors in an $\varepsilon$-sphere around them |
| :---: | :---: |
| Point $q$ is <br> density-reachable <br> from $p$ | If there is a series of points $p=p 1, \ldots, p n=q$ such that pi+1 is directly reachable from pi <br> $\rightarrow$ So all points on the path $p 1, \ldots . p n$ must be core points, except possibly pn <br> Reachability is an asymmetric notion <br> All points not density-reachable from any other points are outliers/noise |
| Points p, q are <br> density-connected | If there is a point o such that both $p$ and $q$ are density-reachable from $o$. <br> $\rightarrow$ A cluster is a set of points which are mutually density-connected. |

```
DBSCAN(DB, dist, eps, minPts) \{
    $\mathrm{C}=0$
    for each point $P$ in database $D B$ \{
        if label(P) $\neq$ undefined then continue
        Neighbors $\mathrm{N}=$ RangeQuery(DB, dist, $\mathrm{P}$, eps)
        if $|\mathrm{N}|<$ minPts then \{
            label $(\mathrm{P})=$ Noise
            continue
        \}
        $\mathrm{c}=\mathrm{c}+1$
        label(P) $=$ C
        Seed set $\mathbf{S}=\mathrm{N} \backslash\{\mathrm{P}\}$
        for each point $Q$ in $S$ \{
            if label $(Q)=$ Noise then label $(Q)=C$
            if label $(Q) \neq$ undefined then continue
            label $(Q)=C$
            Neighbors $\mathrm{N}=$ RangeQuery(DB, dist, Q, eps)
            if $|\mathrm{N}| \geq$ minPts then
                $\mathrm{s}=\mathrm{s} \cup \mathrm{N}$
            \}
        \}
    \}
    \}
```

Each RangeQuery (to find neighbors within the $\varepsilon$-sphere) takes only $O(\log n)$ time.

## Observational studies

## Confounder

The cofounder invalidates the experiment.

Make sure the different cofounders (here motivation) have no influence on who takes the treatment

In practice : randomize which person I give the treatment

- There is equally chance that they have motivation to quit smoking
- Same distribution over motivation among treated and control
- Probability of receiving treatment same for everyone (e.g., even if motivated, can be in control)
- Treatment and control groups are indistinguishable


## Observational studies

How to deal with these cofounders? With matching !

- Pair up two identical people (1 treated / 1 control)
- Then compare the outcome of treated vs control (ex : mean difference, regression analysis)


## Propensity score

$\operatorname{Pr}($ subject is treated | observed covariates)

$\Rightarrow$ Compress the observed covariates into a single number: the probability to receive the treatment

$\Rightarrow$ Match treated/control with same propensity score

$\rightarrow$ The subjects in a matched pair might not have the same observed covariates $x$, but treated and control groups will have similar distributions of $x$ (balancing property of propensity score)

Can be estimated from the data, via logistic regression

- Input: observed covariates
- Output: treatment indicator (1 if treated, O if control)

Problem :

$\rightarrow$ propensity score may differ from true probability to treat:

$\operatorname{Pr}($ treated $\mid$ observed covariates) $\neq \operatorname{Pr}($ treated $\mid$ all covariates)

## Sensitivity analysis model

## Solution - The sensitivity analysis model

$\rightarrow$ How to fix the problem from something we cannot observe ?

Idea: Quantify the degree to which the naive model may be wrong without you having to change your (causal) conclusions

$\rightarrow$ You admit the naive model is wrong (people who look comparable are not comparable), but you ask how wrong my model can be before changing my mind in respect to the causal conclusions.

You assume that two subjects who look identical may differ (the naive model is violated) with respect of the probability receiving the treatment

$\rightarrow$ treatment odds treatment probability

$\rightarrow$ the treatment odds differ by a factor of gamma

Then you reason in the spirit of proof by contradiction : to change conclusion of my study, two identical-looking people (1 treated, 1 control) would have to have hugely different treatment odds (i.e., huge $\Gamma$.

- In order to change my mind, Г has to be huge.
- Common sense suggests that $\Gamma$ cannot be so huge, so by contradiction, I don't change my conclusion.

$$
\frac{1}{\Gamma} \leq \frac{\pi_{k} /\left(1-\pi_{k}\right)}{\pi_{\ell} /\left(1-\pi_{\ell}\right)} \leq \Gamma \text { whenever } \mathbf{x}_{k}=\mathbf{x}_{\ell}
$$

- $\quad \mathbf{p i}_{\boldsymbol{k}}:$ true probability to receive the treatment (not known)
- odds:pi $: 1-p i_{k}$
- the observed covariates of subjects $k$ and I are equals : $x_{k}=x_{1}$ (the two people looks exactly the same but are not identical due to unobserved values)

For the sensitivity analysis model :

- We assume that the odds ratio is bounded by $1 /$ gamma and gamma.
- Even if the treatment probability is not the same.
- You know that pi, is the probability for I to receive the treatment.
- You know that in the pair (k,l), only one receives the treatment.
- $\quad$ ratio $=\operatorname{Pr}(k$ treated $\mid$ either $\boldsymbol{k}$ or $\boldsymbol{\ell}$ treated $) / \operatorname{Pr}(\ell$ treated $\mid$ either $\boldsymbol{k}$ or $\boldsymbol{\ell}$ treated $)$


## Interpretation :

If $\Gamma=1 \rightarrow$ naive model is true

- numérateur = dénominateur
- the odds are equals
- kand I have the same treatment probability

If $\Gamma=2$

- Even if the two subjects have the same observed covariates, one subject is twice likely to be the one to receive the treatment
- You don't know anything : you just need to quantify how much gamma would need to be in order to change my conclusion
- you don't know gamma, in order to change my conclusion, gamma should be 10, but it is huge, so I reject


## $\Gamma=\infty \rightarrow$ void statement

Gives no extra information

Example : smoking and lung cancer

- Under naive model (we match on observed covariates) :
- $H_{0}$ :smoking does not increase lung cancer risk (no true causal effect)
- p-value : what is the probability of observing data extreme as we do even if there is no causal effect
- Data hard to explain without a causal effect

$\rightarrow$ It gives a very small $p$-value for $\mathrm{H}_{0}$

- Under sensitivity analysis model

In general, increasing sensitivity $\Gamma$ increases the $p$-value for null hypothesis (you have more probability to observe your data even under $\mathrm{H}_{0}$ - no actual causal effect).

$\rightarrow$ The two identical person have different treatment probability (the falsly observed effect is due to unobserved values rather than the treatment).

## Example :

Two people with one smoker, the other not smoker.

But making $\boldsymbol{p}>\mathbf{0 . 0 5}$ would require $\boldsymbol{\Gamma}>\mathbf{6}$ (domain expertise)!

$\rightarrow$ The odds of being a smoker would need to be six times higher for one of two people with the exact same observed features (age, gender, education, income, ...).

$\rightarrow$ It's unlikely that any unobserved covariate would have such a large effect on smoking habits. So smoking causes cancer!

## Handling text

## Typical tasks

1. Document retrieval

Given a document collection, and a query document (ex: "What is the weather tonight?"), you rank all the documents in the collection by similarity to the query.

ex: Web search

k-NN for document retrieval :

- Neighbor search
- Given a query $\mathbf{q}$, find the $\mathbf{k}$ docs with smallest distance to $\mathbf{q}$

2. Document classification

Given a document $\mathrm{d}$ and a set of classes, decide to which class the document d belongs to.

3. Sentiment analysis

Given a document d, assign a "sentiment" score capturing how positive/negative $d$ is.

4. Topic detection

Given unlabeled document collection, determine a set of prevalent topics in the docs or determine for each document to which topics it belongs.

## Unsupervised learning for topic detection :

- Represent documents as feature vectors
- Clustering : hierarchical (agglomerative/divisive), point-assignment (k-means, DBSCAN)
- Problem : curse of dimension!
- Matrix factorization


## Word count distribution

Zipf's law:

The probability of observing a word in one document scales inversely with its frequency rank.

- $\mathrm{p}\left(\mathrm{w}_{\mathrm{i}}\right) \propto 1 / \mathrm{i}$
- $w_{i}$ : the i-th most frequent word in the document
- $\mathrm{p}\left(\mathrm{w}_{\mathrm{i}}\right)$ : probability to observe the word $\mathrm{w}_{\mathrm{i}}$ in the document

$E x: w_{2}$ second most frequent word $\rightarrow p\left(w_{2}\right)=1 / 2$

## TF-IDF

- We want to give less weight to more common words $\rightarrow$ use IDF (Inverse Document Frequency)
- More weight for a word if it appears a lot in the doc, less weight if it also appears a lot everywhere else !
- $\quad i d f(w)=-\log ($ docfreq( $w) / N)$

$=\log (N)-\log ($ docfreq(w) )

- $t f(w, d)=T e r m$ frequency of word $w$ in doc $d$


## Normalization

- Along the rows
- L2-normalization : all rows have Euclidean distance 1 from origin (all data points lie on a unit sphere) -> row $/ \|$ row $\|_{2}$
- L1-normalization : all rows sum to 1, one row can be interpreted as distribution -> $x_{i} / x_{1}+\ldots .+x_{n}$


## Overfitting with text

Often more features (words) than documents, can lead to overfitting !

Solution :

- Decrease model capacity : feature selection, regularization, dimensionality reduction
- Use ensemble methods such as random forests


## Closeness with cosine distance

Cosine distance $=1-$ cosine similarity

$$
=1-<q /|q|, v /|v|>
$$

$$
=1-\langle q, v\rangle=\|x-y\|^{2} / 2 \quad \text { if the rows are L2-normalized }
$$

$$
\text { similarity }=\cos (\theta)=\frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}=\frac{\sum_{i=1}^{n} A_{i} B_{i}}{\sqrt{\sum_{i=1}^{n} A_{i}^{2}} \sqrt{\sum_{i=1}^{n} B_{i}^{2}}}
$$

How to quantify closeness of two docs ?

- Cosine of the two associated rows of the TF-IDF matrix

How to quantify closeness of two words ?

- Cosine of the two associated columns of the TF-IDF matrix


## Topic detection

1. Using unsupervised algorithms (ex: $k-$-means)

- Each row of the TF-IDF matrix is data point
- Goal : cluster rows of the TF-IDF matrix and then, inspect clusters manually (read the document which is the clustroid/centroid) and label the clusters with descriptive names (ex: sports, news, ...)

2. Matrix factorization for topic detection (LSA -Latent semantic analysis)

We assume that docs and words have a representation in the "topic space".

Lead to dimensionality reduction : Use A instead of TF-IDF matrix for all your ML algorithms (classification, regression, clustering...) $\rightarrow$ choose the topic space rather than the word space !

$\rightarrow$ Move from sparse to dense vectors with LSA (Latent semantic analysis) or LDA

- How to find A and B ? Via singular-value decomposition (SVD)

$\mathbf{T}=\mathbf{U S V}^{\top}$, with columns of $U$ and $\mathrm{V}$ are orthonormal bases

$\Rightarrow \mathbf{A}=\mathbf{U}, \mathbf{B}=\mathbf{S V} \mathbf{V}^{\top}$ or $\mathbf{A}=\mathbf{U S}, \mathbf{B}=\mathbf{V}^{\top}$

$\rightarrow$ S is diagonal and captures "importance" of topic (amount of variation in corpus w.r.t. topic)

$\rightarrow$ If you want $\mathrm{k}$ topics, keep only the first $\mathrm{k}$ columns of $\mathrm{U}$ and $\mathrm{V}$, and the first $\mathrm{k}$ rows and columns of $\mathrm{S}$

$\rightarrow A=U \Rightarrow A$ is orthogonal $\Rightarrow$ topics vectors (in terms of docs) are uncorrelated

## Graphs

## Properties of real world networks

- Sparsity every node connected to only small fraction of all other nodes
- but some nodes are much more connected than most others (i.e., skewed degree distribution);
- form locally dense clusters via triadic closure,
- which leads to community structure;
- have short paths between random node pairs (partly due to "hubs" [skewed degree distribution!]),
- and the short paths are easily discoverable.


## Spark

sc = SparkContext( )

print "I am a regular Python program, using the pyspark lib"

users = sc.textFile('users.tsv') \# user $<$ TAB> age

.map(lambda s: tuple(s.split((\t')))

.filter(lambda (user, age): age>=18 and age<=25)

pages $=$ sc.textFile('pageviews.tsv') \# user $<T A B>$ url

.map(lambda s: tuple(s.split("tt')))

```
counts = users.join(pages)
    .map(lambda (user, (age, url)): (url, 1)
    .reduceByKey(add)
    .takeOrdered(5)
```


## Transformations

map(func): Return a new distributed dataset formed by passing each element of the source through a function func

$\{1,2,3\} . \operatorname{map}\left(\right.$ lambda $\left.x: x^{*} 2\right) \rightarrow\{2,4,6\}$

filter(func): Return a new dataset formed by selecting those elements of the source on which func returns true

$\{1,2,3\}$.filter(lambda $x: x<=2) \rightarrow\{1,2\}$

my_set = sc.broadcast(set(range(1e80)))

rdd2 = rdd1.filter(lambda $x: x$ in my_set.value)

flatMap(func): Similar to map, but each input item can be mapped to 0 or more output items (so func should return a list rather than a single item)

$\{1,2,3\} . f l a t M a p\left(l a m b d a x:\left[x, x^{\star} 10\right]\right) \rightarrow\{1,10,2,20,3,30\}$

sample(withReplacement?, fraction, seed): Sample a fraction fraction of the data, with or without replacement, using a given random number generator seed

union(otherDataset): Return a new dataset that contains the union of the elements in the source dataset and the argument.

intersection(otherDataset): $\ldots$

distinct(): Return a new dataset that contains the distinct elements of the source dataset.

groupByKey(): When called on a dataset of ( $\mathrm{K}, \mathrm{V}$ ) pairs, returns a dataset of ( $\mathrm{K}$, Iterable $<\vee>$ ) pairs.

$\{(1, a),(2, b),(1, c)\}$. groupByKey ()$\rightarrow\{(1,[a, c]),(2,[b])\}$

reduceByKey(func): When called on a dataset of ( $\mathrm{K}, \mathrm{V}$ ) pairs, returns a dataset of $(\mathrm{K}, \mathrm{V})$ pairs where the values for each key are aggregated using the given reduce function func, which must be of type $(\mathrm{V}, \mathrm{V})=>\mathrm{V}$.

$\{(1,3.1),(2,2.1),(1,1.3)\}$. reduceByKey(lambda (x,y): $x+y)$

$\rightarrow\{(1,4.4),(2,2.1)\}$

sortByKey $($ ): When called on a dataset of $(\mathrm{K}, \mathrm{V})$ pairs, returns a dataset of $(\mathrm{K}, \mathrm{V})$ pairs sorted by keys

join(otherDataset): When called on datasets of type $(\mathrm{K}, \mathrm{V})$ and $(\mathrm{K}, \mathrm{W})$, returns a dataset of $(\mathrm{K},(\mathrm{V}, \mathrm{W}))$ pairs with all pairs of elements for each key

$\{(1, \mathrm{a}),(2, \mathrm{~b})\}$.join $(\{(1, \mathrm{~A}),(1, \mathrm{X})\}) \rightarrow\{(1,(\mathrm{a}, \mathrm{A})),(1,(\mathrm{a}, \mathrm{X}))\}$

Analogous: leftOuterJoin, rightOuterJoin, fullOuterJoin

## Actions

collect(): Return all the elements of the dataset as an array at the driver program. This is usually useful after a filter or other operation that returns a sufficiently small subset of the data.

count(): Return the number of elements in the dataset.

take( $\mathrm{n})$ : Return an array with the "first" $\mathrm{n}$ elements of the dataset.

saveAsTextFile(path): Write the elements of the dataset as a text file in a given directory in the local filesystem or HDFS.

## Counter

counter $=\mathrm{sc}$. accumulator $(0)$

def $f(x)$ : counter.add(1); return $x^{*} 2$

rdd2 = rdd1.map(f)

