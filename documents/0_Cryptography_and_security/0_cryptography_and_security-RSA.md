
## Chapter 3 Rsa Cryptography

In this chapter, we recall basic arithmetic notions, such as the Chinese Remainder Theorem. We study primality testing and present the RSA public-key cryptosystem.

## 3.1 Euler And Other Chinese

We have already seen that Z∗
n is the group of units of the ring Zn: this is the group (for the multiplication) of all elements of Zn which have a multiplicative inverse. We have also seen that for all x ∈ Zn, x is in Z∗
n if and only if gcd(*x, n*) = 1. Finally, we have also seen that Z∗
n contains all elements but 0 (i.e., Zn is a field) if and only if n is a prime number.

The *Euler totient function* is the function φ over the positive integers defined by φ(n) = #Z∗
n.

I.e., φ(n) is the order of the group Z∗
n. Due to the Lagrange theorem, we have the following result.

Theorem 3.1 (Euler Theorem). Given a positive integer n, for all x ∈ Z∗
n *we have* xφ(n) mod n = 1.

Another nice application is the extraction of eth roots in Z∗
n, whenever e has an inverse modulo
φ(n). Indeed, if e has such inverse (i.e., if gcd(*e, φ*(n)) = 1), let d = e−1 mod φ(n). We can easily see that for all x ∈ Z∗
n, xd mod n is the only eth root of x in Z∗
n. To see this, we can first check that it is a root. Then, we show that any root must be equal to this one. To see that xd is an eth root of x, we can just raise it to the power e:

$$(x^{d})^{e}\equiv x^{e d}\equiv x^{1+k\varphi(n)}\equiv x{\pmod{n}}$$
since ed = 1 + kφ(n) for some integer k and since xφ(n) is 1. To see that any eth root y must be equal to x, we start from ye ≡ x. Then, since ye is invertible, ye−1/ye must be an inverse of y, so y ∈ Z∗
n. Consequently, yφ(n) ≡ 1. Now we raise ye ≡ x to the power d and we obtain that

$$x^{d}\equiv y^{e d}\equiv y^{1+k\varphi(n)}\equiv y{\pmod{n}}$$
So, y = xd mod n.

RSA.

This is used in the RSA cryptosystem [71]: the public key consists of a modulus n and some exponent e such that gcd(*e, φ*(n)) = 1. The secret key is the inverse d of e modulo φ(n). To encrypt an element x of Zn, we compute y = xe mod n. To decrypt, we compute x = yd mod n.

Note that, so far, we have shown that it works for x ∈ Z∗
n but not for any x ∈ Zn. We will see this soon. We will also see that by taking n = pq, where p and q are two different prime numbers, then we can compute φ(n) = (p − 1)(q − 1). These are consequences of the Chinese Remainder Theorem.

Chinese Remainder Theorem.

If m and n are coprime positive integers (i.e., gcd(*m, n*) = 1), we can see the rational computations over Zmn as equivalent to the same computations over Zm and Zn in parallel. This is expressed by saying that x 7→ (x mod *m, x* mod n) is a ring isomorphism between Zmn and Zm × Zn.

Theorem 3.2 (Chinese Remainder Theorem). If m and n are coprime positive integers, the
function f defined on Zmn by mapping x to f(x) = (x mod m, x mod n) is a ring isomorphism
between Zmn and Zm × Zn.
  For any a ∈ Zm and b ∈ Zn, we have

f −1(a, b) =
          
           an(n−1 mod m) + bm(m−1 mod n)
                                          
                                            mod (mn)

Proof. Checking that f is a ring homomorphism is straightforward: for the addition, we have

f(x+y) = ((x+y) mod m, (x+y) mod n) = (x mod m, x mod n)+(y mod m, y mod n) = f(x)+f(y)

where the last additions are in Zm × Zn. The same goes for the multiplication.
   We then show that f is injective by showing that f(x) = (0, 0) implies that x = 0 in Zmn.
Indeed, f(x) = (0, 0) implies that both m and n divide x. Since m and n have no prime factor in
common, the unique factoring of x into prime factors must split as the product of m, n, and some
left over prime numbers. More precisely, we can write x = mx′. Let n = pα1
                                                                          1 · · · pαr
                                                                                 r
                                                                                    be the unique
factorization of n into pairwise different primes pi. Since n divides x, each pαi
                                                                              i
                                                                                 divides x = mx′.
Since n is coprime with m, pi does not divide m. Hence, pαi
                                                          i
                                                            divides x′. So, n divides x′ and x′ can
be written x′ = nx′′. Hence, x = mnx′′ and so mn divides x. We deduce that x mod (mn) = 0.
   Finally, f must be an isomorphism because the two rings have the same order and f is injective.
   The explicit formula for f −1 is shown by just checking that f applied to the right-hand side
matches (a, b): the first component of f(
                                         
                                          an(n−1 mod m) + bm(m−1 mod n)
                                                                             
                                                                               mod (mn)) is

$\big{(}an(n^{-1}\bmod m)+bm(m^{-1}\bmod n)\big{)}\bmod(mn)\bmod m\big{)}$

eration is absorbed by the final modulo $m$ reduction.

The modulo mn operation is absorbed by the final modulo m reduction. Then n(n−1 mod m)
reduces to 1 modulo m while m(m−1 mod n) reduces to 0. So, the first component is a. Similarly, the second component is b. So, we have identified f −1(*a, b*).

⊓⊔
The Chinese Remainder Theorem is important enough to see another formulation and proof.

Theorem 3.3 (Chinese Remainder Theorem). Let m and n be coprime positive integers, and let u = n(n−1 mod m) *and* v = m(m−1 mod n). We define g(*a, b*) = (au + bv) mod mn. We note that g(a + *im, b* + jn) = g(a, b) for any integer i and j, so we can define g as a mapping from Zm × Zn to Zmn. We have that g is a ring isomorphism.

Proof. The point that g(a + *im, b* + jn) = g(*a, b*) for any integer i and j is straightforward. The point that g is a group homomorphism is trivial, as g is defined with a linear expression. Now, we can see that g(*a, b*) mod m = a mod m and g(*a, b*) mod n = b mod n. So, we can see that g is a bijection. Therefore, it is a group isomorphism. To show that g is a ring isomorphism, it remains to be shown that it is also homomorphic for the multiplication. For that, we can just see that g−1
is homomorphic for the multiplication (in the way we did it for f before).

⊓⊔
As a direct consequence, we can see that for any a and b, there exists a unique x (modulo mn)
such that x ≡ a (mod m) and x ≡ b (mod n) at the same time. We can use this property, for instance, to deduce from the equalities x ≡ y (mod m) and x ≡ y (mod n) that we in fact have x ≡ y (mod (mn)).

Here is another direct consequence.

Theorem 3.4. Let m and n *be coprime positive integers. We have* φ(mn) = φ(m) × φ(n).

We stress that this holds for gcd(*m, n*) = 1, i.e. not in general.

Proof. We first observe that the group of units of Zm × Zn is the group Z∗
m × Z∗
n. Indeed, if
(*a, b*) is invertible in Zm × Zn, there must be some (*c, d*) such that (a, b) × (*c, d*) = (1, 1). As this means that (ac) mod m = 1 and (bd) mod n = 1, we obtain that (a, b) ∈ Z∗
m × Z∗
n. Conversely, if
(a, b) ∈ Z∗
m × Z∗
n, then (a−1 mod *m, b*−1 mod n) is the inverse of (*a, b*), so (*a, b*) ∈ (Zm × Zn)∗.

Then, the ring isomorphism between Zm × Zn and Zmn induces a group isomorphism between
(Zm × Zn)∗ and Z∗
mn. So, Z∗
m × Z∗
n and Z∗
mn are isomorphic groups. Therefore, they have the same cardinality. I.e., φ(m) × φ(n) = φ(mn).

⊓⊔
Since we already know that φ(p) = p − 1 and φ(q) = q − 1 for two prime numbers p and q, we deduce that when p ̸= q, we have φ(pq) = (p − 1) × (q − 1), which was the announced result in the RSA construction [71].

The Zmn ≈ Zm×Zn result for m and n coprime generalizes to Zpα1
1 ×···×pαr r
≈ Zpα1
1 ×· · ·×Zpαr r for pairwise distinct primes p1*, . . . , p*r. We used this result in Section 2.5 to generate generators of a cyclic group of known order. To compute φ(pa1
1 × · · · × par r ) we have to count the number of invertible elements in the ring Zpα1
1 ×···×pαr r , so to count the number of invertible elements in each Zp
αi i and to multiply them together. In Zp
αi i , a number is invertible if and only if it is coprime with pαi i , hence, if and only if it is coprime with pi. So, we have pαi−1
i non-invertible elements.

So, φ(pαi i ) = (pi − 1)pαi−1
i
. We deduce the general formula to compute φ:

$\varphi(p_{1}^{a_{1}}\times\cdots\times p_{r}^{a_{r}})=(p_{1}-1)p_{1}^{a_{1}-1}\times\cdots\times(p_{r}-1)p_{r}^{a_{r}-1}$
when the pi's are pairwise different prime numbers and the ai's are positive integers.

An application of the Chinese Remainder Theorem is the proof that RSA works over Zn and not only on Z∗
n.

Theorem 3.5. Let p and q be two different primes. Let n = pq, e be coprime with φ(n) and d = e−1 mod φ(n). For all x ∈ Zn*, we have* xed mod n = x.

Therefore, the decryption of the encryption of x is x for all x ∈ Zn. Proof. We know that (ed) mod (p − 1) = 1. So, due to the Little Fermat Theorem (Th. 2.10), we have that xed mod p = x for all x ∈ Z∗
p. For x = 0, we also have xed mod p = x. So, we have xed mod p = x for all x ∈ Zp. Similarly, we have xed mod q = x for all x ∈ Zq. So, xed matches x modulo p and modulo q. Since p and q are coprime, due to the Chinese Remainder Theorem, xed matches x modulo n as well: xed mod n = x.

⊓⊔
Another interesting application is the RSA acceleration algorithm: to compute yd mod n, instead of running the square-and-multiply algorithm with the values y, d, and n, which takes a cubic time in the length of n, we can compute dp = d mod (p − 1), dq = d mod (q − 1), yp = ydp mod p, yq = ydq mod q, and f −1(yp, yq). Clearly, yp is equal to yd modulo p, and yq is equal to yd modulo q. So, f −1(yp, yq) is equal to yd modulo p and modulo q. So, it is yd modulo n. Those operations work in quadratic time, except the ones for computing yp and yq, which work in cubic time, but with half-size inputs. So, the expected speed-up factor must be close to 4 if we implement the computation this way.

## 3.2 Primality Testing

Given an integer n, the regular trial division algorithm factors n within √n arithmetic operations, which is huge. It can also be used to check primality, but this is highly inefficient. Fermat primality test.

If n is prime and b ∈ {1*, . . . , n* − 1}, we know that bn−1 mod n = 1.

This is the little Fermat Theorem (Th. 2.10). We can use this property to check primality: given n, we pick a random b ∈ {1*, . . . , n* − 1} then check if bn−1 mod n = 1. This is called the Fermat test. The algorithm is as follows: Input: n, an integer of ℓ bits, and a parameter k

1: repeat
2:
pick a random b such that 0 < b < n
3:
x ← bn−1 mod n
4:
if x ̸= 1 then
5:
output "n is composite" and stop
6:
end if
7: **until** k iterations are made 8: output "n may be prime" and stop Let Prime be the event that n is prime and Maybe be the event that the algorithm return "n may be prime". The Little Fermat Theorem says that Pr[Maybe|Prime] = 1: prime numbers will always pass this test. But the remaining question is to bound Pr[Maybe|¬Prime]. Unfortunately, there exist a category of non-prime numbers which may pass it with high probability (but not always)
as well: the *Carmichael numbers*. We give below the definition and characterization of Carmichael numbers without a proof.

Theorem 3.6 (Carmichael numbers). For an integer n, the two following properties are equivalent.

- The number n is a product of (at least 2) pairwise different prime numbers pi *such that* pi−1
is a factor of n − 1.
- The number n is composite and for any b *such that* gcd(*b, n*) = 1*, we have* bn−1 ≡ 1 (mod n).
If this happens, we say that n *is a* Carmichael numbers.

For instance, n = 561 is a Carmichael number since n = 3 × 11 × 17, and for p *∈ {*3, 11, 17}, we can check that p − 1 is a factor of n − 1.

When we have a Carmichael number n, we can easily see that whenever b ∈ Z∗
n, we have bn−1 mod n = 1. Indeed, we have bn−1 mod p = 1 for each prime factor p of n due to the Little Fermat Theorem, since n − 1 is a multiple of p − 1. Hence, by applying the Chinese Remainder Theorem, we deduce that bn−1 mod n = 1. When b ̸∈ Z∗
n, we cannot obtain bn−1 mod n = 1. So, in that case, we have that Pr[Maybe|n] =

φ(n)
n−1
k
.

With n = 949 631 589 089, we have another Carmichael number. Actually, we have

$$\begin{array}{r c l}{n}&{=}&{6917\times10193\times13469}\\ {n-1}&{=}&{2^{5}\times7^{3}\times13\times19\times37\times9467}\end{array}$$
Hence

$$\Pr[\mathsf{Maybe}|n]=\left(\frac{\varphi(n)}{n-1}\right)^k=\left(\frac{9464}{9467}\right)^k\approx(1-0.000317)^k$$
So, even with many iterations k, the probability that n passes this test is not acceptable. Therefore, we have to extend this primality test to exclude Carmichael numbers. Miller-Rabin primality test.

Given n, we easily rule out the particular cases of n = 2 and n even. For n odd, we write n − 1 = 2st with t odd. Given a random b ∈ {1*, . . . , n* − 1}, we compute the chain (bt mod *n, b*2t mod *n, . . . , b*2st mod n).

(Note that only the last term of the chain is computed in the Fermat test.) If the chain is of form (1, 1*, . . . ,* 1), or of form (∗, . . . , ∗, −1, 1*, . . . ,* 1), we say that n passes the test.

The algorithm is as follows:
Input: n, an integer of ℓ bits, and a parameter k

1: if n = 2 then
2:
output "n is prime" and stop
3: end if 4: if n is even then
5:
output "n is composite" and stop
6: end if
7: write n = 2st + 1 with t odd
8: repeat
9:
pick b ∈ {1, . . . , n − 1}
10:
x ← bt mod n, i ← 0
11:
if x ̸= 1 then
12:
while x ̸= n − 1 do
13:
x ← x2 mod n, i ← i + 1
14:
if i = s − 1 or x = 1 then
15:
output "n is composite" and stop
16:
end if
17:
end while
18:
end if
19: **until** k iterations are made 20: output "n may be prime" and stop With the same notations as in the Fermat test, we clearly have Pr[Maybe|Prime] = 1: prime numbers always pass this test, as the previous element in the chain must be a square root and that the only square roots of 1 are 1 and −1 in the field Zn (this is when n is prime). We will see this in Th. 3.10. We actually have the following result.

Theorem 3.7. For an odd number n = 2st + 1 where t is odd, n is a prime number if and only
if for all b ∈ Z∗
           n, the chain of (bt mod n, b2t mod n, . . . , b2st mod n) is either of form (1, 1, . . . , 1)
or of form (∗, . . . , ∗, −1, 1, . . . , 1).

Proof (sketch). When n is prime, the proof is straightforward. To prove the backward direction,
we assume that all chains are of form (1, 1, . . . , 1) or (∗, . . . , ∗, −1, 1, . . . , 1). This implies that for
all b ∈ Z∗
        n, we have bn−1 mod n = 1. We can show that this implies that either n is prime or that
n is a Carmichael number. Then, we can prove that if n is a Carmichael number, there are some
b ∈ Z∗
     n such that the chain is not of the correct form.
                                                                                               ⊓⊔

We can even show a more precise result.

Theorem 3.8. Let n be an odd number n = 2st + 1 where t is odd. We say that b passes the
test if the chain of (bt mod n, b2t mod n, . . . , b2st mod n) is either of form (1, 1, . . . , 1) or of form
(∗, . . . , ∗, −1, 1, . . . , 1). The number n is prime if and only if the cardinality of the set of all b ∈ Z∗
                                                                           n
which pass the test is at least 1

4φ(n).

So, we deduce that Pr[Maybe|¬Prime] ≤ 4−k. So, by having k relatively small, we can rule out
composite numbers reliably.
   Note that one iteration of this test has a cubic complexity. A composite number is most likely
to be ruled out in the very first iterations, so they are eliminated in cubic time. Contrarily, a
prime number has to go through all the k iterations before being declared as maybe prime.

Prime number generation.
                         The best way to find a prime number is to pick a random number
and try again until it is prime! We have the following important result from number theory.

ln N .

Theorem 3.9 (Prime Number Theorem). The probability that a random element selected in
the set {1, 2, 3, 4, . . . , N} is prime is asymptotically equivalent to
                                                 1

So, to pick a prime number of size ℓ, we need O(ℓ) trials. Since we repeat O(ℓ) times the primality
test, we want to make sure that for a single test we have Pr[Maybe|¬Prime] ≤ ε

                                                                                                         ℓ for some small
constant ε. So, we need k = 1

                               2 log2
                                      ℓ
                                      ε = O(ℓ) due to Pr[output : maybe prime|¬prime] ≤ 4−k. Each
of the O(ℓ) trials eliminates the composite number in time O(ℓ3). The final test takes a bit more
time but is not larger than O(ℓ4). So, we can pick a random prime number of size ℓ within a
complexity of O(ℓ4).

## 3.3 Rsa Basics

We describe again the RSA cryptosystem [71]: the key generation consists of generating two different large prime numbers p and q. The public key consists of a modulus n = pq and some exponent e such that gcd(*e, φ*(n)) = 1. I.e., pk = (*e, n*). Note that φ(n) = (p − 1)(q − 1). The secret key is the inverse d of e modulo φ(n). Actually, sk = (*d, n*) since we still need n to decrypt.

To encrypt an element x of Zn, we compute y = xe mod n. To decrypt, we compute x = yd mod n.

(See Fig. 3.1.)
The key generation takes time O(ℓ4), where ℓ is the length of the modulus. Encryption and decryption take O(ℓ3). But if we are up to use a fixed exponent e, the length of e becomes constant and the complexity of encryption becomes O(ℓ2). One typical example for such e is e = 216 + 1.

Indeed, raising x to the power e consists of 16 squares and one multiplication. But we shall not forget that p and q must be such that p − 1 and q − 1 are coprime with e. Since e is a prime number, this is most likely to be the case!

Compared with the ElGamal cryptosystem, we can see that the complexity of the key generation in RSA is pretty high (if the ElGamal parameters are common to every users, so that they need not to be generated for each of them). But the ElGamal cryptosystem is length-increasing. Finally, one advantage of the ElGamal cryptosystem is that it can adapt to many types of groups
(e.g., elliptic curves) whereas it is not so easy to make RSA work outside Zn.

## 3.4 Quadratic Residuosity

In a field, the equation x2 = 1 leads to two solutions +1 and −1 and nothing more. Theorem 3.10. For x ∈ K where K *is a field, we have that* x2 = 1 *is equivalent to either* x = +1
or x = −1.

Proof. We have 0 = x2 − 1 = (x + 1)(x − 1) but in a field, ab = 0 is equivalent to either a = 0 or b = 0. So, x2 = 1 is equivalent to either x + 1 = 0 or x − 1 = 0.

⊓⊔
Note that in rings, ab = 0 does not always imply that a = 0 or b = 0. For instance, in Z15, we have 3 × 5 = 0. We also have 42 = 1. So, we may have more than two roots in rings.

In fields, except when 2 = 0 (which happens when we work modulo 2), we have +1 ̸= −1. So, we have exactly two square roots of 1.

The Zp case.

For p prime and odd, elements of Z∗
p have either 0 or 2 square roots. Elements with square roots are called *quadratic residues*. The set of all quadratic residues forms a subgroup of Z∗
p. We can easily identify quadratic residues and even extract square roots in this group.

Theorem 3.11. Given a prime p, an element x of Z∗
p is a quadratic residue if and only if x p−1
2
mod p = 1.

Proof. Indeed, if there is a y such that x = y2 mod p, we have x p−1

                                                                                    2
                                                                                        ≡ yp−1 ≡ 1. So, a quadratic
residue x satisfies x
                         p−1

                      2
                          mod p = 1.
Conversely, if x
                    p−1

2
   mod p = 1, we can write x ≡ ge for a generator g (we know that Z∗
                                                                                             p is

cyclic as shown in Th. 2.11). So, ge p−1

2
   ≡ 1. This implies that p − 1 divides e p−1

                                                                                         2 , since g is a
generator. So, e must be even. We deduce that x is the square of g
                                                                         e
                                                                         2 : it is a quadratic residue.
                                                                                                        ⊓⊔

When p ≡ 3 (mod 4) (so that p+1

                                       4
                                           is integer), there is an easy trick to extract square roots
which is given by the following result.

Theorem 3.12. Given a prime p such that p ≡ 3 (mod 4), if x ∈ Z∗
                                                     p is a quadratic residue, then

x
 p+1

4
   is a square root of x.

Proof. First of all, p+1

4
   is clearly an integer, by the assumption on p. Furthermore, if x ≡ y2, we

4
   is a square root of x.
                                                                        ⊓⊔

have
    
     x
       p+1

4
  2
      ≡ yp+1 ≡ y2 ≡ x. So, x
                                     p+1

   For any odd prime numbers, square roots can be extracted using the Tonelli algorithm, which
works with cubic complexity. The algorithm is as follows.
Input: a prime p ≥ 3 and a quadratic residue a ∈ Z∗
                                                   p

1: repeat
2:
        choose g ∈ Z∗
                         p at random

3: until g is not a quadratic residue
4: let p − 1 = 2st with t odd

p−1

5: e ← 0
6: for i = 2 to s do
7:
        if (ag−e)

2i mod p ̸= 1 then

8:
            e ← 2i−1 + e

9:
        end if

10: end for

2 a
   t+1

11: output g−t e

p

                       2
                           mod p
    Finally, we define the Legendre symbol. Given an odd prime number p and an integer x, we
define
                            x

 =

  0 if x mod p = 0 +1 if x is a quadratic residue modulo p −1 otherwise  2 (mod p) p (Note that this is not a fraction: this is a new notation!) Clearly, we have x  ≡ x p−1
The Zn case.

In the ring Zn, quadratic residuosity is more subtle. For instance, for n = pq, with two different odd prime numbers p and q, since elements can have two square roots modulo p, two square roots modulo q, we have four combinations which, due to the Chinese Remainder Theorem, reconstruct four different square roots. More precisely, if a is a square root of x modulo p and if b is a square root of x modulo q, then x ≡ y2 (mod n) is equivalent to y mod p ∈ {a, p−a}
and y mod q ∈ {*b, q* − b}.

We define the *Jacobi symbol*, which generalizes the Legendre symbol: given an odd integer with known factorization n = pa1
1 × · · · × par r , we define

n p1 pr ar a1 × · · · ×  x  =  x x
Although x ∈ Z∗
p is a quadratic residue if and only if (x/p) = +1 (in the odd prime p case), we only have that x ∈ Z∗
n is a quadratic residue implies that (x/n) = +1 (in the odd composite n case). The converse is not true. There are always some integers x such that (x/n) = +1 but which have no square roots. These are "fake" quadratic residues. We can easily construct them by taking non-quadratic residues modulo p and modulo q and combining them using the Chinese Remainder Theorem. Namely, by taking xp ∈ Zp such that (xp/p) = −1 and xq ∈ Zq such that (xq/q) = −1, then x ∈ Zpq such that x mod p = xp and x mod q = xq, we have (x/p) = (x/q) = −1 so
(*x/pq*) = +1 but x is not a quadratic residue modulo p to it cannot be a quadratic residue modulo pq.

The Jacobi symbol is always easy to compute, even though we may not have the factorization of n at disposal. The algorithm is similar to the Euclid algorithm and is quadratic. Indeed, we have the following properties.

Theorem 3.13. Let a, b, c be integers.

- If b is odd, then
 1
b

= 1.
- If b is odd, then
 a
b

=
 a mod b
b

.
c

=
 a
c
  b
c

.
- If c is odd, then
 ab
- If a is odd, then
- if a *≡ ±*1 (mod 8), then
 2
a

= +1;
a

= −1.

- if a *≡ ±*3 (mod 8), then
 2

- If a and b are odd, then
- if a ≡ b ≡ 3 (mod 4), then a

b
 
   = −
          b

a
 
  ;

- otherwise,
           a

b
 
   =
       b

a
 
  .

b
 
   for b odd, we first reduce to
                                         a mod b

So, to compute
               a

                                                                   b
                                                                        
                                                                          to have the upper part smaller than
the lower part. Then, to compute
                                            a

                                             b
                                               
                                                 with 0 ≤ a < b, we write a = 2αa′ for some odd a′ then
use the multiplicativity property to reduce to the computation of
                                                                                     2

b
 
   (which is covered by the

above properties), and of
                         
                           a′
                           b
                             
                               where a′ is odd and lower than b. Then, we use the last property

                                  a′
                                    
                                      where the lower part is decreased. We iterate this process
and finally obtain a trivial Jacobi symbol to compute.

to reduce to the computation of
                                b

  The mapping x 7→ (x/n) is a group homomorphism from Z∗
                                                   n to {−1, +1}. So, the set of all x
such that (x/n) = +1 is a subgroup of Z∗
                                  n. This subgroup contains another important one: the
subgroup QRn of all quadratic residues. We explain here the properties of QRn.

- x ∈ QRn implies (x/n) = +1. The converse is not true in general. Indeed, there exists
non-quadratic residues x which "look like" quadratic residues in the sense that (x/n) = +1.
These are "fake" quadratic residues.
When n = pq is the product of two different odd primes p and q, (x/n) = +1 is equivalent to (x/p) = (x/q), meaning that the quadratic residuosity status is the same modulo p and modulo q. However, x ∈ QRn is equivalent to (x/p) = (x/q) = +1.

- x ∈ QRn and y ∈ QRn imply xy ∈ QRn. - x ∈ QRn and y ∈ Z∗
n − QRn imply xy ∈ Z∗
n − QRn.
- For p prime, we further have x ∈ Z∗
p − QRp and y ∈ Z∗
p − QRp imply xy ∈ QRp. (We can see
it by using the Legendre symbol of xy.)
When n = pq is the product of two different odd primes p and q and G is the subgroup of Z∗
n of all x such that (x/n) = +1, for x ∈ G, we have x ∈ QRn is equivalent to (x/p) = +1.

Hence, x ∈ G − QRn and y ∈ G − QRn imply xy ∈ QRn.

Quadratic residuosity finds many applications in cryptography.

The Goldwasser-Micali cryptosystem.

For instance, we can construct the Goldwasser-Micali cryptosystem [41, 42]: we set up the keys by taking n = pq for two different odd primes p and q and x ∈ G − QRn. The public key is pk = (*x, n*) and the secret key is sk = p. This cryptosystem can encrypt one bit b by Encpk(b) = r2xb mod n for r ∈ Z∗
n random. We have (x/p) = −1. So, we clearly have (−1)b = (y/p). To decrypt, we can thus define Decsk(y) = b such that (−1)b = (y/p).

(See Fig. 3.2.)
We can also define a primality test. The Solovay-Strassen test [80] checks the primality of an odd p by checking that b p−1
2
= (b/p) for a random b. It relies on the following result.

Theorem 3.14. Let n be an odd number. We have

$n$ prime $\quad\Longrightarrow\quad\forall b\in{\bf Z}_{n}^{*}\quad b^{\frac{n-1}{2}}\equiv\left(\begin{array}{c}b\\ n\end{array}\right)\quad({\rm mod}\ n)$

$n$ prime $\quad\Longleftarrow\quad\Pr_{b\in{\bf Z}_{n}^{*}}\left[b^{\frac{n-1}{2}}\equiv\left(\begin{array}{c}b\\ n\end{array}\right)\quad({\rm mod}\ n)\right]>\frac{1}{2}$
for b ∈ Z∗
n with uniform distribution.

We can break the DDH problem (seen in the previous chapter) in Z∗
p: let g be a generator of Z∗
p. Given (X, Y, Z) ∈ (Z∗
p)3, we let *x, y, z* be such that X = gx, Y = gy, and Z = gz in Z∗
p.

Then, we can decide if (*X, Y, Z*) was taken randomly with uniform distribution or if (*X, Y* ) was taken randomly with uniform distribution but z was selected as being z = xy, so Z is the solution of the Diffie-Hellman problem in basis g with input (*X, Y* ). For this, we compute a = 1(Z/p)=−1, b = 1(X/p)=(Y/p), and compare a and b. If a = b we output 1. Otherwise we output 0.

We first observe that (g/p) = −1 because g is a generator. (Otherwise, all group elements would have a Legendre symbol equal to 1, which is incorrect.) So, (gz/p) = (−1)z. We deduce that a = 1(gz/p)=−1 = 1(−1)z=−1 = z mod 2. Similarly, we obtain that b = xy mod 2. Hence, the above attack answer 1 if and only if xy ≡ z (mod 2). If z = xy, then the output is 1 for sure. But if z is independent of x and y, then z = xy modulo 2 with probability 1
2. So, taking a decision by checking a = b gives Adv = 1
2, which is much more than deciding at random.

This result implies that the ElGamal cryptosystem is not IND-CPA secure,1 so unsafe to use in the group Z∗
p. This is why we rather take a subgroup of Z∗
p. But then we have to map messages into this subgroup in an injective and invertible way, and it is not always easy.

It is easy for the subgroup QRp of Z∗
p of quadratic residues modulo p, when p = 2q + 1 with p and q prime. In this case, we can see (with the Legendre symbol) that −1 is not a quadratic residue. Indeed, (−1)
p−1
2
= (−1)q = −1 since q is odd. So, for all x ∈ Z∗
p, either x or −x is in QRp but not both. So, we can define map(x) to be the unique element in {x, −x} ∩ QRp. This defines a bijective mapping from {1*, . . . , q*} to QRp. So, a message can be first converted into an integer between 1 and q, then into a QRp element. So, we can use the ElGamal cryptosystem on the QRp group in this case.

## 3.5 The Factoring Problem

Given a pseudorandom number generator, the *factoring problem* is specified by a generated integer n. It consists in finding prime factors of n. We define the factoring game relative to algorithm Gen as follows: Factoring(λ):
1: Gen(1λ) → n
▷ λ may represent the modulus bitlength
2: A(n) → (*p, q*)
3: **return** 1p×q=n ∧ p,q∈{2,...,n−1}
It is actually the problem to split n into non-trivial factor rather than the problem to find the full factorization. For RSA moduli, it is the same.

For instance, we can consider the pseudorandom generator generating RSA moduli n = pq.

We hope that this problem is hard. So far, the factoring record is obtained on the RSA768 number having 768 bits. We have RSA768 = 1230186684530117755130494958384962720772853569595334792197322452151726400507
2636575187452021997864693899564749427740638459251925573263034537315482685079 1702612214291346167042921431160222124047927473779408066535141959745985690214 3413
= 3347807169895689878604416984821269081770479498371376856891243138898288379387
8002287614711652531743087737814467999489
×
3674604366679959042824463379962795263227915816434308764267603228381573966651 1279233373417143396810270092798736308917
It was factored by the equivalent of 1500 years of computation on a core 2.2GHz Opteron in 2009.

It used NFS, the Number Field Sieve algorithm [56] working with complexity

$e^{\sqrt[3]{\frac{64}{9}+o(1)}(\ln n)^{\frac{1}{3}}(\ln\ln n)^{\frac{2}{3}}}$

... 
Another useful factoring algorithm is the Elliptic Curve Method (ECM) which can recover a prime factor p of n with complexity

$e^{\sqrt{2+o(1)}(\ln p)^{\frac{1}{2}}(\ln\ln p)^{\frac{1}{2}}}$

. 
which can be better than for NFS if p is small [54]. So, for RSA moduli in which there are two prime factors of equal size, the best algorithm is NFS. But ECM is better for very imbalanced moduli.

With quantum computers, we can factor in quasi-quadratic time using the Shor [78] algorithm.

Hence, factoring could become easy if quantum computers with enough memory are built.

Computing square roots relates to factoring as the following result shows.

Theorem 3.15. *We consider a pseudorandom generator* Gen to produce an RSA modulus n of size ℓ. We consider the two following problems:

- find the two factors p and q of n;
- given a random quadratic residue x ∈ Zn, finds a square root y of x.
Any algorithm solving one of the two problem can be transformed into an algorithm solving the other problem, with a complexity which is polynomially bounded in terms of ℓ. Proof (sketch). Clearly, being able to factor implies being able to compute square roots: we just have to compute square roots modulo each factor p and q of n using the Tonelli algorithm and to combine them with the Chinese Remainder Theorem. This solves the square root problem in Zn.

Conversely, if we can compute square roots, by computing the square root of x2 mod n, for some random x, it is likely to give a different square root than x or −x. If we have x2 ≡ y2 with x ̸= y and x ̸= −y, the result below yields a non-trivial factor of n, so p or q. Then, we can fully factor n.

⊓⊔
Lemma 3.16. For x, y ∈ Zn

$$\left.\begin{array}{rcl}x^{2}&\equiv&y^{2}\pmod{n}\\ x&\not\equiv&y\pmod{n}\\ x&\not\equiv&-y\pmod{n}\end{array}\right\}\Longrightarrow\gcd(x-y,n)\not\in\{1,n\}$$

Proof.: If we have $x^{2}\equiv y^{2}$ with $x\not\equiv y$ and $x\not=-y$, we obtain that $(x-y)(x+y)$ is a multiple of $n$ but that $n$ is not a factor of either $x-y$ or $x+y$. So, $\gcd(x-y,n)$ is a non-trivial factor of $n$. For $n=pq$, this is either $p$ or $q$.

There are other problems related to the factoring problem. For instance, if we know λ(n) or any multiple (such as φ(n)), we can factor n by writing λ(n) = 2st with t odd, computing the chain (bt mod *n, b*2t mod *n, . . . , b*2st mod n) for a random b. If the chain is of the form (1, 1*, . . . ,* 1)
or (∗, . . . , ∗, −1, 1*, . . . ,* 1), this is bad luck and we can try with another b. Otherwise, we obtain some z such that z ̸= 1, z ̸= −1, but z2 mod n = 1. So, gcd(z − 1, n) is a non-trivial factor of n.

To conclude, we list some computational problems related to Zn which are equivalent to factoring n:

- computing square roots in Zn;
- computing φ(n); - computing λ(n); - computing a multiple of λ(n).
We can deduce, for instance, that computing an RSA secret key (*d, n*) from the public key (*e, n*)
is as hard as factoring n since ed − 1 must be a multiple of λ(n). This means that the RSA key recovery problem is as hard as the factoring problem.

Regarding the RSA decryption problem, it can of course be solved if factoring is easy but the two problems are not known to be equivalent. It is believed to be hard, but maybe not equivalent.