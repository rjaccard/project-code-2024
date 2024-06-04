# 8. Collects and snapshots 

Until now we discussed read-write abstractions in which a read operation returns the last value written to a single specified register. It would also be convenient to have an abstraction that allows the reader to get, in a single operation, the vector of the last values written by all the processes. As usual, we expect the operation to be wait-free, and we explore several definitions of the "last written value". We start with from the weaker collect object, and then proceed to the stronger snapshot and immediate snapshot objects.

### 8.1. Collect object

A collect object exports the operation store () that is used to post values and the operation collect () that returns a view, a collection of "most recent" values posted so far. More precisely, a view $V$ is an $n$-vector, with one value per process. Intuitively, store $(v)$ is invoked by process $p_{i}$ to replace the value in position $i$ of the view with $v$. If no value has been posted by $p_{i}$ so far, the view returned by a collect () operation contains $\perp$ at position $i$.

### 8.1.1. Definition and implementation

A collect object can be seen as an array of $n$ elements. Each element $i$ can be updated by process $i$ using the store () operation. An evaluation of the content of the array can be obtained using the collect() operation: each position $i$ of the returned $n$-vector, called a view, contains the argument of a concurrent store operation or the argument of the latest store operation of $p_{i}$.

For simplicity, we assume that every value written by a given process $p_{i}$, including the initial value in position $i$, is unique. This way the value at position $i$ in a view $V$ returned by a collect operation is associated with a unique store operation $s_{i}$ by $p_{i}$ that has written that value, and we simply write $s_{i} \in V$ (the initial value $\perp$ the view is associated with an artificial "initializing" store operation performed by $p_{i}$ in the beginning). We also say that view $V$ is contained in a view $V^{\prime}$, and we write $V \leq V^{\prime}$, if for all $j, V[j]$ is written before $V^{\prime}[j]$. We write $V<V^{\prime}$ if $V \leq V^{\prime}$ and $V \neq V^{\prime}$.

To define what does it mean for a collect object to behave correctly, consider a history $H$ of events inv $[$ store ()$]$, resp $[$ store ()$]$, inv $[\operatorname{collect}()] \operatorname{resp}[\operatorname{collect}()]$ issued by the processes. Recall that $<_{H}$ denotes the total order on the events in $H$ and $\rightarrow_{H}$ denoted the real-time order on the operations in $H$. As usual, we assume that $H$ is well-formed: no process invokes a new operation on the collect object before its previous operation returns. Thus, any two operations invoked by a given process in $H$ are related by $\rightarrow_{H}$. Every history $H$ of invocations and responses on a collect object must satisfy the following properties (here $C$ denotes a collect operation and $s_{i}$ denotes a store operation of process $p_{i}$ ):

B0 : For each collect operation $C$ that returns $V$, and each $s_{i} \in V: C \neg \rightarrow_{H} s_{i}$. (No collect returns a value not yet written.)

$B 1$ : For each collect operation $C$ that returns $V$, store operations $s$ and $s^{\prime}$ by process $p_{i}$, such that $s^{\prime} \in V:\left(s \rightarrow_{H} C\right) \Rightarrow\left(s=s^{\prime} \vee s^{\prime} \rightarrow_{H} s^{\prime}\right)$. (No collect returns an overwritten value.)

$B 2: \forall V, V^{\prime}$ returned by $C, C^{\prime}:\left(C \rightarrow_{H} C^{\prime}\right) \Rightarrow\left(V \leq V^{\prime}\right)$. (Every collect contains all preceding ones.)

A straightforward implementation of a collect object maintains $n$ atomic registers, $R E G[1], \ldots, R E G[n]$, one per process. To store a value, $p_{i}$ simply writes it to $R E G[i]$. To collect the content, $p_{i}$ reads $R E G[1], \ldots, R E G[n]$ in any order. We can construct a collect reading function as a composition of corresponding atomic reading functions $\pi_{1}, \ldots, \pi_{n}$ : for each collect operation, define $\pi(C)[i]=\pi_{i}\left(r_{i}^{C}\right)$, where $r_{i}^{C}$ is the read operation on $R E G[i]$ performed within $C$. The reader can easily see that the resulting reading function satisfies properties $B 0-B 2$ above.

### 8.1.2. A collect object has no sequential specification

An abstraction $A$ has a sequential specification $\mathcal{S}$, if its behavior can be expressed through a set of sequential histories in $\mathcal{S}$. Formally:

- Every implementation of $A$ is an atomic implementation of $\mathcal{S}$, and
- Every atomic implementation of $\mathcal{S}$ is an implementation of $A$.

Note that the second property implies that every sequential history of $\mathcal{S}$ should be a history of $A$. If an abstraction $A$ has a sequential implementation, we say that $A$ is an atomic object.

## Lemma 5 Collect is not an atomic object.

Proof Suppose, by contradiction, that the collect abstraction has a sequential specification $\mathcal{S}$.

Consider the execution history in Figure 8.1. Here the $\operatorname{collect}()$ operation issued by $p_{1}$ is concurrent with two store operations issued by $p_{2}$ and $p_{3}$. The history could have been exported, for example, by an execution of the simple algorithm described above (Section 8.1.1), in which $p_{1}$, within its $\operatorname{collect}()$ operation, reads $R E G[2]$ before the write on $R E G[2]$ performed by $p_{2}$ and $R E G[3]$ after the write on $R E G[3]$ performed by $p_{3}$.

By our assumption, the history should be atomic with respect to $\mathcal{S}$. We recall that any linearization of $H$ should respect the real-time order on operations and, thus, we should put $\left[\right.$ store $(v)$ by $\left.p_{2}\right]$ before [store $\left(v^{\prime}\right)$ by $\left.p_{3}\right]$ in any linearization of $H$. We establish a contradiction by showing that there is no way to find a place for the collect () operation in any such linearization.

Suppose that $\mathcal{S}$ allows placing the $\operatorname{collect}()$ operation before store $\left(v^{\prime}\right)$ by $p_{3}$. Thus, $\mathcal{S}$ contains a sequential history that violates property $B 0$ (the collect operation returns a value which is not written yet).

Now suppose that $\mathcal{S}$ allows placing the $\operatorname{collect}()$ operation after store $\left(v^{\prime}\right)$ by $p_{3}$. This results in a history that violates property $B 1$ (the collect operation returns an overwritten value).

In both cases, $\mathcal{S}$ contains a history that does not respect the properties of collect. $\quad \square_{\text {Lemma }} 5$

Note that the proof will hold even for a weaker abstraction that only satisfies $B 0$ and $B 1$ : a collect abstraction would not have a sequential specification even without the requirement that any collect operation should contain all preceding collect operations.

### 8.2. Snapshot object

One of the reasons why the collect object cannot be captured by a sequential specification is that it allows concurrent collect operations to return views that are not "ordered", i.e., not related by containment.

In this chapter, we introduce an "atomic restriction" of collect: a snapshot object that exports two operations: update() and snapshot(). The snapshot() operation returns a vector of $n$ values (one per process). The value in position $i$ of the vector contains the argument of the last preceding or a concurrent update () operation executed by process $p_{i}$.

### 8.2.1. Definition

In every history $H$, a snapshot object satisfies properties $B 0-B 2$ of collect (Section 8.1.1), where store and collect are replaced with update and snapshot, respectively, plus the following two properties:

$B 3$ For any two views $V$ and $V^{\prime}$ obtained by snapshot operations, $\left(V \leq V^{\prime}\right) \vee\left(V^{\prime} \leq V\right)$.

$B 4$ For any two updates $u$ and $u^{\prime}$, where $u$ is performed by a process $p_{i}$, and any view $V$ obtained by a snapshot operation, if $u^{\prime} \in V$ and $u \rightarrow_{H} u^{\prime}$, then $V$ contains $u$ or a later update at position $i$.

In other words, non-concurrent updates cannot be observed by snapshot operations in the opposite order: new-old inversion on the level of snapshot and updates is not allowed.

If snapshot operations $S$ and $S^{\prime}$ return views $V$ and $V^{\prime}$, respectively, such that $V \leq V^{\prime}$, we say that $S$ is contained in $S^{\prime}$, and write $S \leq S^{\prime}$. Thus, $B 3$ implies that any two snapshot operations are related by containment.

### 8.2.2. The sequential specification of snapshot

The sequential specification of type snapshot is defined as a set of sequential histories of update and snapshot operations. In every such sequential history, each position $i$ of the vector returned by every snapshot operation contains the argument of last preceding update operation of $p_{i}$ (if any, or the initial value $\perp$ otherwise). Note that, unlike the operational definitions of collect and snapshot objects proposed above, the definition of the sequential snapshot type is valid even if we do not assume that every value written by a given process is unique.

Intuitively, a concurrent implementation of the snapshot type gives the illusion of update and snapshot operations taking place instantaneously. We show that this type indeed captures the behavior of a snapshot object.

Lemma 6 The snapshot abstraction is atomic (with respect to the snapshot type).

Proof Consider a finite history $H$ of a snapshot implementation. Recall that $H$ satisfies properties B0-B2 of collect (where store and collect are replaced with update and snapshot), plus B3 and B4.

We construct a linearization $L$ of $H$ as follows. First we order all complete snapshot operations in $H$, based on the $\leq$ relation, which is possible by property $B 3$.

Let update $(v)=U$ be an operation performed by $p_{i} . U$ is then inserted in $L$ just before the first snapshot operation that returns $v$ or a later value in position $i$, or at the end of the sequence if there is no such a snapshot. After having done this for every update, we obtain a sequence $\left[U_{0}\right], S_{1},\left[U_{1}\right], S_{2},\left[U_{2}\right]$, $\ldots, S_{k},\left[U_{k}\right]$, where each $\left[U_{j}\right]$ is a (possibly empty) sequence of update operations $U$ such that snapshot $S_{j}$ returns values older that written by $U$ and $S_{j+1}$ returns the value written by $U$ or a later value. Now we rearrange elements of each $\left[U_{j}\right]$ so that the real-time order is respected. This is possible since the real-time order is acyclic.

Now we show that the resulting linearization $L$ respects the order $\rightarrow_{H}$. Consider two operations op and $o p^{\prime}$, such that $o p \rightarrow_{H} o p^{\prime}$. Three cases are possible:

- Both $o p$ and $o p^{\prime}$ are update operations. Let $o p$ and $o p^{\prime}$ belong to $\left[U_{\ell}\right]$ and $\left[U_{m}\right]$, respectively. If $\ell<m, o p \rightarrow_{L} o p^{\prime}$, as $\left[U_{\ell}\right]$ precedes $\left[U_{m}\right]$ in $L$. If $\left.\ell=m, L\right)$, then $o p \rightarrow_{L} o p^{\prime}$, as $L$ preserves the real-time order of $H$ in each $\left[U_{m}\right]$.

Suppose now that $\ell>m$. But, by $B 4, S_{m+1}$ contains $o p^{\prime}$ and any update that precedes it, including $o p$. By the construction of $L, o p^{\prime}$ cannot belong to $U_{\ell}$ - a contradiction.

- Both $o p$ and $o p^{\prime}$ are snapshot operations that return views $V$ and $V^{\prime}$, respectively. If $o p^{\prime}$ is incomplete, then it does not appear in $L$. If $o p^{\prime}$ is complete, then by $B 2, V \leq V^{\prime}$. Since $L$ orders snapshots based on the $\leq$ relation, if $o p^{\prime}$ appears in $L$, we have $o p \rightarrow_{L} o p^{\prime}$ in $L$.
- $o p$ is an update and $o p^{\prime}$ is a snapshot. By $B 1, o p^{\prime}$ returns the value written by $o p$ or a later value, and, by the construction of $L$ and $B 3, o p \rightarrow_{L} o p^{\prime}$.
- $o p$ is a snapshot and $o p^{\prime}$ is an update. By $B 0$, the value written by $o p^{\prime}$ does not appear in the result of $o p$. By the construction of $L, o p \rightarrow_{L} o p^{\prime}$.

Thus, any snapshot object is an atomic implementation of the snapshot type.

Now consider a history $H$ of a atomic implementation of the snapshot type. We are going to show that $H$ satisfies properties $B 0-B 4$. Let $L$ be a linearization of $H$. Thus, $L$ is a legal (with respect to the snapshot type) sequential history, that is equivalent to a completion of $H$ and respects the real-time order in $H$. In particular, $L$ contains every complete operation in $H$.

- Suppose that a snapshot operation $S$ returns a value $v$ at position $i$ in $H$. Since $L$ is legal, $v$ is the value written by the last update $u$ of $p_{i}$ that precedes $S$ in $L$. Since $L$ respects the real-time order, $S$ cannot precede $u$ in $H$, and, thus, $B 0$ is ensured in $H$.
- Suppose an update $u$ precedes a snapshot $S$ in $H$. Since $L$ respects the real-time order of $H, u$ precedes $S$ also in $L$. Since $L$ is legal, $S$ returns the value written by $u$ or a later value at the corresponding position and, thus, $B 1$ is ensured in $H$.
- Suppose a snapshot $S_{1}$ precedes a snapshot $S_{2}$ in $H$. Since $L$ respects the real-time order of $H$, $S_{1}$ precedes $S_{2}$ also in $L$. Legality of $L$ implies that $S_{1} \leq S_{2}$ and, thus, $B 2$ is ensured in $H$.
- All complete snapshot operations appear in $L$ and, since $L$ is legal, are related by $\leq: B 3$ is ensured in $H$.
- Suppose that an update $u_{1}$ precedes an update $u_{2}$ and a snapshot $S$ returns the value written by $u_{2}$. Since $L$ respects $\rightarrow_{H}$ and is legal, we have $u_{1} \rightarrow_{L} u_{2}$ and $u_{2} \rightarrow_{L} S$. Thus, $u_{1} \rightarrow_{L} S$ and, since $L$ is legal, $S$ returns the value written by $u_{1}$ or a later value at the corresponding position: $B 4$ is ensured in $H$.

Thus, any atomic implementation of the snapshot type is indeed a snapshot object.

### 8.2.3. Non-blocking snapshot

We start with a simple non-blocking snapshot implementation that only guarantees that at least one correct process completes each of its operations. The construction assumes that the underlying base registers can store values of arbitrary (unbounded) size, i.e., we may associate ever-growing sequence numbers with every stored value. Then we turn the construction into an unbounded wait-free one. Finally, we present a wait-free snapshot implementation that uses bounded memory.

```
operation update $(v)$ invoked by $p_{i}$ :

$\begin{array}{lc}s n_{i}:=s n_{i}+1 & \{\text { local sequence number generator }\} \\ R E G[i]:=\left[v, s n_{i}\right] & \{\text { store the pair }\}\end{array}$
```

Figure 8.2.: Update operation

```
operation snapshot () :
    $a a:=R E G \cdot \operatorname{scan}()$
    repeat forever
        $b b:=R E G \cdot \operatorname{scan}()$
        if $(a a=b b)$ then return (aa.val); $\quad\{$ return the vector of read values $\}$
        $a a:=b b$
```

Figure 8.3.: Snapshot operation

Our $n$-process snapshot implementation uses an array of atomic registers $R E G[]$. Each value that can be stored in a register $R E G[i]$ is associated with a sequence number that is incremented each time a new value is stored. Each $R E G[i]$ consists of two fields, denoted $R E G[i] . s n$ and $R E G[i] . v a l$. The implementation of update() is presented in Figure 8.2. Here $s n_{i}$ is a local variable, initially 0, that $p_{i}$ uses to generate sequence numbers.

In an update operation, process $p_{i}$ simply writes the value, together with its sequence number, in the corresponding register. To ensure that the result of every snapshot operation is consistent, i.e., contains the most recent the implementation uses the "double scan" technique: the process keeps reading registers $R E G[1, \ldots, n]$ until two consecutive collects return identical results. The result of the last scan is then returned by the snapshot operation.

The $\operatorname{scan}()$ function asynchronously reads the last (sequence number, data) pairs posted by each process:

```
function $R E G \cdot \operatorname{scan}()$ :
    for $j \in\{1, \ldots, n\}$ do
        $R[j]:=R E G[j]$
    return $(r)$
```

Theorem 19 The algorithm in Figures 8.2 and 8.3 is a non-blocking atomic snapshot implementation.

Proof To prove that the implementation is non-blocking, consider any infinite execution of the algorithm.

The update operation terminates in only one base-object step. Suppose now that a snapshot operation performed by a correct process $p_{i}$ never terminates. By the algorithm, $p_{i}$ thus executes infinitely many scans of $R E G$. The only reason not to return in line 4 is to find out that one of the positions in $R E G$ has changed since the last scan. Thus, for every two consecutive scan operations $C_{1}$ and $C_{2}$ executed by $p_{i}$, another process $p_{j}$ executes an update operation $U$ such that write to $R E G[j]$ in $U$ takes place between the read of $R E G[j]$ in $C_{1}$ and the read of $R E G[j]$ in $C_{2}$. Since there are only finitely many processes, at least one process performs infinitely update operations concurrently with the snapshot operation of
$p_{i}$. Thus, in every infinite execution of the algorithm, at least one correct process completes every its operation. So the implementation is indeed non-blocking.

Now we show that the implementation is linearizable with respect to the snapshot type. Let $E$ be any finite execution of the algorithm and $H$ be the corresponding history. Consider any complete snapshot () operation in $E$. Let $C_{1}$ and $C_{2}$ be its last two scans. By the algorithm, $C_{1}$ and $C_{2}$ return the same result. Now we choose the linearization point of the snapshot operation to be any point in $E$ between the response of $C_{1}$ and the invocation of $C_{2}$ (see example in Figure 8.4). Otherwise, if a snapshot operation does not return in $E$, we remove the operation from our completion of the corresponding history $H$.

Consider now an update $(v)$ operation executed by a process $p_{i}$ in $E$. We linearize the operation at the point when it performs a write on $R E G[i]$ in $E$ (if it does not, we remove it from the completion of $H)$.

Let $L$ be the resulting linearization of $H$, i.e., the sequential history where operations appear in the order of their linearization points in $E$. By the construction, $L$ is equivalent to a completion of $H$. Also, since each operation is linearized within its interval in $E, L$ respects the real-time order of $H$. We show that $L$ is legal, i.e., at every position $i$, every snapshot operation in $L$ returns the value written by the latest preceding update of $p_{i}$.

Let $S$ be a snapshot operation in $L$, and let $C_{1}$ and $C_{2}$ be the two last scans of $S$. For each $p_{i}$, let $u_{i}$ be the last update operation of $p_{i}$ preceding $S$ in $L$. Recall that $u_{i}$ is linearized at the write on $R E G[i]$ and $S$ is linearized between the response of $C_{1}$ and the invocation of $C_{2}$. Since, by the algorithm, $C_{1}$ and $C_{2}$ read the same value in $R E G[i]$, no write on $R E G[i]$ takes place between the read of $R E G[i]$ performed within $C_{1}$ and the read of $R E G[i]$ performed within $C_{2}$. Thus, since the write operation performed within $u_{i}$ is the last write on $R E G[i]$ to precede the linearization point of $S$ in $E$, we derive that it is also the last write on $R E G[i]$ to precede the read of $R E G[i]$ performed within $C_{1}$.

Therefore, for each $p_{i}$, the value of $p_{i}$ returned by $C_{1}$ and, thus, by $S$ is the value written by $u_{i}$. Hence, $L$ is legal, and the algorithm in Figures 8.2 and 8.3 gives a linearizable implementation of snapshot.

### 8.2.4. Wait-free snapshot

In the non-blocking snapshot implementation in Figures 8.2 and 8.3, update operations may starve a snapshot operation out by "selfishly" updating $R E G$. This implementation can be turned into a waitfree one using helping: an update operations can help concurrent snapshot operations to terminate. An update operation may itself take a snapshot of and store the result together with the new value in $R E G$ (Figure 8.5). Of course, for this helping mechanism to work, we need to make sure that the intertwined snapshot and update operations do not prevent each other from terminating.

First we can make the following two observations on the non-blocking snapshot implementation:

- If two consecutive scans performed within a snapshot operation are not identical, then at least one process has concurrently performed an update operation.
- If a snapshot operation $S$ issued by a process $p_{i}$ witnesses that the value of $R E G[j]$ has changed twice, i.e., $p_{j}$ concurrently executed two update operations $u_{1}$ and $u_{2}$, then the second of these updates was entirely performed within the interval of $S$ (see Figure 8.5). This is because $S$ observed the value written by $u_{1}$ (and, thus, $u_{2}$ was invoked after the invocation of $S$ ) and the (atomic) write by $p_{j}$ of the base atomic register $R E G[j]$ is the last operation of $u_{2}$.

As the execution interval of the second update falls entirely within the interval of $S$, we may use the update to "help" $S$ as follows:

- Within $u_{2}, p_{j}$ takes a snapshot itself (using the algorithm in Figure 8.3 ) and writes the result help to $R E G[j]$.
- Within $S, p_{i}$ uses the result read in $R E G[j]$ as the response of $S$. This is going to be a valid result, since the execution of $u_{2}$ (and, thus, of the snapshot performed by $u_{2}$ ) takes place entirely within the interval of $S$, so $S$ can simply "borrow" the snapshot result help from $U_{2}$.

Note that for this kind of helping to work, $S$ must witness at least two concurrent updates of the same process. For example, even though the write on $R E G[j]$ performed within $u_{1}$ takes place within the interval of $S$, the snapshot written by $u_{1}$ together with its value may have taken place way before the invocation of $S$. Thus, adopting the result of $u_{1}$ 's snapshot as the result of $S$ may violate linearizability, since it may miss updates executed after the snapshot taken by $u_{1}$ but before the invocation of $S$. This is why, before adopting the snapshot taken by $p_{j}, p_{i}$ should wait until it observes the second change in $R E G[j]$.

The resulting implementations of update() and snapshot() are described in Figure 8.6. The atomic register $R E G[i]$ consists now of three fields, $R E G[i] . v a l$ and $R E G[i] . s n$ as before, plus the new field $R E G[i]$.help_array that contains the result of the snapshot taken by $p_{i}$ in the course of its latest update operation.

The new local variable $i d c o u l d \_h e l p_{i}$ is used by process $p_{i}$ when it executes snapshot(). Initially $\emptyset, i d c o u l d \_h e l p_{i}$ contains the set of the processes that terminated update operations concurrently
with the snapshot operation currently executed by $p_{i}$ (lines 11-15). When $p_{i}$ observes that a process $p_{j} \in$ could_help updated its value in $R E G$, i.e., $p_{i}$ finds out that $a a_{i}[j] . s n \neq b b_{i}[j] . s n, p_{i}$ returns $R E G[j]$. help_array as the result of its snapshot operation.

```
operation update $(v)$ invoked by $p_{i}$ :
(1) help_array is $_{i}:=$ snapshot ()
(2) $s n_{i}:=s n_{i}+1$
(3) $R E G[i]:=\left(v, s n_{i}\right.$, help_array $\left._{i}\right)$
operation snapshot () :
(4) could_help $:=\emptyset$;
(5) $a a_{i}:=R E G \cdot \operatorname{scan}()$
(6) while true do
(7) $b b_{i}:=R E G . \operatorname{scan}()$;
(8) $\quad$ f $\left(\forall j \in\{1, \ldots, n\}: a a_{i}[j] \cdot s n=b b_{i}[j] . s n\right)$ then
(9)
return $\left(a a_{i} \cdot v a l\right)$
(10) else for all $j \in\{1, \ldots, n\}$ do
(11)
if $\left(a a_{i}[j] . s n \neq b b_{i}[j] . s n\right)$ then
(12)
if $\left(j \in\right.$ could_help $\left.{ }_{i}\right)$ then
(12)
return $\left(b b_{i}[j]\right.$.help_array $)$
(15)
else
could_help $:=$ could_help $p_{i} \cup\{j\}$
(16)
$a a_{i}:=b b_{i}$
```

Figure 8.6.: Atomic snapshot object construction

### 8.2.5. The snapshot object construction is bounded wait-free

Theorem 20 Each update() or snapshot() operation returns after at most $O\left(n^{2}\right)$ operations on base registers.

Proof Let us first observe that an update() by a correct process always terminates as long as the snapshot () operation it invokes always returns. So, the proof consists in showing that any snapshot() issued by a correct process $p_{i}$ terminates.

Suppose, by contradiction, that a snapshot operation executed by $p_{i}$ has not returned after having executed $n$ times the while loop (lines 5-16). Thus, each time it has executed the loop, $p_{i}$ has found out that for some new $j \notin$ could_help $p_{i}, a a_{i}[j] . s n \neq b b_{i}[j] . s n$ (line 11), i.e., $p_{j}$ has executed a new update() operation since the last $\operatorname{scan}()$ of $p_{i}$. After this $j$ is added to the set could_hel $p_{i}$ in line 14.

Note that $i \notin$ could_help $p_{i}\left(p_{i}\right.$ does not change the value of $R E G[i]$ while executing snapshot ()$)$. Thus, after $n-1$ iterations, could_help $p_{i}$ contains all other $n-1$ processes $\{1, \ldots, i-1, i+1, \ldots, n\}$. Therefore, when $p_{i}$ executes the while loop for the $n$th time, for any $p_{j}$ such that $a a_{i}[j] . s n \neq b b_{i}[j] . s n$ (line 11), it finds $j \in i d$ could_hel $p_{i}$ in line 12 . By the algorithm, $p_{i}$ returns in line 13 , after having executed $n$ iterations in lines $5-16-$ a contradiction.

Thus, every snapshot operation returns after having executed at most $n$ while loops in lines 5-16. Since every loop involves exactly $n$ base-object reads (in the scan operation on registers $R E G[1], \ldots$, $R E G[n])$, every snapshot terminates in $n^{2}$ base-object steps. An update operation additionally executes only one base-object write, thus its complexity is also within $O\left(n^{2}\right)$.

### 8.2.6. The snapshot object construction is atomic

Theorem 21 The object built by the algorithms described in Figure 8.6 is atomic with respect to the snapshot type.

Proof Let $E$ be an execution of the algorithm and $H$ be the corresponding history of $E$. To prove that the algorithm is indeed an atomic snapshot implementation, we construct a linearization of $H$, i.e., a total order $L$ on the operations in $H$ such that: (1) $L$ is equivalent to a completion of $H$, (2) $L$ respects the real-time order of $H$, and (3) $L$ is legal, i.e., each snapshot () operation $S$ in $L$ returns, for each process $p_{j}$, the value written by the last update() operation of $p_{j}$ that precedes $S$ in $L$.

The desired linearization $L$ is built as follows. The linearization point of a complete update() operation in $E$ is the write in the corresponding 1WMR register (line 3). Incomplete update operations are not included to $L$. The linearization point of a snapshot() operation $S$ issued by a process $p_{i}$ depends on the line at which it returns.

(i) If $S$ returns in line 9 (successful double $\operatorname{scan}()$ ), then the linearization point is any time between the end of the first $\operatorname{scan}()$ and the beginning of the second $\operatorname{scan}()$ (see the proof of Theorem 19 and Figure 8.4).

(ii) If $S$ returns in line 13 (i.e., $p_{i}$ terminates with the help of another process $p_{j}$ ), then the linearization point is defined recursively as the linearization point of the corresponding update operation of $p_{i}$. In the example depicted in Figure 8.7, the arrows show the direction in which snapshot results are adopted by one operation from another.

We show now that the linearization point is well-defined. If $S$ returns in line 13, the array (say help_array) returned by $p_{i}$ has been provided by an update() operation executed by some process $p_{j_{1}}$. As we observed earlier, this update() has been entirely executed within the interval of $S$, since help_array is the result of the second update operation of $p_{j}$ that is observed by $p_{i}$ to be concurrent with $S$. Thus, this update started after the invocation of $S$ and its last event (the write in $R E G[j]$ in line 8 ) before the response of $S$.

Recursively, help_array has been obtained by $p_{j_{1}}$ from a successful double scan, or from another process $p_{j_{2}}$. As there are at most $n$ concurrent processes, it follows by induction that there is a process $p_{j_{k}}$ that has executed a snapshot () operation within the interval of $S$ and has obtained help_array from a successful double scan.

The linearization point of the snapshot () operation issued by $p_{i}$ is thus defined as the linearization point of snapshot () operation of $p_{j_{k}}$ whose double scan determined help_array.

This association of linearization points to the operations in $H$ results in a complete sequential history $L$ that puts the operations in $H$ in the order their linearization points appear in $E$.

$L$ trivially satisfies properties (1) and (2) stated at the beginning of the proof. Reusing the proof of Theorem 19, we observe that, for every $p_{j}$, every snapshot operation $S$ (be it a standalone snapshot or a part of an update) returns the value written to $R E G[j]$ by the last update of $p_{j}$ to precede the linearization point of $S$ in $E$. Thus, $L$ also satisfies (3), and the algorithm in Figure 8.6 is an atomic implementation of snapshot.

### 8.3. Bounded atomic snapshot

Implementing atomic abstractions is of our central concern. In Chapter 6, we described a space-optimal implementation of an atomic bit using three safe bits. In Chapter 7, we discussed how to implement a multi-valued bounded atomic registers from bounded regular registers.

In contrast, our implementation of the atomic snapshot abstraction in Section 8.2.4 assumes underlying atomic registers of unbounded capacity. Indeed, the values written to the abstraction by update operations are assumed to be unique, e.g., equipped with distinct sequence numbers that are taken in an unbounded range.

On can see an apparent gap between these transformations, and a natural question is whether we can use atomic registers of bounded size to implement atomic snapshot.

### 8.3.1. Double collect and helping

The unbounded construction of atomic snapshots was based on two simple ideas: double collect and helping.

Two consecutive collects returning identical results within a snapshot operation guarantee that no register has been changed in the interval of time between the return of the first collect and the invocation of the second one. Thus, all the updates affecting the result of these collects can be safely linearized before the end of the first one.

If, after taking $n$ collects, process $p_{i}$ did not observe two identical ones, then at least one of the $n-1$ other processes (let us denote it $p_{j}$ ) performed two concurrent updates. Now assume that each update operation of $p_{j}$ includes taking a snapshot and attaching its outcome to the written snapshot value. Clearly, the snapshot attached to the second update performed by $p_{j}$ and witnessed by $p_{i}$ took place within the interval of the snapshot operation of $p_{i}$. Thus, it is safe for $p_{i}$ to adopt this outcome as its own.

Notice, however, that these mechanisms rely on the assumption that every value written to the snapshot object is unique: otherwise two identical collects do not necessarily imply that no concurrent update took place. An amusing exercise is to find an incorrect execution of our algorithm, assuming that the "uniquewrite" requirement is lifted. Intuitively, the so called $A B A$ problem ( $A$ in a snapshot position is replaced with $B$ and then with $A$ again, so that a concurrent reader does not see the change) may cause a snapshot operation to return an inconsistent value (see Exercise 3).

In histories with an unbounded number of updates, using a distinct value for each update operation requires unbounded memory. But suppose now that we are after a bounded atomic snapshot object: processes only write values from a bounded range. It turns out that a simple bounded-space handshaking mechanism can be used to detect modifications in a snapshot position.

### 8.3.2. Binary handshaking

Let us recall the signalling mechanism in the 1W1R atomic register construction (Chapter 6): the writer uses a special bit $W$ to inform the reader that the value of the implemented register has been modified, and the reader uses another special bit $R$ to inform the writer that the last written value has been read.

Intuitively, in an atomic snapshot construction, every process executing a snapshot operation acts as a reader, and every process executing an update operation acts as a writer. Therefore, for each distinct pair of processes $\left(p_{i}, p_{j}\right)$, we can maintain two atomic binary registers $W[i, j]$ and $R[i, j]$, where $W[i, j]$ can be written by $p_{i}$ when it performs an update and read by $p_{j}$ when it performs a snapshot, while $R[i, j]$ can be written by $p_{j}$ when it performs a snapshot and read by $p_{i}$ when it performs an update.

Now suppose that after $p_{i}$ modifies $R E G[i]$, it also checks $R[i, j]$ for each $j \neq i$ and sets $W[i, j]$ to be different from $R[i, j]$. Respectively, whenever $p_{j}$ collects the values of $R E G$ it checks $W[i, j]$ and, if needed, sets $R[i, j]$ to be equal to $W[i, j]$. Therefore, whenever $p_{j}$ takes a subsequent scan of $R E G$ and observes $R[i, j] \neq W[i, j]$, it may deduce that $R E G[i]$ has been recently changed.

It is still, however, possible that $p_{i}$ changes $R E G[i]$ but $p_{j}$ takes its scan before $p_{i}$ modifies $W[i, j]$. That is why we also introduce an additional toggle bit that is attached to the value written to $R E G[i]$. The bit $R E G[i]$.toggle is inverted each time $R E G[i]$ is written by $p_{i}$. This way $p_{j}$ can detect a concurrent update operation via a change either in $R E G[i]$.toggle or in $W[i, j]$.

### 8.3.3. Bounded snapshot using handshaking

Figure 8.8 describes a bounded implementation of the snapshot object. Now the atomic register $R E G[i]$ consists of three fields, $R E G[i] . v a l$ for the written value, $R E G[i]$. help_array for the result of the snapshot taken by $p_{i}$ within its latest update operation, and $R E G[i]$.toggle for the bit inverted with each new update performed by $p_{i}$.

The update operation is very similar to that in the unbounded algorithm (Figure 8.6). But instead of using a unique sequence number with every written value, process $p_{i}$ inverts the toggle bit and makes sure that $W[i, j] \neq R[i, j]$, in order to inform every other process $p_{j}$ that a new value has been written.

In the snapshot operation, process $p_{i}$ first ensures that $W[j, i]=R[j, i]$ for every $j \neq i$, and then performs two scans of $R E G$. We are going to show that, for any $j \neq i, R E G[j]$.toggle has different values in these two scans or $W[j, i]$ does not equal $R[j, i]$ if and only if $R E G[j]$ has been concurrently modified. Thus, if no $j$ satisfies the conditions in line 14, it is safe to return the outcome of the latest scan taken by $p_{i}$ (line 20). If, for some $j$, the conditions are satisfied in three iterations, then it is safe to return the snapshot attached to last the value written by $p_{j}$ (line 16). Note that, unlike the unbounded version (Figure 8.6), two concurrent modification of the shared memory performed by another process are not enough (see Exercise 7).

### 8.3.4. Correctness

Essentially, we use the correctness arguments of the unbounded snapshot algorithm (Section 8.2.4). As before, we linearize each update operation of a process $p_{i}$ at the point it writes to $R E G[i]$. Each snapshot operation that detected no conflicts and returned in line 20 in any point between the end of its first scan (line 11) and the beginning of its second scan (line 12), taken just before returning. Recursively, each snapshot operation that adopts the value written by a concurrent update operation op (line 16) is linearized at the linearization point of the corresponding snapshot operation performed within $o p$ (line 1).

It remains to prove two points in this bounded algorithm though.

First, we need to show that if a snapshot operation $S$ does not detect any change in $R E G[j]$ in line 14, then indeed no $R E G[j]$ has not been modified between the moment it was read in line 11 and the moment point it was read in line 12 .

Lemma 7 Let $s_{1}$ and $s_{2}$ be two consecutive scans performed within a snapshot operation $S$ by a process $p_{i}$. If $R E G[j]$ has been modified between the moment it has been read in $s_{1}$ and the moment it has been read in $s_{2}$, then the check in line 14 performed by $S$ immediately after $s_{2}$ will succeed.

Proof If $R E G[j]$ has been modified only once after it was read in $s_{1}$ but before it was read in $s_{2}$, then the toggle field is different in $a a_{i}[j]$ and $b b_{i}[j]$ and, thus, the check in line 14 will succeed.

Suppose now that $R E G[j]$ has been modified twice or more in the chosen interval. By the update algorithm, between any two modifications of $R E G[j], p_{j}$ must make sure that $R[j, i] \neq W[j, i]$ (lines 8 5). Since between $s_{1}$ and $s_{2}, p_{i}$ does not modify $R[j, i]$, when it reads $W[j, i]$ immediately after the scans (line 14), it will find $R[j, i] \neq W[j, i]$ in line 14 and the check will succeed.

Thus, a snapshot operation that, for all $j$, passed through the checks in line 14 and returned in line 20 can be safely linearized at any point between its last two scans.

Second, we need to show that it is also safe to a snapshot operation to "borrow" the outcome of a snapshot taken by a process that has been witnessed "moving" three times (line 16). within the interval of $S$. For this, we first prove the following auxiliary result:

Lemma 8 Let $s_{1}$ and $s_{2}$ be two consecutive scans performed within a snapshot operation $S$ by a process $p_{i}$ (lines 11 and 12). If the check in line 14 performed by $S$ immediately after $s_{2}$ succeeds for some $j$, then $R E G[j]$ or $W[j, i]$ has been modified in the interval between time $t_{1}$, when $W[j, i]$ has been read just by $p_{i}$ before $s_{1}$ (line 9), and time $t_{2}$, when $W[j, i]$ has been read by $p_{i}$ just after $s_{2}$ (line 14).

Proof Suppose that the check in line 14 succeeds because the toggle bit of $R E G[j]$ has changed. This can only happen if $p_{j}$ has written to $R E G[j]$ (line 2 )) between the reads of the register performed by $p_{i}$ within $s_{1}$ and $s_{2}$ and, thus, in the desired interval.

Suppose now that $p_{i}$ finds out, in line 14 , that $R[j, i] \neq W[j, i]$. But after having read $W[j, i]$ at time $t_{1}$ and before executing $s_{1}, p_{i}$ has made sure that $R[j, i]=W[j, i]$ (lines 9 and 10 . Thus, the only reason to find out later that $R[j, i] \neq W[j, i]$ can be a modification of $W[j, i]$ (line 5) performed in the interval between $t_{1}$ and $t_{2}$.

Lemma 9 If a snapshot operation $S$ returns the view provided by an update operation $U$ (line 16), then the execution of the snapshot $S^{\prime}$ taken by $U$ falls within the interval of $S$.

Proof Suppose that $p_{i}$, within a snapshot operation $S$, returns the view written by an update operation $U$ performed by $p_{j}$. By the algorithm and Lemma 8 , during $S, p_{j}$ "moved" (by modifying $R E G[j]$ or $W[j, i])$ at least three times.

Note that $p_{j}$ can modify each of the registers $R E G[j]$ and $W[j, i]$ at most once during an update operation: in lines 2 and 5 , respectively. Thus, if three checks in line 14 performed by $S$ succeed, the first and the third modifications of $R E G[j]$ and $W[j, i]$ witnessed by $S$ must belong to different update operations performed by $p_{j}$, let us denote these update operations by $U_{1}$ and $U_{2}$.

Since an update operation performed by $p_{j}$ first takes a snapshot, then writes the outcome to $R E G[j]$ (together with its value and the toggle bit), and then modifies $W[j, i]$ (if needed), we conclude that the value read by $S$ in $R E G[j]$ in line 16 was written by a concurrent operation $U$, which is $U_{2}$ or a subsequent update operation. But since $U_{1}$ is concurrent with $S$ and $U$ succeeds $U_{1}$, we have that the snapshot operation $S^{\prime}$ taken within $U$ is entirely contained within the interval of $S$.

Thus, we can safely assign the linearization point of $S$ to the linearization point of $S^{\prime}$. As in the unbounded case, this recursive assignment of linearization points to snapshot operations is well-defined. The reader is encouraged to check this and to show that the sequential history based on these linearization points is legal, following the proof for the unbounded algorithm.

