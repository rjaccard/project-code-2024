
## Chapter 1 Ancient Cryptography

This chapter focuses on encryption. It introduces elementary notions of cryptography, terminology, and important historical milestones. Basic principles such as the Kerckhoffs principle is stated. An approach of cryptography based on information theory is made. Essentially, we state what is the perfect notion of secrecy and what is the optimal way to achieve it.

Cryptography used to focus on enforcing the confidentiality of communication. During the
"prehistory" of cryptography, it was used for military purposes, to protect business, private affairs. When it is used between two determined individuals, this can be done by establishing a secret convention to encode information. We refer to this as *security by obscurity*. This paradigm has some limitations, especially when one needs to communicate with more people, as it is cumbersome to invent a new convention each time. For that, some systems started to use the concept of an easy-to-configure *secret key*: people can use the same system, possibly developed by others, or even public, but select private keys on their own. The trend was to use more automatic procedures with the raise of the industrial era for communication. Finally, the *Kerckhoffs principle* was stated: the security should only rely on the secrecy of the key. (This will be discussed later.) The prehistory ended this way.

The *industrial era* was strongly influenced by the raise of the industrial communication (e.g., based on radio), and by the raise of industrial computing (namely: computers). Mass communication made the problem of selecting common algorithms more severe. Automatic computing made the security of cryptographic system more complicated since, suddenly, we could not bound the effort to break a system with the limit of humans, but could suddenly rely on new automatic devices which could work with virtually no limit.

Modern cryptography was marked by several results which appeared in different periods: the development of information theory and Shannon's result on cryptography, the appearing of public standards for cryptography such as DES, and the discovery of public-key cryptography in the 1970's.

## 1.1 Scope Of Cryptography

There are a few technical terms which should be correctly used.

A *code* is a way to represent information. This notion makes no reference to cryptography. A
cipher is a secret code. I.e., a secret way to represent information (so that it cannot be understood by unauthorized parties). In *coding theory*, people focus on the problem to keep the information available, e.g. by adding redundancy to protect against random noise. This is fundamentally different to cryptography, where we have to protect against a *malicious* process.

People often use *cryptology* as a broader notion than *cryptography*. They separate cryptography
(designing cryptographic systems) from cryptanalysis (analyzing cryptographic systems), both notions being part of cryptology.

Many people think of cryptanalysis as the action to break systems. This is however only one of the aspects of cryptanalysis. While analyzing, either we disprove security by breaking, but we can sometimes prove security as well.

In cryptology, people also include *steganography*, which consists of hiding the existence of some information. One good example is the (somewhat pornographic) correspondence between George Sand and her lover Alfred de Musset, in which she was hiding her message in a long text looking like a genuine poetry.

Actually, modern cryptography does not focus solely on confidentiality. Many other cryptographic problems are considered: data integrity protection, data authentication, access control, timestamping, fair exchange, digital rights management, privacy, etc. These are used in many daily applications such as bank cards, e-commerce, mobile telephony, biometric passports, mobile communication, traceability in supply chains, pay-TV systems, car locks, public transport fees, electronic voting, etc.

In this lecture, we focus (but not only) on three fundamental problems which are encountered in the communication between a sender and a receiver:

- confidentiality (only the receiver shall receive the message), - authentication (only the sender shall be able to send the message), - integrity (the sent message shall match the received one).
We introduce the main cryptographic primitives which will be considered. First of all, we will discuss primitives which belong to the "symmetric cryptography" techniques. There is the symmetric encryption, which encrypt and decrypt messages with the same symmetric (secret) key. There is the *message authentication code*, which computes a tag for a message and verify the tag of a message using the same symmetric (secret) key. This is used to authenticate messages. We often include *hash functions* in this category of primitives. It is a deterministic function which computes a bitstring of fixed length for any message. The output is a kind of "fingerprint" of the message.

There is also the "public-key cryptography" technique. We consider public-key cryptosystems in which encryption and decryption are done with different keys, the decryption key being secret. What is new is that the encryption key can be made public without compromising privacy. We also consider *digital signatures* in which a secret key is used to "sign" a message and a public key is used to verify if a signature is valid. Usually, we also consider *key agreement protocols* which allow two participants to establish a common secret key over a public communication channel.

In the famous TLS standard which is mainly used to secure browsing on the internet, when a client (browser) wants to connect to a secure server, the server first sends its *certificate*, which is a signed document including the association between the address of the server (the URL) and a public key. The browser knows how to verify the certificate as the list of public keys of certificate authorities is already built in. This way, the browser can trust that a URL is associated to a given public key. The browser can then select a symmetric key and encrypt it using the public key of the server. The server is able to decrypt it and to retrieve the symmetric key. With this symmetric key, the client and the server can communicate securely using symmetric cryptography. We can see here that public-key cryptography is used to bootstrap secure communication, which is made using symmetric cryptography.

## 1.2 Cryptography Prehistory

Cryptography appeared at the same time as History: once people started to write, there was a need to protect information. In ancient civilizations such as ancient Egypt, the ability to write was the secret of scribes, transmitted from father to son. This was not public knowledge. Once the written language became widely spread, there was a need to transform the public encoding into a secret one.

Warriors in ancient Sparta used scytales. It was a common way to write messages by exchanging the position of some characters in the message. Typically, a message would be written in clear on a leather belt, when wrapped around a cylinder, and by writing along the axis of the cylinder. By unwrapping the belt, consecutive characters suddenly became distant on the belt, the distance matching the circumference of the cylinder. Moving characters is a technique known as *transposition*.

Caesar was rather using a convention to replace every character by another character, following a permutation of the entire alphabet. This is a technique known as *simple substitution*.

We could think that simple substitution is pretty secure as the set of all possible permutations of the alphabet is huge. In an alphabet of 26 characters (although the one of Caesar was a bit smaller), we have 26! possible permutations, i.e. roughly 288.4. This means we can have a secret key of more than 88 bits, which is pretty long. Unfortunately, simple substitution can be broken by statistical analysis.

If we count on that the plaintext follows some biased distribution (typically, the plaintext would be written in Latin, and each character of the alphabet would be subject to a non-regular frequency), we can guess that the most frequent character of the ciphertext is the encryption of a very frequent character in the language of the plaintext. We can also analyze the frequency of consecutive characters. E.g., the frequency of *digrams* (which is a sequence of two characters) or even *trigrams* (sequences of three characters). Eventually, we can decrypt non-ambiguously.

Anyway, the Caesar cipher used a permutation with a very special structure (namely, a circular rotation of the letters in the alphabet by two positions).

In the XVI-th Century appeared the *Vigen`ere cipher*. It was one of the first using a configurable secret key. A key would be a sequence of characters (e.g., "ABC"). To encrypt a plaintext, we would do an operation character-wise on the plaintext applied to the repetition of the key (i.e., "ABCABCABC*. . .*").

The operation between two characters, a plaintext character and a key character, consists of applying a circular rotation of the alphabet which maps "a" to the key character. For instance, if the key character is "B", we rotate the alphabet by one position to map "a" to "B". So, if the plaintext character is "h" and the key character is "B", the ciphertext character is "I". If we denote this operation with a +, it is defined by the addition table on Fig. 1.1.

We can prove that the alphabet together with this + rule forms an *Abelian group* and that it is isomorphic to Z26, as it will be seen in the next chapter.

If we write the message in a table with a number of columns corresponding to the length of the key, we observe that all characters in the same column are mapped through the same alphabet rotation. So, we could do some statistical analysis in each column separately.

An interesting observation was made by Kasiski in the XIX-th Century. If we find a frequent pattern of consecutive characters in the ciphertext, it most likely corresponds to the encryption of a frequent pattern in the plaintext and that the distance between the occurrences are multiple of the key length. This could be used to deduce the key length from the ciphertext. It is known as the *Kasiski test*.

Another common tool to analyze the Vigen`ere cipher is the *index of coincidence*. Given a sequence of characters x1*, . . . , x*n, the index of coincidence is the probability that xI = xJ, given I and J uniformly distributed among pairs such that 1 ≤ *I < J* ≤ n. If Z denotes the alphabet and nc is the number of occurrences of a character c ∈ Z in the sequence, we have

$$\mathsf{Index}(x_{1},\ldots,x_{n})=\Pr_{I<J}[x_{I}=x_{J}]=\frac{1}{n(n-1)}\sum_{1\leq i,j\leq n\atop i\leq j}\frac{1}{x_{i}=x_{j}}=\sum_{c\in\mathcal{Z}}\frac{n_{c}(n_{c}-1)}{n(n-1)}$$

The index of coincidence is invariant under simple substitution: for any permutation $\sigma$ of $Z$, we have

$$\mathsf{Index}(\sigma(x_{1}),\ldots,\sigma(x_{n}))=\mathsf{Index}(x_{1},\ldots,x_{n})$$

Similarly, the index of coincidence is invariant under transposition: for any permutation $\sigma$ of $\{1,\ldots,n\}$, we have

$$\mathsf{Index}(x_{\sigma(1)},\ldots,x_{\sigma(n)})=\mathsf{Index}(x_{1},\ldots,x_{n})$$
We can compute the expected value of the index of coincidence by

$$E(\mbox{Index}(x_{1},\ldots,x_{n}))=\frac{1}{n(n-1)}\sum_{\begin{subarray}{c}1\leq i,j\leq n\\ i\neq j\end{subarray}}\mbox{Pr}[x_{i}=x_{j}]$$ $$=\sum_{c\in\mathbb{Z}}f_{c}^{2}$$
By assuming that the xi's are independent and identically distributed, with Pr[xi = c] = fc. The expected index of coincidence of a sequence of uniformly distributed characters is thus 0.039 (by taking fc =
1
|Z| and |Z| = 26) while it is close to 0.065 for an English text (using the frequency table of characters in English). As n goes to infinity, the real index of coincidence become close to the expected one. Hence, we can find the length of the Vigen`ere key by making a guess and checking that the index of coincidence of every column is high. Then, we can recover the alphabet rotation of each column.

## 1.3 Pre-Modern Industrial Cryptography

In 1918, Siemens invented Enigma: an electro-mechanical encryption device which could be used to type a message and plugged to a radio transmitter. This device was patented (so, it is public), and easily configurable by setting up an initial state.

This device was massively used by the Germans during the Second World War. The communications were also massively intercepted. To decrypt it, several mathematicians joined their forces, and people (including Alan Turing) had to invent computers to make the decryption task automatic. So, computer science originally appeared to solve a cryptanalysis task.

Without entering into the technical design of the Enigma device, we can define one instance of the Enigma cipher as follows. First of all, the system assumes a common (public) permutation π of the 26-letter alphabet and a set of (say five) permutations S. The permutation π is such that it is an involution (i.e., we have π(π(x)) = x for all letter x) which has no fixed point (i.e., we have π(x) ̸= x for all letter x). We call *reflector* the permutation π. Permutations in the set S are called *rotors*. We further define ρ, the circular rotation of the alphabet. E.g., ρ(a) = b,
ρ(b) = c, ... Given a rotor α ∈ S and an integer i ∈ Z, we say that α in position i defines the permutation αi = ρi ◦ α ◦ ρ−i. (Technically, the rotor is a wheel connecting 26 input plugs to 26
output plugs, and when the rotor rotates by
1
26th of a complete circle, it is equivalent as making the input rotate by ρ−1 and the output rotate by ρ at the same time. So, αi is the permutation defined after i rotations.)
In Enigma, there is a *plug board* of 26 plugs and we can connect plugs by a cable. Concretely, we have 6 cables and we can select 6 non-overlapping pairs of distinct plugs. After connection, this defines an additional permutation σ which lets fixed letters corresponding to an unconnected plug and permutes the other letters by pairs. I.e., the set of all {x; σ(x) = x} has cardinality 14
and σ is an involution: for all x, we have σ(σ(x)) = x. A key of Enigma is a tuple consisting of

- an order triplet (*α, β, γ*) of different rotors, i.e., *α, β, γ* ∈ S;
- an integer a;
- an involution σ with 14 fixed points.
We can compute the total number of keys. The total number of selection of rotors is 5×4×3 = 60
if S has only 5 rotors. The number of possibilities for a is 263 = 17 576. The number of possible
σ is
26
14

× 11 × 9 × 7 *× · · · ×* 1 = 100 391 791 500 Finally, we have 60 × 17 576 × 100 391 791 500 ≈ 257
so an Enigma key is equivalent to a 57-bit key.

The plaintext x is a sequence of letters x1*, . . . , x*m.

It is encrypted on-the-fly into y =
(y1*, . . . , y*m). To encrypt xi, we write i − 1 + a in basis 26 and obtain i − 1 + a = i3i2i1. I.e., i − 1 + a = 262i3 + 262i2 + i1 and i1, i2, i3 ∈ {0, 1*, . . . ,* 25}. Then, we define

yi = σ−1 ◦ α−1 i1 ◦ β−1 i2 ◦ γ−1 i3 ◦ π ◦ γi3 ◦ βi2 ◦ αi1 ◦ σ(xi)
In the Enigma device, typing xi sends a signal to the corresponding plug, goes through the involution σ, then through the three rotors α, β, γ, then through the reflector, then comes back through the rotors γ, β, and α, the permutation σ again, and lights up a lamp corresponding to yi. Every time we type a key, the rotor α moves by one position (i.e., the least significant i1 is incremented). Every 26 keystrokes, the rotor β moves by one position (i.e., i2 is incremented).

Every 262 keystrokes, the rotor γ moves by one position (i.e., i3 is incremented). Also: the initial position of the rotors corresponds to a.

Interestingly, Enigma is also an involution: by encrypting yi in the very same position of the rotors, we must obtain xi.

This means that the encryption and the decryption operation are exactly the same.

Laws in modern cryptography.

In modern cryptography, we must keep in mind some fundamental laws.

Firstly, we should not make the security of a system dependent on the secrecy of its design.

Based on that cryptographic systems are not designed by their users, or that they may be stolen, we cannot assume that the adversary ignores the design of the system. This law is known as the Kerckhoffs principle. Many people misread this and claim it says that cryptographic systems must be publicly known. This is a common mistake.

Secondly, in a network of n users, the number of potential pairs of users willing to communicate securely has the order of magnitude of n2. So, we should think of a common system and keep it configurable by an easy-to-select secret key.

Thirdly, we must keep in mind that the computational power of available devices is always increasing. Moore's law says that the growth is exponential. As the computational power doubles every cycle (say 18 months), breaking a key by exhaustive search is twice faster after a cycle. Considering that a standard computer CPU could try about one million keys per second in the 2007 technology, breaking a 128-bit key by exhaustive search within 14 billion years requires 770 000 such computers. Assuming the Moore law goes on until 2215, a single computer would do the same job within a second! This leads us to an interesting philosophical answer: if we have 14 billions years to spend to break a 128-bit key, it is better to launch the Big Bang, take vacations, wait until computers invent by themselves, then go down to Earth in 2215 to buy one, rather than make too many machines work for too long.

Finally, we must keep in mind the Murphy law: the worst case scenario will eventually happen.

If there is a single place for failure, it will put the security down.

## 1.4 Cryptography And Information Theory

We consider the set {0, 1}n of bitstrings of length n with the bitwise XOR operation, i.e.

$(x_{1},\ldots,x_{n})\oplus(y_{1},\ldots,y_{n})=(x_{1}\oplus y_{1},\ldots,x_{n}\oplus y_{n})$
with a ⊕ b = (a + b) mod 2 for a, b *∈ {*0, 1}. Note that ⊕ is associative, commutative, (0*, . . . ,* 0) is neutral, and each element is self-inverse since

x ⊕ x = (0*, . . . ,* 0)
So, we have an Abelian group in which all elements are self-inverse. We define an encryption scheme over this group. Given a message X in this set and a key K in the same set, the encryption of X
is Y = X ⊕ K. To decrypt, we just compute

$Y\oplus K=(X\oplus K)\oplus K=X\oplus(K\oplus K)=X\oplus(0,\ldots,0)=X$
The *Vernam cipher* [83] assumes that K is of same length as X, uniformly distributed, and used to encrypt only once. We often call it *one-time-pad*.

The Vernam cipher can be nicely implemented without any computing devices as observed by Naor and Shamir [60]. This is called *visual cryptography*. The idea is to decrypt images by using transparent paper, eyes, and brain! Both the ciphertext and the key are black-and-white images consisting of pixels. As shown on Fig. 1.2, each pixel is encoded by a pattern which is half white and half black. The encoding of the pixel 0 is the complement of the encoding of the pixel 1. So, an image is encoded by tiles which encode each pixel. If we overlay the ciphertext and the key and look through the transparent papers, a pixel b which is put on another pixel b will look like the encoding of the pixel b, i.e., it will be half white and half black. This is what the eye can see but from far away, the brain will take it as a grey tile. (See Fig. 1.3.) Interestingly, b ⊕ b = 0. This is the corresponding bit of the decryption operation. We say that a grey tile corresponds to a 0 bit in the plaintext. If we overlay a pixel 0 and a pixel 1, as they are complement of each other, the eye and brain will see a completely black tile. Since 0⊕1 = 1, we say that a black tile corresponds to a 1 bit of the plaintext. So, the brain will interpret the grey and black tiles and will "see" the plaintext. As an application, someone can just hold the key as printed on a transparent paper and use it to decrypt ciphertexts which could be sent by fax.

We don't encrypt twice with the same key. Otherwise, the system would be insecure. Indeed, assume that Y1 resp. Y2 is the encryption of X1 resp. X2 under the same key K. We have

$Y_{1}\oplus Y_{2}=(X_{1}\oplus K)\oplus(X_{2}\oplus K)=X_{1}\oplus X_{2}$
So, if the plaintexts X1 and X2 have some structure, their XOR may leak some information and this XOR can be computed from the ciphertexts only. As an example, if X1 and X2 are black and white digital images with a lot of blank, we can see in Y1 ⊕ Y2 the blank zones from both X1 and X2 and the shape of the two pictures. So, the plaintexts leak.

Similarly, we must use a key which is at least as long as the plaintext. If it is too short, some part of the plaintext may remain in clear.

Finally, the key must be uniformly distributed. Otherwise, Y = X ⊕ K will follow a biased distribution which may leak some information about X. We will see that Y is uniformly distributed otherwise.

It is pretty cumbersome to require a key as long as the plaintext every time we need to encrypt.

It is unsuitable for most of applications. In the case of the red telephone, during the Cold War, this was making sense: USSR and USA could exchange some long keys K over a secure slow channel (typically: an ambassador with a case full of keys flying from one capital to the other) in order to prepare emergency calls over a fast insecure channel (typically: radio).

When Vernam published this cipher in 1926, it was believed to be perfectly secure but there were no available formalism to express it or prove it. We had to wait until 1949 to obtain the appropriate formalism by Shannon.

In the Shannon model [77], there are two algorithms C and C−1 to encrypt and to decrypt, respectively. (See Fig. 1.4.) The plaintext X and the key K are two independent random variables.

The distribution of K is specified by the encryption scheme, and the one of X is dependent on the application. We stress that in the Shannon model, the distribution of X is part of the cryptographic system. This is not so common now as we favor systems working for arbitrary plaintext distributions. The ciphertext Y = CK(X) is also a random variable, with a distribution induced by the distributions of X and K. The cryptographic scheme is *correct* if Pr[C−1
K (CK(X)) = X] = 1.

As an example, we can formalize a generalized form of the Vernam cipher in this model. Given a finite group G (with additive notations), imagine that the plaintext message X follows a given distribution D in G. We use a key K which is independent and uniformly distributed in G. We define Y = K + X to encrypt and X = (−K) + Y to decrypt. This cipher is to be used for a single X. (More encryptions need to set up new keys.)
The adversary has access to Y only and tries to retrieve some information about X.

We say that the cryptographic scheme provides *perfect secrecy* if the value y taken by Y leaks no a posteriori information on X which was not already known *a priori*.

This is formalized by Pr[X = x|Y = y] = Pr[X = x] for all x and all y such that Pr[Y = y] ̸= 0. Actually, perfect secrecy is defined by the following result.

Definition 1.1 (Perfect Secrecy). Given some independent random variables X and K in a discrete space and a cipher C in the Shannon model to define Y = CK(X), the following properties are equivalent:

- for all x and y *such that* Pr[Y = y] ̸= 0*, we have* Pr[X = x|Y = y] = Pr[X = x];
- X and Y are independent;
- H(X|Y ) = H(X), where H *denotes the Shannon entropy.*1
If these properties are satisfied, we say that the cipher provides perfect secrecy. Proof. The equivalence of the first two properties comes from the definition of independence. By definition of the conditional entropy, we have H(X|Y ) = H(*X, Y* ) − H(Y ). So, the equivalence with the last property is a consequence of the result saying that X and Y are independent if and only if H(*X, Y* ) = H(X) + H(Y ).

⊓⊔
The above notion of perfect secrecy is relative to a specific distribution on the plaintext X
and we can wonder what is the influence of the choice of this distribution on perfect secrecy. The following result shows that if we have perfect secrecy for a plaintext distribution giving a nonzero probability to any possible plaintext in the domain of C, then we have perfect secrecy for all distributions on this domain.

Theorem 1.2. Let CK be a cipher with K following a given distribution and input plaintext on a given domain X. Let p and p′ be two distributions on X such that the support of p is X. In what follows, we denote by Prp resp. Prp′ the probability using the distribution p resp. p′.

CK provides perfect secrecy with p implies that CK provides perfect secrecy with p′.

Proof. Let Y = CK(X) be the ciphertext. Let y be such that Prp′[Y = y] ̸= 0. (Note that Prp′[Y = y] is the probability that Y = y given the distribution p′ on X.) We need to prove that for any x, Prp′[Y = y] = Prp′[Y = y|X = x].

Since Prp′[Y = y] ̸= 0, there exist k and x0 such that Ck(x0) = y, Pr[K = k] ̸= 0, and p′(x0) ̸= 0. Thanks to p having a full support, we have p(x0) ̸= 0 so Prp[Y = y] ̸= 0.

Let us take an arbitrary x. Due to perfect secrecy, we have Prp[Y = y] = Prp[Y = y|X = x].

But Prp[Y = y|X = x] = Pr[CK(x) = y] does not depend on the distribution of X so we have Prp[Y = y|X = x] = Pr[CK(x) = y] = Prp′[Y = y|X = x]. Hence, Prp[Y = y] = Prp′[Y = y|X =
x].

Then

$$\Pr_{p^{\prime}}[Y=y]=\sum_{x}\Pr[Y=y|X=x]p^{\prime}(x)$$ $$=\sum_{x}\Pr[Y=y]p^{\prime}(x)$$ $$=\Pr[Y=y]\sum_{x}p^{\prime}(x)=\Pr[Y=y]$$ $$=\Pr[Y=y|X=x]$$
and we have proven perfect secrecy with p′.

⊓⊔
Given this formalism, it is straightforward to prove that for any distribution of X, the Vernam cipher provides perfect secrecy. Actually, the good distribution of Y comes from the following lemma:

Lemma 1.3. Let X and K be two independent random variables over a discrete group.
                                                                     We
assume that K is uniformly distributed. Then, Y = K + X is also uniformly distributed, and
independent from X.

Proof. Let x and y be two group elements. We have Pr[X = *x, Y* = y] = Pr[X = *x, K* = y − x] =
1
#G Pr[X = x], where #G is the cardinality of the group. By summing over all x, we obtain Pr[Y = y] =
1
#G. So, Pr[X = *x, Y* = y] = Pr[X = x] Pr[Y = y]: X and Y are independent.

⊓⊔
Since the Vernam cipher imposes that the key is as long as the plaintext and that it provides perfect secrecy, a natural question consists of wondering if there are ciphers with perfect secrecy without this drawback. Shannon answered by the negative.

Theorem 1.4 (Shannon 1949). In a correct cryptographic system providing perfect secrecy, we have H(K) ≥ H(X).

Proof. Once the value of K is determined, we can compute Y = CK(X) or X = C−1
K (Y ) due to the correctness of the cryptographic system. So, we can make changes in the variable of the sum defining the conditional entropy and obtain H(Y |K) = H(X|K). Since X and K are independent, we have H(X|K) = H(X). Thus, we obtain H(Y |K) = H(X).

Due to Lemma B.2 in Appendix, we have H(Y ) ≥ H(Y |K). We thus have H(Y ) ≥ H(X).

Note that we did not use perfect secrecy. So, H(Y ) ≥ H(X) is a general property of correct cryptographic systems.

If the value of X is determined, we can compute Y = CK(X) from K. So, many terms in the sum of the joint entropy of K|X and Y |X vanish and we obtain H(*Y, K*|X) = H(K|X). Since X
and K are independent, we have H(K|X) = H(K). So, H(*Y, K*|X) = H(K).

Due to Lemma B.2 in Appendix, we have H(*Y, K*|X) ≥ H(Y |X). Thus, H(K) ≥ H(Y |X).

Again, this is a general property of correct cryptographic systems.

Now, if we have perfect secrecy, we have H(Y |X) = H(X|Y ) + H(Y ) − H(X) = H(Y ). So, we have H(K) ≥ H(Y ) ≥ H(X).

⊓⊔
There is another form of the Shannon Theorem which is more common.

**Theorem 1.5**: **(Shannon 1949).** _In a correct cryptographic system providing perfect secrecy, we have_

$$\#\{k;\Pr[K=k]\neq0\}\geq\#\{x;\Pr[X=x]\neq0\}$$
So, we cannot have less keys than messages.

Proof. Let y be a fixed value such that Pr[Y = y] ̸= 0. Since X and K are independent, we have Pr[X = *x, Y* = y] = Pr[X = *x, C*K(x) = y] = Pr[X = x] Pr[CK(x) = y]
For all x such that Pr[X = x] ̸= 0, perfect secrecy implies Pr[CK(x) = y] = Pr[Y = y|X = x] =
Pr[Y = y] ̸= 0. Consequently, for all x such that Pr[X = x] ̸= 0, there must exist one k such that Ck(x) = y and Pr[K = k] ̸= 0. Let us write it k = f(x).

Due to correctness, for any x which has a nonzero probability, we have C−1
f(x)(y) = x. So, f(x) = f(x′) implies x = x′. Consequently, we have an injection from the set of all possible x to the set of all possible k. We deduce the inequality.

⊓⊔
Interestingly, we could also prove that the set of possible X cannot be infinite and enumerable.

Theorem 1.6. *In a correct cryptographic system providing perfect secrecy,* {x; Pr[X = x] ̸= 0}
cannot be infinite and enumerable. I.e., we cannot have perfect secrecy over an infinite enumerable message space.

Proof. We defined cryptographic systems for discrete sets. So, they are enumerable. We have to show that {x; Pr[X = x] ̸= 0} must be a finite set.

Let y be a fixed value such that p = Pr[Y = y] ̸= 0. (Such y must exist because we have an enumerable domain.) Due to perfect secrecy, we have p = Pr[Y = y] = Pr[CK(x) = y] for all possible x. Due to correctness, CK(x) = y implies C−1
K (y) = x. So, Pr[C−1
K (y) = x] ≥ Pr[CK(x) =
y] = p for all possible x. Furthermore, we know that by summing Pr[C−1
K (y) = x] over all possible x, we must obtain 1. So,

$1\geq\sum_{x;\Pr[X=x]\neq0}\Pr[C_{K}^{-1}(y)=x]\geq p.\#\{x;\Pr[X=x]\neq0\}$
Consequently, #{x; Pr[X = x] ̸= 0} ≤ 1
p. So, it is a finite set.

⊓⊔
For practical reasons, secure ciphers over a domain of finite bitstrings also leak the length of a message. Indeed, we ideally want that the encryption of a short message (e.g. 100 bytes) remains short, while we also want to encrypt messages of several megabytes. Hence, the length often leaks and there is little we can do about it: we must live with it.

So now, we conclude that there exists a cipher providing perfect secrecy. It has a drawback of using keys as long as the message to encrypt, but we can show that it is necessary for perfect secrecy. Furthermore, it may be the simplest cipher we could imagine, given this drawback. So, we have modeled encryption, security, and identified the best possible cipher. Could we stop the lecture here? Certainly not, because there is an important notion which is not captured at all in this theory: *complexity*.

So far, the Shannon notion for perfect secrecy wonders if recovering the information *could* be possible, no matter the cost. As computer science began, it became clear that feasibility in theory does not mean feasibility in practice. So, we should add the notion of *cost* - that we usually call complexity - of the information recovery in the security model. Ideally, we would like to say that recovering some information about the confidential message is too expensive for the adversary so that the system is secure. This way, we could hope to have secure ciphers better than the Vernam cipher in terms of efficiency with reusable and short key.