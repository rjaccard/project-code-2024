# 10. Consensus and universal construction 

In the first part of this book, we considered multiple powerful abstractions that can be implemented, in the wait-free manner, from read-write registers. In this chapter, we address a more general question:

Given object types $T$ and $T^{\prime}$, is there a wait-free implementation of an object of type $T$ from objects of type $T^{\prime}$ ?

We define a fundamental consensus object type and show that consensus objects are universal: any object type can be implemented, in the wait-free manner, using read-write registers and consensus objects. In the next chapter, we show that read-write register cannot, by themselves, implement a wait-free consensus object shared by 2 processes and, thus, are not universal even in a system of 2 processes. This observation brings the notion of a consensus number of a given object type: the maximal number of processes in which the type is universal.

Overall, in this chapter we give a definition of consensus and demonstrate its power in implementing arbitrary object types. In the next chapter, we discuss the downside of this abstraction, namely, the difficulty of its implementations.

### 10.1. Consensus object: specification

The consensus object type exports an operation propose() that takes one input parameter $v$ in a value set $V(|V| \geq 2)$ and returns a value in $V$. Let $\perp$ denote a default value that cannot be proposed by a process $(\perp \notin V)$. Then $V \cup\{v\}$ is the set of states a consensus object can take, $\perp$ is its initial state, and its sequential specification is defined in Figure 10.1. A consensus objects can thus be seen as a "write-once" register that keeps forever the value proposed by the first propose() operation. Then, any subsequent propose() operation returns the first written value.

Given a linearizable implementation of the consensus object type, we say that a process proposes $v$ if it invokes propose $(v)$ (we then say that it is a participant in consensus). If the invocation of propose (v) returns a value $v^{\prime}$, we say that the invoking process decides $v^{\prime}$, or $v^{\prime}$ is decided by the consensus object. We observe now that any execution of a wait-free linearizable implementation of the consensus object type satisfies three properties:

- Agreement: no two processes decide different values.
- Validity: every decided value was previously proposed.
- Termination: Every correct process eventually decides.

Indeed, otherwise, there would be no way to linearize the execution with respect to the sequential specification in Figure 10.1 which only allows to decide on the first proposed value.

```
operation $\operatorname{propose}(v)$ :
    if $(x=\perp)$ then $x:=v$ endif;
    return $(x)$.
```

Figure 10.1.: Sequential specification of consensus

This property is implied by wait-freedom: every process taking sufficiently many steps of the consensus implementation must decide.

### 10.2. A wait-free universal construction

In this section, we show that if, in a system of $n$ processes, we can wait-free implement consensus, then we can implement any total object type.

Recall that a total object type can be represented as a tuple $\left(Q, q_{0}, O, R, \delta\right)$, where $Q$ is a set of states, $q_{0} \in Q$ is an initial state, $O$ is a set of operations, $R$ is a set of responses, and $\delta$ is a binary relation on $O \times Q \times R \times Q$, total on $O \times Q:\left(o, q, r, q^{\prime}\right) \in \delta$ if operation $o$ is applied when the object's state is $q$, then the object can return $r$ and change its state to $q^{\prime}$. Note that for non-deterministic object types, there can be multiple such pairs $\left(r, q^{\prime}\right)$ for given $o$ and $q$.

The goal of our universal construction is, given an object type $\tau=(Q, O, R, \delta)$, to provide a wait-free linearizable implementation of $\tau$ using read-write registers and atomic consensus objects.

### 10.2.1. Deterministic objects

For deterministic object types, $\delta$ can be seen as a function $O \times Q \rightarrow R \times Q$ that associates each state an operation with a unique response and a unique resulting state. The state of a deterministic object is thus determined by a sequence of operations applied to the initial state of the object. The universal construction of an object of a deterministic type is presented in Figure 10.2.

Every process $p_{i}$ maintains a local variable linearize $_{i}$ that stores a sequence of operations that are executed on the implemented object do far. Whenever $p_{i}$ has a new operation op to be executed on the implemented object it "registers" $o p$ in the shared memory using a collect object $R$. As long as $p_{i}$ finds new operations that were invoked (by $p_{i}$ itself or any other process) but not yet executed in $R$, it tries to agree on the order in which operations must be executed using the "next" consensus object $C\left[k_{i}\right]$ that was not yet accessed by $p_{i}$. If the set of operations returned $C\left[k_{i}\right]$ contains $o p, p_{i}$ deterministically computes the response of op using the specification of the implemented object and linearized $_{i}$. Otherwise, $p_{i}$ proceeds to the next consensus object $C\left[k_{i}+1\right]$.

Intuitively, this way the processes make sure that their perspectives on the evolution of the implemented object's state are mutually consistent.

## Correctness.

Lemma 17 At all times, for all processes $p_{i}$ and $p_{j}$, linearize $_{i}$ and linearized $d_{j}$ are related by containment.

Proof We observe that each linearized $_{i}$ is constructed by adding the batches of requests decided by consensus objects $C_{1}, C_{2}, \ldots$, in that order. The agreement property of consensus (applied to each of these consensus objects) implies that, for each $p_{j}$, either linearized $d_{i}$ is a prefix of linearized ${ }_{j}$, or vice versa.

Lemma 18 Every operation returns in a finite number of its steps.

Proof Suppose, by contradiction, that a process $p_{i}$ invokes an operation $o p$ and executes infinitely many steps without returning. By the algorithm, $p_{i}$ forever blocks in the repeat-until clause in lines 8 14. Thus, $p_{i}$ proposes batches of requests containing its request $\left(o p, i, s e q_{i}\right)$ to an infinite sequence of consensus instances $C_{1}, \ldots$ but the decided batches never contain $\left(o p, i, s e q_{i}\right)$. By validity of consensus, there exists a process $p_{j} \neq p_{i}$ that accesses infinitely many consensus objects. By the algorithm, before proposing a batch to a consensus object, $p_{j}$ first collects the batches currently stored by other processes in a collect object $R$. Since $p_{i}$ stores its request in $R$ and never updates it since that, eventually, every such process $p_{j}$ must collect the $p_{i}$ 's request and propose it to the next consensus object. Thus, every value returned by the consensus objects from some point on must contain the $p_{i}$ 's request-a contradiction.

```
Shared objects:
    $R$, collect object, initially $\perp$
    $C_{1}, C_{2}, \ldots$, consensus objects
Local variables, for each process $p_{i}$ :
    integer $s e q_{i}$, initially $0 \quad\left\{\right.$ the number of executed requests of $\left.p_{i}\right\}$
    integer $k_{i}$, initially $0 \quad\{$ the number of batches of executed requests $\}$
    sequence linearized $_{i}$, initially empty $\{$ the sequence of executed requests $\}$
Code for operation $o p$ executed by $p_{i}$ :
$6 \operatorname{seq}_{i}:=s e q_{i}+1$
7 R.store $\left(o p, i\right.$, seq $\left._{i}\right) \quad\{$ publish the request $\}$
repeat
    $V:=$ R.collect ()$\quad\{$ collect all current requests $\}$
    requests $:=V-\left\{\right.$ linearized $\left._{i}\right\} \quad\{$ choose not yet linearized requests $\}$
    $k_{i}:=k_{i}+1$
    decided $:=C\left[k_{i}\right]$.propose (requests)
    linearized_i = linearized_i.decided {append decided requests}
    until $\left(o p, i\right.$, seq $\left._{i}\right) \in$ linearized $_{i}$
    return the result of $\left(o p, i\right.$, seq $\left._{i}\right)$ in linearized ${ }_{i}$ using $\delta$ and $q_{0}$
```

Figure 10.2.: Universal construction for deterministic objects

Theorem 25 For each type $\tau=\left(Q, q_{0}, O, R, \delta\right)$, the algorithm in Figure 10.2 describes a wait-free linearizable implementation of $\tau$ using consensus objects and atomic registers.

Proof Let $H$ be the history an execution of the algotihm in Figure 10.2. By Lemma 17, local variables linearize $_{i}$ are prefixes of some sequence of requests linearized. Let $L$ be the legal sequential history, where operations and are ordered by linearized and responses are computed using $q_{0}$ and $\delta$. We construct $H^{\prime}$, a completion of $H$, by adding responses to the incomplete operations in $H$ that are present in $L$. By construction, $L$ agrees with the local history of $H^{\prime}$ for each process.

Now we show that $L$ respects the real-time order of $H$. Consider any two operations $o p$ and $o p^{\prime}$ such that $o p \rightarrow_{H} o p^{\prime}$ and suppose, by contradiction that $o p^{\prime} \rightarrow_{L} o p$. Let $\left(o p, i, s_{i}\right)$ and $\left(o p^{\prime}, j, s_{j}\right)$ be the corresponding requests issued by the processes invoking $o p$ and $o p^{\prime}$, respectively. Thus, in linearized, $\left(o p^{\prime}, j, s_{j}\right)$ appears before $\left(o p, i, s_{i}\right)$, i.e., before $o p$ terminates it witnesses $\left(o p^{\prime}, j, s_{j}\right)$ being decided by consensus objects $C_{1}, C_{2}, \ldots$ before $\left(o p^{\prime}, j, s_{j}\right)$. But, by our assumption, op $\rightarrow_{H} o p^{\prime}$ and, thus, $\left(o p^{\prime}, j, s_{j}\right)$ has been stored in the collect object $R$ after op has returned. But the validity property of consensus does not allow to decide a value that has not yet been proposed-a contradiction. Thus, $o p \rightarrow_{L} o p^{\prime}$, and we conclude that $H$ is linearizable.

### 10.2.2. Bounded wait-free universal construction

The implementation described in Figure 10.2 is wait-free but not bounded wait-free. A process may take arbitrarily many steps in the repeat-until clause in lines 8-14 to "catch up" with the current consensus object.

It is straightforward to turn this implementation into a bounded wait-free. Before returning an operation's response (line 15), a process posts in the shared memory the sequence of requests it has witnessed committed together with the id of the last consensus object it has accessed. On invoking an operation, a process reads the memory to get the "most recent" state on the implemented object and the "current" consensus id. Note that multiple processes concurrently invoking different operations might get the same estimate of the "current state" of the implementation. In this case only one of them may "win" in the current consensus instance and execute its request. But we argue that the requests of "lost" processes must be then committed by the next consensus object, which implies that every operation returns in a bounded number of its own steps.

The resulting implementation is presented in Figure 10.3.

To prove the following theorem, we recall that collect objects $R$ and $S$ can be implemented with $O(n)$ read-write step complexity (Chapter 8 ).

Theorem 26 For each type $\tau=\left(Q, q_{0}, O, R, \delta\right)$, the algorithm in Figure 10.3 describes a wait-free linearizable implementation of $\tau$ using consensus objects and atomic registers, where every operation returns in $O\left(n^{2}\right)$ shared-memory steps.

Proof As before, all invoked operations are ordered in the same way using a sequence of consensus objects, so the proof of linearizability is similar the one of Theorem 25.

To prove bounded wait-freedom, consider a request $(o p, i, \ell)$ issued by a process $p_{i}$. By the algorithm, $p_{i}$ first publishes its request and obtains the current state of the implemented object (line 18), denoted $k$ and $s$, respectively. Then $p_{i}$ proposes all requests it observes to be proposed but not yet committed to
consensus object $C_{k}$. If ( $o p, i, \ell$ ) is committed by $C_{k}$, then $p_{i}$ returns after taking $O(n)$ read-write steps (we assume that both collect operations involve $O(n)$ read-write steps).

Suppose now that $(o p, i, \ell)$ is not committed by $C_{k}$. Thus, another process $p_{j}$ has previously proposed to $C_{k}$ a set of requests that did not include $(o p, i, \ell)$. Thus, $p_{j}$ collected requests in line 20 before or concurrently with the store operation in which $p_{i}$ published $(o p, i, \ell)$ (line 17). Moreover, $p_{j}$ did not store the result of its operation in $S$ (line 26) before $p_{i}$ performed its collect of $S$ in line 18. The situation may repeat when $p_{i}$ proceeds to consensus object $C_{k+1}$, but only if there is another process $p_{k}$ that previously "won" $C_{k+1}$ with a sequence not containing $(o p, i, \ell)$, but has not yet stored its state in $S$. Note that $p_{k}$ must be different from $p_{j}$, otherwise, $p_{j}$ would store $k_{i}+1$ in $S$ before collecting $R$ which, as $(o p, i, \ell)$ was not found in $R$ by $p_{j}$ should have happened before of concurrently with the store in $S$ performed by $p_{i}$.

There can be at most $n-1$ processes that may prevent $p_{i}$ from "winning" consensus objects and, thus, $p_{i}$ may perform at most $n-1$ iterations in lines 19-25. As each iteration consists of $O(n)$ shared-memory steps, we get $O\left(n^{2}\right)$ step complexity for individual operations.

### 10.2.3. Non-deterministic objects

The universal construction in Figure 10.2 assumes the object type is deterministic, where for each state and each operation there exists exactly one resulting state and response pair. Thus, given a sequence of request, there is exactly one corresponding sequence of responses and state transitions.

A "dumb" way to use our universal construction is to consider any deterministic restriction of the given object type. But this may not be desirable if we expect the shared object to behave probabilistically (e.g., in randomized algorithms). A "fair" non-deterministic universal construction can be derived from the algorithm in Figure 10.3 as follows. Instead of only proposing a sequence of requests in line 22, process $p_{i}$ (using a local random number generator) proposes a sequence of responses and state transitions corresponding to a sequence of operations requests applied to the last state in linearized ${ }_{i}$. One of the proposed sequences of responses and state transitions will "win" the consensus instance and will be used to compute the new object state.

