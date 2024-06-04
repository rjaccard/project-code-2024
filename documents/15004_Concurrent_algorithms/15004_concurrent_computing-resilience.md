# 13. Resilience 

In Chapter 10, we introduced the notion of consensus and showed that consensus is a universal object.

In Chapter ?? we convinced oursleves that there is no wait-free implementation of consensus using basic reads and writes. One way to circumvent this impossibility is to relax either safety property (atomicity) or liveness property (wait-freedom) of consensus.

In this chapter we introduce two such relaxations. The Commit-Adopt abstraction that may produce different outputs at different processes under some circumstances and, thus, relaxes safety of consensus. In contrast, the Safe Agreement abstraction permits cases when a process takes infinitely many steps without an output and, thus, violates liveness of consensus.

We then show how these two abstractions can be used for building more sophisticated abstractions. First, Commit-Adopt, combined with randomization or eventual leader oracle, can be used for solving consensus. Second, we show that safe agreement enables simulations: it allows a set of $k+1$ simulators "mimic" a $k$-resilient execution of an arbitrary algorithm running on $m>k$ processes.

### 13.1. Pre-agreement with Commit-Adopt

The commit-adopt abstraction (CA), like consensus, exports one operation propose ( $v$ ) that, unlike in consensus, returns (commit, $v^{\prime}$ ) or (adopt,$v^{\prime}$ ), for $v^{\prime}$ and $v$ are in a (possibly unbounded) set of values $V$. If propose ( $v$ ) invoked by a process $p_{i}$ returns ( $a d o p t, v^{\prime}$ ), we say that $p_{i}$ adopts $v^{\prime}$. If the operation returns (commit, $v^{\prime}$ ), we say that $p_{i}$ commits on $v^{\prime}$. Intuitively, a process commits on $v^{\prime}$, when it is sure that no other process can decide on a value different from $v^{\prime}$. A process adopts $v^{\prime}$ when it suspects that another process might have committed $v^{\prime}$. Formally, CA guarantees the following properties:

(a) every returned value is a proposed value,

(b) if all processes propose the same value then no process adopts,

(c) if a process commits on a value $v$, then every process that returns adopts $v$ or commits $v$, and

(d) every correct process returns.

### 13.1.1. Wait-free commit adopt implementation

The commit-adopt abstraction can be implemented using two (wait-free) store-collect objects, $A$ and $B$, as follows. Every process $p_{i}$ first stores its input $v$ in $A$ and then collects $A$. If no value other than $v$ was found in $A, p_{i}$ stores (true $v$ ) in $B$. Otherwise, $p_{i}$ stores $(f a l s e, v)$ in $B$. If all values collected from $B$ are of the form $(t r u e, *)$, then $p_{i}$ commits on its own input value. Otherwise, if at least one of the collected values is (true, $v^{\prime}$ ), then $p_{i}$ adopts $v^{\prime}$. Intuitively, going first through $A$ guarantees that there is at most one such value $v^{\prime}$. Otherwise, if $p_{i}$ cannot commit or adopt a value from another process, it simply adopts its own input value.

```
Shared objects:
    $A, B$, store-collect objects, initially $\perp$
propose $(v)$
    est $:=v$
    A.store $(e s t)$
    $V:=A . \operatorname{collect}()$
    if all values in $V$ are est then
        B.store $(($ true, est $))$
    then
        B.store $(($ false, est $))$
    $V:=B . \operatorname{collect}()$
    if all values in $V$ are $($ true,$*)$ then
        (return (commit, est)
    else if $V$ contains $\left(\right.$ true,$\left.v^{\prime}\right)$ then
        est $:=v^{\prime}$
    (return (adopt, est)
```

Figure 13.1.: A commit-adopt algorithm

Correctness. Now we prove that the algorithm in Figure 13.1 satisfies properties (a)-(d) of commitadopt.

Property (a) follows trivially from the algorithm and the Validity property of store-collect (see Section 8.1.1): every returned value was previously proposed by some process. If all processes propose the same value, then the conditions in the clauses in lines 60 and 65 hold true, and thus, every process that returns must commit—property (b) is satisfied. Property (d) is implied by the fact that the algorithm contains only finitely many steps and every store-collect object is wait-free.

To prove (c), suppose, by contradiction, that two processes, $p_{i}$ and $p_{j}$, store two different values, $v^{\prime}$ and $v^{\prime \prime}$, respectively, equipped with flag true in $B$ (line 61). Thus, the collect operation performed by $p_{i}$ in line 59 returns only values $v$. By the up-to-dateness property of store-collect and the algorithm, $p_{i}$ has previously stored $v^{\prime}$ in $A$ (line 58). Similarly, $p_{j}$ has stored $v^{\prime \prime}$ in $A$.

Again, by the up-to-dateness property of store-collect, the A.store $\left(v^{\prime \prime}\right)$ operation performed by $p_{j}$ does not precede the $A$.collect () operation performed by $p_{i}$. (Otherwise $p_{i}$ would find $v^{\prime \prime}$ in $A$.) Thus, $\operatorname{inv}[$ A. $\operatorname{collect}()]$ by $p_{i}$ precedes resp $\left[\right.$ A.store $\left.\left(v^{\prime \prime}\right)\right]$ by $p_{j}$ in the current execution. But, by the algorithm resp $\left[\right.$ A.store $\left.\left(v^{\prime}\right)\right]$ precedes $i n v[$ A.collect ()$]$ at $p_{i}$ and, resp $\left[\right.$ A.store $\left.\left(v^{\prime \prime}\right)\right]$ precedes $i n v[$ A.collect ()$]$ at $p_{j}$. Hence, resp $\left[\right.$ A.store $\left.\left(v^{\prime}\right)\right]$ by $p_{i}$ precedes $i n v[A . \operatorname{collect}()]$ by $p_{j}$ and, by up-to-dateness of storecollect, $p_{j}$ should have found $v^{\prime}$ is $A$ - a contradiction.

Thus, no two different values can be written to $B$ with flag true. Now suppose that a process $p_{i}$ commits on $v$. If every process that returns either commits or adopts a value in line 68 , then property (c) follows from the fact that no two different values with flag true can be found in $B$. Suppose, by contradiction that some process $p_{j}$ does not find any value with flag true in $B$ (65) and adopts its own value. By the algorithm, $p_{j}$ has previously stored $\left(\right.$ false,$\left.v^{\prime \prime}\right)$ in line 63 . But, again, B.store $\left(\left(\right.\right.$ true,$\left.\left.v^{\prime}\right)\right)$ performed by $p_{i}$ does not precede $B . \operatorname{collect}()$ performed by $p_{j}$ and, thus, B.store $\left(\left(f a l s e, v^{\prime \prime}\right)\right)$ performed by $p_{j}$ precedes $B$.collect () performed by $p_{i}$. Thus, $p_{i}$ should have found $\left(\right.$ false, $\left.v^{\prime \prime}\right)$ in $B$ contradiction. Thus, if a process commits on $v^{\prime}$, no other process can commit on or adopt a different value-property (c) holds.

### 13.1.2. Using commit-adopt

Commit-adopt can be viewed as a way to establish safety in shared-memory computations.

For example, consider a protocol where every processes goes through a series of instances of commitadopt protocols, $C A_{1}, C A_{2}, \ldots$, one by one, where each instance receives a value adopted in the previous instance as an input (the initial input value for $C A_{1}$ ). One can easily see that once a value $v$ is committed in some CA instance, no value other than $v$ can ever be committed (properties (a) and (c) above). One the other hand, if at most one value is proposed to some $\mathrm{CA}$ instance, then this value must be committed by every process that takes enough steps (property (b) above).

This algorithm can be viewed as a safe version of consensus: every committed value is a proposed value and no two processes commit on different values (properties (a), (b) and (c) above). Given that every correct process goes from one CA instance to the other as long as it does not commit (property (d) above), we can boost the liveness guarantees of this protocol using external oracles.

In fact, the algorithm per se guarantees termination in every obstruction-free execution, i.e., assuming that eventually at most one process is taking steps. Moreover, we can build a consensus algorithm that terminates almost always if we allow processes to toss coins when choosing an input value for the next CA instance [10]. Also, if we allow a process to access an oracle (e.g., the $\Omega$ failure detector of [19]) that eventually elects a correct leader process, we get a live consensus algorithm.

### 13.2. Safe Agreement and the power of simulation

The interface of the safe agreement (SA) abstraction is identical to that of consensus: processes propose values and agree one of the proposed values at the end. Indeed, the BG-agreement protocol ensures the agreement and validity properties of consensus (Section ??)—every decided value was previously proposed, and no two different values are decided- but not termination. The SA-termination property only guarantees that every correct process returns if every participant every takes enough sharedmemory steps. Here a process is called a participant if it takes at least one step, and "enough" is typically $O(n)$, where $n$ is the number of processes.

### 13.2.1. Solving safe agreement

A safe agreement algorithm using two atomic snapshot objects $A$ and $B$ is given Figure 13.2. In the algorithm, a process inserts its input in the first snapshot object (line 71) and takes a scan of the inputs of other processes (line 72) . Then the process inserts the result of the scan in the second snapshot object (line 73) and waits until every participating process finishes the protocol (the repeat-until clause in lines 74- 76). Finally, the process returns the smallest value (we assume that the value set is ordered) in the smallest-size non- $\perp$ snapshot found in $B$ (containing the smallest number of non- $\perp$ values). (Recall that for every two results of scan operation, $U$ and $U^{\prime}$, we have $U \leq U^{\prime}$ or $U^{\prime} \leq U$. Thus, there indeed exists the smallest such snapshot.)

Correctness. SA-termination follows immediately from the algorithm: if every process that executed line 71 also executes line 73 , then the exit condition of the repeat-until clause in line 76 eventually holds and every correct participant terminates. If snapshot object $A$ is implemented from atomic registers (8), then it is sufficient for every participant to take $O(n)$ read-write steps to ensure that every correct participant terminates.

The validity property of consensus is also immediate: only a previously proposed value can be found in a snapshot object.

To prove the agreement property of consensus, consider the process $p_{t}$ that wrote the smallest snapshot $U_{t}$ to $B$ in line 73. First we observe that $U_{t}[t] \neq \perp$, i.e., $p_{t}$ found its own input value in the snapshot taken in line 72. Moreover, every other snapshot taken in $A$ is a superset of $U_{t}$. Thus, every other process waits until $p_{t}$ writes $U_{t}$ in line 73 before terminating. Hence, every terminated process evaluates $U_{t}$ to be the smallest snapshot in line 77 and decides on the same (smallest) value found in $U_{t}$.

```
Shared objects:
    $A, B$, snapshot objects, initially $\perp$
propose $(v)$
    est $:=v$
    A.update (est)
    $U:=A \cdot \operatorname{scan}()$
    B.update $(U)$
    repeat
        $V:=B \cdot \operatorname{scan}()$
    until for all $j:(U[j]=\perp) \vee(V[j] \neq \perp)$
        $S:=\operatorname{argmin}_{j}\{|V[j]| ; V[j] \neq \perp\}$
    (return $\min (S)$
```

Figure 13.2.: Safe agreement

### 13.2.2. BG-simulation

$B G$-simulation (BG for Elizabeth Borowsky and Eli Gafni) is a technique by which $k+1$ processes $s_{1}, \ldots, s_{k+1}$, called simulators, can wait-free simulate a $k$-resilient execution of any algorithm $A l g$ on $n$ processes $p_{1}, \ldots, p_{n}(n>k)$. The simulation guarantees that each simulated step of every process $p_{j}$ is either agreed upon by all simulators using $\mathrm{SA}$, or one less simulator participates further in the simulation for each step which is not agreed on.

If one of the simulators slows down while executing SA, the protocol's execution at other correct simulators may "block" until the slow simulator finishes the protocol. If the slow simulator is faulty, no other simulator is guaranteed to decide.

Suppose the simulation tries to trigger read-write steps of a given algorithm $A$ for $n$ simulated processes in a fair (e.g., round-robin) way. Therefore, as long there is a live simulator, at least $m-k$ simulated processes performs infinitely many steps of $A l g$ in the simulated execution, i.e., the resulting simulated execution is $k$-resilient.

## PK: define simulation here

Thus:

Theorem 39 Let $A$ be any algorithm for $n$ processes. Then $B G$-simulation allows $k+1$ simulators $(k<n)$ to trigger a $k$-resilient execution of $A$.

Theorem ?? implies that, for a large class of colorless tasks, finding a $k$-resilient solution for $n$ processes is equivalent to finding a wait-free solution for $k+1 \leq n$ processes Informally, in a solution of a colorless task, a process is free to adopt the input or output value of any other participating process. Thus, a colorless tasks can be defined as a relation between the sets of inputs and the sets of outputs.

PK: do we need to talk about tasks? Or set agreement would be enough?

Thus:

Corollary 7 Let $T$ be any colorless task. Then $T$ can be solved by $n$ processes $k$-resiliently $(k<n)$ if and only if $T$ can be solved by $k+1$ processes wait-free.

