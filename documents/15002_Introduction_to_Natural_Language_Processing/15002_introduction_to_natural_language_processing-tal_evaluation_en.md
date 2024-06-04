# NLP evaluation 

## NLP evaluation protocol

1. Define a control task
2. Produce a reference (golden truth) from a large amount of typical data (for the task)
3. Assess the quality of the reference
4. Evaluate NLP system(s) on the reference
5. Compare evaluations (statistical significance)
6. Publish and discuss results

## Example: $n$-ary classification of linguistic entities

## 1. Define a control task

Many of the tasks performed by the existing NLP tools can be generically modeled as tagging tasks, i.e.:

the NLP tool automatically assigns, to each of the linguistic entities (documents, sentences, words, ...) to be processed, a single tag selected out of a finite number of possible tags.

For example:

- a part-of-speech tagger assigns, to each of the words present in a sentence, the grammatical category this word is associated with within this sentence;
- a parser assigns, to each of the sentences present in a corpus, a tag "correct" (resp. "incorrect) depending on whether this sentence can be considered as syntactically correct (resp. incorrect) w.r.t. the grammar used by the parser;
- a language identifier assigns, to each of the documents present in a corpus, a tag identifying the language this document is written in.


## Binary vs. $n$-ary classifications

If the number of distinct tags that can be assigned by a classifier is equal to $\mathrm{n}$, the classification is generically referred to as an $n$-ary classification;

More specifically, we have:

- if $\mathrm{n}=2 \longrightarrow$ binary classification

if $\mathrm{n}=3 \longrightarrow$ ternary classification

Notice that any $n$-ary classification (using tags $t_{1}, t_{2}, \ldots, t_{n}$ ) can be decomposed into a combination of $n$ binary classifications (respectively using the two tags $t_{i}$ and "not $t_{i}$ "); however, these $n$ classifications may not be independent!

## Examples of binary and $n$-ary classifications

Examples of binary classifications:

- sentiment analysis: negative feeling vs. positive feeling
- relevance analysis: relevant vs. "not relevant"

Examples of $n$-ary classifications:

- part-of-speech tagging: as many tags as grammatical categories (e.g. Noun, Verb, Adjective, Adverb, Determiner, Pronoun, ...)
- language identification: as many tags as languages to be identified (English, French, Spanish, German, ...)


## An illustrative example: an English identifier

Consider a language identifier, i.e. an NLP tools able to automatically associate to any text (or fraction of text) a tag identifying the language it is written in (e.g. EN for English, FR for French, GE for German, ES for Spanish, etc)

If $\mathrm{N}$ languages can be identified, the language identifier corresponds to an $\mathrm{N}$-ary classifier, and ...

...if we keep all EN tags unchanged and transform all the other produced tags into a new tag notEN, we transform the $\mathrm{N}$-ary classifier into a binary classifier (one of the $\mathrm{N}$ possible ones) corresponding to an English (text) identifier, i.e. an NLP tools that determines whether a text (or a fraction of text) is written in English or not

## Need for a set of correct answers

Contrary to some other tasks, there is generally no simple way to know if a NLP system gives correct results

especially when the goal of an NLP task is to mimic something that a human can do

gold standard : set of correct answers to a task, for a sample of typical inputs for the control task

Evaluation methodology:

the sample of input is then given to the automatic system and its output is compared to the gold standard

## Reference $=$ data annotated with expected outputs

In NLP, the reference (golden truth) often takes the form of a corpus, in which each of the linguistic entities to be processed is associated with the expected (i.e. "correct") output, i.e. the output that would be produced by a human expert performing the control task.

We talk of an annotated corpus, the annotations being the outputs associated with the linguistic entities.

When the annotations are produced by humans (and not by an automated NLP system), we talk of a manually annotated corpus.

A reference is therefore a manually annotated corpus produced by humans, who can be considered as experts for performing the control task.

## Annotations can be very simple...

For example, in the case of the English text identifier, it could be a simple EN/notEN tag associated with each of the texts to be processed:

```
The cat ate the mouse EN
My tailor is rich EN
Sie ist jung notEN
Luttons ensemble notEN
El llega tarde notEN
Come on dude EN
Come state notEN
```


## ...or quite complicated!

## Example (the Penn Discourse Treebank)

Intelogic holds $27.5 \%$ of Datapoint's common shares outstanding.

(

```
(NP-SBJ (NNP Intelogic) )
(VP (VBZ holds)
    (NP
        (NP (CD 27.5) (NN %) )
        (PP (IN of)
            (NP
                (NP
                        (NP (NNP Datapoint) (POS 's) )
                        (JJ common) (NNS shares) )
                            (ADJP (JJ outstanding) )))))
(. .) )
```


## What does it mean?

The former annotation example is a parse tree representing the syntactic structure

- Gold standard creation is extremely expensive
- But globally amortized: if a gold standard exists, the whole field is likely to use it for comparison and evaluation

Notice however that a systematic reuse of the same gold standard introduces a bias to the evaluated task.

## Gold standard creation process

- Properly define the task in an annotator manual
- Select the corpus to annotate
- Train annotators:
- annotation instructions
- assess annotation quality: inter-annotator agreement (or other appropriate measures)
- Annotate


## Humans do not always agree on NLP tasks

- Despite the annotator manual, divergences always exist
- These divergences highly depend on the subjectivity of the task
- A resource is considered good only if the divergences are low
- measure : Inter-annotator agreement


## Measuring inter annotator agreement

- "Inter annotator agreement" (IAA) is considered a measure of the quality of gold standards
- It is also a measure of the subjectivity of a task
- It must be objectively measured and reported


## Raw agreement

Simplest measure of agreement:

$$
\text { raw agreement }=\frac{\mathrm{nb} \text { items agreed }}{\text { total } \mathrm{nb} \text { of items }}
$$

## Raw agreement drawback

Raw agreement doesn't take by-chance agreement into account

## Example

On a binary classification corpus having $70 \%$ of non-ambiguous items, two annotators systematically disagree about all ambiguous items:

|  |  | A |  |
| :--- | :--- | :--- | :--- |
|  |  | yes | no |
| B | yes | 0 | 10 |
|  | no | 20 | 70 |

$$
\text { raw agreement }=\frac{70}{100}
$$

They get a $70 \%$ raw agreement despite their complete disagreement!

## Dealing with chance agreement

Taking chance agreement into account:

- Idea: subtract chance agreement

$$
\frac{\text { observed_agreement }- \text { chance_agreement }}{1-\text { chance_agreement }}
$$

- Several measures exist
- Measures differ in the way they represent chance agreement


## Cohen's kappa

Cohen's $\kappa$ ("kappa") is the most famous inter annotator agreement coefficient for 2 graders only (generalization: Fleiss' kappa).

It takes each annotator into account (independently).

## Example

|  |  | A |  |
| :--- | :--- | :--- | :--- |
|  |  | yes | no |
| B | yes | 0 | 10 |
|  | no | 20 | 70 |

- Chance of saying yes: A: $0.2, \quad B: 0.1$
- Chance of saying no: A: $0.8, \quad B: 0.9$
- Chance of saying both yes if independent: $0.2 \times 0.1=0.02$
- Chance of saying both no if independent: $0.8 \times 0.9=0.72$
- Chance of independent agreement: $0.72+0.02=0.74$

$$
\begin{aligned}
\kappa & =\frac{\text { observed_agreement }- \text { chance_agreement }}{1-\text { chance_agreement }}=\frac{0.7-0.74}{1-0.74} \\
& =-0.15
\end{aligned}
$$

## Interpretation of Cohen's kappa

- Positive: better than chance
- Negative: worse than chance (correlated disagreement)

1: perfect agreement

- 0 statistical independence
- more than 0.6 is usually considered ok, and more than 0.8 considered good


## Practices

- IAA measures are almost always reported, but often only the raw agreement is given
- IAA is often only measured on a sample, sometimes on the whole corpus
- Each rest of the corpus is often annotated by only one person
- Only one annotation set is given at the end. When several annotations exist, they are merged


## Importance of separating the data

Comparing the program output to a gold standard

Methodological issue: clearly separate the data:

- Separate training (and validation) from testing

Do it fully honestly blindly randomly!! ; ;-)
- Validation set: allows to estimate overfitting or meta-parameters, clearly separated from test set (validation set is indeed a kind of training set):
- Train on the training set
- Test and adjust meta parameters on validation set
- Reduce overfitting using the validation set
- Final testing on the testing set (don't even look at it before!)
- Repeat all this several times (to estimate variance)[^0]

## The confusion matrix

 corresponding items.|  | reference |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  | A | B | C |
| $\frac{\varepsilon}{\infty}$ <br> $\frac{\Phi}{\omega}$ <br> $\omega$ | A | 35 | 2 | 10 |
|  | B | 3 | 46 | 1 |
|  | C | 5 | 6 | 12 |

The confusion matrix is not an evaluation metric (i.e. a measure) itself, but it gives complete information about the success and errors from which several evaluation metrics can be derived.

All the evaluation metrics are summaries of the confusion matrix in one way or another.

The confusion matrix represents, for each reference class, how the system classifies its

## Evaluation measures

- Standard/Usual (not specific to NLP):
- Accuracy
- Precision, Recall (and F-score)
- Dedicated ones


## Accuracy

$$
\begin{aligned}
\text { accuracy } & =\frac{\text { number of correctly classified items }}{\text { total number of items }} \\
& =\text { (normalized) trace of the confusion matrix }
\end{aligned}
$$

## Example (former English identifier)

$$
\text { accuracy }=\frac{2+3}{2+1+1+3}=\frac{5}{7} \simeq 71 \%
$$

- Can be used with any number of classes
- Used for classification tasks where all class have the same importance
- Accuracy does not take the difference between two classes into account:
- asymmetry can result from classes of different importance (e.g. diagnostic)
- or a class containing much more items than another


## A task with asymmetrical classes: information retrieval

IR seen as a binary classification task

- a document is relevant or irrelevant to a query

Example of asymmetry:

- Take a query to which 20 out of 100 '000 documents are relevant
- The perfect classifier has the following accuracy

$$
\frac{100^{\prime} 000}{100^{\prime} 000}=100 \%
$$

- The uninteresting all documents are irrelevant classifier gets

$$
\frac{99^{\prime} 980}{100^{\prime} 000}=99.98 \%
$$

For uneven classes, accuracy may not distinguish excellent from very poor systems

## Two types of error for information retrieval and similar

- False positives: documents retrieved that should not have been
- False negatives: document not retrieved that should have been

A specific confusion matrix:

|  |  | reference |  |
| :--- | :--- | :--- | :--- |
|  |  | relevant $(R)$ | irrelevant |
|  | retrieved $(S)$ | true positives | false positives |
|  | true |  |  |
|  | not retrieved | false negatives | true negatives |

## Precision, Recall and F-score

Deal with unbalanced classes:

- Use two measures instead of one:

Precision and Recall (to be defined in next slides)

F-score is a summary of the two measures

$$
\begin{aligned}
\text { precision } & =\frac{\text { correctly retrieved documents }}{\text { total number of retrieved documents }} \\
& =\frac{\text { true positives }}{\text { true positives + false positives }}
\end{aligned}
$$

- Estimates the likelihood that a retrieved document is indeed relevant to the query
- Ignores false negatives. Take only false positives into account
- Ignores non-retrieved documents. Takes only retrieved documents into account
- Could be biased by retrieving very few documents

Recall (a.k.a. "true positive rate")

$$
\begin{aligned}
\text { recall } & =\frac{\text { correctly retrieved documents }}{\text { total number of relevant documents }} \\
& =\frac{\text { true positives }}{\text { true positives + false negatives }}
\end{aligned}
$$

- Estimates (one minus) the probability to miss relevant documents
- Ignores false positives. Take only false negatives into account
- Ignores irrelevant documents. Takes only relevant documents into account
- Can be biased by retrieving all documents: gives a perfect score to the system that retrieves all documents


## F-score

- Harmonic mean of precision and recall
- The harmonic mean penalizes large divergence between numbers, contrary to other means

$$
\text { F-score }=2 \times \frac{\text { precision } \times \text { recall }}{\text { precision }+ \text { recall }}
$$

More generally (for given different emphasis to precision and recall):

$$
F_{\beta}=\left(1+\beta^{2}\right) \times \frac{\text { precision } \times \text { recall }}{\left(\beta^{2} \times \text { precision }\right)+\text { recall }}
$$

## Other NLP measures

For some specific NLP tasks, ad-hoc measures have been defined:

- BLEU (bilingual evaluation understudy) measure: $n$-gram precision-like measure for machine translation
- METEOR (Metric for Evaluation of Translation with Explicit ORdering) measure: unigram $\mathrm{F}$-score-like measure for machine translation
- ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures: $n$-gram recall-like measures for automated summarization


## Variability of the results

Whatever evaluation metric you use, measuring it only once on one single test set is not appropriate.

You shall estimate its variability (e.g. variance) as well!

This means having several different test sets...

How to?

One common way is to use so-called "cross-validation".

## Cross-validation

- Idea: using several test//earning sets splittings to get a more accurate estimation of the results

(Notice: not necessarily any validation set here, despite the name!)

- Repeat $k$ times:
- split the original data set into $n$ subsets:
- Repeat $n$ times with a different test (sub)set each time:
- use $n-1$ subsets for learning and 1 for testing
- compute evaluation using the (different) test set
- estimate variability of the results

$k \times n$ cross-validation (e.g. $2 \times 5,1 \times 10$ ): run $k$ times a (different) $n$-fold cross-validation

Note: why $k \times n$ rather than $1 \times(k n)$ ?

(increases variability; e.g. chance to have two given samples in the same subset is $\simeq k / n$ versus $1 /(k n)$.

(“ $\simeq k / n^{\prime \prime}$ is in fact $\left.1-(n-1)^{k} / n^{k}=k / n-\sum_{i=2}^{k}(-1)^{i}\binom{k}{i} / n^{i}\right)$

## Statistically significant evaluation

- Having evaluations allow to compute standard deviations of results
- Which allows to compute confidence intervals or even confidence boxes


## Comparing two systems in a statistically significant way

Simple example: (paired) Student's $t$-test: compare two classifiers on the same data of $T$ test subsets

(assuming normal distribution and equal variance; generalizations: Welch's $t$-test, ANOVA)

$\Delta_{i}$ : performance difference between the two classifiers on test subset \#i

empirical arithmetic mean: $\mu=\frac{1}{T} \sum_{i=1}^{T} \Delta_{i}$

empirical unbiased standard deviation: $s=\sqrt{\frac{1}{T-1} \sum_{i=1}^{T}\left(\Delta_{i}-\mu\right)^{2}}$

Then $t=\frac{\mu \sqrt{T}}{s}$ is compared to some threshold value for the desired confidence level.

For instance, at $95 \%,|t|$ must be bigger than 1.645 (for $T \gg 1$ )

To have a result statistically significant at more than $99 \%,|t|$ must be bigger than 2.326

## Conclusions

- NLP systems need to be evaluated in order to be objectively compared
- Most NLP task can only be evaluated by being compared to solutions done by humans
- Humans do not always agree and some tasks are subjective
- Several measure exist that need to be computed and which significance need to be statistically measured
- To get clean results, test data should never be used in anyway for development


[^0]:    ${ }^{1}$ The more so as so-called "cross-validation" is an evaluation method, done on the test set, which has

