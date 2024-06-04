
## Chapter 3 Cryptanalysis (Public-Key)

In this chapter, we review some case studies about situations where things can become badly insecure with public-key cryptography. We also start a systematic study of security analysis, to try to assess the difficulty of breaking security.

## 3.1 Rsa

The so-called *textbook-RSA* cryptosystem [52] works as follows (see Fig. 3.1):

- for key generation, we generate two different prime numbers p and q, compute N = pq and
φ(N) = (p − 1)(q − 1). Then, we pick some e such that gcd(*e, φ*(N)) = 1 and compute
d = e−1 mod φ(N) using the extended Euclid algorithm. The public key is (*e, N*) and the
secret one is (*d, N*).
- for encrypting a number x ∈ ZN, we compute y = xe mod N.
- for decrypting a number y ∈ ZN, we compute x = yd mod N.
For signature, we sign y by computing x = yd mod N and we check that x is a valid signature of y by checking y = xe mod N. Interestingly, y can be extracted from x in the RSA case, so we could have a signature with *message recovery* (see Fig. 3.2).

RSA engineering.

The textbook-RSA cryptosystem looks nice in textbooks. But using it in practice is not a piece of cake. Actually, we first have to realize that messages are not integers in practice, so we need some formatting rules. Then, there are usage and implementation issues. For instance, broadcasting a message to several users (each receiving the encryption of that message with his key) is insecure if the encryption exponent e is small. In general, there are many problems related to small e's or d's. In addition to this, implementation may leak some information through side channels.

Side channels can have various forms. For instance, devices provided with external power leak how much power they use over time. When stressed, devices can make computation errors, and the type of error may leak some information. The execution time may also leak some information. Finally, formatting rules added by protocols may also leak. We will see some leakage examples later.

**RSA ISO standard.** The ISO/IEC 9796 standard is an RSA signature standard providing _message recovery_, but suffering from some vulnerabilities. To sign a message, we apply an invertible formatting rule to transform it into a number, then sign that number using textbook RSA signature. When applying the textbook RSA extraction to the signature, we recover the number of terms of the form $m$.

The formatting rule looks like a look recipe. What is important for the cryptanalysis to follow its to know that given a four-byte message $m=m_{3}m_{3},m_{2}m_{1}$ such that $m_{1}=66$ in hexadecimal and the most significant bit of $S(m_{4})$ is 1 for some byte permutation $S$, then formatting the message will lead to the number

$$x(m)\times\Gamma$$

for the constant $\Gamma=1+2^{64}+2^{128}+\cdots+2^{k-64}$ (where $k$ is the modulus bitlength, assumed to be a multiple of 64) and
x(m) = S(m4)m4S(m3)m3S(m2)m22266
Actually, the ISO standard requires that a single bit of x(m) × Γ is flipped. However, we will ignore it in what follows.

To break the standard (or, actually, the variant of it with no bit flip), we prepare many messages m of the above form and factor x(m). (Since x(m) has a bitlength of 64, this is easy.) Then, we only keep messages m such that x(m) has no prime factor larger than 216. With a pool of a few hundred of such messages, it is likely that we find four messages mg, mh, mi, mj such that x(mg) × x(mh) = x(mi) × x(mj). Consequently, if the σ's denote the signature of these messages, we obtain that σg × σh ≡ σi × σj (mod N). So, we can make an existential forgery under chosen message attack: we just query the signatures σg, σh, σi and we construct the signature σj.

This attack was presented in [17]. It was later extended to the full ISO signature standard [18].

Attack on broadcast RSA with low exponent.

Assuming n users having an RSA public key (*e, N*i), i = 1*, . . . , n* with same e and e so low that e ≤ n, if someone broadcasts the message x
(i.e., sends yi = xe mod Ni to the ith user, i = 1*, . . . , n*), then an adversary can easily decrypt x.

Indeed, he can compute y = xe mod N for N = N1 *· · ·* Nn using the Chinese remainder theorem.

Then, since x must be lower than all Ni's, we have xe < N. So, y = xe over Z. Now, we can use one's favorite algorithm to extract eth roots to y over Z to obtain x. This attack is due to H˚astad [36]. It can be extended when the e's are different but all small.

Attack on related messages.

There are extensions of the previous attack when several messages (with a known algebraic relation between them) are all encrypted with the same RSA public key. For instance, if a message x is concatenated with a counter (e.g., because the protocol requires messages to be numbered) and sent several times with a different counter, we can recover x. Typically, we can extract x from y = xe mod N and y′ = (x + 1)e mod N when e is small.

The idea is essentially the same as the Euclid algorithm: we consider the ideal polynomials (in z) spanned by ze − y and (z + 1)e − y′. This is a pair of polynomials generating the ideal. By linear combination, we can reduce this pair into another equivalent pair where one polynomial is unchanged and the degree of the other is lowered. Typically, if the polynomial P(z) with lowest degree starts has leading monomial αzd and the other Q(z) has βzd′, we replace the latter by Q(z) − β
αzd′−dP(z) mod N. We iterate this reduction until we obtain a pair with a polynomial of form αz − β, yielding the solution x = β
α mod N. This attack was proposed by Coppersmith, Franklin, Patarin, and Reiter [21]. Attacks on low exponents.

There are other problems related to low e's. Actually, the Coppersmith algorithm [19, 20] can be used to solve modulo N a polynomial equation of degree e when a root is known to be lower than N
1
e .

This can be used to decrypt a message when
2
3 of the plaintext bits are already known and e = 3. For instance, using a standard of form Enc(x) = (pattern∥x)3 mod N with x over ℓ bits and N larger than 3ℓ bits, we can write the equation y = (2ℓpattern + x)3 mod N and solve it with the Coppersmith algorithm.

There are other insecurity cases when d is short. For instance, for d of 64 bits, the Wiener algorithm [63] computes d from e and N.

Power analysis.

Using the square-and-multiply algorithm, an RSA-decryption device just scans all the bits of d. For every bit, it is doing a squaring operation. If the bit is 1, it is doing an extra multiplying operation. In some implementations, these operations are done by an arithmetic coprocessor which is using more power than the microprocessor alone. Furthermore, squaring is typically faster than multiplying. So, when looking at the power consumption over time, we can see the square and multiply operations over time (see Fig. 3.3). We deduce all bits of d. This power analysis works for some smartcards, since they use external power sources. The smartcard industry has to address these potential problems by having countermeasures to smoothen the power consumption, of other decryption algorithms.

There are several possible attacks based on power consumption or on the time variation of computations. (See Kocher [39, 40].)
Differential fault analysis.

When RSA decryption is implemented using the Chinese remainder theorem, the device computes yd mod p, yd mod q, and reconstruct yd mod N using CRT.

If the device is stressed (by heating, increasing the power voltage, the clock frequency, etc) at some point it starts making errors. If there is only one computation error, it is likely to be done during either yd mod p or yd mod q. An adversary who feeds the device with y = xe mod N for some random x will get some x′ which is equal to x modulo either p or q but not both. Hence, gcd(x − x′, N) is a prime factor of N and we can deduce p and q. This attack was presented by Boneh, DeMillo, and Lipton [13]. To defeat that, smartcards should have sensors to disconnect when some external stress is detected. A protocol side channel in PKCS#1v1.5.

The PKCS#1v1.5 standard imposes that plaintext messages shall start with 0002 in hexadecimal. Hence, for a k-byte long modulus, the plaintext is between 2 × 256k−2 and 3 × 256k−2. An adversary who has got a ciphertext y can try to submit sey mod N to the server for some chosen s. The server will decrypt and accept it as a valid message only when sx mod N is in this interval. This can be used as an oracle to query whether sx mod N is in this interval for some chosen s. Bleichenbacher [12] made this observation and derived an algorithm which, by using such oracle, is able to fully decrypt y into x. The algorithm was improved by Bardou *et al.* [3].

## 3.2 Diffie-Hellman

The so-called textbook Diffie-Hellman key agreement protocol [24] works as follows. We assume a standard cyclic group (such as Z∗
p, a subgroup of it, an elliptic curve, etc) which is generated by some element g. Alice has a secret key x ∈ Z and a public key X = gx. Bob has a secret key y ∈ Z and a public key Y = gy. They both exchange X and Y and compute K = gxy: Alice computes K = Y x and Bob computes K = Xy. The final key shared by Alice and Bob is K.

If an adversary - Eve - can interfere with the communication, she can perform a man-inthe-middle attack. It consists in running protocols independently with Alice and Bob, then ending up with sharing a key K1 with Alice and a key K2 with Bob. The protocol is supposed to resist to passive attacks: i.e., a passive Eve cannot infer K given g, X, and Y .

To assess the security of the protocol, we consider first the two following problems:

- the Diffie-Hellman problem: given (*g, X, Y* ) in a given group, where X, Y *∈ ⟨*g⟩, compute
K = Xy where Y = gy.
- the discrete logarithm problem: given (*g, Y* ) in a given group, where Y *∈ ⟨*g⟩, compute y
such that Y = gy.
Clearly, the Diffie-Hellman problem reduces to the discrete logarithm. However, the converse is still an open problem.

It must be stressed that the discrete logarithm problem is not always hard. Actually, in the group Zn, which is cyclic, with additive notations, computing the discrete logarithm of Y in basis g means finding y such that Y = gy mod n. This is clearly easy to solve by using the extended Euclid algorithm.

If n is a smooth number, i.e., if all its prime factors are less than a bound B which is small, then the discrete logarithm in a group of order n can be solved with O(
√
B log n) group operations by using the Pohlig-Hellman algorithm. So, the hardness implies a large prime factor in the order of the group. Consequences to cryptography were explored by van Oorschot and Wiener [45].

The Pohlig-Hellman algorithm [48] works as follows: in a group of order n = pα1
1
× · · · × pαr r where the pi's are pairwise different primes and the αi's are non-negative integers, we compute the logarithm of y in basis g

1: for i = 1, . . . , r do
2:
        g′ ← gn/p
                    αi
                    i

3:
        g′′ ← g′p
                   αi−1
                   i

4:
        y′ ← yn/p
                    αi
                    i

5:
        xi ← 0

6:
for j = 0 to αi − 1 do
7:
y′′ ← y′p
αi−j−1
i
8:
compute the discrete logarithm u of y′′ in the subgroup of order pi which is spanned
by g′′ (next algorithm)
9:
y′ ← y′/g′u.pj i
10:
xi ← xi + u.pj i
11:
end for
12: end for
13: reconstruct and yield x such that x ≡ xi (mod pαi i )
Essentially, for each i we do αi discrete logarithms in a group of order pi. The idea is that for each i, by raising y and g to the power n/pαi i , we end up in a group of order pαi i where the new y has the same logarithm in the new basis, modulo pαi i . Then, we recover all "basis-pi digits" of the logarithm from the least significant to the most significant. If some digits are known, we divide y by g raised to the known part power, then raise the remainder to some power of pi so that we end up in a group of order pi, to compute the next digit. The final reconstruction is done by applying the Chinese Remainder Theorem.

To compute a logarithm in a group of prime order p, we apply the Baby-step Giant-step algorithm by Shanks [58]:
Precomputation
1: let ℓ = ⌈
√
B⌉ be the size of a "giant step"
2: **for** i = 0*, . . . , ℓ* − 1 do
3:
insert (giℓ, i) into a hash table
4: end for

## Computation

5: **for** j = 0*, . . . , ℓ* − 1 do
6:
compute z = yg−j
7:
if we have a (*z, i*) in the hash table then
8:
yield x = iℓ + j and stop
▷ we get yg−j = giℓ
9:
end if
10: end for B log n).

Essentially, we store all "giant steps" giℓ in the table and make "baby steps" yg−j from y until we reach one value of the table. This algorithm has a complexity bounded by O(√p) group operations.

So, the Pohlig-Hellman algorithm has a complexity bounded by O((α1 +*· · ·*+αr)√maxi pi). Since the sum of the αi's is bounded by log2 n and pi is bounded by B, we obtain O(
√
The decisional Diffie-Hellman problem.

We already defined the CDH and the DDH problems. Intuitively, the DDH problem consists of deciding whether a value K is the solution to the Diffie-Hellman problem (*g, X, Y* ) or something independent.

There are some groups for which this new hardness assumption does not hold. Among them, we have those for which the discrete logarithm problem is easy, but there are others. For instance, when p is an odd prime, Z∗
p does not satisfy this hardness assumption. Indeed, we can define A(*g, X, Y, K*) as producing 1 if and only if the property K
p

= −1 holds at the same time as the property X
p

=

Y
p

= −1. That is, K is not a quadratic residue if and only if both X and Y
are not quadratic residues. In exp1, we know that if either X or Y is a quadratic residue, then its logarithm is even, so the solution to the Diffie-Hellman problem is always a quadratic residue.

So, A always outputs 1 in this experiment. In exp0, K is independent from (*X, Y* ) so A output 1
with probability 1
2. Thus, Adv(A) = 1
2. This is not negligible!

We can generalize this distinguisher to any group with order equal to some integer w multiplied by a smooth number. Indeed, by raising every element to the power w, we end up in a group in which we can compute logarithms. So, we can have a distinguisher

$$\mathcal{A}(g,X,Y,K)=1\Longrightarrow\log_{y^{w}}K^{w}=\left(\log_{y^{w}}X^{w}\right)\times\left(\log_{y^{w}}Y^{w}\right)$$

Using the same arguments, the advantage of $\mathcal{A}$ is $1-\frac{w}{n}$, where $n$ is the order of $g$. So, the order is close to $1$.

Other man-in-the-middle attacks.

We could refine the man-in-the-middle attack to make sure that K1 = K2 and that Eve can have it as well. A trivial way consists, for Eve, in sending the public key 1 to both Alice and Bob. Clearly, we end up with K1 = K2 = 1. An easy way to avoid this attack is to check that the public keys are not equal to 1.

A more subtle attack works when the order of the group has small factors. For instance, if the order of the group is 2w, Eve can receive X from Alice and send Xw to Bob, receive Y from Bob and send Y w to Alice. The final key for Alice and Bob is K = gxyw. We have X′ and Y ′ living in the subgroup of the square roots of 1. The group is generated by gw. So, Eve can compute the logarithm of X′ in basis gw (which is a bit ξ) and raise Y wξ to obtain K.

More generally, if the order is bw and b is smooth, Eve can proceed the same way. X′ = Xw will be in a subgroup of order b, which is smooth, so she will be able to compute its logarithm in basis gw, obtain ξ (which is now a residue modulo b), and raise K = Y wξ.

To summarize, what could happen with small factors is as follows.

- The discrete logarithm problem is easy if the order is smooth. - The Diffie-Hellman problem can have problem if the order has small factors. For instance:
active attacks leading to K1 = K2, or leakage of static keys.
- The DDH problem is easy if the order has small factors.
To avoid these problems, we could mandate that the group has a prime order.

For the (supposedly) hard cases, we will consider a large subgroup of prime order of Z∗
p, or of an elliptic curve. In the Z∗
p case, one way to define Gen is as follows:

1: pick a random prime q of size s
2: pick a random number p of size poly(s) such that q|p − 1
3: start again until p is prime
4: pick a random h of Z∗
p
p−1
q
mod p
5: set g = h
6: if g = 1, start again with a new h In the Diffie-Hellman protocol, it is also important to check membership to ⟨g⟩ to avoid other attacks. For g ∈ Z∗
p, this can be easily done with the following result.

Alice Bob pick x ∈ Z∗ q, X ← gx X −−−−−−−−−−−−→ if X ̸∈ ⟨g*⟩ − {*1}, abort if Y ̸∈ ⟨g*⟩ − {*1}, abort Y ←−−−−−−−−−−−− pick y ∈ Z∗ q, Y ← gy K ← KDF(Y x) K ← KDF(Xy) (K = KDF(gxy))

Theorem 3.1. Let p, q, g be integers such that p and q are prime, q divides p − 1, g mod p ̸= 1,
and gq mod p = 1. Then, ⟨g⟩ is a subgroup of Z∗
                                      p of order q. Furthermore, ⟨g⟩ is the set of all
Y ∈ Z∗
    p such that Y q mod p = 1.

So, to check membership of Y , we only have to check Y q mod p = 1.

Making the Diffie-Hellman protocol secure.
                                           Another problem could be that K has a weird
distribution depending on how the group is represented. To avoid that, we should consider K as
a seed for a key derivation function KDF.
  Finally, we consider the following Diffie-Hellman protocol: a parameter g generates a group of
prime order q. Alice selects her secret key x ∈ Z∗
                                         q and takes her public key X = gx. Bob selects
his secret key y ∈ Z∗
                 q and takes his public key Y = gy. Alice and Bob check that the received
public keys X and Y are in the group but not equal to 1. Alice and Bob compute Xy = Y x = gxy

then K = KDF(gxy).

One property of this protocol is that if Alice is honest and Y is selected independently of X, then Y x is uniformly distributed in the group except 1. If Bob is honest, then Xy is uniformly distributed in the group except 1.

## 3.3 Elgamal

We assume a cyclic group generated by some g. The *ElGamal* cryptosystem [26] works as follows: (see Fig. 3.5):
- for key generation, we pick an integer x as a secret key and compute the public key y = gx.

- for encrypting a group element m, we pick an integer r and compute the ciphertext (*u, v*) =
(gr*, my*r).
- for decrypting (*u, v*), we compute m = vu−x.
We note that encryption is probabilistic. Indeed, running it multiple times will produce many different ciphertexts which all decrypt to the same message.

To assess the security of the ElGamal cryptosystem, we essentially consider two problems:

- the ElGamal decryption problem: given an ElGamal public key y and a ciphertext (*u, v*),
compute m such that v = myr for some r such that u = gr.
- the ElGamal key recovery problem: given an ElGamal public key y, find x such that y = gx.
Clearly, the ElGamal key recovery problem is equivalent to the discrete logarithm problem.

We can also show that the ElGamal decryption problem is equivalent to the Diffie-Hellman problem. Indeed, given a Diffie-Hellman solving oracle, we decrypt (*u, v*) for key y as follows: we compute X = u and Y = y and submit (*g, X, Y* ) to the oracle to get K = grx. Then, we just divide v by K to obtain m. So, ElGamal decryption reduces to the Diffie-Hellman problem.

Conversely, given an ElGamal decryption oracle, we solve the Diffie-Hellman problem (*g, X, Y* )
by setting u = X, y = Y , picking v at random in ⟨g⟩, sending (*g, y, u, v*) to the oracle to get m = vu−x. Then, we set K = *v/m* and it solves the Diffie-Hellman problem. So, the Diffie-
Hellman problem reduces to ElGamal decryption. Therefore, both problems are equivalent.

Clearly, the ElGamal cryptosystem is not deterministic.

We will further show (in another chapter) that it is IND-CPA-secure, assuming that the DDH problem is hard. ElGamal signature.

The ElGamal digital signature scheme [26] works in the cyclic group Z∗
p generated by some g. It works as follows (see Fig. 3.6):

- for key generation, we pick an integer x as a secret key and compute the public key y = gx.
- to sign a message M, we pick k ∈ Z∗
p−1 at random and the signature is (*r, s*) with r =
gk mod p and s = H(M)−xr
k
mod (p − 1), where H is a hash function.
- to verify that (*r, s*) is a valid signature for M, we check that 0 ≤ *r < p* and that yrrs ≡ gH(M)
(mod p).
Clearly, the key recovery problem is equivalent to the discrete logarithm problem in the same group. There exists a security result further saying that making existential forgeries under chosen message attack is hard, *on average* over the random choice of the parameters (*p, g*), and in the random oracle model, provided that the discrete logarithm problem is hard [49]. We will explain the random oracle model in an upcoming chapter. Unfortunately, security is only guaranteed for the average case: we will see that there are indeed some unfortunate choices of p and g which could make the signature scheme weak.

First, we have to stress that the condition 0 ≤ *r < p* in the signature verification is important.

If we miss it, we can easily make universal forgeries. For that, we first pick rp−1, s ∈ Z∗
p−1 at s y−
rp−1
random. Then, we set rp = g H(M)
s mod p. By using the Chinese remainder theorem, we can find r such that r mod (p − 1) = rp−1 and r mod p = rp at the same time. So, we easily see that (*r, s*) is a valid signature for M, except that r is of order p2 instead of p. So, we really have to check that 0 ≤ *r < p*.

Next, we see an unfortunate choice for p and g which was found by Bleichenbacher [11]. We have to assume that p − 1 = bw with b smooth (e.g., we could take b = 2 since p is odd), and that we know some relation g1/t mod p = cw for some integers t and c. As an example, whenever b generates Z∗
p and p mod 4 = 1, we can take g = b, t = p−3
2 , and c = 1. Indeed,

$$(c w)^{t}\equiv\left({\frac{p-1}{g}}\right)^{\frac{p-1}{2}-1}\equiv-g{\frac{(-1)^{\frac{p-1}{2}}}{g^{\frac{p-1}{2}}}}\equiv g{\pmod{p}}$$
Once we have these two assumptions p−1 = bw and g1/t mod p = cw, we make a universal forgery for M by setting r = cw, finding the discrete logarithm z of ycw in basis gcw, i.e., ycw = gcwz, and taking s = t(H(M) − *cwz*) mod (p − 1). We clearly have 0 ≤ *r < p* and yrrs ≡ ycw(cw)t(H(M)−cwz) ≡ ycwgH(M)−cwz ≡ gH(M)
(mod p)
So, (*r, s*) is a valid signature for M!