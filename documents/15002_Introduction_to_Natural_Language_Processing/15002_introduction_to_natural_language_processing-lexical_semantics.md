# Lexical Semantics 

## Lexical Semantics vs. Compositional Semantics

- Lexical semantics: The study of the meaning of words
- Word meaning is:
    - structured, i.e. words have lexical relationships
    - context-sensitive, i.e. can vary with different contexts
- Compositional Semantics: the study of the meaning of linguistic sentences
- Words contribute to the meaning of sentences but don't have a meaning by themselves
- Example: "John likes Mary” -> likes(John,Mary)


## Compositional Semantics

- Compositional Semantics is the study of the meaning of complex linguistic units such as sentences, paragraphs, or documents
- A standard approach for exploring compositional semantics with human subjects are reading tests


## How could this be automated?

- We need to be able to convert the information expressed in linguistic units into some exploitable (formal) representation
- For a formal representation, to be exploitable means, among others, that:
    - it can be modified through various transformations, also expressed in linguistic terms;
    - it can the subject of various analysis (e.g. counting some of its constituents), also expressed in linguistic terms.


## Usual representations

- Symbolic representations:

$>$ various formal logics: the meaning is expressed as a logical formula that can then be manipulated through various inferential mechanisms;

$>$ various graph based representations: the meaning is expressed as a graph that can then be manipulated through various graph transformations;

- Vectorial representations:

$>$ typically approaches based on "distributional semantics" (e.g. Word embeddings): the meaning is represented as a vector in a (usually high dimension) vector space and can then be manipulated through vector based operations (e.g. weighted sums, projections, etc.)

- Currently, only vectorial representations can be deployed at a large scale because:

>it is extremely difficult (if not impossible) to guarantee the consistency of large sets of logical propositions derived from textual input, which often makes the inferential mechanisms very hard to use;

> there isn't yet a consensus neither on which are the most suitable graph based representations (semantic nets? Conceptual graphs? ...) for expressing the meaning of linguistic entities, nor on which are the proper operations to be applied to these representations;

- ... but the associated vector based operations seems to be too simplistic for suitably mimicking the transformations that are required to manipulate linguistic meaning.


## Intermediate conclusion

- Large scale Compositional Semantics is still out of reach, and
- This lecture will therefore restrict on a simpler form of semantics, the semantics of individual words, e.g. Lexical Semantics


## The triangle of signification [Frege]

- Minds grasp senses,
- Words express them,
- Objects are referred to by them


## Lexical Semantics

- Lexical Semantics is the study of the meaning of words (i.e. of the simplest linguistic units)
- A standard approach for exploring lexical semantics for human subjects are dictionaries (not to be confused with encyclopedias which are not concerned with word meanings but with comprehensive information about subjects/topics/fields from the real world)

Note: In this course, a dictionary (especially when tailored for some automated processing) will also often be called a lexicon

## Lexeme

- An individual entry in the lexicon
- A pairing of a particular orthographic and phonological form with some symbolic meaning representation

| Orthographic <br> form | Phonological <br> form | Meaning |
| :--- | :--- | :--- | :--- |
| 1. bass | [beys $]$ | adj. low in pitch; a bass instrument |
| 2. bass | $[$ bas $]$ | n. (...) freshwater or marine fishes (...) |
| 3. wood | [woo d] | n. (...) substance of a tree (...) |
| 4. would | [woo d] | v. A pt. and pp. of WILL |

## Lexicon

- Finite list of lexemes
- Can include
- Compound nouns
- Other non-compositional phrases, e.g. proper names


## Word sense

- A lexeme's meaning component
- Different dictionaries have different notions of word senses, how to represent them and how to split them
- A word sense can be represented for example as :
- A text description
- A definition based on it's relationship to other lexemes ("is a", "has a")


## Lexical semantics vs. Compositional semantics

- If the different meanings (aka senses) of a words are defined by well chosen definitions in natural language (as it is the case in dictionaries), we are faced with a vicious circle:
    - understanding the meaning (i.e. making it exploitable) of the different senses of a word (lexical semantics) requires to understand the meaning of the associated definitions and thus the availability of some form of compositional semantics...
- To break this vicious circle, natural language cannot be used to define the various meanings of a word and some more formal representations must be used instead; in this course, we will consider two types of formalisms:
    - semantic relations, and
    - synsets (see the slides on Wordnet)


## Semantic Relations

### Homonymy

- A relation that holds between words that have the same surface form but different meanings
- Bat ${ }^{1}$ : The wooden club used in certain games
- Bat ${ }^{2}$ : Flying mammal of the order Chiroptera
- Homophones: distinct lexemes with the same pronunciation (wood, would)
- Homographs: distinct lexemes with the same orthographic form (bass [bas], bass [beys])


### Homonym, homophony, homography

- Homophony: two distinct words are homophones is they have the same pronunciation (i.e. the same "phonological form")

Example: "die" and "dye"

- Homography: two words are homographs if they are spelled the same (i.e. have the same "orthographic form") but not pronounced the same

Example: "bass" (the fish) and "bass" (the guitar)

- Homonymy: two words are homonyms if they are spelled and pronounced the same, but do not have the same meaning Example: "bat" (the wooden club) and "bat" (the flying mammal)


### Polysemy

- A relation that holds between multiple related meanings within a single lexeme

| Orthographical <br> form | Meaning |
| :--- | :--- |
| Crown | 1. Headgear worn by a monarch <br> 2. The highest part of anything, e.g. a tree <br> 3. The part of a tooth that is covered by <br> enamel <br> $\ldots$ |

### Homonymy vs. Polysemy

- Both homonyms and polysems are spelled and pronounced the same but ...
- homonyms have a different etymology and usually correspond to two distinct entries in a lexicon, while polysems share the same etymology but correspond to two different meaning of the same lexicon entry

Example:

> "bat" (the flying mammal) comes from a dialectal variant of the M iddle English "bakke", while "bat" (the wooden club) comes from the Old English "batt", while

> "crown" (the headgear) and "crown" (the highest part) both come from the Anglo-Norman "coroune"

### Types of polysemy

- Metaphor
- "Germany will pull Slovenia out of its economic slump"
- "I spent 2 hours on that homework"
- Metonymy
- "The White House announced yesterday"
- "This chapter talks about part-of-speech tagging"
- Bank (building) and bank (financial institution)


### Synonym

- Two words are synonymous if they have the same sense
- Criteria for synonymy:
- They have the same value for all their semantic features
- They map to the same concept
- They satisfy the Leibniz substitution theory
- The substitution of one for the other never changes the truth value of a sentence in which the substitution is made
- Example of non-synonyms:
- Tony is the big brother
- Tony is the large brother


### Hyponymy

A hyponym is a word whose meaning contains the entire meaning of another, known as the superordinate or hypernym.

### Overlap

Two words overlap in meaning if they have the same value for some (but not all) of the «semantic features».

- Hyponymy is a special case of overlap where all the features of the hypernym is contained by the hyponym.


### Meronymy/Holonymy

- A word $\mathrm{w} 1$ is a meronym of another word w2 (the holonym) if the relation is-part-of holds between the meaning of $w 1$ and w2.
- Meronymy is transitive and asymmetric
- A meronym can have many holonyms
- Meronyms are distinguishing features that hyponyms can inherit.
- Ex. If "beak" and "wing" are meronyms of "bird", and if "canary" is a hyponym of "bird", then (by inheritance), "beak" and "wing" must be meronyms of "canary".
- Limited transitivity:
- Ex. "A house has a door" and "a door has a handle", then "a house has a handle" (?)


### Different type of meronymic (partwhole) relationships

- Component-object (branch/tree)
- Member-collection (tree/forest)
- Portion-mass (slice/cake)
- Stuff-object (aluminium/airplane)
- Feature-activity (paying/shopping)
- Place-area (Lausanne/Vaud)
- Phase-process (addolescence/growing up).


## Intermediate conclusion

- In a relation based approach to Lexical Semantics, the word meanings are defined as the nodes of a directed graph the arcs of which correspond to various semantic relations
- The targeted semantic graph is built with the main purpose of correctly differentiating the various meanings of the words (which is one of the primary objectives of Lexical Semantics), and, as such, it will most often lead to a semantic model that will not be sophisticated enough to more advanced exploitations such as the automated generation of the answers to the questions asked in the simple reading test given at the beginning of the lecture; for this the semantic model will have to be embedded in a more complex one providing the possibility to produce semantic representation for more complex linguistic units than words (Compositional Semantics)


## Synsets

- Synset is the set of word forms that share the same sense
- Synsets do not explain what the concepts are, they signify that concepts exists
- Hypothesis: A synonym is often sufficient to identify the concept.


## How is meaning represented?

- Differential approach (Wordnet)
- Meanings (concepts) are represented as a list of word forms that distinguish their meaning from other meanings: the synset.
- No two synsets should have exactly the same set of word forms
- Constructive approach (conventional dictionaries)
- the meaning representation (e.g. dictionary gloss) has to contain sufficient information to accurately define a concept
- Not so easy, definitions are often cyclic
- Tree: "a plant having a permanently woody main stem or trunk..."
- Wood: "the hard, fibrous substance composing most of the stem and branches of a tree"
- Conventional dictionaries rarely meet this requirement


## Application of lexical semantics in language engineering

## Applications of lexical semantics

Applications

- Speech processing
- Linguistic analysis
- Information Retrieval
- Information Extraction
- Machine translation
- Cohesive extractive summarization
- Spelling error correction
Tasks
- Word sense disambiguation
- Lexical cohesion
- A group of words is lexically cohesive when all of the words are semantically related; for example, when they all concern the same topic.
- Lexical cohesion can be computed using lexical semantic resources (thesaurus)
- Semantic indexing
- Semantic role labeling


## Lexical semantics in Speech Processing

- Text to speech
- WSD
- Choose the right pronunciation of a word depending on the word sense
- Speech recognition
- WSD
- Choose the right word among possible words with the same pronunciation (homophones)
- Lexical cohesion
- A measure of lexical cohesion can be used to recognize when speech recognition software has made errors. The incorrect words usually do not cohere with the rest of the


## Lexical semantics in Information Retrieval

- Semantic indexing
- Indexing word senses instead of words
- Improves
- Recall by handling synonymy
- Precision by handling homonymy and polysemy

Example 1: Different indexing of the term "Java"

- Programming language
- Type of coffee
- Location

Example 2: a query for "cars" will also return a document that mentions only "automobiles"

- Indexing schemes

a) Standard indexing with words (stems or lemmas)
b) Indexing with a semantic ontology, each indexing term is extended with all the hypernym senses
c) Synset (or hypernyms synsets) indexing, each indexing term is replaced with it's hypernym synset
d) Minimum Redundancy Cut (MRC) indexing, each indexing term is replaced with it's dominating semantic concept defined by MRC

## Lexical semantics in Spelling Error Correction

- In some cases a spelling error can result in a real word in the lexicon and therefore cannot be detected by a conventional spell checker

Example: It is my sincere hole [hope] that you will recover soon

- Such errors can only be detected by computing lexical cohesion and identifying tokens that are semantically unrelated to their context

