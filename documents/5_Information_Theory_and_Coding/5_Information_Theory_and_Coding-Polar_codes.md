
## Lecture 24: Polar Codes (1)

In this lecture, we investigate polar codes.

These are more recent codes that turn out to be capacity achieving for binary communication channels. The advantages of polar codes is that their encoding and decoding complexities are both of order O(n log n) (compared to O(n2) for linear codes). However, it turns out that the error probability converges more slowly to 0, something of the order of O(2^{−√n}). We start by describing the general idea of a polar code, introducing the polar transformation and detail both the encoding and decoding processes.

## 1 General Polar Coding Idea

The basic idea is the following: we wish to try and convert a given channel into what we qualify as an "easy" case. An "easy" case involves considering either a channel that gives us a distinct output regardless of the input (i.e. no two inputs lead to the same output) or a channel on which the input does not influence the output (i.e. a channel that looses everything). We can represent this idea using the following scheme:
In the above, we want Ui → Vi to be "easy" and |{i : Ui → Vi good} ≈ nC(W). Our goal will be to design systems to fit the red questions marks in the above scheme.

## 2 Polar Transform

We define the simple polar transformation for two inputs as follows:
In the above, X1 = U1 ⊕ U2 and X2 = U2 so that U2 = X2 and U1 = X1 ⊕ X2. These W's are called the "real" channels. From there, we create two synthetic channels W^− : U1 → Y1Y2 and W^+ : U2 → Y1Y2U1. Let I(W) be the mutual information between the input and output of W
when the input is uniformly distributed on F2. Note that (U1, U2) ↔ (X1, X2) one-to one implies that if (U1, U2) is uniform on F_2^2 (i.e. U1 and U2 are iid equally probable) then (X1, X2) is also uniform on F_2^2 (i.e. X1 and X2 are iid equally probable). Suppose U1 and U2 are uniform. Then

$2I(W)=I(X_{1};Y_{1})+I(X_{2};Y_{2})$

$=I(X_{1}X_{2};Y_{1}Y_{2})$

$=I(U_{1}U_{2};Y_{1}Y_{2})$ since there is a one-to-one relationship

$=I(U_{1};Y_{1}Y_{2})+I(U_{2};Y_{1}Y_{2}|U_{1})$

$=I(U_{1};Y_{1}Y_{2})+I(U_{2};Y_{1}Y_{2}|U_{1})+I(U_{2};U_{1})$

$=I(W^{-})+I(W^{+})$,

so that polar transforms preserve mutual information. We get that I(W^−) ≤ I(W) ≤ I(W^+).

When moving to the next step, we obtain figure (3). The idea is to copy the preceding step and perform the same operation recursively. Here, since we perform t operations that take approximately n/2 time, the encoding phase takes O(n/2 log n) time. Note that

$$W^{-}(y_{1},y_{2}|u_{1})=\frac{1}{2}W(y_{1}|u_{1})W(y_{2}|0)+\frac{1}{2}W(y_{1}|u_{1}\oplus1)W(y_{2}|1).$$
So, if we are given (W(y1|0), W(y1|1)) and (W(y2|0), W(y2|1)), we can compute

$$(W^{-}(y_{1},y_{2}|0),W^{-}(y_{1},y_{2}|1))$$
using the above formula. We thus encode by doing approximately 10 arithmetic operations. Similarly, for the decoding process, we have

$$W^{+}(y_{1},y_{2},u_{1}|u_{2})=\frac{1}{2}W(y_{1}|u_{1}\oplus u_{2})W(y_{2}|u_{2}).$$
So again given (W(y1|0), W(y1|1)) and (W(y2|0), W(y2|1)), we can compute
(W +(y1, y2, u1|0), W +(y1, y2, u1|1))
using at most 10 arithmetic operations.
