
## Chapter 7 Public-Key Cryptography

This chapter presents elementary notions of public-key cryptography such as public-key cryptosystems, digital signatures, and key agreement protocols. It focuses on RSA and ElGamal -like cryptography.

## 7.1 Public-Key Cryptography

In 1976, Diffie and Hellman published the seminal paper "New Directions in Cryptography". This gave birth to public-key cryptography [32]. In this paper, they proposed the notions of trapdoor permutation, public-key cryptosystem, *digital signature scheme*, and *key agreement protocol*. They provided an instance only for the last primitive.

A trapdoor permutation is defined by a probabilistic algorithm Gen and two deterministic algorithms Perm and InvPerm. Gen generates a pair (param, K) (in which K is called the *trapdoor*)
such that Permparam and InvPermK define two permutations over a given domain which are inverse of each other. So, for any input X in the domain, we have InvPermK(Permparam(X)) = X. The security notion relates to the secrecy of X even though Permparam(X) and param are public.

In a public-key cryptosystem, this is essentially the same with different notations, without requiring Permparam to be a permutation or even deterministic: we have two probabilistic algorithms Gen and Enc and one deterministic one Dec. Gen generates a pair (pk, sk) where pk is called the public key and sk is called the *secret key*, and such that for any X in the domain, we always have Decsk(Encpk(X)) = X. The security notion relates to the secrecy of X even though Encpk(X) and pk are public.

In a key agreement protocol (also called key exchange or *key establishment*), there are two probabilistic interactive algorithms with no input which generate the same output (the key) when interacting with each other. It should be such that this output is secret even though the messages between the two algorithms are public.

Public-key cryptosystems are the asymmetric equivalent to symmetric encryption. There is also an asymmetric equivalent to MAC which is the called a *digital signature scheme*. In a digital signature scheme, we have two probabilistic algorithms Gen and Sig and one deterministic one Ver.

Gen generates a pair (pk, sk) where pk is called the *public key* and sk is called the *secret key*, and such that for any X in the domain, we have Verpk(Sigsk(X)) = X for sure. The security notion relates to the unforgeability of a valid signature Y (i.e. a value such that Verpk(Y ) does not abort)
even though pk is public.

A digital signature scheme is typically used in a *certificate*: a server holding a public key K
requests a *certificate authority* to sign (by Sigsk) a message saying that K belongs to the server.

The signature is verified by Verpk. So, a client holding pk can verify the certificate and extract K
from it. Based on K, he can establish a secure communication with the server.

## 7.2 Diffie-Hellman Key Exchange

We already covered the Diffie-Hellman key exchange protocol in Chapter 2. Essentially, the two algorithms (one for Alice and one for Bob) exchange their public keys and derive a key from their secret key and the received public key. The public key comes with a secret one. In *static* mode, the public keys are long-term values and may be obtained from a directory. In *ephemeral* mode, the public keys are freshly generated for each session of the protocol. In *semi-static* mode, one key is fresh and the other is a long-term one.

In ephemeral mode, the generated secret key can be erased after the protocol completes since the next session will generate a new one. This has the nice property of adding *forward secrecy*: If any long-term key is corrupted in the far future, this cannot compromise the secrecy of encryptions which are done now using the output of the key exchange. Indeed, there is no longer any long-term secret. In static mode, the corruption of the state of Alice, for instance, makes possible to recover the output of the protocol (by feeding Alice's algorithm with her state and Bob's public key). So, secrecy is not guaranteed in that case. Forward secrecy also appears in the Signal protocol, which is discussed in Section A.4.

Diffie and Hellman did not propose any public-key cryptosystem. They could have transformed their key exchange protocol in a hybrid encryption model, by using the output of the protocol with symmetric encryption or by proposing the ElGamal cryptosystem (which appeared in 1984 [37]). Actually, the first proposal of a secure cryptosystem was RSA [71].

## 7.3 Rsa Cryptography

In 1978, Rivest, Shamir, and Adleman proposed their RSA cryptosystem [71]. It is actually a trapdoor permutation. It can also be used in a reversed way as a digital signature scheme. We have already seen it. Actually, what we saw is often called plain RSA, textbook RSA, *vanilla RSA*, or even *raw RSA*, as it is not used as a real-life cryptosystem. It is the one we find in textbooks or lowlevel introduction to cryptography. Indeed, real-life messages are not ZN numbers. Furthermore, RSA has some homomorphic properties such as Enc(ab) = Enc(a)Enc(b), which may lead to potential weaknesses. Different ways to implement RSA may also leak some information.

A popular standard (although outdated) is PKCS#1v1.5 [8]. Essentially, to encrypt a message M, we run the textbook RSA on the byte string 00∥02∥PS∥00∥M converted into an integer, where PS is a string of random nonzero bytes such that the complete byte string has the same length as the modulus N. To decrypt, we check that the textbook-RSA decryption parses to this type of byte string and extract M. The size of the message to encrypt is limited so that PS has at least
64 bits.

This standard is supposed to be replaced by RSA-OAEP [9]. There, we apply the textbook RSA to the string 00∥maskedSeed∥maskedDB, where maskedDB = DB⊕MGF(seed), maskedSeed = seed ⊕ MGF(maskedDB), seed is selected at random, and DB is the concatenation of some padding string with the message M (see Fig. 7.1). MGF is an ad-hoc function in the PKCS#1 standard based on a hash function. Decryption is straightforward.

We can construct an equivalent cryptosystem to RSA which uses e = 2 (this is not allowed in RSA since 2 is never coprime with φ(N)).

This is called the *Rabin cryptosystem* [66] (see Fig. 7.2). The idea is that we have to extract a square root to decrypt. Unfortunately, decryption is ambiguous since we have four square roots. One way to get around this problem is to add enough redundancy in the message to encrypt so that it is unlikely that there will be more than one square root passing the redundancy check. For instance, the redundancy may consists of having
64 specific bits set to zero. One concrete proposal is the SAEP-Rabin cryptosystem [21] in which the encryption is the textbook-Rabin encryption applied on maskedDB∥seed, with maskedDB =
DB ⊕ MGF(seed) and DB = M∥00 *· · ·* 0 with a fixed (but large enough) number of 0 bits in the padding.

We say that a digital signature scheme has the property of *message recovery* if from σ =
Sigsk(X), we can extract X by Verpk(σ). This corresponds to the way we defined signature schemes,

In many concrete schemes, the output of Sigsk(X) is of form X∥σ where σ is called the *signature*. In that case, Verpk(X∥σ) is aborting if σ is an invalid signature of X, and producing X as an output otherwise. Quite often, we say that that σ (instead of X∥σ) is the output of Sigsk and that it must be concatenated to X for transmission. We then say that the signature has no message recovery as the verification needs both X and σ instead of σ alone.

Using a trapdoor permutation in a reversed way, we can construct a signature scheme with message recovery: we just say that Sigsk(X) is the decryption of X using InvPerm and that Verpk(σ) is just running Perm (see Fig. 7.3). When Perm and InvPerm are the RSA encryption and decryption algorithms, this is the textbook-RSA signature scheme. So, textbook-RSA can be regarded as a digital signature scheme with message recovery.

A more popular way to construct a signature scheme (without message recovery) from a trapdoor permutation is by using a hash function.

In this construction, we have Sig(X) =
InvPerm(H(X)). To run Ver(*X, σ*), we compare H(X) with Perm(σ) and yield X if they match.

It can be generalized to extend the domain of any elementary signature scheme Sig0 by Sig(X) =
Sig0(H(X)) (see Fig. 7.4). This type of construction is actually called the *hash-and-sign* paradigm.

PKCS#1v1.5 also includes a signature scheme: we apply the textbook-RSA signature (see Fig. 7.5) on the byte string 00∥01∥FF *· · ·* FF|00∥D where D is the encoding (following a specific format) of H and H(X). Again, the padded string must have the same length as the modulus.

To verify a signature σ of a message X, we apply the textbook-RSA message recovery based on

σ, check that it parses into the correct format, extract H and digest from D, then compare H(X) with digest. Interestingly, the choice of H is not fixed as it is specified in D. There is a list of allowed hash functions though. E.g., SHA1.

This outdated standard is supposed to be replaced by *RSA-PSS* [9], where the textbook-RSA
signature is applied on maskedDB∥H∥BC, where BC is an hexadecimal constant byte, maskedDB =
0 *· · ·* 0∥salt ⊕ MGF(H), and H = H(0 *· · ·* 0∥H(X)∥salt) (see Fig. 7.6).

## 7.4 Elgamal Cryptography

The ElGamal cryptosystem [37], which was already covered in Chapter 2, comes with an ElGamal signature scheme which is quite independent. In the group Z∗
p generated by some public g, where p is a public prime number, the secret key is some x (modulo p − 1) and the public key is y = gx mod p. To sign M, we pick a random k ∈ Z∗
p−1 and compute σ = (*r, s*), where r = gk mod p and s = H(M)−xr k mod (p − 1) (see Fig. 7.7). A signature (*r, s*) is valid for M if 0 ≤ *r < p* and yrrs ≡ gH(M) (mod (p − 1)).

This scheme is not favored, because the signatures are quite long (we need two number of the size of p, which can be pretty large) and there is a lack of uniform security proof. Indeed, we can construct some parameters p and g making the signature insecure. Nevertheless, this scheme initiated a long dynasty of variants.

We must mention an important problem in the ElGamal signatures: although it is required that k is picked at random for every new signature generation, it could be the case that, occasionally, some k repeats. The consequences of a k repetition are here terrible. Indeed, from two signed messages (M1, r1, s1) and (M2, r2, s2) using the same value k (this is visible from r1 = r2), we deduce that s1
s2
≡ H(M1) − xr1

H(M2) − xr2 (mod (p − 1))
which allows to deduce x. Hence, the secret key leaks from a single repetition of k!

In 1989, Schnorr [73, 74] introduced a second prime number q, factor of p − 1, and worked in a subgroup of Z∗
p of order q. The scheme was also changed so that the signature consisted of a digest and a number of the size of q.

In 1995, DSA was adopted as a US signature standard (the version 2 is available as reference [4]). It was essentially based on the ideas by Schnorr with a slightly changed algorithm.

Some other variants followed: Nyberg-Rueppel in 1995 [61], Pointcheval-Vaudenay [27] in 1997, KCDSA in 1998 [57], ... Quite importantly, ECDSA, the elliptic-curve variant of DSA, appeared in

k mod q (see Fig. 7.8).

1998 [4]. The main idea was to work in a group defined by an elliptic curve instead of a subgroup of Z∗
p.

To generate some parameters for the above variants (except ECDSA), we first select a prime number q, then take p = aq + 1 for a random a, until p is prime. Then a random element of Z∗
p is raised to the power a to get g until g if different from 1.

In DSA, the secret key is some x ∈ Zq. The public key is y = gx mod p. To sign M, we pick k ∈ Z∗
q and compute σ = (*r, s*), with r = (gk mod p) mod q and s = H(M)+xr A signature (*r, s*) for M is valid if r =

g H(M)
s y r s mod p mod q. (Note that the fractions in the exponents are taken modulo q.)
For ECDSA, the public parameters consist of some finite field and some elliptic curve over this field, together with a reference point G generating a group of order n in the elliptic curve. The number n is also part of the public parameters and must be prime. A secret key is a number d ∈ Z∗
n. A public key is a point Q = dG. To sign M, we pick k ∈ Z∗
n and compute the point kG. It has two coordinates x1 and y1 which are field elements. The element x1 is converted into an integer
¯x1 ∈ Zn following a standard scheme. Then, we compute r = ¯x1 mod n and s = H(M)+dr k mod n.

If either r or s is zero, the algorithm shall restart. The signature is σ = (*r, s*) (see Fig. 7.9). A
signature (*r, s*) for M is valid if both r and s are in Z∗
n, Q is a valid public key, and r = ¯x1 mod n where x1 is the first coordinate of the point u1G+u2Q, with u1 = H(M)
s mod n and u2 = r s mod n.

The BLS signature scheme [25] (Boneh-Lynn-Shacham) which is based on pairings allow to have a signature which is a single group element σ. Here, this is one point on an elliptic curve. Using point compression, this is a single finite field element. Hence, the signature is pretty short compared to other schemes. The signature scheme is depicted on Fig. 7.10.

The Boneh-Boyen signature scheme [22, 23] is also based on pairing. What is new is that is requires no hashing for security. (Previous constructions all require a function H to behave like a random function to be secure.) Here, we can sign a finite field element. A simplified version of the signature scheme is depicted on Fig. 7.11.

## 7.5 Selecting Key Lengths

So far, the best way to break RSA is to factor N. So, the keys must be chosen such that factoring N is infeasible. We just have to adjust the length of p and q and avoid some known forms of weak moduli.

For schemes such as Diffie-Hellman, ElGamal and the variants, the best way is to solve the discrete logarithm problem. So, the parameters shall just make this infeasible. For this, we favor groups of prime order. Either we work in a subgroup of Z∗
p, given a prime p (in which case we must specify the size of p and the size of the order), or we work over an elliptic curve, in which case we must select a finite field and the size of the order of the curve.

We compare the security with the cost of bruteforce attack on symmetric encryption. There exist several tables proposing vector of equivalent security parameters. The order of magnitudes are very similar. For instance, a table by Lenstra [55] suggests that the following security parameters propose equivalent security:

- symmetric encryption with a 82-bit key; - RSA with a 1613-bit modulus; - discrete logarithm with a subgroup of order q of Z∗
p, where p has 1613 bits and q has 145
bits;
- an elliptic curve over a field whose cardinality has 154 bits; - a hash function with digest length of 163 bits.
Those parameters are not considered as being enough for security nowadays. We recall that the digest length is doubled compared to the key length in symmetric encryption, due to the birthday paradox. We can see that the order of the groups on which we operate must have a similar size, due to a generic attack of square root complexity, but the p's and RSA moduli must be much larger.

## 7.6 Formalism

We first define a public-key cryptosystem.

Definition 7.1. A public-key cryptosystem *is a tuple* (Gen, M, Enc, Dec) with a plaintext domain M ⊆ {0, 1}∗ *and three efficient algorithms* Gen, Enc*, and* Dec*. The algorithm* Dec is deterministic and output either something in M or an error ⊥. It is such that

$$\forall X\in{\mathcal{M}}\quad\operatorname*{Pr}[\operatorname{Dec}(\mathsf{sk},\operatorname{Enc}(\mathsf{pk},X))=X]=1$$
where (pk, sk) *is generated from running* Gen*. The probability is over the randomness used in* Gen and Enc.

We stress that decryption must be deterministic while encryption may be probabilistic. Indeed, a single plaintext may have several possible ciphertexts but they must all decrypt to the right plaintext. Next, we define IND-CPA and IND-CCA security as follows.

Definition 7.2. *A PKC* (Gen, M, Enc, Dec) is (*t, ε*)-secure under chosen plaintext attacks (IND-
CPA-secure) if for any interactive process A = (A1, A2) limited to a time complexity t, given a bit b, when we first run the following steps Game Γb:
1: Gen → (pk, sk)
2: pick r
3: A1(pk; r) → (pt0, pt1, st) 4: if |pt0| ̸= |pt1| **then return** 0
5: Enc(ptb)
$−→ ct

6. ${\cal A}_{2}({\sf st},{\sf ct};r)\to z$
7. _return $z$_

_we have_

$${\rm Pr}[\Gamma_{1}\ \mbox{returns}1]-{\rm Pr}[\Gamma_{0}\ \mbox{returns}1]\leq\varepsilon.$$
It is (q, t, ε)-**secure under chosen plaintext/ciphertext attacks** (IND-CCA-secure) if the same holds for any similar interactive process ADec(sk,.) who is limited to q queries to a decryption oracle Dec(sk, .) but not allowed to send it c.

So, we have a game in which the adversary proposes two messages.

Then, one of the two is encrypted and the adversary must guess which one of the two from the ciphertext. Clearly, if encryption is deterministic, this is easy since the adversary can just encrypt the messages himself and compare with the challenge ciphertext. So, the RSA cryptosystem that we saw is not IND- CPA secure. Most modern cryptosystems are actually probabilistic. Some are just variants of the ElGamal cryptosystem which starts by making a key agreement on a random ephemeral key then use the generalized Vernam cipher with this key.

The restriction that m0 and m1 must have the same length comes from the impossibility to make a secure cryptosystem on {0, 1}∗: it is actually impossible to perfectly hide the message length. So, we must live with cryptosystems leaking the message length.

We define digital signature schemes as follows.

Definition 7.3. A digital signature scheme *is a tuple* (Gen, D, Sig, Ver) with a message domain D ⊆ {0, 1}∗ *and three efficient algorithms* Gen, Sig*, and* Ver*. The algorithm* Ver is deterministic and outputs 0 (reject) or 1 (accept). It is such that

$\forall X\in\mathcal{D}$ Pr[Ver(pk,X,Sig(sk,X))=1]=1\)
where (pk, sk) *is generated from running* Gen*. The probability is over the randomness used in* Gen and Sig.

Definition 7.4. *A digital signature scheme* (Gen, D, Sig, Ver) is (q, t, ε)-secure against existential forgery under chosen message attacks (EF-CMA) if for any probabilistic algorithm A
limited to a time complexity t and to q *queries, the advantage* Adv is bounded by ε.

## Adv = Pr[*Game Returns* 1]

| Game        | Oracle   |
|-------------|----------|
| OSig        |          |
| (           | X        |
| 1:          |          |
| Gen         |          |
| $           |          |
| −→          |          |
| (           |          |
| pk          |          |
| ,           |          |
| sk          |          |
| )           |          |
| 2:          |          |
| Queries     |          |
| ← ∅         |          |
| 6:          |          |
| σ           |          |
| ←           |          |
| Sig         |          |
| (           |          |
| sk          |          |
| , X         | )        |
| 7:          |          |
| Queries     |          |
| ←           |          |
| Queries     |          |
| ∪ {         |          |
| X           |          |
| }           |          |
| 8:          |          |
| return      |          |
| σ           |          |
| 3:          |          |
| A           |          |
| OSig        |          |
| (           |          |
| pk          |          |
| )           |          |
| →           |          |
| (           | X, σ     |
| )           |          |
| 4:          |          |
| if          |          |
| X           |          |
| ∈           |          |
| Queries     |          |
| then return |          |
| 0           |          |
| 5:          |          |
| return      |          |
| 1           |          |
| Ver         |          |
| (           |          |
| pk          |          |
| ,X,σ        | )        |

So, EF-CMA is very similar to the security notion we have for MAC.

## 7.7 Towards Post-Quantum Cryptography

All public-key algorithms we have seen so far are either based on the factoring problem or the discrete logarithm problem. Both problems can easily be solved with quantum computers [78]. When these devices will become available (although it is impossible to predict when and if this will be the case), we will not have any security when using these algorithms. For that, we need alternate schemes based on different problems.

So far, the most promising directions seem to rely either on problems from coding theory (such as the McEliece cryptosystem [58] or the TCHo cryptosystem [34]), or based on lattices (such as NTRU [44] or Regev [67]).

Lattices are discrete subgroup of the vector space Rm, or more simply, the set of the linear combinations with integral coefficients of vectors from a basis of the lattice.

$${\mathcal{L}}({\vec{a}}_{1},\ldots,{\vec{a}}_{n})=\left\{\sum_{i=1}^{n}s_{i}{\vec{a}}_{i}\ ;\ s_{1},\ldots,s_{n}\in{\mathbf{Z}}\right\}$$
In this structure, given the basis ⃗a1*, . . . ,⃗a*n, it is hard to find short non-zero vectors ⃗x ∈ L(⃗a1*, . . . ,⃗a*n).

Given the basis and some vector ⃗b ∈ Rm, it is also hard to find ⃗x ∈ L(⃗a1*, . . . ,⃗a*n) making ∥⃗b − ⃗x∥

small. Many cryptographic algorithms are based on lattices. We can even construct some _fully homomorphic encryption_, i.e. some encryption $\mathsf{Enc}$ such that we have public functions $f_{+}$ and $f_{\times}$ such that for all $x$ and $y$,

$$\mathsf{Dec}\left(f_{+}(\mathsf{Enc}(x),\mathsf{Enc}(y))\right)=x+y$$

and

$$\mathsf{Dec}\left(f_{\times}(\mathsf{Enc}(x),\mathsf{Enc}(y))\right)=xy$$
or at least with high probability. Based on f+ and f×, we can compute any polynomial function on encrypted data, so consider secure outsourced computations. One problem with lattice-based cryptography is that the size of public keys is typically large. Nevertheless, it is likely to become standard in the near future.

As an example, we describe the cryptosystem of Regev [67] on Fig. 7.12. First, we have some common parameters which consist of some prime p, some real *ε >* 0, some integers m and n such that n2 ≤ p ≤ 2n2 and m = (1 + ε)(n + 1) log2 p, and some real number α =
1
√n log2
2 n. If X is a random variable with normal distribution N(0*, αp*) with expected value 0 and standard deviation
αp, we denote by χ the distribution of the random variable ⌊X⌉ obtained by rounding X to the nearest integer. (So, the order of magnitude of a random variable following χ is 4√p/ log2
2 p.) A
secret key is just a vector ⃗s ∈ Zn p. To construct a public key, we first pick a random m×n matrix A
with coefficients in Zp. Then, we pick a vector ⃗e of length m with random independent coefficients following χ. (So, ⃗e has a short norm.) We set ⃗b = *A⃗s*+⃗e mod p. (So, ⃗b is close to *A⃗s* and *A⃗s* leaks
⃗s because m is larger than n. Clearly, we really need the search for a close vector to be hard.)
The public key is the pair (A,⃗b). To encrypt a bit x, we compute the pair (c1, c2) defined by first picking a random row (v1*, . . . , v*m) of bits, then by c1 = Pm i=1 viAi mod p (where Ai is the ith row of A) and c2 = x p

                     2
                      
                        + Pm
                             i=1 vibi mod p. To decrypt (c1, c2), we compute d = c2 − c1⃗s mod p,
which is normally equal to x
                                p

2
 
  −Pm
       i=1 viei mod p, so close to x
                                      p

                                                                       2
                                                                         
                                                                          . Then, we check if it is closer
to 0 than
            p

            2
             
               to deduce x.
   The Regev scheme inspired many others which are essentially some variants of the following
construction.
   We define the following algebra. We consider six additive Abelian groups Ssk, SA, SB, St, SU,
and SV and four bilinear mappings which are all denoted with ×: SA ×Ssk → SB, SU ×Ssk → SV ,
St × SA → SU, and St × SB → SV . We assume associativity in the sense that

$$(t\times A)\times{\mathsf{s k}}=t\times(A\times{\mathsf{s k}})$$
for all t ∈ St, A ∈ SA, and sk ∈ Ssk. We also assume that there is a norm *∥ · ∥* on Ssk, SB, St, SU, and SV . (It is symmetric, positive, and satisfies the triangular inequality.) We assume we can upper bound ∥x × y∥ in terms of ∥x∥ and ∥y∥ for the four bilinear functions. Finally, we assume two functions encode : *M →* SV and decode : SV *→ M* such that encode is injective. The image set C = encode(M) is called a *code*. Decoding finds *one* closest codeword in the following sense:

$\forall W\in S_{V}\quad\text{decode}(W)=\underset{\text{pt}}{\operatorname{arg\,min}}\ \|W-\text{encode}(\text{pt})\|$
Informally, elements with a small norm are called *sparse*. In what follows, we use small letters to designate sparse elements. We define a PKC as follows in which the choice of the algebra, norm, encoding/decoding, and the probability distributions are left free:
Algorithm gen(coinA):
1: pick a random A ∈ SA and random *sparse* sk ∈ Ssk and d ∈ SB by using coinA 2: B ← A × sk + d 3: pk ← (*A, B*)
4: **return** (sk, pk)
Algorithm enc(pk, pt; coinB):
5: parse pk = (*A, B*)
6: pick random *sparse* t ∈ St, e ∈ SU, and f ∈ SV by using coinB 7: U ← t × A + e 8: V ← t × B + f + encode(pt)
9: **return** ct = (*U, V* )
Algorithm dec(sk, ct):
10: parse ct = (*U, V* )
11: W ← V − U × sk
12: pt′ ← decode(W).

13: **return** pt′
Thanks to bilinearity and associativity, we have W = δ + encode(pt) with

$\delta=t\times d+f-e\times\mathsf{sk}$ (7.1)
This value δ will be called the *noise*. By controlling (with their respective probability distribution)
the size of t, d, f, e, sk, we can make sure that the noise δ is sparse. Hence, decode(W) = pt. The scheme is depicted on Fig. 7.13.

We mention two examples of real cryptosystems based on this construction.

* _FrodoPKE-640_: we set $q=2^{15}$, $\bar{m}=\bar{n}=8$, $n=640$, and $\ell=2$. Then, the algebra is defined by $$S_{\bf k}=S_{B}={\bf Z}_{q}^{n\times\bar{n}}\quad S_{A}={\bf Z}_{q}^{n^{2}}\quad S_{t}=S_{U}={\bf Z}_{q}^{\bar{m}\times\bar{n}}\quad S_{V}={\bf Z}_{q}^{\bar{m}\times\bar{n}}$$ So, elements are matrices of various sizes, with coefficients in ${\bf Z}_{q}$. The bilinear functions are matrix multiplications. The norm is defined by

$$||X||=\max_{1,j}\qquad\qquad2\choose2\bmod q\Bigr{)}-\frac{q}{2}$$
and encoding works as follows:

$$\left|\left(\left(X_{i,j}+\frac{q}{2}\right.\right.\right.$$

$$\left.\left(\text{encode(pt)}\right)_{i,j}=q2^{-\ell}\sum_{k=1}^{\ell}2^{k-1}\text{pt}_{\ell((i-1)\bar{n}+(j-1))+k}\right.\right.$$
This means that each matrix element encodes ℓ bits of the plaintext.

- *NewHope512CPA-PKE*: We set q = 12 289 and n = 512. Then, the algebra is defined by
Ssk = SA = SB = St = SU = SV = Zq[z]/(zn + 1)
So, elements are polynomials in $z$ modulo $z^{n}+1$ and modulo $q$. Hence, they are represented as polynomials with degree bounded by $n-1$ and coefficients in $\mathbf{Z}_{q}$. The bilinear functions are defined by the multiplication in this structure, i.e. the multiplication of polynomials modulo $z^{n}+1$ and modulo $q$. The norm is defined by

$$\left\|\sum_{i=0}^{n-1}X_{i}z^{i}\right\|=\max_{i}\left|\left(\left(X_{i}+\frac{q}{2}\right)\,\mathrm{mod}\;q\right)-\frac{q}{2}\right|$$

and encoding works as follows:

$$\mathsf{encode}(\mathsf{pt})=\frac{q}{2}\sum_{i=1}^{n}(z^{i-1}+z^{i+255})\mathsf{pt}_{i}$$
This means that each bit of the plaintext appears as the most significant bit of two elements.

In 2022, NIST selected for the post-quantum cryptography standard one encryption algorithm and three digital signature schemes. The encryption algorithm is CRYSTALS-KYBER. It is based on lattices and follows the above meta-structure. Like for NewHopes, it uses Zq[z]/(zn + 1) but for q = 3329 and n = 256. In addition to this, it uses heavily optimized algorithms. For instance, instead of representing polynomials in Zq[z]/(zn +1) by their sequence of coefficients, it represents them through the so-called *NTT transform* which enables faster multiplication.

The three NIST selected signature schemes are CRYSTALS-DILITHIUM, FALCON, and SPHINCS+. The first two are based on lattices. The last one is so called *hash-based*.

The Fujisaki-Okamoto transform.

Most of the cryptosystems start with a weakly secure
(typically: INDCPA-secure) scheme which is transformed by a strongly secure one (typically: INDCCA) using standard techniques.

These techniques are essentially based on the one proposed by Fujisaki and Okamoto in 1999 [39, 40].

Essentially, they start from a cryptosystem
(Gen0, Enc0, Dec0) which is secure against decryption under CPA and also γ-spread. This latter notion means that there is no ciphertext value which is taken too often. More precisely

$$\forall\mathsf{pk},\mathsf{pt},\mathsf{ct}\qquad\quad\Pr[\mathsf{Enc}_{\mathsf{pk}}(\mathsf{pt})=\mathsf{ct}]\leq2^{-\gamma}$$
The construction also uses a one-time secure cipher (which we take as one-time pad below) and two random oracles G and H. The new cryptosystem is defined with Gen = Gen0 as follows:
Encpk(pt):
Decsk(ct1, ct2):

1: pick σ
2: ct2 ← pt ⊕ G(σ)
3: ct1 ← Enc0,pk(σ; H(σ, ct2))
4: return (ct1, ct2)

1: σ ← Dec0,sk(ct1)
2: if σ = ⊥ then return ⊥
3: if
       ct1
             ̸=
                  Enc0,pk(σ; H(σ, ct2))
   then return ⊥

4: pt ← ct2 ⊕ G(σ)
5: return pt

Hash-based signatures.

Unlike encryption, we can build a signature scheme from a one-way function only.

One key idea dates from the Lamport signature scheme which can be used only once, to sign an n-bit message: the secret key is a tuple of 2n random values (ski,b)i,b for b *∈ {*0, 1} and i = 1*, . . . , n*.

The public key is the tuple of all pki,b = OW(ski,b), following a one-way function OW. To sign an n-bit message m1 *· · ·* mn, the signer reveals σi = ski,mi for i = 1*, . . . , n*. To verify the signature, the verifier checks that pki,mi = OW(σi) for every i.

Many improvements are possible. A substantial one was made to enable a signature scheme which could be used a few times instead of only once. The secret key is a tuple of kt random values
(ski,j)i,j for i = 1*, . . . , k* and j = 1*, . . . , t*. The public key is the tuple of all pki,j = OW(ski,j). To sign a message m, we first hash it and parse the result H(m) as a sequence j1*, . . . , j*k of indices ji ∈ {1*, . . . , t*}. In other words, the hash is a sequance of k indices between 1 and t. The signature is the tuple of all σi = ski,ji for i = 1*, . . . , k*. To verify the signature, the verifier (after hashing the message) checks that pki,ji = OW(σi) for every i.

In both constructions, the public key can be compressed into a single hash by using a Merkle tree. The idea is that every value to authenticate is put on a leave of a binary tree. In this tree, the values of the children of a node are hashed together in order to define the value of the parent. Hence, by propagating the hashes, we obtain the value of the root of the tree. This value is the compression of all others. In order to authenticate a single value, we provide the valus of the sibling of every ancestor so that the value of the root can be computed again. Provided that the hash function is collision-resistant, this is a secure way to compress.

The SPHINCS+ signature scheme is based on all these techniques. It uses a Merkle tree to authenticate many public keys. Each key is a compressed public key of the few-time signature scheme. To sign a message, it is first hashed together with a random value (to be provided in the signature) in order to define a digest and the index of a compressed key to use. Then, this key is used to sign the digest as above.

## 7.8 Other Primitives

There is a variant of the public-key cryptosystem primitive called key encapsulation mechanism (KEM) [30]. In this primitive, there are again three algorithms: a key generation, an encryption KemEnc, and a decryption algorithm KemDec.

Key generation and decryption are similar as in public-key cryptosystems.

Encryption however is not used to encrypt a message.

Instead, running the KEM encryption algorithm KemEnc with a public key pk produces a plaintext K and a ciphertext C. I.e., there is no control on which plaintext K is encrypted. The produced plaintext K is just random.

The plaintext K is meant to be used as a symmetric key in *hybrid encryption* (see Fig. 7.14).

Indeed, KEM is to be used with a *data encapsulation mechanism (DEM)* which can encrypt or decrypt a message with a symmetric key. So, with KEM and DEM together, we DEM-encrypt a message with the key produced by the KEM-encryption and we concatenate the two ciphertexts (the one from KEM and the one from DEM). To decrypt, we first apply the KEM-decryption to recover the symmetric key then run the DEM-decryption to recover the message.

Another useful primitive which can be met in cryptographic protocols is the commitment scheme. We have already seen some construction based on hash functions. We can also propose some based on the discrete logarithm problem.

In the *Pedersen commitment* [62], we use a subgroup of Z∗
p of prime order q, proposed with two generators g and h. To commit on a number X, we pick r ∈ Zq and disclose c = gXhr mod p.

Opening the commitment consists of revealing X and r and checking the correctness of c.

This commitment scheme is unconditionally hiding: the distribution of c is statistically independent from X. The commitment is also computationally binding: being able to open c on two different values X and X′ is equivalent to computing the discrete logarithm of h in basis g.

Indeed, if c = gXhr mod p and c = gX′hr′ mod p, a = X′−X
r−r′ mod q is such that h = ga mod p.