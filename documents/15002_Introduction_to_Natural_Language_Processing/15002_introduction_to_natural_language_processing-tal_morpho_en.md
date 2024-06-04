# Morphology

Interest: use a priori knowledge about word structure to decompose it into morphemes and produce additional syntactic and semantic information (on the current word)

| processable $\rightarrow$ | process- | -able 2 morphemes |
| ---: | :---: | :---: |
| meaning: | process | possible |
| role: | root | suffix |
| semantic information: | main | less |

The importance and complexity of morphology vary from language to language

Some information represented at the morphological level in English may be represented differently in other languages (and vice-versa). The paradigmatic/syntagmatic repartition changes from one language to another

## Stems - Affixes

Words are decomposed into morphemes: roots (or stems) and affixes.

There are several kinds of affixes:

1. prefixes: in- -credible
2. suffixes: incred- - ible
3. infixes: Man-fucking-hattan
4. circumfixes

## Computational Morphology

The objective of computational morphology tools is precisely to go from one to the other:

- Analysis: Find the canonical representation corresponding to the surface form
- Generation: Produce the surface form described by the canonical representation

Challenge: have a "good" implementation of these two transformations

Tools: associations of strings $\rightarrow$ transducers

## String associations

$$
\begin{gathered}
\left(X_{1}, X_{1}^{\prime}\right) \\
\vdots \\
\left(X_{n}, X_{n}^{\prime}\right)
\end{gathered}
$$

(eaten, eat)

(processed, process)

(thought, think)

Easy situation: $\forall i, \quad\left|X_{i}\right|=\left|X_{i}^{\prime}\right|$

Example: $(a b c, A B C)$

$\Rightarrow$ represented as a sequence of character transductions

$$
(\mathrm{abc}, \mathrm{ABC})=(\mathrm{a}, \mathrm{A})(\mathrm{b}, \mathrm{B})(\mathrm{c}, \mathrm{C})
$$

strings on a new alphabet: strings of character couples

Not so easy: If $\exists i, \quad\left|X_{i}\right| \neq\left|X_{i}^{\prime}\right| \Rightarrow$ requires the introduction of empty string $\varepsilon$ Example: $(a b, A B C) \simeq(\varepsilon a b, A B C)=(\varepsilon, A)(a, B)(b, C)$

Where to put the $\varepsilon$ ?

Example: $(a b, A B C) \simeq(\varepsilon a b, A B C)$

but also $(a b, A B C) \simeq(a \varepsilon b, A B C)$

or $(a b, A B C) \simeq(a b \varepsilon, A B C)$

General case

$$
\binom{n}{m} \quad(\text { with } m<n)
$$

Hard problem in general $\rightarrow$ need for a convention

## Transducer (definition)

Let $\Sigma_{1}$ and $\Sigma_{2}$ be two enumerable sets (alphabets), and

$$
\begin{aligned}
\Sigma= & \left(\left(\Sigma_{1} \cup\{\varepsilon\}\right) \times\left(\Sigma_{2} \cup\{\varepsilon\}\right)\right) \backslash\{(\varepsilon, \varepsilon)\} \\
& \text { A transducer is a DFSA on } \Sigma
\end{aligned}
$$

## Transduction

Walk through the FSA following one or the other element of the couple (projections)

The fact that a transducer is a deterministic (couple-)FSA does not at all imply that the automaton resulting from one projection or the other is also deterministic!

$$
\left.\begin{array}{l}
\text { non-deterministic evaluation } \\
\text { backtracking on "wrong" solutions }
\end{array}\right\} \Rightarrow \text { The projection is not constant time (in general) }
$$

When a transducer is deterministic with respect to one projection or the other, it is called a sequential transducer

A transducer in not sequential in general. In particular if one language or the other (upper or lower) is not finite, it is not sure that a sequential transducer can be produced.

aa $\rightarrow$ ba
$\mathrm{ab} \rightarrow \mathrm{ba}$
b.bab $\rightarrow$ ba

## Operations and Regular Expressions on Transducers

$\Rightarrow$ All FSA regular expressions: concatenation, or, Kleene closure (*), ...

Example:(concatenation) "a:b c:a" recognizes ac and produces ba

- Composition of transducers: $T=T_{1} \circ T_{2}$

$$
\left(X_{1}, X_{2}\right) \in T \Longleftrightarrow \exists Y:\left(X_{1}, Y\right) \in T_{1} \text { and }\left(Y, X_{2}\right) \in T_{2}
$$

- Reduction: extraction of the upper or the lower FSA


## Computational morphology using transducers

Use of composition:

$\rightarrow$ Identification of a paradigm $\left(T_{1}\right)$

$\rightarrow$ Implementation of this paradim $\left(T_{2}\right)$

$\rightarrow$ Exception handling $\left(T_{3}\right)$

Example: input: chat+NP, fox+NP, ... ("+NP" means "noun plural")

$T_{1}:([a-z]+)(\backslash+N P \otimes \backslash+1) \quad$ paradigm identification: plural nouns (trivial here: only one paradigm $(+1))$

$T_{2}:([a-z]+)(\backslash+1 \otimes \backslash+X s) \quad$ plural inflection of nouns (regular part)

$T_{3}:([\mathrm{a}-\mathrm{z}]+)\left(\mathrm{h} \backslash+\mathrm{Xs} \otimes\right.$ hes $\left.|\mathrm{x} \backslash+\mathrm{Xs} \otimes \mathrm{xen}| \ldots \mid\left[{ }^{\wedge} \mathrm{h} \mathrm{x} ..\right](\backslash+\mathrm{X} \otimes \varepsilon) \mathrm{s}\right)$ correction of exceptions

$T_{1} \circ T_{2} \circ T_{3}:$ plural for nouns

Detailed example on the plural of nouns:

- general case: add a terminal 's'
- cat+NP $\rightarrow$ cats, dog+NP $\rightarrow$ dogs, ...

Method:

- find all the paradigms (linguists' role) and implement a transducer for each of them
- add the paradigm identification in the lexical description


## A quick reminder about noun plurals in English 

## Fully regular plurals

- default rule: Add " $s$ " to the end of the singular form}
- Examples: (dog, dogs), (arrow, arrows)


## Semi-regular plurals

Some "regular" plurals need to be modified to be easy to pronounce ("euphonic rules)

- Euphonic rule 1: if the singular noun ends in "s", " $x$ ", " $z$ ", "ch”, or "sh", add "es" instead of " $s$ "
Example : (guess, guesses), (box, boxes), (buzz, buzzes), (catch, catches), (dish, dishes)
- Euphonic rule 2: if the singular noun ends in a consonant followed by " $y$ ", change the " $y$ " to "ies"
Example : (baby, babies), (fly, flies)


## Irregular plurals

- Collective nouns (aka uncountable nouns) have no plural form Example :  (hair, ---),(mud, ---)
- Invariant nouns (aka invariable nouns) do not change when inflected to the plural
Example : "Deer have antlers"

$\rightarrow$ uncountable: "Her hair is black" is correct, while "Her hair are black" is not

$\rightarrow$ invariable: "This deer is fast" and "Deer are fast" are both correct (but do not mean the same)

## Other irregular plurals

- Case 1: For most nouns ending in " $\mathrm{f}$ " or "fe", change the ending " $\mathrm{f}$ " or "fe" to "ves"
Example :  (half, halves), (knife, knives)
- Case 2: For most nouns ending in "is", change the ending "is" to "es" (crisis, crises)
Example :  (hypothesis, hypotheses)
- Case 3: For many nouns ending in " $\mathrm{o}$ ", change the ending " 0 " to "oes"
Example : (tomato, tomatoes), (mosquito, mosquitoes)


## Fully iregular plurals

- For some (often very frequent) words, the plural corresponds to a much more complicated modification
Example : (man, men), (mouse, mice)

(foot, feet)

(tooth, teeth)

# Computational morphology for English nouns 

## Fundamentals

Goal: use transducers to represent associations between strings representing:

- surface forms, i.e. words as they appear in texts;
and
- canonical representations, i.e. formal representations of the morphological analysis of these words

Examples of surface forms: cats, book, flies, $\ldots$
Example of canonical representations: cat $+N+p$, book+N+s, fly+N+p, ...

Implementing some Computational Morphology for English nouns is finding an efficient way of representing a, potentially very large, set of (canonical representation, surface form) associations, such as:

(cat+N+s, cat) <br> cat $+N+p$, cats) <br> book+N+s, book) <br> (book+N+p, books) <br> $(\mathrm{fl} y+\mathrm{N}+\mathrm{s}$, fly) <br> fly $+N+p, f l i e s)$ <br> fox $+N+s$, fox) <br> fox+N+p, foxes) <br> deer+N+s, deer) <br> deer $+N+p$, deer) <br> (mouse $+N+s$, mouse) <br> (mouse $+N+p$, mice) <br> $(\mathrm{ox}+\mathrm{N}+\mathrm{s}, \mathrm{ox})$ <br> $(0 x+N+p, 0 x e n)$ <br> ...

By "efficient way", we mean a method that:

- allows to describe all the targeted associations without having to write them explicitly one-by-one;
- provides a computational mechanism with a low algorithmic complexity able to produce the surface form(s) associated with a given canonical representation ("generation"), or the canonical representation(s) associated with a given surface form ("analysis"


## Canonical representations

The typical format of a canonical representations is:
Lemma+GrammaticalCategory+MorphoSyntacticFeature ${ }_{1}+$ MorphoSyntacticFeature ${ }_{2}+\ldots$

where:

- Lemma (or Root) is the canonical form of an inflected word; i.e. the form usually found in dictionaries, e.g. the singular form for nouns, or the infinitive for verbs;
- GrammaticalCategory (or Part-of-Speech) is the tag used to represent the grammatical category of the word, e.g. $\mathrm{N}$ for a noun, Adj for an adjective, or $\mathrm{V}$ for a verb;
- MorphoSyntacticFeature $(k=1,2,3, \ldots)$ are the tags used to represent the morphosyntactic features (e.g. the number, the gender, the tense, the person, etc.) that are relevant to identify a specific inflection of a word;
- "+" is a (conventional) separating character.


## Examples of canonical representations

- (cat+N $\mathbf{+ p}$, cats): associating the canonical representation "cat $+\mathrm{N}+\mathrm{p}$ " to the surface form "cats" expresses in a formal way that "cats" is the flection of the noun "cat" corresponding to its plural form ("p" being the tag for the value "plural" of the morphosyntactic feature "number")
- (turn+V+Ind+Pres+3+s, turns): associating the canonical representation "turn+V+Ind+Pres+3+s" to the surface form "turns" expresses in a formal way that the surface form corresponding to the flection of the verb ("V") "to turn" at the 3rd person ("3") singular ("s") of the present ("Pres") indicative ("Ind") is "turns".

)

## How to do this with transducers?

The idea is to use the composition $T_{1} \circ T_{2} \circ T_{3}$ of 3 transducers:

1. a transducer $T_{1}$ that identifies the morphological paradigm, i.e. the systematic transformation rule(s) to be implemented for regular forms
2. a transducer $\mathbf{T}_{2}$ that implements the identified systematic rule(s)
3. a transducer $\mathbf{T}_{3}$ that handles all the exceptions to the implemented rules

## $\mathrm{T}_{1}:$ Identifying the morphological paradigm

- In English, the morphology of regular noun plurals is very simple, as it corresponds to a single systematic rule
- The morphological paradigm thus consists of only one rule, arbitrarily numbered here as rule 1
- $\mathrm{T}_{1}$ is therefore the transducer that associates a canonical representation of the form "root+N+p", where root is any possible nominal root, to the intermediate string "root+1":

$$
T_{1}=([a-z]+)((\backslash+N \backslash+p) x(\backslash+1))
$$

where " $x$ " represents the "cross-product" operator, " $\backslash$ " is a special character that prevents the character " + " to be interpreted as the Kleene plus operator, and "[a-z]" represents any alphabetic character

## $\mathrm{T}_{1}$ : Example

When applied to the list

( cat $+N+p$, book+N+p, fly+N+p, fox $+N+p$, deer $+N+p$, mouse $+N+p$, $o x+N+p)$
(cat+N+p, cat+1)

(book+N+p, book+1)

(fly+N+p, fly+1)

(fox+N+p, fox+1)

(deer $+N+p$, deer +1 )

(mouse $+N+p$, mouse +1 )

$(o x+N+p, o x+1)$

## $\mathrm{T}_{2}$ : Implementing the morphological paradigm

- The identified (single) systematic rule for English regular noun plurals is:

Add " $s$ " to the end of the root

(as, for nouns, the root corresponds to the singular form)

- $T_{2}$ is therefore the transducer that associates an intermediate string of the form "root +1 " to a new intermediate string of the form "rootXs", where the character X (called the "trace") identifies the "border" between the root and the suffix " $s$ ":

$$
T_{2}=([a-z]+)((\backslash+1) x(X s))
$$

Note: placing a trace $X$ in the new intermediate string will make it easier to handle the various exceptions to be implemented in $\mathrm{T}_{3}$

## $T_{2}$ : Example

When applied to the list (resulting from $T_{1}$ )
( cat +1 ,
book+1,
fly+1,
fox +1 ,
deer +1 ,
mouse +1 ,
0 x+1)

$T_{2}$ represents the following list of associations
(cat +1 , catXs)
(book+1, bookXs)
(fly+1, flyXs)

## $T_{3}:$ Handling the exceptions

- In this illustrative example, we will only consider 2 types of exceptions:

1. Euphonic rule 1 (simplified) :

If the root ends in " $x$ ", change the ending " $x$ " to "xes"

2. Euphonic rule 2 (simplified) :

If the root ends in " $y$ ", change the ending " $y$ " to "ies"

- $T_{3}$ is therefore the transducer that associates an intermediate string of the form "rootxXs" (resp, "rootyXs") to a new intermediate string of the form "rootxes" (resp. "rooties"), where "rootx" (resp. "rooty") is any root ending in " $x$ " (resp. "

$$
\left.\mathrm{T}_{3}=([\mathrm{a}-z]+)(((\mathrm{xXs}) \mathrm{x}(\mathrm{xes})) \mid((y X s) \times(\text { ies })) \mid([\wedge x y]]((X s) x(s)))\right)
$$

where " $[\wedge x y]$ " represents any character but " $x$ " or " $y$ "

## $T_{3}$ : Example

When applied to the list (resulting from $T_{2}$ )

( catXs, bookXs, flyXs, foxXs, deerXs, mouseXs, oxXs )
(catXs, cats)

(bookXs, books)

(flyXs, flies)

(foxXs, foxes)

(deerXs, deers)

(mouseXs, mouses)

(oxXs, oxes)

## $\mathrm{T}_{1} \circ \mathrm{T}_{2} \circ \mathrm{T}_{3}$ : Example

When applied to the original list

(cat $+N+p$,

book+N+p,

fly $+N+p$,

fox $+N+p$,

deer $+N+p$, mouse $+N+p$, $o x+N+p)$ (cat $+N+p$, cats)

(book+N+p, books)

(fly+N+p, flies)

(fox $+N+p$, foxes)

(deer+N+p, deers)

(mouse $+N+p$, mouses)

(ox+N+p, oxes)

where the first 4 associations are correct, but the last 3 (in red) are erroneous and would require a more sophisticated definition of the transducer T3 responsible for handling the exceptions

