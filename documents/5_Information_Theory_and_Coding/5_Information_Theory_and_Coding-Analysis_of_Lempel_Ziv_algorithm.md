# Lecture 10: Analysis Of Lempel-Ziv Algorithm

In this lecture, we will compute the average number of bits per letter the Lempel-Ziv algorithm produces and we will compare its efficiency to the one of finite state machines. In a second part, we will change the discussion topic and start to introduce the notion of data communication.

## 1 Analysis Of Lempel-Ziv 1.1 Expected Efficiency Of Lempel-Ziv

Suppose the sequence u1, u2*, . . .* is fed to Lempel-Ziv's procedure, we are interested in the question of how many bits are produced. Suppose for instance we read this sequence up to un. The Lempel-Ziv algorithm will create a representation of this sequence from w1 up to wm for some *m < n*. If we stop close to un, it is possible that the next w (that includes un) is smaller than the one we could have had by continuing to read the sequence from un+1. For example, if our input is aababcaab and we let n = 7, running LZ on u1 *. . . u*7 will create four w's that will respectively be equal to a, ab, *abc* and a. If we hadn't stopped at n = 7, given the elements in the current dictionary, we could have had a bigger w4, namely w4 = *aab*. The above essentially means that stopping at a given n does not necessarily give the correct code assignment. Note that the w_{1}*, . . . , w*{m−1} are guaranteed to be distinct. u^n is made of w_{1} *. . . w*_{m−1}, wm and note that if we group (w_{m−1}, w_{m})
we get a distinct parsing of u^n into m − 1 words. Together with ∅ concatenated to u^{n}, we get a parsing to m distinct words. Consequently, m ≤ m∗(u^{n}).

## 1.2 Expected Output Length

If we compute the length of a typical output of Lempel-Ziv, we get

$\#$ bits produced by $\text{LZ}=\lceil\log_{2}(1+|\mathcal{U}|)\rceil+\lceil\log_{2}(1+2|\mathcal{U}|)\rceil+\ldots+\lceil\log_{2}(1+m|\mathcal{U}|)\rceil$

$$\leq m\lceil\log_{2}(1+m|\mathcal{U}|)\rceil$$ $$\leq m^{*}(u^{n})\lceil\log_{2}(1+m^{*}(u^{n})|\mathcal{U}|)\rceil.$$
Note that 1 + m∗(un)|U|≤ 2m∗(un)|U| and ⌈log2 x⌉ < 1 + log2 x = log2(2x) so our new bound becomes

$\#$ bits produced by $\mathrm{LZ}\leq m^{*}(u^{n})\log_{2}(4|\mathcal{U}|m^{*}(u^{n}))$

$$=m^{*}(u^{n})\log_{2}m^{*}(u^{n})+m^{*}(u^{n})\log_{2}4|\mathcal{U}|.$$
We recall from last week the lower bound we gave on the number of bits produced by any IL machine with s states. Namely,

$\#$ bits produced by $s$-states IL machine $\geq m^{*}(u^{n})\log_{2}\frac{m^{*}(u^{n})}{8s^{2}}$

$$=m^{*}(u^{n})\log_{2}m^{*}(u^{n})-m^{*}(u^{n})\log_{2}8s^{2}.$$

Dividing by n on both sides give us the number of bits per letter produced, namely

$\frac{1}{n}\#$ bits produced by $s$-states IL machine $\geq\frac{1}{n}m^{*}(u^{n})\log_{2}m^{*}(u^{n})-\frac{1}{n}m^{*}(u^{n})\log_{2}8s^{2}$.

Notice how the two bounds we have stated are similar. In fact, by making n grow to +∞, the second term of both bounds disappears which, when taking their difference, gives us

$${\frac{1}{n}}\,(\mathrm{length~of~LZ-length~of~IL~machine})\leq{\frac{1}{n}}m^{*}(u^{n})\log_{2}32s^{2}|{\mathcal{U}}|,$$
which → 0 as n *→ ∞*. Thus, we conclude that as n gets large, Lempel-Ziv performs at least as well as any IL finite state machine, in terms of bits per letter. Note that this works for every sequence.

## 1.3 Overall Performance Of Lempel-Ziv

As a corollary of the above, note that if U1, U2*, . . .* is a stationary information source, Lempel-Ziv will compress it to its entropy rate H in expectation. To convice ourselves of this statement, we know that, if we know that statistics of the given distribution, we can design a Huffman code cn : Un → {0, 1}∗ s.t.

$$\frac{1}{n} E[length c_n(U^n)] ≤ \frac{1}{n} H(U^n) + \frac{1}{n} → H$$ as n gets large. By the prefixfree property, the Huffman code can, for any n, be implemented by an IL finite state machine. From there, we deduce that Lempel-Ziv cannot do worse than any other machine and hence must converge to H.