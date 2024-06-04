# 5. CLASSIFICATION METHODOLOGY 

Internet has become a primary data source

- Data is sometimes questionable, misleading or even erroneous
- Actions taken on the basis of incorrect data can have serious consequences

Imagine we would like to solve the problem identifying fake news and fake information in the Web. This is definitely an important problem in many domains, like health, politics, eDemocracy. Evaluating fake information is a complex problem with many facets. For example, it concerns both the question of whether the sources of information are on the one hand well-intentioned, and on the other hand knowledgeable. To evaluate these factors we can consider properties both of the content that is published, but also information about the authors. So it constitutes a complex classification problem. In the following, we will describe of how such a problem could be approached, what considerations have to be taken and what pitfalls can occur.

## Classification Pipeline

### Main steps

#### 1. Data collection and preparation

- Domain knowledge and understanding essential


#### 2. Model training, selection and assessment

- Understanding potential and limits of machine learning essential

Tackling a classification problem, such as credibility evaluation requires more than just the knowledge of classification algorithms. First of all, even before starting to learn, an important task, and of the most labor-intensive is the collection and preparation of the data. This step requires in particular a good understanding of the problem domain, the questions that need to be answered and the meaning of the data that is available. Only after this step is performed, in a second step, the learning of the classification model per se can be performed. In this second step it is important to understand not only the working of the different algorithms, but also more largely, the potential and limits of learning a classification function, how the quality of learning depends both on the choice of the model and the data.

## DATA COLLECTION AND PREPARATION

## 1. Feature Identification

The first step is collecting data related to the classification task

- Definition of the attributes (or features) that describe a data item and the class label

The first step is collecting data related to the classification task. This step implies the definition of the attributes (or features) that describe a data item and the class label. In general, domain knowledge is needed to know which attributes are relevant and potentially useful for the classification task, as well as to label the data items. The choice of the class labels is also closely related to the problem that should be solved by the classification task, i.e. it represents the question to be answered.

In the case of credibility evaluation we will quickly identify a number of features that are both related to the content of documents, and those that are related to the authors of documents. Performing this step, requires first to have the fundamental insight that both content and social features are of relevance, and then to know what typical features are available, e.g. in a Web document, or about an author in a social network, as well as which of these features can be extracted or acquired.

One important task when identifying features is to distinguish them by their type: numerical, ordinal or categorical. The type of the feature has an impact on the type of classifier that can be used, as some can work only with one type of feature (e.g. categorical features). Therefore, it might be necessary to transform features into another space. We will show examples later.

## 2. Labelling

- Collecting lot of data is easy
- Labelling data is time consuming, expensive, difficult and sometimes even impossible.

Once the type of features and labels is determined, the big question is how to obtain data WITH LABELS. For example, in the case of building classifiers for credibility evaluation we would first need a corpus of documents where the document have been labelled as being credible or not. In many cases such data is not readily available, and also cannot be easily obtained. In the case of credibility evaluation the problem is complicated by the fact that often specialized expert knowledge is necessary to decide whether data is credible or not, and sometimes even experts would not agree on some questions. A nice example for this would be a document that states that climate change is occurring. This fact is not undisputed as we know.

What to do if no labelled data is available? There exist three main options:

1. We label the data ourselves manually (which is a lot of work and often boring) or we ask experts (or students) to such work, which can be expensive
2. We use crowd-sourcing, i.e. we ask non-experts at large scale. This method has recently become very popular, but has to deal with the issues that nonexperts can provide unreliable information
3. We can use some other information sources, that provide labels. For example, if we have text documents, we could identify specific names (e.g. Obama) and find then in databases other information about the name (e.g. that he is president) and use this to label the document (e.g. that this is a document talking about presidents).

## Crowdsourcing

Crowd-sourcing has become popular with platforms such as Amazon mechanical turk and is today widely used for data labelling. Here we describe how crowdsourcing works

- The requester creates a task to be performed by the crowd (= workers). For example, a collection of webpages to be labelled as Credible or Not credible
- The task is submitted to a crowdsourcing platform
- The platform distributes the task to the interested workers that provide their answers; the workers receive a payment for their work
- The requester collects the answers for further analysis


## Different Types of Crowd-Workers

One of the problems with crowd-sourcing platforms is that not all the workers are equally good. We can have different types of "bad" workers:

- Sloppy Worker: gives many wrong answers due to limited knowledge or misunderstanding of the question
- Random Spammer: gives random answers for any question (e.g. to save time)
- Uniform Spammer: gives the same answer for every question (e.g. to save time)


## Answer Aggregation Problem

Given that the labelling provided by workers might not coincide for a given question, the requester is faced with the problem of aggregating the (possibly conflicting) answers on a single label.

## Non-Iterative Aggregation Algorithms

There are two main classes of answer aggregation algorithms: non-iterative and iterative. Non-iterative algorithms take the matrix of answers provided by the workers, pre-process it and produce an estimate of the probability of the most likely answer to be correct (the most likely correct label for a webpage in our example of credibility evaluation).

## Iterative Aggregation Algorithms

Iterative algorithms take the matrix of answers provided by the worker and produce an estimate of the probability that a webpage $\mathrm{X}$ is labelled by label $\mathrm{L}$. With this estimate they update the expertise of each worker, that is, a metric that indicates how good is the worker at performing the labelling task. With this new information, the probability that a webpage $\mathrm{X}$ is labelled by label $\mathrm{L}$ is estimated again. This cycle continues until convergence.

## Majority Decision (MD)

Non-iterative aggregation algorithm

- No pre-processing step
- Estimate $P\left(x_{j}=\ell\right)$ as

$$
P\left(x_{j}=\ell\right)=\frac{1}{N} \sum_{i=1}^{N}\left(1 \mid a_{i}\left(x_{j}\right)=\ell\right)
$$

$x_{j} \quad$ webpage to label

$N \quad$ number of workers

$\ell \quad$ label

$a_{i}\left(x_{j}\right)$ answer of worker $i$ to webpage $x_{j}$

The MD algorithm is a very fast and appropriate non-iterative aggregation algorithm. It is very sensitive to spammers, since these workers have the same weight in the voting decision as good workers.

## Honey Pot (HP)

Non-iterative aggregation algorithm

- Pre-processing step
- Insert webpages $\hat{x}_{1}, \hat{x}_{2}, \ldots, \hat{x}_{k}$ for which the labels $\hat{\ell}_{1}, \hat{\ell}_{2}, \ldots, \hat{\ell}_{k}$ are known
- Remove workers and corresponding answers that fail at correctly labelling more than $m \%$ of webpages (either spammer or sloppy worker)
- Same decision rule as MD

The HP algorithm is an extension of the MD algorithm. It is also fast, but more robust to spammers than MD, thanks to the honey pot traps that helps to filter out spammers. However, trapping questions are not always available, they are often constructed subjectively. Thus truthful and good workers might be misidentified as spammers if trapping questions are too difficult or workers do not think in the same way as the requester.

## Expectation Maximisation (EM)

- Iterative aggregation algorithm
- Iterates in two steps

1. E-Step: estimate the labels from the answers of workers
2. M-Step: estimate the reliability of workers from the consistency of answers

In the EM algorithm, the probability that a webpage $\mathrm{X}$ is labelled by label $\mathrm{L}$ is computed as a weighted vote. It is the main example of an iterative aggregation algorithm. The idea is to reduce the expertise of spammers (therefore their weight in the voting is less important) during the iteration and to increase the expertise of good workers. The weighting is determined by checking the consistency of answers among the different workers.

(E) step: estimate $P\left(x_{j}=\ell\right)$ as

$$
P\left(x_{j}=\ell\right)=\frac{1}{\sum_{i=1}^{N} w_{i}} \sum_{i=1}^{N}\left(w_{i} \mid a_{i}\left(x_{j}\right)=\ell\right)
$$

(M) step: update the expertise $w_{i}$ as

$$
w_{i}=\frac{1}{M} \sum_{j=1}^{M}\left(1 \mid a_{i}\left(x_{j}\right)=\underset{\ell}{\arg \max } P\left(x_{j}=\ell\right)\right)
$$

$w_{i} \quad$ expertise of worker $i$

$M \quad$ number of webpages to label

The EM algorithm proceeds in two steps: in the E-Step, the probability of the label is estimated as a weighted vote among all workers, i.e. the normalized sum of all weights of workers voting for a specific label. In the $\mathrm{M}$ step, the expertise of each worker is updated as the number of times worker i was correct at selecting the most probable label for object x (based on the probability determined in the E-Step). Since in the M step the worker's weights chance, in the E-Step new probabilities will be computed and so on. The EM algorithm is very accurate and very robust to spammers, but slow to converge. Usually the initial weights of workers are chosen to be equal (unless pre-existing knowledge exist).

| (E) step: | $\mathrm{P}(\mathrm{x}=0)$ | 0.867 | 0.2 | 0 | 0.133 | 0.667 |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
|  | $\mathrm{P}(\mathrm{x}=1)$ | 0.133 | 0.8 | 1 | 0.867 | 0.333 |
|  |  |  |  |  |  |  |

## Discretisation Methods

### Unsupervised Discretisation

A first approach to discretization is unsupervised discretization. Unsupervised discretisation do not take class information (labels) into account. These methods have the following strengths and weaknesses:

- The obvious weakness of the equal-width method is that in cases where the feature values are not distributed uniformly, a large amount of important information can be lost after the discretization process, e.g. with many very sparsely populated bins.
- For equal-frequency discretization, many occurrences of the same value could cause those occurrences to be assigned into different bins, which does not make sense. This problem could be addressed by merging neighbouring bins that contain duplicate values.
- The advantage of using clustering as discretisation method is that it can be performed on all the features at the same time, capturing in this way possible interdependencies of the features. Sometimes discretisation can even improve the performance of algorithms that do not need discretisation.


### Supervised Discretisation

Idea: if the class label does not depend on the choice among two (adjacent) intervals, the separation of the intervals does not provide useful information to the classifier

$$
\begin{aligned}
& \text { Independence test: } \chi^{2} \text { statistics } \\
& \\
& \mathrm{O}_{\mathrm{ij}} \text { observed frequency } \\
& \text { Interval } 2 \quad R \\
& \mathrm{E}_{\mathrm{ij}} \text { expected frequency } \\
& \begin{array}{cccc} 
& \mathrm{E}_{21}=(\mathrm{R} 2 \times \mathrm{C} 1) / \mathrm{N} & \mathrm{E}_{22}=(\mathrm{R} 2 \times \mathrm{C} 2) / \mathrm{N} & \\
\end{array} \\
& \chi^{2}=\sum_{i=1,2} \sum_{j=1,2} \frac{\left(O_{i j}-E_{i j}\right)^{2}}{E_{i j}}
\end{aligned}
$$

\$\$

In order to test the independence of two adjacent intervals, one can use the $\chi^{2}$ statistics. $\mathrm{E}_{\mathrm{ij}}$ is the expected frequency of the number of distinct values in the ith interval belonging to the jth class, while $\mathrm{n}_{\mathrm{ij}}$ is the observed frequency. $\mathrm{N}$ is the total number of values.

## Supervised Discretisation

Null hypothesis: Assumes that the class label is independent of the feature intervals

If $\mathrm{P}\left(\mathrm{X}^{2} \mid D F=1\right)>0.05$ (independent), merge the intervals $D F=$ degrees of freedom $=(\# \text { rows-1 })^{\star}(\#$ cols -1$)$.

If the probability of the computed $\chi^{2}$ value is greater than a threshold $p$ (typically 0.05 or 0.01 ), the two intervals are independent and can be merged (Pearson's chi squared test).

In statistics, the number of degrees of freedom is the number of values in the final calculation of a statistic that are free to vary.

Pearson's chi-squared test $\left(\chi^{2}\right)$ is a statistical test applied to sets of $\underline{\text { categorical }}$ data to evaluate how likely it is that any observed difference between the sets arose by chance.

## Example

| observed | No | Yes | SUM |
| :--- | ---: | ---: | ---: |
|  | 51 | 0 | 51 |
| Interval 2 | 1 | 50 | 51 |
| SUM | 52 | 50 | 102 |


| expected | No | Yes |
| :---: | :---: | :---: |
| Interval 1 | 26.00 | 25.00 |
| Interval 2 | 26.00 | 25.00 |


| chisquare statistics | No | Yes |
| :--- | :--- | :--- |
|  | 24.04 | 25.00 |
| Interval 2 | 24.04 | 25.00 |


| chisquare | 98.0769231 | Percentage Points of the Chi-Square Distribution |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | ![](https://cdn.mathpix.com/cropped/2024_05_17_ccc0c0a39ad39a5a083fg-33.jpg?height=46&width=71&top_left_y=994&top_left_x=1101) | Protustity of stwper nhe of of $x^{2}$ |  |  |  |  |  |  |  |  |
| P(chi \| df = 1) | $4.0244 \mathrm{E}-23$ |  | 0.59 | 0.95 | 0.00 | 0.75 | 0.50 | 0.85 | 0.10 | 0.05 | 0.01 |

p-value of $4.0244 \mathrm{e}-23$ is less than $0.05 \rightarrow$ we reject the null hypothesis (there is a dependence $\rightarrow$ no merge)

## Feature Selection

Reducing the number of $N$ features to an optimal subset of $M$ features, $M<N$.

There are $\binom{N}{M}$ possible subsets

### Approaches

- Filtering: consider features as independent
- Wrapper: consider dependencies among features

There are $N$ choose $M$ possible subset (choosing a subset of $M$ features from a fixed set of $N$ features).

Exhaustive exploration of all possible subset of features is impossible, therefore some heuristics must be used.

We will discuss two classes of approaches, filtering and wrapping, that differ in the assumptions made on feature dependency.

## Feature Selection: Filtering

Filtering: rank features according to their predictive power and select the best ones

Pros

- Independent of the classifier (performed only once)

Cons

- Independent of the classifier (ignore interaction with the classifier)
- Assumes features are independent

Filtering starts from the assumption that features are independent. Thus the predictive power of each feature can be evaluated independently, and finally the top features are chosen. It also assumes that the choice of features is independent of the classifier used. Thus it can be performed without interacting with the classifier, and potentially as a result revise the selection of the features.

- $P\left(X^{2} \mid D F=n-1\right)$ gives a rank measure

For ranking features we can use the same idea that was used in the discretization of continuous features. We perform an independence test between the feature values and the class labels. Since we now consider multiple feature values (and a binary classification) we have instead of 1 degree of freedom, $n-1$ degrees of freedom, that have been considered in the independence test.

## Information-theoretic approach

Mutual information between feature $F$ and class label C

$$
\begin{aligned}
& I(F ; C)=H(C)-H(C \mid F)=H(F)+H(C)-H(F, C) \\
& H(F)=-\sum_{i} P\left(f_{i}\right) \log _{2} P\left(f_{i}\right) \\
& H(F, C)=-\sum_{i} \sum_{j} P\left(f_{i}, c_{j}\right) \log _{2} P\left(f_{i}, c_{j}\right)
\end{aligned}
$$

Alternatively, we measure the mutual information between a class label $C$ and a feature $F$. Mutual information measures the information that $F$ and $C$ share. It measures how much knowing one of these variables reduces uncertainty about the other. If $I(F, C)=0$, knowing $F$ does not tell anything about $C$, when $I(F, C)$ is maximal, by knowing $F$ we already know $C$.

## Selection of Features - Pitfalls Correlation $\neq$ Causality

When eliminating features, we have to be careful to not emphasize features that are only accidentally correlated with the class labels. In general, correlation does not imply causality, and we can find many examples of so-called spurious correlations illustrating that point. Be aware, that such curious correlations are often used to prove statistically "facts" that or no existent.

Collectively relevant features may look individually irrelevant.

An important drawback of the filtering approach to feature selection is the independence assumption for features. In fact, it is easy to see, that combined feature can have a high classification power, whereas each of the features alone have not. This motivates the use of more complex methods for feature selection, such as wrapping.

## Feature Selection: Wrapping

### Iteratively add features

- at each iteration create a classifier for each new feature and evaluate its performance
- Add best feature or stop when no further improvement

Pros

- Interact with the classifier
- No independence assumption

Cons

- Computationally intensive

The wrapper method starts with no features and add the features that provide the highest improvement in classification accuracy The wrapper method can also work the other way around, considering all the features at the beginning and iteratively removing the feature that harms the classification accuracy the least. The method avoids some of the pitfalls of feature filtering, at the price of significantly higher cost.

## 5. Feature Normalisation

Some classifiers do not manage well features with very different scales

Features with large values dominate the others, and the classifier tend to over-optimise them

Some classifiers and performance evaluation methods are sensitive to the absolute values of the features. Then the features should be normalized to comparable scales.

## Standardisation and Scaling

Standardisation: map to a normal distribution $N(0,1)$
The new feature $x_{i}^{\prime}$ has mean 0 and unit variance

Min-Max Scaling: map to interval $[0,1]$

Standardization makes the underlying assumption that the (numerical) data is normally distributed. Then it makes sense to map to a normal distribution with mean 0 and variance 1 . An alternative is to map directly into a standardized $[0,1]$ interval.

## Standardisation vs Scaling

Standardisation

- Assumes that the data has been generated by a Gaussian process (not necessarily true)

Scaling

- If the data has outliers, they scale the "normal" values to a very small interval

Standardisation assumes that data has been generated by a Gaussian process, which is not always true. Scaling is not good if there are outliers, and almost all datasets have outliers. Such outliers risk to "compress" the relevant data in a very small interval, which would e.g. be harmful of some discretization is applied.

## MODEL TRAINING, SELECTION AND ASSESSMENT

## 1. Choosing Performance Metrics

Model Assessment

Once the dataset is ready, we start to learn a model. For the learnt model we need to evaluate its performance, by testing which error it produces for a test data set. That is why we hold out a subset of the available data as test data, that is not used in the training and is independent of the training data. This step is called model assessment. The error obtained in model assessment is a good estimate of the true error that it will commit once it is "in production".

## Performance Metric for Binary Classification

For categorical binary classification, the usual metrics consider four types of outcomes

Correct results

- True Positive (positive examples classified as positive)
- True Negative (negative examples classified as negative)

Incorrect results

- False Positive (negative examples classified as positive)
- False Negative (positive examples classified as negative)

In order to do model assessment we have to choose the performance metric for evaluating the error. We will present this in the following for the case of binary classification with a categorical label. In such a case we have for possible types of outcomes, true positives and negatives, and false positives and negatives. We represent these outcomes as a matrix.

## Accuracy

$$
A=\frac{T P+T N}{T P+T N+F P+F N}=\frac{T P+T N}{N}
$$

## Appropriate metric when

- Classes are not skewed
- Errors have the same importance

The most basic metric is the accuracy, that is, the total correct examples divided by the total examples to be classified. Accuracy is thus in the interval $[0,1]$.

Accuracy is appropriate if the examples are approcimtaely equally split between class $\mathrm{A}$ and $\mathrm{B}$, and if $\mathrm{FP}$ and $\mathrm{FN}$ have the same importance as error.

## Accuracy - Pitfall

Here we give an example of skewed classes, where the majority of data available refers to No Fraud, and only few examples belong to the class Fraud. Accuracy as a performance metrics is inappropriate in case of such skewed label distributions. The typical problem is that a trivial classifier that classifies everything as belonging to the majority class, can achieve easily higher accuracies than a classifier that attempts to also correctly classify samples in the minority class.

## Precision

$$
P=\frac{T P}{T P+F P}
$$

## Recall

$$
R=\frac{T P}{T P+F N}
$$

As the example in the previous question illustrates, apart from issues with skewed distributions, accuracy has also an issue when the importance of errors is not equal, e.g. when false negatives are much worse then false positives. In such a case we can use the measures of precision and recall that we have already introduced in the context of information retrieval.

With precision and recall we can better control the kind of results we prefer. For example, for the case of cancer detection we would prefer to have higher recall to miss fewer cancer cases, even if we diagnose erroneously cancer in a few cases. Therefore, classifier 1 would be preferred over classifier 2 (which did better in terms of accuracy). Of course we can increase the recall arbitrarily, e.g. with a trivial classifier diagnosing cancer for everyone. But this also causes that $50 \%$ of the patients with no cancer go home worried about their health status That is why still precision needs to be considered in the evaluation as second measure.

Note that by using precision and recall we make the evaluation "assymmetric". We focus in the evaluation on the positive class, since higher recall means more positive cases identified.

## F-score

$$
\begin{array}{ll}
\text { F-score (or F1-score) } & F 1=2 \cdot \frac{P \cdot R}{P+R} \\
\text { F-beta score } & F_{\beta}=\frac{\left(1+\beta^{2}\right) P R}{\left(\beta^{2} P+R\right)}
\end{array}
$$

As in information retrieval, we sometimes would like to compare classifiers using a single measure. In this case we can also use F-Score. F-score is the harmonic mean of precision and recall. Precision and Recall can be differently weighted, if one is more important than the other using F_beta score, where beta is a real number.

## 2. Model Selection

Usually a classifier has some parameters to be tuned

- Regularisation factor
- Threshold
- Distance function
- Number of neighbours

Model Selection: Estimating performances of different models to select the best one

Usually for a given type of classifier, we have one or several parameters that can be tuned. This means that we can produce many different classifiers for the same training set, and then select the one with the best performance (according to the performance metric that has been selected). This process is called model selection.

## Model Selection

Model selection also needs evaluation of error, but in this case not to determine the performance of a classifier on unknown data, but to select the best model. If, on the other hand, we want to still evaluate the performance of the resulting final model, we need to distinguish two types of data that is used for evaluating model performance. The validation date that is used to select the best model, and the test data that is used to assess the performance of the finally resulting model.

## Model Selection

![](https://cdn.mathpix.com/cropped/2024_05_17_ccc0c0a39ad39a5a083fg-66.jpg?height=477&width=1276&top_left_y=583&top_left_x=403)

Once the validation data is given, the process of model selection is straightforward: different parameters of the model are chosen, models are trained on the training set using those parameters, the resulting models are evaluated using the validation data, and the process stops when a model with appropriate parameters is found (or the parameter space is exhausted).

The typical situation in model selection is that for a changing parameter the loss function has a local minimum, which indicates the parameter with the best performance. In the context, of model one uses the term loss function instead of performance metric, in order to formulate the search for an optimal model as a minimization problem. However, the are equivalent. For example, if the performance metric would be the accuracy $\mathrm{A}$, then the loss function $\mathrm{J}$ would be taken as $\mathrm{J}=1-\mathrm{A}$

## Loss Function (Error Function)

Categorical output

- 0-1 loss function: $J=\sum_{i=1}^{n} \#\left(y \neq f\left(x_{i}\right)\right)$


## Real value output

- Squared error: $J=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-f\left(x_{i}\right)\right)^{2}$
- Absolute error: $J=\frac{1}{n} \sum_{i=1}^{n}\left|y_{i}-f\left(x_{i}\right)\right|$

Here we give different examples of loss functions. The 0-1 loss function used for categorical functions to be learnt, essentially corresponds to accuracy (without normalization). For learning functions that return numerical outputs, the squared error or the absolute error can be used as loss function.

Here $\mathrm{x}_{\mathrm{i}}$ indicates a feature and $\mathrm{y}$ is the class label.

## 3. Training and Validation Set

The simplest way to do model selection is constructing a training and validation set.

The drawback of this approach is that it does not use all the data to train, and it is possible that the validation set is not representative for the classification tasks (e.g., rare cases are missed).

In order to address the drawback of holding out a simple validation set, a better approach is to split the training set into $\mathrm{k}$ partitions, and train a model for each subset the dataset where one of the partitions has been removed as validation set. Then the model is evaluated against the validation set that has been held out. Finally the performance as averaged over all $\mathrm{k}$ runs. K-fold cross-validation is a good compromise between having an unbiased estimate of the true accuracy and reasonable computation time.

## Leave-one-out Cross Validation

Leave-one-out Cross Validation is the extreme form of k-fold cross-validation, where each individual data item is considered as a separate partition. Leave-oneout is most unbiased estimate of the true accuracy, however is time consuming because it performs a number of iterations equal to the number of examples in the dataset.

## Skewed Distributions

Some class labels might be heavily skewed, e.g.

- Non-Fake pages 10000
- Fake pages 10

As for performance evaluation, also for creating suitable validation sets, skewed data distributions pose problems. Rare data points might be simply missed in the validation set, and this the performance evaluation becomes questionable.

## Fighting Skew

## Stratification

- Select validation set as random sample, but assure that each class is (approximately) proportionally represented


## Over- and Under-Sampling

- Including over-proportionally number from the smaller class (over-sampling)
- Including under-proportional number from larger class (under-sampling)

In order to avoid the above mentioned problems more sophisticated approaches for constructing the validation set are required.

Stratification chooses for each class a random sample of a size that is proportionally to the overall representation of the class. In this way it is avoided to miss classes completely in the validation set. This approach can also be taken when using $\mathrm{k}$-fold cross-validation.

With over- and undersampling, small classes are emphasized whereas large classes are under-emphasized. Many variations of such sampling methods have been proposed, including some that generate artificial data points for underrepresented classes.

## Evaluating the error

$$
\operatorname{Err}\left(f_{D}, T\right)=\frac{1}{|T|} \sum_{X \in T}\left(f_{D}(X)-y\right)^{2}
$$

$D=$ Training set from which the model is learnt

$\mathrm{T}=$ Validation set on which error is evaluated

Squared error measure

So far we have assumed that the choice of model parameters influences the quality of a model in model selection, but we have no clear understanding what are the factors that are driving the quality of a model. Having such an understanding is essential, in order to devise strategies to find good models. This is what we want to investigate in the following in greater detail.

To start with, a model is nothing else than a function $f_{D}$ that approximates some function $f$. The function $f_{D}$ has been learnt from a training set $D$ and is evaluated using a validation set $\mathrm{T}$. In the following we will use the squared error model. Under this model we can compute the error of the function when evaluated using the validation set.

## Training and Test Error

Evaluate error on training set $D$ : training error

$$
E r r_{\text {train }}=\operatorname{Err}\left(f_{D}, D\right)
$$

Test model with an independent test set $\mathrm{T}$ : test error

$$
\operatorname{Err}_{\text {test }}=\operatorname{Err}\left(f_{D}, T\right)
$$

The error function can be evaluated on different data sets. We can evaluate on the training set itself, which results in the training error, and we can evaluated it on the test set, which results in the test error. An interesting question is whether it is useful to evaluate the training error, and how it behaves compared to the test error.

## Comparing Training and Test Error

This figure illustrates the comparison between training an test error. On the x-axis we see increasing model complexity, on the $y$-axis increasing prediction error. Models of different complexity have been built multiple times, using different training sets and both the test error (red) and training error (blue) have been evaluated. The bold lines average over the different training sets for which the models have been built. If we look at the training error, we see that it decreases as the model becomes more complex. This corresponds to the fact that the model can capture more properties of the training data, as it has more parameters. However, this does not mean that the model becomes better. This is illustrated when looking at the test error. Initially, also the test error decreases as the model becomes more complex. We see that it has lower bias. But at a certain point the tendency changes and it increases again. This is the point where the model starts to overfit the training data, and this as soon as new data is tested against the model, it performs worse. For the test error, we also observe that the spread of the different lines increases as the model complexity increases. Thus the model is in some sense less stable, we say it has higher variance.

## Expected Errors

Repeatedly evaluate error for different models generated from different training sets $D \in \mathcal{D}$ and corresponding test sets $T(D)$

Expected training error

$$
E E \operatorname{Err}_{\text {train }}=E_{\mathcal{D}}\left[\operatorname{Err}\left(f_{D}, D\right)\right]=\frac{1}{|\mathcal{D}|} \sum_{D \in \mathcal{D}} \operatorname{Err}\left(f_{D}, D\right)
$$

## Expected test error

$$
\begin{aligned}
& E E r r_{\text {test }}=E_{\mathcal{D}, T}\left[\operatorname{Err}\left(f_{D}, T(D)\right)\right] \\
& =\frac{1}{|\mathcal{D}|} \sum_{D \in \mathcal{D}} \operatorname{Err}\left(f_{D}, T(D)\right)
\end{aligned}
$$

We now will formally introduce the notions of bias and variance, by analyzing the expected errors that we obtain from generating multiple models from different training sets. We can define the expected training error, respectively the expected test error as the expectation of the error that is obtained from building models over multiple training sets. For computing the expected test error we also assume that for each training set $D$ some test set $T(D)$ is used (as e.g. in crossvalidation). Note, that does not correspond exactly to the approach that is taken with cross-validation, where $\mathrm{D}$ and $T(\mathrm{D})$ are always derived from the same dataset, but this formulation is easier to handle analytically.

## Bias and Variance

The error can be rewritten as follows

$$
E_{E r r_{\text {test }}}=\text { Bias }^{2}+\text { Variance }
$$

Using some basic arithmetic we can rewrite the expression for the test error in two components, bias and variance. For computing bias we compute the expected error of the model with respect to the true value, averaging over all training sets $D$ and data points $X$ in the test set $T(D)$. For a given data point $X$ we can compute the expected estimate $\bar{f}(X)$ by averaging over all training sets $\mathrm{D}$. Using this expected estimate we can compute the variance as the expected square of the difference between the expected estimate $\bar{f}(X)$ and the model $f_{D}(X)$, again averaging over all training sets $D$ and data points $X$ in the test set $\mathrm{T}$ (D). In this way we have isolated the two different contributions to the test error, called Bias and Variance.

## Bias / Variance and Model Complexity

There is usually a bias-variance tradeoff caused by model complexity

Complex models (many parameters) usually have lower bias, but higher variance

$\rightarrow$ over-fitting

Simple models (few parameters) have higher bias, but lower variance

$\rightarrow$ under-fitting

Empirical and analytical studies have revealed that there is bias-variance tradeoff that is related to the model complexity. Ideally we would like to have a low bias and low variance. This is however not possible as with decreasing bias of the test error in general variance increases. Generally, complex models lower the bias (up to a certain point) but increase variance, resulting in overfitting, and for simple models the inverse is true.

## Bias / Variance and Data Volume

High variance

When looking in more detail on the question whether more training data helps the question is not so clear-cut. Other experiments have shown, that more data helps, if the variance is high, i.e. over-fitting occurs. Then more data can indeed help. Intuitively, this is the case because the models are more complex and have thus more capacity to absorb information from the training data.

Putting all these insights together we can come to the following conclusions for the 4 possible scenarios of bias and variance:

- When bias and variance is low, nothing is to be done, we have a good model.
- When bias and variance are both high, nothing is to be done, we have probably a problem that is too difficult to learn
- When bias is low, but variance is high, we have overfitting: we can either reduce the complexity of the model, or add more data.
- When bias is high, but variance is low, we have underfitting: we can increase the complexity of the model

