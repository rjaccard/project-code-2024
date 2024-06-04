# 6. Optimal atomic bit construction 

### 6.1. Introduction

In the previous chapter, we introduced the notions of safe, regular and atomic (linearizable) read/write objects (also called registers). In the case of $1 \mathrm{~W} 1 \mathrm{R}$ (one writer one reader) register, assuming that there is no concurrency between the reader and the writer, the notions of safety, regularity and atomicity are equivalent. This is no longer true in the presence of concurrency. Several bounded constructions have been described for concurrent executions. Each construction implements a stronger register from a collection of weaker base registers. We have seen the following constructions:

- From a safe bit to a regular bit. This construction improves on the quality of the base object with respect to concurrency. Contrarily to the base safe bit, a read operation on the constructed regular bit never returns an arbitrary value in presence of concurrent write operations.
- From a bounded number of safe (resp., regular or atomic) bits to a safe (resp., regular or atomic) $b$-valued register. These constructions improve on the quality of each base object as measured by the number of values it can store. They show that "small" base objects can be composed to provide "bigger" objects that have the same behavior in the presence of concurrency.

To get a global picture, we miss one bounded construction that improves on the quality in the presence of concurrency, namely, a construction of an atomic bit from regular bits. This construction is fundamental, as an atomic bit is the simplest nontrivial object that can be defined in terms of sequential executions. Even if an execution on an atomic bit contains concurrent accesses, the execution still appears as its sequential linearization.

In this chapter, we first show that to construct a $1 \mathrm{~W} 1 \mathrm{R}$ atomic bit, we need at least three safe bits, two written by the writer and one written by the reader. Then we present an optimal three-bit construction of an atomic bit.

### 6.2. Lower bound

In Section 5.1, we presented the construction of a 1W1R atomic register from an unbounded regular register. The base regular register had to be unbounded because the construction was using sequence numbers, and the value of the base register was a pair made up of the data value of the register and the corresponding sequence number. The use of sequence numbers makes sure that new-old inversions of read operations never happen.

A fundamental question is the following: Can we build a 1W1R atomic register from a finite number of regular registers that can store only finitely many values, and can be written only by the writer (of the atomic register)?

This section first shows that such a construction is impossible, i.e., the reader must also be able to write. In other words, such a construction must involve two-way communication between the reader and the writer. Moreover, even if we only want to implement one atomic bit, the writer must be able to write in two regular base bits.

### 6.2.1. Digests and sequences of writes

Let $A$ be any finite sequence of values in a given set. A digest of $A$ is a shorter sequence $B$ that "mimics" $A$ : $A$ and $B$ have the same first and last elements; an element appears at most once in $B$; and two consecutive elements of $B$ are also consecutive in $A$. $B$ is called a digest of $A$.

As an example let $A=v_{1}, v_{2}, v_{1}, v_{3}, v_{4}, v_{2}, v_{4}, v_{5}$. The sequence $B=v_{1}, v_{3}, v_{4}, v_{5}$ is a digest of $A$. (there can be multiple digests of a sequence).

Every finite sequence has a digest:

Lemma 3 Let $A=a_{1}, a_{2}, \ldots, a_{n}$ be a finite sequence of values. For any such sequence there exists $a$ sequence $B=b_{1}, \ldots, b_{m}$ of values such that:

- $b_{1}=a_{1} \wedge b_{m}=a_{n}$,
- $\left(b_{i}=b_{j}\right) \Rightarrow(i=j)$,
- $\forall j: 1 \leq j<m: \exists i: 1 \leq i<n: b_{j}=a_{i} \wedge b_{j+1}=a_{i+1}$.

Proof The proof is a trivial induction on $n$. If $n=1$, we have $B=a_{1}$. If $n>1$, let $B=b_{1}, \ldots, b_{m}$ be a digest of $A=a_{1}, a_{2}, \ldots, a_{n}$. A digest of $a_{1}, a_{2}, \ldots, a_{n}, a_{n+1}$ can be constructed as follows:

- If $\forall j \in\{1, \ldots, m\}: b_{j} \neq a_{n+1}$, then $B=b_{1}, \ldots, b_{m}, a_{n+1}$ is a digest of $a_{1}, a_{2}, \ldots, a_{n}$.
- If $\exists j \in\{1, \ldots, m\}: b_{j}=a_{n+1}$, there is a single $j$ such that $b_{j}=a_{n+1}$ (this is because any value appears at most once in $B=b_{1}, \ldots, b_{m}$ ). It is easy to check that $B=b_{1}, \ldots, b_{j}$ is a digest of $a_{1}, \ldots, a_{n}, a_{n+1} . \quad \square_{\text {Lemma } 3}$

Consider now an implementation of a bounded atomic 1W1R register $R$ from a collection of base bounded 1W1R regular registers. Clearly, any execution of a write operation $w$ that changes the value of the implemented register must consist of a sequence of writes on base registers. Such a sequence of writes triggers a sequence of state changes of the base registers, from the state before $w$ to the state after $w$.

Assuming that $R$ is initialized to 0 , let us consider an execution $E$ where the writer indefinitely alternates $R$.write $(1)$ and $R$.write $(0)$. Let $w_{i}, i \geq 1$, denotes the $i$-th $R$.write $(v)$ operation. This means that $v=1$ when $i$ is odd and $v=0$ when $i$ is even. Each prefix of $E$, denoted by $E^{\prime}$, unambiguously determines the resulting state of each base object $X$, i.e., the value that the reader would obtain if it read $X$ right after $E^{\prime}$, assuming no concurrent writes. Indeed, since the resulting execution is sequential, there exists exactly one reading function and we can reason about the state of each object at any point in the execution.

Each write operation $w_{2 i+1}=$ R.write $(1), i=0,1, \ldots$, contains a sequence of writes on the base registers. Let $\omega_{1}, \ldots, \omega_{x}$ be the sequence of base writes generated by $w_{2 i+1}$. Let $A_{i}$ be the corresponding sequence of base-registers states defined as follows: its first element $a_{0}$ is the state of the base registers before $\omega_{1}$, its second element $a_{2}$ is the state of the base registers just after $\omega_{1}$ and before $\omega_{2}$, etc.; its last element $a_{x}$ is the state of the base registers after $\omega_{x}$.

Let $B_{i}$ be a digest derived from $A_{i}$ (by Lemma 3 such a digest sequence exists).

Lemma 4 There exists a digest $B=b_{0}, \ldots, b_{y}(y \geq 1)$ that appears infinitely often in $B_{1}, B_{2}, \ldots$

Proof First we observe that every digest $B_{i}(i=1,2, \ldots)$ must consists of at least two elements. Indeed if $B_{i}$ is a singleton $b_{0}$, then the read operation on $R$ applied just before $w_{i}$ and the read operation on $R$ applied just after $w_{i}$ observe the same state of base registers $b_{0}$. Therefore, the reader cannot decide when exactly the read operation was applied and must return the same value-a contradiction with the assumption that $w_{i}$ changes the value of $R$.

Since the base registers are bounded, there are finitely many different states of the base registers that can be written by the writer. Since a digest is a sequence of states of the registers written by the writer in which every state appears at most once, we conclude that there can only be finitely many digests. Thus, in the infinite sequence of digests, $B_{1}, B_{2}, \ldots$, some digest $B$ (of two or more elements) must appear infinitely often.

Note that there is no constraint on the number of internal states of the writer. Since there may be no bound on the number of steps taken within a write operation, all the sequences $A_{i}$ can be different, and the writer may never perform the same sequence of base-register operations twice. But the evolution of the base-register states in the course of $A_{i}$ can be reduced to its digest $B_{i}$.

### 6.2.2. Impossibility result and lower bound

Theorem 14 It is not possible to build a 1W1R atomic bit from a finite number of regular registers that can take a finite number of values and are written only by the writer.

Proof By contradiction, assume that it is possible to build a 1W1R atomic bit $R$ from a finite set $S$ of regular registers, each with a finite value domain, in which the reader does not update base registers.

An operation $r=$ R.read () performed by the reader is implemented as a sequence of read operations on base registers. Without loss of generality, assume that $r$ reads all base registers. Consider again the execution $E$ in which the writer performs write operations $w_{1}, w_{2}, \ldots$, alternating R.write (1) and R.write $(0)$.

Since the reader does not update base registers, we can insert the complete execution of $r$ between every two steps in $E$ without affecting the steps of the writer. Since the base registers are regular, the value read in a base register $X$ by the reader performing $r$ after a prefix of $E$ is unambiguously defined by the latest value written to $X$ before the beginning of $r$. Let $\lambda(r)$ denote the state of all base registers observed by $r$.

By Lemma 4, there exists a digest $B=b_{0}, \ldots, b_{y}(y \geq 1)$ that appears infinitely often in $B_{1}, B_{2}, \ldots$, where $B_{i}$ is a digest of $w_{2 i+1}$. Since each state in $\left\{b_{0}, \ldots, b_{y}\right\}$ appears in $E$ infinitely often, we can construct an execution $E^{\prime}$ by inserting in $E$ a sequence of read operations $r_{0}, \ldots, r_{y}$ such that for each $j=0, \ldots, y, \lambda\left(r_{j}\right)=b_{y-j}$. In other words, in $E^{\prime}$, the reader observes the states of base registers evolving downwards from $b_{y}$ to $b_{0}$.

By induction, we show that in $E^{\prime}$, each $r_{j}(j=0, \ldots, y)$ must return 1 . Initially, since $\lambda\left(r_{0}\right)=b_{y}$ and $b_{y}$ is the state of the base registers right after some $R$.write (1) is complete, $r_{0}$ must return 1 . Inductively, suppose that $r_{j}$ (for some $j, 0 \leq j \leq y-1$ ) returns 1 in $E^{\prime}$.

Consider read operations $r_{j}$ and $r_{j+1}(j=0, \ldots, y-1)$. Recall that $\lambda\left(r_{j}\right)=b_{y-j}$ and $\lambda\left(r_{j+1}\right)=$ $b_{y-j-1}$. Since digest $B$ appears in $B_{1}, B_{2}, \ldots$ infinitely often, $E^{\prime}$ contains infinitely many base-register
writes by which the writer changes the state of base registers from $b_{y-j-1}$ to $b_{y-j}$. Let $X$ be the base register changed by these writes.

Since $X$ is regular, we can construct an execution $E^{\prime \prime}$ which is indistinguishable to the reader from $E^{\prime}$, where $r_{j}$ are concurrent with a base-register write performed within $R$.write(1) in which the writer changes the state of the base registers from $b_{y-j-1}$ to $b_{y}-j$ (Figure 6.1).

By the induction hypothesis, $r_{j}$ returns 1 in $E^{\prime}$ and, thus, in $E^{\prime \prime}$. Since the implemented register $R$ is atomic and $r_{j}$ returns the concurrently written value 1 in $E^{\prime \prime}, r_{j+1}$ must also return 1 in $E^{\prime \prime}$. But the reader cannot distinguish $E^{\prime}$ and $E^{\prime \prime}$ and, thus, $r_{j+1}$ returns 1 also in $E^{\prime}$.

Inductively, $r_{y}$ must return 1 in $E^{\prime}$. But $\lambda\left(r_{y}\right)=b_{0}$, where $b_{0}$ is the state of base registers right after some R.write (0) is complete. Thus, $r_{y}$ must return 0 - a contradiction.

Therefore, to implement a 1W1R atomic register from bounded regular registers, we must establish two-way communication between the writer and the reader. Intuitively, the reader must inform the writer that it is aware of the latest written value, which requires at least one base bit that can be written by the reader and read by the writer. But the writer must be able to react to the information read from this bit. In other words:

Theorem 15 In any implementation a 1W1R atomic bit from regular bits, the writer must be able to write to at least 2 regular bits.

Proof Suppose, by contradiction, that there exists an implementation of a 1W1R atomic bit $R$ in which the writer can write to exactly one base bit $X$.

Note that every write operation on $R$ that changes the value of $X$ and does not overlap with any read operation must change the state of $X$. Without loss of generality assume that the first write operation $w_{1}=$ R.write(1) performed by the writer in the absence of the reader changes the value of $X$ from 0 to 1 (the corresponding digest is 0,1 ).

Consider an extension of this execution in which the reader performs $r_{1}=R$.read () right after the end of $w_{1}$. Clearly, $r_{1}$ must return 1 . Now add $w_{2}=R$. write $(0)$ right after the end of $r_{1}$. Since the state of $X$ at the beginning of $w_{2}$ is 1 , the only digest generated by $w_{2}$ is 1,0 .

Now add $r_{2}=R$.read () right after the end of $w_{2}$, and let $E$ be the resulting execution. Now $r_{2}$ must return 0 in $E$. But since $X$ is regular, $E$ is indistinguishable to the reader from an execution in which $r_{1}$ and $r_{2}$ take place within the interval of $w_{1}$ and thus both must return 1 - a contradiction. $\square_{\text {Theorem }} 15$

As we have seen in the previous chapter, there is a trivial bounded algorithm that constructs a regular bit from a safe bit. This algorithm only requires one additional local variable at the writer. The combination of this algorithm with Theorem 15 implies:

Corollary 1 The construction of a 1W1R atomic bit from safe bits requires at least 3 1W1R safe bits, two written by the writer and one written by the reader.

As the construction presented in the next section uses exactly $31 \mathrm{~W} 1 \mathrm{R}$ regular bits to build an atomic bit, it is optimal in the number of base safe bits.

### 6.3. From three safe bits to an atomic bit

Now we present an optimal construction of a high level 1W1R atomic bit $R$ from three base 1W1R safe bits. The high level bit $R$ is assumed to be initialized to 0 . It is also assumed that each R.write $(v)$ operation invoked by the writer changes the value of $R$. This is done without loss of generality, as the writer of $R$ can locally keep a copy $v^{\prime}$ of the last written value, and apply the next $R$.write $(v)$ operation only when it modifies the current value of $R$.

The construction of $R$ is presented in an incremental way.

### 6.3.1. Base architecture of the construction

The three base registers are initialized to 0 . Then, as we will see, the read and write algorithms defining the construction, are such that, any write applied to a base register $X$ changes its value. So, its successive values are 0 , then 1 , then 0 , etc. Consequently, to simplify the presentation, a write operation on a base register $X$, is denoted "change $X$ ". As any two consecutive write operations on a base bit $X$ write different values, it follows that $X$ behaves as regular register.

The 3 base safe bits used in the construction of the high level atomic register $R$ are the following:

- $R E G$ : the safe bit that, intuitively, contains the value of the atomic bit that is constructed. It is written by the writer and read by the reader.
- WR: the safe bit written by the writer to pass control information to the reader.
- $R R$ : the safe bit written by the reader to pass control information to the writer.


### 6.3.2. Handshaking mechanism and the write operation

As we saw in the previous section, the reader should inform the writer when it read a new value $v$ in the implemented register. Otherwise, the uninformed writer may subsequently repeat the same digest of state transitions executing R.write $(v)$ so that the reader would be subject to new-old inversion. Therefore, whenever the writer is informed that a previously written value is read by the reader, it should change the execution so that critical digests are not repeated.

The basic idea of the construction is to use the control bits $W R$ and $R R$ to implement the handshaking mechanism. Intuitively, the writer informs the reader about a new value by changing the value of $W R$ so that $W R \neq R R$. Respectively, the reader informs the writer that the new value is read by changing the value of $R R$ so that $W R=R R$. With these conventions, we obtain the following handshaking protocol between the writer and the reader:

- After the writer has changed the value of the base register $R E G$, if it observes $W R=R R$, it changes the value of $W R$.

As we can see, setting the predicate $W R=R R$ equal to false is the way used by the writer to signal that a new value has been written in $R E G$.

- Before reading $R E G$, the reader changes the value of $R R$, if it observes that $W R \neq R R$. This signaling is used by the writer to update $W R$ when it discovers that the previous value has been read.

As we are going to see in the rest of this chapter, the exchange of signals through $W R$ and $R R$ is also used by the reader to check if the value it has found in $R E G$ can be returned.

### 6.3.3. An incremental construction of the read operation

The reader's algorithm is much more involved than the writer's algorithm. To make it easier to understand, this section presents the reader's code in an incremental way, from simpler versions to more involved ones. In each stage of the construction, we exhibit scenarios in which a simpler version fails, which motivates a change of the protocol.

The construction: step 1 We start with the simplest construction in which the reader establishes $R R=W R$ and returns the value found in $R E G$. (The line numbers are chosen to anticipate future modifications of the algorithm.)

```
3 if $W R \neq R R$ then change $R R ; \%$ Strive to establish $W R=R R \%$
4 val $\leftarrow R E G$
5 return (val)
```

We can immediately see that this version does not really use the control information: the value returned by the read operation does not depend on the states of $R R$ and $W R$. Consequently, this version is subject to new-old inversions: suppose that while the writer changes the value of $R E G$ from 0 to 1 (line ii in Figure 6.2), the reader performs two read operations. The first read returns 1 (the "new" value of $R$ ) and the second read returns 0 (the "old" value), i.e., we obtain a new-old inversion.

The construction: step 2 An obvious way to prevent the new-old inversion described in the previous step is to allow the reader to return the current value of $R E G$ only if it observes that the writer has updated $W R$ to make $W R \neq R R$ since the previous read operation.

Here we assume that the local variable val initially contains the initial value of $R$ (e.g., 0). Checking whether $W R \neq R R$ before changing $R R$ in line $3^{\prime}$ looks unnecessary, since the reader does not touch the shared memory between reading $W R$ in line 1 and in line 3 , so we dropped it for the moment.

Unfortunately, we still have a problem with this construction. When a read is executed concurrently with a write, it may happen that the read returns a concurrently written value but a subsequent read finds $R R \neq W R$ and returns an old value found in $R E G$.

Indeed, consider the following scenario (Figure 6.3):

1. $w_{1}=R$.write $(1)$ changes $R E G$ and starts changing $W R$.
2. $r_{1}$ reads $W R$, finds $W R \neq R R$ and changes $R R$, reads $R E G$ and returns 1 .
3. $r_{2}$ reads $W R$ and still finds $W R \neq R R$ (new-old inversion on $W R$ ).
4. $w_{1}$ completes changing $W R$ and returns.
5. $w_{2}=R$.write $(0)$ starts changing $R E G$.
6. $r_{2}$ changes $R R$ (establishing that $R R \neq W R$ now), reads $R E G$ and returns 0 .
7. $r_{3}$ reads $W R$, finds $W R \neq R R$, reads $R E G$ and returns 1 (new-old inversion on $R E G$ ).
8. $w_{2}$ completes changing $R E G$ and returns.

In other words, we obtain a new-old inversion for read operations $r_{2}$ and $r_{3}$.

The construction: step 3 The problem with the scenario above is that read operation $r_{2}$ changes $R R$ while it is not necessary: it previously evaluated $W R \neq R R$ due to a new-old inversion on $W R$. Thus, when $r_{2}$ changes $R R$, it sets $W R \neq R R$ again. Thus, the subsequent read $r_{3}$ finds $W R \neq R R$ will be forced to return a value read in $R E G$, and the value can be "old" due to the ongoing change in $R E G$.

A naïve solution to this could be for the reader to check again if $W R \neq R R$ still holds before changing $R R$. By itself, this additional check will not change anything, since we could schedule this check performed by $r_{2}$ immediately after the first one and concurrently with $w_{1}$ 's change of $W R$. Thus, additionally, the reader may first read $R E G$ and only then check if the condition $W R \neq R R$ still holds and change $R R$ if it does.

$$
\begin{aligned}
& 1 \quad \text { if } W R=R R \text { then return }(v a l) \\
& 2^{\prime} \text { val } \leftarrow R E G \\
& 3 \text { if } W R=R R \text { then change } R R \\
& 5 \text { return }(v a l)
\end{aligned}
$$

This way we fix the problem described in Figure 6.3 but face a new one. The value read in $R E G$ may get overly conservative in some cases. Consider, for example, the scenario in Figure 6.4. Here read operation $r_{2}$ evaluates $W R=R R$ and returns the old value 1 , even though the most recently written value is actually 0 . This is because, the preceding read operation $r_{1}$ changed $R R$ to be equal to $W R$ without noticing that $R E G$ was meanwhile changed

The construction: step 4 One solution to the problem exemplified in Figure 6.4 is, as put in the pseudocode below, to evaluate $R E G$ after changing $R R$ and then check $R R$ again. If the predicate $R R=W R$ does not hold after $R R$ was changed and $R E G$ was read again, the reader returns the old (read in line 2) value of $R E G$. Otherwise, the new (read in line 4 ) value is returned.

Unfortunately, there is still a problem here. The variable val evaluated in line 4 may be too conservative to be returned by a subsequent read operation that finds $R R=W R$ in line 1 .

Again, suppose that $w_{1}=R$.write(1) is followed a concurrent execution of $r_{1}=R$.read () and $w_{2}=$ R.write $(0)$ as follows (Figure 6.5):

1. $w_{1}=$ R.write $(1)$ completes.
2. $w_{2}=R$.write $(0)$ begins and starts changing $R E G$ from 1 to 0 .
3. $r_{1}$ finds $W R \neq R R$, reads 0 from $R E G$ and stores it in aux (line 2 ), changes $R R$, reads 1 from $R E G$ and stores it in val (the write operation on $R E G$ performed by $w_{2}$ is still going on).
4. $w_{2}$ completes its write on $R E G$, finds $R R=W R$ and starts changing $W R$.
5. $r_{1}$ finds $W R \neq R R$ (line 5), concludes that there is a concurrent write operation and returns the "conservative" value 0 (read in line 2 ).
6. $r_{2}=R \cdot \operatorname{read}()$ begins, finds $R R=W R$ (the write operation on $W R$ performed by $w_{2}$ is still going on), and returns 1 previously evaluated in line 4 of $r_{1}$.

That is, $r_{1}$ returned the new (concurrently written) value 0 while $r_{2}$ returned the old value 1 .

The construction: last step The complete read algorithm is presented in Figure 6.6. As we saw in this chapter, safe base registers allow for a multitude of possible execution scenarios, so an intuitively correct implementation could be flawed because of an overlooked case. To be convinced that our construction is indeed correct, we provide a rigorous proof below.

```
operation R.read () :
    1 if $W R=R R$ then return $(v a l)$
    2 aux $\leftarrow R E G$
    3 if $W R \neq R R$ then change $R R$;
    4 val $\leftarrow R E G$;
    5 if $W R=R R$ then return $(v a l)$
    6 val $\leftarrow R E G$;
    7 return $(a u x)$
```

Figure 6.6.: The R.read () operation

### 6.3.5. Cost of the algorithms

The cost of the R.read () and R.write $(v)$ operations is measured by the the maximal and minimal numbers of accesses to the base registers. Let us remind that the writer (resp., reader) does not read $W R$ (resp., $R R$ ) as it keeps a local copy of that register.

- R.write $(v):$ maximal cost: 3 ; minimal cost: 2.
- R.read(): maximal cost: 7 ; minimal cost: 1 .

The minimal cost is realized when the same type of operation (i.e., read or write) is repeatedly executed while the operation of the other type is not invoked.

Notice we have assumed that if R.write $(v)$ and R.write $\left(v^{\prime}\right)$ are two consecutive write operations, we have $v \neq v^{\prime}$. If the user issues two consecutive write operations with the same argument, the cost of the second one is 0 , as it is skipped and consequently there is no accesses to base registers.

