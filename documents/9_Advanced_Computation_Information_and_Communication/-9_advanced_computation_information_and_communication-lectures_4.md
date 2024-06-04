Logic circuits. Remember the cmos design principle introduce during the previous lecture, and the simple circuit to compute the negation $\neg A$ of input signal $A \in$ $\{0,1\}$.

The second cmos circuit that we considered is in Figure 4 on the next page (where we assume that both top wires labelled ' 1 ' are directly connected to the current (or, equivalently, the "voltage"), and that the single bottom wire labelled ' 0 ' is grounded). It was argued that on input two signals $A \in\{0,1\}$ and $B \in\{0,1\}$ the output wire $Y$ will contain the signal that corresponds to $\neg(A \wedge B)$.

In Figure 4 the curved red arrow shows what happens if both $A$ and $B$ are equal to 1, and the output signal $Y$ is (thus) equal to zero (and there is no connection between the " 1 " wires on top and $Y$ via either of the pmos transistors); for all other possible inputs (than $A=1$ and $B=1$ ) there will not be a connection between the "ground" ("0") wire at the bottom and $Y$, but there will be a connection between $Y$ and the " 1 " wire on top via either of the pmos transistors. Note the complementarity of the design, with two sequential (" $\wedge$ ") nmos gates in the lower part and two corresponding parallel (" $\vee$ ") pmos gates in the upper part of the circuit: complementarity then follows from the De Morgan laws.

If the " $\neg(A \wedge B)$ "-circuit in Figure 4 is followed by the negation circuit (applied to $Y$ ) from Figure 3 (by connecting the output signal $Y$ of Figure 4 to input signal $A$ of Figure 3), we get the ordinary conjunction $\wedge$, because $\neg \neg(A \wedge B)=A \wedge B$.

Arithmetic circuits. Given that we now know how to build logical operators using cmos circuits, how can we use them to build arithmetic circuits, for instance for addition or multiplication of integers? First of all, we must be able to represent integers using just the truth values 0 and 1 , which means that we have to understand how to represent integers as bitstrings (i.e., as sequences consisting of zeros and ones). You are supposed to be familiar with how to do this, but if it is new to you, read section 4.2 of the book. Below a brief summary of the main points:

Base $b$ representation: For any integer $b \geq 2$ any integer $n \in \mathbf{Z}_{>0}$ allows a unique base $b$ representation (or radix $b$ representation) using the string of digits $d_{k} d_{k-1} d_{k-2} \ldots d_{1} d_{0}$ for some integer $k \geq 0$ and with $0 \leq d_{i}<b$ for $0 \leq i \leq k$ and $d_{k} \neq 0$ such that

$$
\begin{aligned}
n & =d_{k} b^{k}+d_{k-1} b^{k-1}+d_{k-2} b^{k-2}+\ldots+d_{1} b^{1}+d_{0} b^{0} \\
& =d_{k} b^{k}+d_{k-1} b^{k-1}+d_{k-2} b^{k-2}+\ldots+d_{1} b+d_{0} \\
& =\sum_{i=0}^{k} d_{i} b^{i}
\end{aligned}
$$

Furthermore, $n=0$ is denoted, exceptionally, by the single digit $d_{0}$ with $d_{0}=0$ and $k=0$. Check that for $b=2,3,4,5,6,7,8,9,10,11,12$ and 13 the base $b$ representation of the (decimal) integer 13 is given by the digit-strings $1101,111,31,23,21,16,15,14,13,12,11$ and 10.

Binary representation: The binary representation of $n \in \mathbf{Z}_{\geq 0}$ is the base 2 representation (thus take $b=2$ above). Because $0 \leq d_{i}<2$, all digits are 0 or 1 ; such digits are referred to as "bits".

Conversion to binary representation: To find the binary representation of a nonnegative integer $\ell$, set $k=0$ and $d_{0}=0$ if $\ell=0$. Otherwise, if $\ell>0$, initialize $k$ as 0 , and successively perform the following three steps as long as $\ell>0$ :

(1) if $\ell$ is even then let $d_{k}=0$ else (if $\ell$ is odd) let $d_{k}=1$;

(2) replace $\ell$ by $\lfloor\ell / 2\rfloor$;

(3) if $\ell \neq 0$ replace $k$ by $k+1$.

For example, let $\ell=205$, then we start with $k=0$ and $d_{0}=1$, replace $\ell$ by 102 and $k$ by 1 , continue with $d_{1}=0$, replacing $\ell$ by 51 and $k$ by 2 , continue with $d_{2}=1$, replacing $\ell$ by 25 and $k$ by 3 , continue with $d_{3}=1$, replacing $\ell$ by 12 and $k$ by 4 , continue with $d_{4}=0$, replacing $\ell$ by 6 and $k$ by 5 , continue with $d_{5}=0$, replacing $\ell$ by 3 and $k$ by 6 , continue with $d_{6}=1$, replacing $\ell$ by 1 and $k$ by 7 , continue with $d_{7}=1$, replacing $\ell$ by 0 and terminate. We find the $7+1=8$-bit string 11001101 that is the binary representation of 205.

Conversion from binary representation: Given a bitstring $d_{k} d_{k-1} d_{k-2} \ldots d_{1} d_{0}$, let $\ell=d_{0}$ if $k=0$. Otherwise, if $k>0$, initialize $\ell$ as 1 and for $i=k-1, k-2, \ldots, 1,0$ in succession replace $\ell$ by $2 \ell+d_{i}$. Examples were done in class and there is another example below. Correctness again follows from the definition of the base 2 representation.

Checking using complementarity: If $\ell$ has a $k+1$-bit binary representation $d_{k} d_{k-1} d_{k-2} \ldots d_{1} d_{0}$, then the complementary bitstring $\bar{d}_{k} \bar{d}_{k-1} \bar{d}_{k-2} \ldots \bar{d}_{1} \bar{d}_{0}$ is the representation of $2^{k+1}-1-\ell$ (where $\bar{d}_{i}=1-d_{i}$ is the bit that is complementary to $d_{i}$ ): this follows from the fact that the sum of the $k+1-$ bit strings $d_{k} d_{k-1} d_{k-2} \ldots d_{1} d_{0}$ and $\bar{d}_{k} \bar{d}_{k-1} \bar{d}_{k-2} \ldots \bar{d}_{1} \bar{d}_{0}$ is the bitstring that consists of $k+1$ ones, which corresponds to the value $2^{k+1}-1$. This bitstring is referred to as the ones' complement of $\ell$. Note that at least one of these bitstrings has at least one leading zero bit.

So, after computing the $k+1$-bit representation of $\ell$, the correctness of this bit representation may be verified by complementing the bitstring (leading to the ones' complement), converting the ones' complement back to decimal, and checking that the result $r$ satisfies $\ell+r=2^{k+1}-1$ : for $\ell=23$ one finds the 5 -bit string 10111 , the ones' complement 1000 of which is the binary representation of 8 and indeed $23+8=31=2^{5}-1$.

As another example, we can check the correctness of the 8 -bit binary representation 11001101 of 205 that was found above. First find the ones' complement of 11001101 which is (trivially) 110010, then convert this to decimal: start with $k=5$ and $r=1$, then for $i=4$ we get $r=2 * 1+1=3$ because $d_{4}=1$, for $i=3$ we get $r=2 * 3=6$ because $d_{3}=0$, for $i=2$ we get $r=2 * 6=12$ because $d_{2}=0$, for $i=1$ we get $r=2 * 12+1=25$ because $d_{1}=1$, and finally for $i=0$ we get $r=2 * 25=50$ because $d_{5}=0$. We find that $\ell+r=205+50=255=2^{8}-1$, so the result indeed checks out (unless we have made two complementary errors that cancel each others' wrong effects).

We could also regard 11001101 as a 10 -bit string 0011001101 , take its ones' complement 1100110010, compute the latter's decimal equivalent $r=$ $50+512+256=818$ (here we just take the 50 as seen before from the trailing bits 110010 and recognize that the two leading bits represent $2^{9}=512$ and $2^{8}=256$, whereas the bits for $2^{7}$ and $2^{6}$ are zero (or "off")), after which the correctness follows from $\ell+r=205+818=1023=2^{10}-1$.

Conversions for arbitrary base: The above "to" and "from" conversions (and the verification method) easily generalize to arbitrary bases.

Binary addition. Assume we want to use a circuit to add two integers $m$ and $n$. Assume that both $m$ and $n$ can be represented (unlike above) using just $k$ bits, so let

$$
m_{k-1} m_{k-2} \ldots m_{2} m_{1} m_{0}
$$

and

$$
n_{k-1} n_{k-2} \ldots n_{2} n_{1} n_{0}
$$

be the $k$-bit strings representing $m$ and $n$ (where the $m_{i}$ and the $n_{i}$ are all bits, i.e., 0 or 1). When doing an example addition in binary notation, you quickly notice that, after the "first" (rightmost) bit-addition (where bit $m_{0}$ is added to bit $n_{0}$ ), you have to take into account not just the two bits that are next to be added (namely $m_{1}$ and $n_{1}$ ), but that you may also have to deal with a carry that may have been generated by the addition of the bits $m_{0}$ and $n_{0}$. And when adding $m_{2}$ and $n_{2}$ you may have to deal with a carry that may have been generated by the addition of $m_{1}$ and $n_{1}$ (and the then relevant carry), and so on until the addition of $m_{k-1}$ and $n_{k-1}$ - which may also generate a carry and if so an overall $k+1$-bit string outcome of the addition (as opposed to the inputs that are just $k$-bit strings). Just try a few examples, and convince yourself that carries are unavoidable - as you already know since elementary school when adding numbers in their decimal representation - and that "overflow" also easily occurs (namely, if $m+n \geq 2^{k}$ ).

Thus a circuit to add two bits is useless: we need a circuit that can add three bits: a bit $m_{i}$ from the first of the terms to be added, the corresponding bit $n_{i}$ from
the second number to be added, and a carry-in bit that is the carry-out bit from the previous bit-addition (if there is a previous addition, i.e., if $i>0$ ). Furthermore, as if this is not enough trouble yet, the output of this "bit-adder" must consist of two bits: the sum-bit and the carry-out bit (the latter to be used in the next round or, if $i=k-1$, produced as overflow bit). Denoting bits $m_{i}$ and $n_{i}$ as $a$ and $b$, respectively, adding bits $a, b$ and the carry-in bit $c_{\text {in }}$ must produce a sum bit $s$ and a carry-out bit $c_{\text {out }}$. Below the table of all possibilities that may occur (note that there are $8=2^{3}$ distinct possibilities):

| $a$ | $b$ | $c_{\text {in }}$ | $c_{\text {out }}$ | $s$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

Here the first three columns just give all possible combinations of the three input bits $a, b, c_{\text {in }}$, and the final two columns represent the two bits of the sum $a+b+c_{\mathrm{in}}$ : thus $a+b+c_{\text {in }}=2 c_{\text {out }}+s$ (as values) and $a+b+c_{\text {in }}$ is represented by the 2 -bit string $c_{\text {out }} s$. To be able to figure out what circuit to build, we have to find the logical functions of $a, b$ and $c_{\text {in }}$ that correspond to the two bit-values $s$ and $c_{\text {out }}$.

We managed to figure out that $s=1$ if and only if the parity of $a+b+c_{\text {in }}$ is odd, and that this parity can be calculated as the exclusive or of $a, b$ and $c_{\mathrm{in}}$. Therefore $s=a \oplus b \oplus c_{\text {in }}$ (this can be parenthesized, if desired, as $s=(a \oplus b) \oplus c_{\text {in }}$ or $s=a \oplus\left(b \oplus c_{\text {in }}\right)$, but parentheses are not required for this expression). We also figured out that $c_{\text {out }}=1$ if and only if at least two of $a, b$ and $c_{\text {in }}$ are 1 . Therefore $c_{\text {out }}=(a \wedge b) \vee\left(a \wedge c_{\text {in }}\right) \vee\left(b \wedge c_{\text {in }}\right)$ (here parentheses, as given, are required!). It now follows that to add numbers in binary it suffices to be able to perform the standard logical operations, which we already know how to do.

Efficiency considerations. When adding $m$ and $n$ as above, we can do so in $k$ sequential steps (by $k$ times using a single bit-adder that takes the two bits and the carry into account). This process requires time linear in $k$ and thus becomes slow when $k$ is large. Can we do better?

One may contemplate the possibility to use a table where the $n$-th item in the $m$-th row contains the value $m+n$ : addition then becomes equivalent to table look-up. Given that the table would have to be enormous this is not an option: just for the limited range of $m$ and $n$ values with $0 \leq m, n<10^{9}$ on the order of $10^{9} \times 10^{9}=10^{18}$ values between 0 and $2 \times\left(10^{9}-1\right)$ would have to be stored; too many values, and it would not even solve the problem in general, i.e., for $m$ or $n$ larger than or equal to $10^{9}$. This argument does not imply that table look-up is always a bad idea: there are plenty of computational methods where it makes perfect sense to memorize all kinds of results in a table, and where efficient performance relies on this kind of memo(r)ization: doing so is called dynamic programming, a common sense technique that may be further discussed later in the course.

We could also try to use $k$ distinct bit-adders and use them all simultaneously: unfortunately the bit-adders to the left (for the more significant bits) must wait for the bit-adders to the right (for the less significant bits) to finish to properly take into account their carries. The example $m=2^{k}-1, n=1$ shows that a single carry may have to propagate from the far right to the far left ${ }^{1}$. This gives rise to a delay[^0]that is linear in $k$, which is as "bad" as the sequential approach that we used before: even though we use $k$ times more hardware compared to the sequential approach, this simpleminded parallellization does not lead to a speed-up.

Further remarks on basic arithmetic functions. A more sophisticated approach to binary addition leads to a delay of about $\log _{2} k$ "steps", which is just logarithmic in $k$. This implies that moving from 32 -bit addition to 64 -bit addition does not slow addition down by a factor $2=\frac{64}{32}$ but requires $6\left(=\log _{2} 64\right)$ instead of $5\left(=\log _{2} 32\right)$ of those "steps". This approach is sketched with a few examples at the end of these notes, after a few other pitfalls and nasty "tricks" that were quickly presented during the lecture:

Addition modulo $2^{k}$ : Currently, actual hardware is restricted to fixed lengths such as (until a few years ago) $k=32$ or (now) $k=64$; here we assume that $k=64$. This implies that unless precautions are taken (using special purpose programming) nonnegative integers are limited to the range from 0 up to $2^{64}-1$ (the largest 64 -bit integer); this equals $2^{4} 2^{10 * 6}-1$ which is $\left(\right.$ with $\left.2^{10}=1024 \approx 1000\right)$ somewhat larger than $2^{4} 1000^{6}=1.6 * 10^{19}$. Note that with these hard-wired 64 bits all integers are represented using 64 bits, even if they would in principle require far fewer bits: zero is represented by a sequence of 64 zero bits, one is represented by $\underbrace{000 \ldots 0}_{63 \text { zeros }} 1,2^{10}$ by $\underbrace{000 \ldots 0}_{53 \text { zeros }} 1 \underbrace{000 \ldots 0}_{10 \text { zeros }}$, etc.

Addition is also limited to 64 -bit numbers and the result of any addition is chopped off at 64 bits: in the notation used above, the carry bit that may be generated by the addition of the bits $m_{63}$ and $n_{63}$ (along with the carry that must be taken into account in that addition) is simply - and silently - ignored. As a result addition is only correct "modulo $2^{64 "}$ ". If there indeed is a nonzero final carry (which is by necessity ignored), we say that "overflow occurs". Checking for overflow is easy: if the result of an addition of two positive integers turns out to be less than (either) one of the two integers to be added, then overflow occurred.

Using all available 64 bits to represent nonnegative integers corresponds to what is called unsigned integer arithmetic.

For example, in unsigned 5-bit arithmetic (thus with unsigned integers in the range $[0,31]$ ) the sum of 18 (10010 in binary) and 17 (10001 in binary) would be 3 because even though regular binary addition $10010+10001=$ 100011 produces the right result 35 (with binary representation 100011), 35 is outside the range of numbers that can be represented in unsigned 5-bit arithmetic, and anything beyond (i.e., to the left of) the fifth bit position is simply chopped off, thus leading to the 5 -bit result 00011 with decimal value 3. Note, however, that the result 3 is "correct modulo 25 ": $3+32=35$.

Representing negative numbers: Obviously, it would be convenient to be able to work with negative numbers as well. This complicates matters a bit: we have no choice but to stick to the 64 bits that are available per integer, making it unavoidable to reserve one of the bits for the sign. Also, we need to figure out how to do subtraction, i.e., addition of a positive integer to a negative integer. As you may remember from elementary school this leads to all kinds of unpleasant complications with "borrows", and subtraction indeed becomes troublesome if we simply reserve the leftmost bits for the sign (say $\underbrace{000 \ldots 0}_{63 \text { zeros }} 1$ represents 1 , and $1 \underbrace{000 \ldots 0}_{62 \text { zeros }} 1$ represents -1 ). It is also
inelegant (because both $\underbrace{000 \ldots 0}_{64 \text { zeros }}$ and $1 \underbrace{000 \ldots 0}_{63 \text { zeros }}$ would represent zero, where the latter would actually be -0 ): having a non-unique representation for one of the values is ugly and inconvenient.

Two's complement representation and subtraction: If we use a smarter representation for negative numbers, namely as the two's complement representation of the corresponding positive number, then all subtraction troubles disappear - along with the ugly -0 . This is based on our earlier observation that we are doing arithmetic modulo $2^{64}$ anyhow, and our earlier complementarity-based checking method: there we saw that $23+8=2^{5}-1$, so that $23+9=2^{5}$ where, if we would be using 5 -bit hardware (and thus work modulo $2^{5}$ ), the $2^{5}$ would "disappear". As a result we get (on our imaginary 5 -bit hardware) $23=-9$ and thus that the negative number -9 is represented as 23 . In case you are wondering what now happens to 23 itself, note that on 5-bit hardware we can only use 4 bits for the integer value if we allow signs, thus the largest integer is $2^{4}-1=15$ which is smaller than 23: so, 23 is "out of range" anyhow, when signs are used, so nothing is lost. Check out the picture on the next page ("Sam's diagram" from tp://www.willamette.edu/ ^ fruehr/353/), where all values are depicted (along with their binary representations) when the two's complement 5 -bit representation is used; note that zero is uniquely represented as a bitstring of five zeros, that there is no -0 and that the range of the negative numbers is one larger than the range of the positive numbers: negatives range from -16 to -1 , but nonnegatives range from 0 to only 15 .

More in general, on 64 -bit (or, in general, $k$-bit) hardware, for any positive number $\ell$ in the range $\left[1,2^{63}-1\right]$ (or $\left[1,2^{k-1}-1\right]$ ) the value $-\ell$ is represented as $2^{64}-\ell$ (or $2^{k}-\ell$ ). It remains to consider how to compute $2^{64}-\ell$ (or $2^{k}-\ell$ ) given $\ell$ : this is done by first complementing the 64 -bit (or $k$-bit) binary representation of $\ell$ (i.e., flipping all its 64 (or $k$ ) bits), resulting in the ones' complement $2^{64}-1-\ell$ (or $2^{k}-1-\ell$ ) already seen above, after which one is added resulting in the two's complement representation of $-\ell$. The resulting values (nonnegatives in $\left[0,2^{63}-1\right]$ (or $\left[0,2^{k-1}-1\right]$ ) and negatives in $\left[-2^{63},-1\right]$ (or $\left[-2^{k-1},-1\right]$ ) in their two's complement representation) can now be operated on using the regular addition circuit: even if the results get out of range, they are still always correct modulo $2^{64}$ (or $2^{k}$ ).

To check that we only have a single zero, let $\ell=0$ be represented as $k$ zero bits, then the ones' complement is $k$ one bits (thus $2^{k}-1$ ), adding one results in $2^{k}-1+1=2^{k}$ - but $2^{k}$ disappears when using $k$ bits (i.e., everything in "modulo $2^{k "}$ "). It follows that the representation of $-\ell$ consists of $k$ zero bits, so that no distinction is made between 0 and -0 .

As a further example, to compute $5-10$ on 5 -bit hardware, we first compute the representation of -10 by taking the two's complement representation of 10 : flip the bits of the 5-bit string 01010 (the binary representation of the decimal value 10) to get the ones' complement 10101 and then add one, resulting in the 5 -bit string 10110 which represents the decimal value -10 . Because 5 is represented by the 5 -bit string 00101 , we calculate $5-10$ by adding the 5 -bit strings 00101 and 10110 resulting in 11011 which (cf. picture) indeed represents $-5=5-10$ : though 11011 represents 27 in binary, we get $32-x=27$ for $x=5$ so indeed 11011 represents -5 .

If, using the same 5 -bit arithmetic, we add 9 to 12, i.e., bitstring 01001 to bitstring 01100 , we get the bitstring 10101 which represents the negative integer -11 : incorrect as positive sum of 9 and 12 but correct modulo $2^{5}=32$ because $-11+32=21=9+12$.

Multiplication: Regular "schoolbook" multiplication works digit-by-digit, requiring a number of digit-by-digit multiplications that equals the product of the numbers of digits of the numbers to be multiplied: for $k$-bit strings this amounts to an amount of work that is proportional to $k^{2}$. When fast addition is used, it costs about $k$ additions of about $k$-bit numbers, which is better but still substantial.

Faster multiplication: Note that the product of the polynomials $v=a X+b$ and $w=c X+d$ equals $v w=a c X^{2}+(a d+b c) X+b d$. The coefficients of this product polynomial can be computed using four multiplications (to compute $a c, a d, b c$, and $b d$ ) followed by an addition (to compute $a d+b c$ ), but it can also be computed in just three multiplications (plus four additions): compute $a c, b d$ and $(a-b)(c-d)$, after which $a d+b c$ follows as $a c+b d-$ $(a-b)(c-d)$. If multiplications are more costly than additions (which is normally the case), then this trick, known as Karatsuba multiplication, is advantageous.

Note that it can be used to calculate a 2-digit by 2-digit multiplication using not 4 but just 3 digit-by-digit multiplications (and some additions), by using the above trick with $X=10$ (when using decimal numbers where multiplication by powers of 10 comes for free), thus to compute a 4-digit by 4-digit multiplication using just 9 digit-by-digit multiplications (instead of 16; use the trick with $X=100$ for 4 digits, and with $X=10$ for 2 digits), thus to compute an 8-digit by 8-digit multiplication using just 27 digit-bydigit multiplications (as opposed to $64 ; X=10000$ )), etc. and ultimately to compute a $k$-digit by $k$-digit multiplication using just $k^{\log _{2} 3}<k^{1.585}$ digit-by-digit multiplications (instead of $k^{2}$ ). We will see later where the
$\log _{2} 3$ comes from (it helps if you realize that $k^{\log _{2} 3}=3^{\log _{2} k}$, cf. Exercise 2 in week 1). Obviously, when the binary representation is used, we would not use powers of 10 for $X$, but powers of 2 (because multiplying by a power of two is just a shift to the left (adding zeros to the right), similar to the "easy" multiplication by a power of ten in decimal notation).

Karatsuba example. Let $v=1298$ and $w=4687$ in decimal. We compute $v w=6083726$ using Karatsuba's method. Take $X=100$ and $a=12, b=98, c=46$, and $d=87$. Compute the following doubleunderlined two-digit-by-two-digit products (below it is shown how): $a c=$ $\underline{\underline{12 \times 46}}=552, b d=\underline{\underline{98 \times 87}}=8526$, and

$a d+b c=a c+b d-(a-b)(c-d)=552+8526-\underline{\underline{(-86) \times(-41)}}=9078-3526=5552$.

Then $v w=a c X^{2}+(a d+b c) X+b d=5520000+555200+8526=6083726$.

Computation of $(v=12) \times(w=46)$ : Take $X=10$ and $a=1, b=2$, $c=4$, and $d=6$. Compute $a c=\underline{1 \times 4}=4, b d=\underline{2 \times 6}=12$, and

$a d+b c=a c+b d-(a-b)(c-d)=4+12-\underline{(-1) \times(-2)}=16-2=14$.

Then $v w=a c X^{2}+(a d+b c) X+b d=400+140+12=552$.

We have done three digit-by-digit multiplications (single-underlined above).

Computation of $(v=98) \times(w=87)$ : Take $X=10$ and $a=9, b=8$, $c=8$, and $d=7$. Compute $a c=\underline{9 \times 8}=72, b d=\underline{8 \times 7}=56$, and

$a d+b c=a c+b d-(a-b)(c-d)=72+56-\underline{(1) \times(1)}=128-1=127$.

Then $v w=a c X^{2}+(a d+b c) X+b d=7200+1270+56=8526$.

So far we have done three plus three equals six digit-by-digit multiplications (the single-underlined multiplications above).

Computation of $(v=86) \times(w=41)$ : Take $X=10$ and $a=8, b=6$, $c=4$, and $d=1$. Compute $a c=\underline{8 \times 4}=32, b d=\underline{6 \times 1}=6$, and

$a d+b c=a c+b d-(a-b)(c-d)=32+6-\underline{(2) \times(3)}=38-6=32$.

Then $v w=a c X^{2}+(a d+b c) X+b d=3200+320+6=3526$.

Overall we have done six plus three equals nine digit-by-digit multiplications (all single-underlined above), as opposed to the sixteen we would have done using "schoolbook" multiplication. In practice the method turns out to be faster than "schoolbook" even for moderately sized numbers (despite the larger number of additions that are required, and that are disregarded in the argument presented above). Admittedly, the administrative details are a bit too contrived to make this method suitable for schoolkids.

Open problem: the true "complexity" of multiplication: Karatsuba is not the end of the integer multiplication story: for truly large numbers even faster methods are used. Strangely, at this point in time no one knows yet how this story ends! It is known that there are much faster multiplication methods (that become practical when $k$ gets really big). For instance, the Schönhage-Strassen multiplication method requires effort on the order of $k \log (k) \log (\log (k))$, which is much "better" than Karatsuba's $k^{\log _{2}(3)}$. Even faster methods are known, with the most recently invented improvement (due to the Swiss computer scientist Martin Fürer) dating back to 2007. It is still not known if it is possible - or not - to multiply two $k$-bit numbers in time that is only linear in $k$, i.e., to do it about as fast as addition. Same for matrix multiplication: we do not know how fast we may be able to do it.

Side-remark on representing information: There is no universal way to represent information: it all depends on conventions, and makes use of context, consistency, and (often) redundancy. Our conventional ways to denote numbers is not redundant, and the ordering of the digits is relevant (but just a convention): "12345" has a different "natural interpretation" than "14325" or "13425". However hardly any French speaking person (who can read) will find it difficult to decypher "dcffiile à dceéffhirr": errcie qleuuqe coshe en fnaçiars would be made considerably less complicated if people realize that to understand a piece of text it suffices to have the correct first and the correct last character of each word in place, while the other characters may appear in any garbled order. Tihs alipeps to oehtr lgaueagns too. Unlike numbers, text contains a lot of redundancy.

Example of addition faster than linear in $k$ : The first example uses decimal numbers; for binary representations it works in the same way (see further below). Let $m=62055303843399410504896107228145$ and $n=$ 45028995932035150397709975774678 be randomly selected 32-digit numbers. We want to compute their sum 107084299775434560902606083002823 exploiting parallelism.

First we write both $m$ and $n$ as sixteen 2 -digit values (32 1-digit values would work too, of course, but would require more typing):

$\begin{array}{llllllllllllllll}62 & 05 & 53 & 03 & 84 & 33 & 99 & 41 & 05 & 04 & 89 & 61 & 07 & 22 & 81 & 45\end{array}$

$\begin{array}{llllllllllllllll}45 & 02 & 89 & 95 & 93 & 20 & 35 & 15 & 03 & 97 & 70 & 99 & 75 & 77 & 46 & 78\end{array}$

Using 16 parallel 2-digit plus 2-digit adders, we compute the 16 corresponding sums, along with the first 15 of these sums plus one: this makes it possible to offer the choice between the sum with or without a nonzero carry added to it, and thus does not include the rightmost sum to which no nonzero carry will have to be added. For convenience a second sum is added in the final column too, but it does not offer a choice; the red part of it indicates the finished part of the computation:

![](https://cdn.mathpix.com/cropped/2024_05_17_4543dbc4ef1bd985d26bg-11.jpg?height=43&width=968&top_left_y=1663&top_left_x=550)

![](https://cdn.mathpix.com/cropped/2024_05_17_4543dbc4ef1bd985d26bg-11.jpg?height=43&width=985&top_left_y=1715&top_left_x=541)

A sum value in the top row will be used if there is no nonzero carry coming in from the right, and a sum value plus one (in the bottom row) will be used if there is a nonzero carry coming in from the right. Any number larger than 99 starts with a one, which is the nonzero carry that may have to be propagated to the left: once propagated, this one that indicates the nonzero carry is removed.

The computational part is now done, we only need to do some administration to make sure that all carries are propagated in the correct way. This goes as follows: for the second, fourth, sixth, eighth, tenth, twelfth, fourteenth, and sixteenth of the above stacks of two values of $\ell=2$ or $u=3$ digits do the following (which can be done in parallel for all eight stacks):

- if they both have $u$ digits (and thus both start with a one) then remove those leading digits one (twice) and replace the top value of the stack of two values before it by the bottom value while keeping the bottom value unchanged (both having $u$ digits means both start with a one, indicating that a nonzero carry must be propagated),
- if they both have $\ell$ digits then replace the bottom value of the stack of two values before it by the top value while keeping the top value unchanged (both having $\ell$ digits indicates that no nonzero carry has to be propagated),


[^0]:    ${ }^{1}$ We are familiar with his effect in decimal, when we add 1 to 999999999 to get 1000000000.

