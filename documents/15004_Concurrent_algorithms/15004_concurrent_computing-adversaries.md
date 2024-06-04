# 14. Adversaries 

Until now assumed that failures are "uniform": processes are equally probable to fail and a failure of one process does not affect reliability of the others. In real systems, however, processes may not be equally reliable. Moreover, failures may be correlated because of software or hardware features shared by subsets of processes. In this chapter, we survey recent results addressing the question of what can and what cannot be computed in systems with non-identical and non-independent failures.

### 14.1. Non-uniform failure models

A failure model describes the assumptions on where and when failures might occur in a distributed system. The classical "uniform" failure model assumes that processes fail with equal probabilities, independently of each other. This enables reasoning about the maximal number of processes that may, with a non-negligible probability, fail in any given execution of the system. It is natural to ask questions of the kind: what problems can be solved $t$-resiliently, i.e., assuming that at most $t$ processes may fail. In particular, the wait-free ( $(n-1)$-resilient, where $n$ is the number of processes) model assumes that any subset of processes may fail.

However, in real systems, processes do not always fail in the uniform manner. Processes may be unequally reliable and prone to correlated failures. A software bug makes all processes using the same build vulnerable, a router's failure may makes all processes behind it unavailable, a successful malicious attack on a given process increases the chances to compromise processes running the same software, etc. Thus, understanding how to deal with non-uniform failures is crucial.

Adversaries. Consider a system of three processes, $p, q$, and $r$. Suppose that $p$ is very unlikely to fail, and otherwise, all failure patterns are allowed. Since we only exclude executions in which $p$ fails, the set of correct processes in any given execution must belong to $\{p, p q, p r, p q r\}^{1}$.

Now we give an example of correlated failures. Suppose that $p$ and $q$ share a software component $x, p$ and $r$ share a software component $y$, and $q$ and $r$ are built atop the same hardware platform $z$ (Figure 14.1). Further, let $x, y$, and $z$ be prone to failures, but suppose that it is very unlikely that two failures occur in the same execution. Hence, the possible sets of correct processes in our system are $\{p q r, p, q, r\}$.

The notion of a generic adversary introduced by Delporte et al. [28] intends to model such scenarios. An adversary $\mathcal{A}$ is defined as a set of possible correct process subsets. E.g., the $t$-resilient adversary $\mathcal{A}_{\text {t-res }}$ in a system of $n$ processes consists of all sets of $n-t$ or more processes. We say that an execution is $\mathcal{A}$-compliant if the set of processes that are correct in that execution belongs to $\mathcal{A}$. Thus, an adversary $\mathcal{A}$ describes a model consisting of $\mathcal{A}$-compliant executions.

The formalism of adversaries [28] assumes that processes fail only by crashing, and adversaries only specify the sets of processes that may be correct in an execution, regardless of the timing of failures. Of course, this sorts out many kinds of possible adversarial behavior, such as malicious attacks or timing failures. However, it is probably the simplest model that still captures important features of non-uniform failures.[^0]

Distributed tasks. In this chapter, we focus on a class of distributed-computing problems called tasks. A task can be seen as a distributed variant of a function from classical (centralized) computing: given a distributed input (an input vector, specifying one input value for every process) the processes are required to produce a distributed output (an output vector, specifying one output value for every process), such that the input and output vectors satisfy the given task specification.

The classical theory of computational complexity theory categorizes functions based on their inherent difficulty (e.g., with respect to solving them on a Turing machine). In the distributed setting, the difficulty in solving a task also depends on the adversary we are willing to consider. There are tasks that can be trivially solved on a Turing machine, but are not solvable in the presence of some distributed adversaries. For example, the fundamental task of consensus, in which the processes must agree on one of the input values, cannot be solved assuming the 1 -resilient adversary $\mathcal{A}_{1 \text {-res }}[34,77]$. More generally, the task of $k$-set consensus [21], where every correct process is required to output an input value so that at most $k$ different values are output, cannot be solved in the presence of $\mathcal{A}_{k \text {-res }}[52,87,13]$.

Most of this chapter deals with colorless tasks (also called convergence tasks [15]). Informally, colorless tasks allow every process to adopt an input or output value from any other participating process. Colorless tasks include consensus [34], $k$-set consensus [21] and simplex agreement [53].

The relative power of an adversary. This chapter primarily addresses the following question. Given a task $T$ and an adversary $\mathcal{A}$, is $T$ solvable in the presence of $\mathcal{A}$ ?

Intuitively, the more sets an adversary comprises, the more executions our system may expose, and, thus, the more powerful is the adversary in "disorienting" the processes. In this sense, the wait-free adversary $\mathcal{A}_{w f}=\mathcal{A}_{n-1-\text { res }}$ is the most powerful adversary, since it describes the set of all possible executions

In contrast, a "singleton" adversary $\mathcal{A}=\{S\}$ that consists of only one set $S \subseteq \mathcal{P}$ is very weak. For example, we can use any process in $S$ as the "leader" that never fail. This allows us to solve consensus or implement any sequential data type $[48]$.

But in general, there are exponentially many adversaries defined for $n$ processes that are not related by containment. Therefore, it is difficult to say a priori which of two given adversaries is stronger.

Superset-closed adversaries. We start with recalling the model of dependent failures proposed by Junqueira and Marzullo [62], defined in terms of cores and survivor sets. In brief, a survivor set is a minimal subset of processes that can be the set of correct processes in some execution, and a core is a minimal set of processes that do not all fail in any execution.

We show that, in fact, the formalism of [62] describes a special class of superset-closed adversaries: every superset of an element of such an adversary $\mathcal{A}$ is also an element of $\mathcal{A}$. The minimal elements of
$\mathcal{A}$ (no subset of which are in $\mathcal{A}$ ) are the survivor sets of the resulting model.

It turns out that the power of a superset-closed adversary $\mathcal{A}$ in solving colorless tasks is precisely characterized by the size of its minimal core, i.e., the minimal-cardinality set of processes that cannot all fail in any $\mathcal{A}$-compliant execution. A superset-closed adversary with minimal core size $c$ allows for solving a colorless task $T$ if and only if $T$ can be solved $(c-1)$-resiliently. In particular, if $c=1$, then any task can be solved in the presence of $\mathcal{A}$, and if $c=n$, then $\mathcal{A}$ only allows for solving waitfree solvable tasks. Thus, all superset-closed adversaries can be categorized in $n$ classes, based on their minimal core sizes.

We present two ways of deriving this result: first, using the elements of modern topology (proposed by Herlihy and Rajsbaum [51]) and second, through shared-memory simulations (proposed by Gafni and Kuznetsov [40]).

Characterizing generic adversaries. The dependent-failure formalism of [62] is however not expressive enough to capture the task solvability in generic non-uniform failure models. It is easy to construct an adversary that has the minimal core size $n$ but allows for solving tasks that can cannot be wait-free solved. One example is the "bimodal" adversary $\{p q r, p, q, r\}$ (Figure 14.1) that allows for solving 2 -set consensus.

Therefore, to characterize the power of a generic adversary, we need a more sophisticated criterion than the minimal core size. Surprisingly, such a criterion, that we call set consensus power, is not difficult to find. Suppose that we can partition an adversary $\mathcal{A}$ into $k$ sub-adversaries, each powerful enough to solve consensus. We conclude that $\mathcal{A}$ allows for solving $k$-set consensus: simply run $k$ consensus algorithms in parallel, each assuming a distinct sub-adversary. Moreover, we show that the set consensus power of $\mathcal{A}$, defined as the minimal such number of sub-adversaries, precisely characterizes the power of $\mathcal{A}$ in solving colorless tasks.

Therefore, generic adversaries defined on $n$ processes can still be split into $n$ equivalence classes. Each class $j$ consists of adversaries of set consensus power $j$ that agree on the set of colorless tasks they allow for solving: namely, tasks that can be solved $(j-1)$-resiliently and not $j$-resiliently. In particular, class $n$ contains adversaries that only allow for solving tasks that can be solved wait-free, and class 1 allows for solving consensus and, thus, any task.

In this chapter, we discuss several approaches to model non-uniform failures: dependent failure model of Junqueira and Marzullo [62], adversaries of Delporte et alii [28], and asymmetric progress conditions by Imbs et alii [58].

Then we present a complete characterization of superset-closed adversaries. The result is first shown using elements of combinatorial topology [51] and then through simple shared-memory simulations [40].

We then characterize generic (not necessarily superset-closed) adversaries using the notion of set consensus power and relate it with the disagreement power proposed by Delporte et alii [28].

We conclude with a brief overview of open questions, primarily related to solving generic (not necessarily colorless) tasks in the presence of generic (not necessarily superset-closed) adversaries.

### 14.2. Background

In this section, we briefly state our system model and recall the notion of a distributed task and two important constructs used in this chapter: Commit-Adopt and BG-simulation.

### 14.2.1. Model

We consider a system $\Pi$ of $n$ processes, $p_{1}, \ldots, p_{n}$, that communicate via reading and writing in the shared memory. We assume that the system is asynchronous, i.e., relative speeds of the processes are
unbounded. Without loss of generality, we assume that processes share an atomic snapshot memory [1], where every process may update its dedicated element and take atomic snapshot of the whole memory.

A process may only fail by crashing, and otherwise it must respect the algorithm it is given. A correct process never crashes.

### 14.2.2. Tasks

In this chapter, we focus on a specific class of distributed computing problems, called tasks [53]. In a distributed task [53], every participating process starts with a unique input value and, after the computation, is expected to return a unique output value, so that the inputs and the outputs across the processes satisfy certain properties. More precisely, a task is defined through a set $\mathcal{I}$ of input vectors (one input value for each process), a set $\mathcal{O}$ of output vectors (one output value for each process), and a total relation $\Delta: \mathcal{I} \mapsto 2^{\mathcal{O}}$ that associates each input vector with a set of possible output vectors. An input $\perp$ denotes a not participating process and an output value $\perp$ denotes an undecided process.

For example, in the task of $k$-set consensus, input values are in $\{\perp, 0, \ldots, k\}$, output values are in $\{\perp, 0, \ldots, k\}$, and for each input vector $I$ and output vector $O,(I, O) \in \Delta$ if the set of non- $\perp$ values in $O$ is a subset of values in $I$ of size at most $k$. The special case of 1-set consensus is called consensus [34].

We assume that every process runs a full-information protocol: initially it writes its input value and then alternates between taking snapshots of the memory and writing back the result of its latest snapshots. After a certain number of such asynchronous rounds, a process may gather enough state to decide, i.e., i.e., to produce an irrevocable non- $\perp$ output value.

In colorless task (also called convergence tasks [15]) processes are free to use each others' input and output values, so the task can be defined in terms of input and output sets instead of vectors. ${ }^{2}$ The $k$-set consensus task is colorless.

Note that to solve a colorless task, it is sufficient to find a protocol (a decision function) that allows just one process to decide. Indeed, if such a protocol exists, we can simply convert it into a protocol that allows every correct process to decide: every process simply applies the decision function to the observed state of any other process and adopts the decision.

### 14.2.3. The Commit-Adopt protocol

One tool extensively used in this chapter is the commit-adopt abstraction (CA) [36]. CA exports one operation propose $(v)$ that returns $\left(\right.$ commit,$\left.v^{\prime}\right)$ or $\left(a d o p t, v^{\prime}\right)$, for $v^{\prime}, v \in V$, and guarantees that

(a) every returned value is a proposed value,

(b) if only one value is proposed then this value must be committed,

(c) if a process commits on a value $v$, then every process that returns adopts $v$ or commits $v$, and

(d) every correct process returns.

The CA abstraction can be implemented wait-free [36]. Moreover, CA can be viewed as a way to establish safety in shared-memory computations.

For example, consider a protocol where every processes goes through a series of instances of commitadopt protocols, $C A_{1}, C A_{2}, \ldots$, one by one, where each instance receives a value adopted in the previous instance as an input (the initial input value for $C A_{1}$ ). One can easily see that once a value $v$ is[^1]committed in some CA instance, no value other than $v$ can ever be committed (properties (a) and (c) above). One the other hand, if at most one value is proposed to some $\mathrm{CA}$ instance, then this value must be committed by every process that takes enough steps (property (b) above).

This algorithm can be viewed as a safe version of consensus: every committed value is a proposed value and no two processes commit on different values (properties (a), (b) and (c) above). Given that every correct process goes from one CA instance to the other as long as it does not commit (property (d) above), we can boost the liveness guarantees of this protocol using external oracles.

In fact, the algorithm per se guarantees termination in every obstruction-free execution, i.e., assuming that eventually at most one process is taking steps. Moreover, we can build a consensus algorithm that terminates almost always if we allow processes to toss coins when choosing an input value for the next CA instance [10]. Also, if we allow a process to access an oracle (e.g., the $\Omega$ failure detector of [19]) that eventually elects a correct leader process, we get a live consensus algorithm.

### 14.2.4. The BG-simulation technique.

Another important tool used in this chapter is $B G$-simulation $[13,15]$. BG-simulation guarantees that each simulated step of every process $p_{j}$ is either agreed upon by all simulators, or one less simulator participates further in the simulation for each step which is not agreed on.

The central building block of the simulation is the BG-agreement protocol. BG-agreement reminds consensus: processes propose values and agree one of the proposed values at the end. Indeed, the BGagreement protocol ensures safety of consensus-every decided value was previously proposed, and no two different values are decided - but not liveness. If one of the simulators slows down while executing BG-agreement, the protocol's execution at other correct simulators may "block" until the slow simulator finishes the protocol. If the slow simulator is faulty, no other simulator is guaranteed to decide.

Suppose the simulation tries to promote $m>k$ simulated processes in a fair (e.g., round-robin) way. As long there is a live simulator, at least $m-k$ simulated processes performs infinitely many steps of Alg in the simulated execution.

Recently the technique of BG-simulation was extended to show that any colorless task that can be solved assuming the $(k-1)$-resilient adversary can also be solved using read-write registers and $k$-set consensus objects [37].

### 14.3. Non-uniform failures in shared-memory systems

In this section, we overview several approaches to model non-uniform failures: dependent failure model of Junqueira and Marzullo [62], adversaries of Delporte et alii [28], and asymmetric progress conditions by Imbs et alii $[58]$ and Taubenfeld $[91]$.

### 14.3.1. Survivor sets and cores

Junqueira and Marzullo $[63,62]$ proposed to model non-uniform failures using the language of survivor sets and cores. A survivor set $S \subseteq \Pi$ if a set of processes such that:

(a) in some execution, $S$ is the set of correct processes, and

(b) $S$ is minimal: for every proper subset $S^{\prime}$ of $S$, there is no execution in which $S^{\prime}$ is the set of correct processes.

A collection $\mathcal{S}$ of survivor sets describes a system such that the set of correct processes in every execution contains a set in $\mathcal{S}$.

Respectively, a core $C$ is a set of processes such that:

(a) in every execution, some process in $C$ is correct, and

(b) $C$ is minimal: for every proper subset $C^{\prime}$ of $C$, there is an execution in which every process in $C^{\prime}$ fails.

Thus, a core is a minimal set of processes that cannot be all faulty in any execution of our system. Note that the set of cores is unambiguously determined by the set of survivor sets.

A core is actually a minimal hitting set of the set system built of survivor sets, and a core of smallest size is a corresponding minimum hitting set. Determining minimum hitting set of a set system is known to be NP-complete [64].

The language of cores $[63,62]$ proved to be convenient in understanding the ability of a system with non-uniform failures to solve consensus or build a fault-tolerant replicated storage.

### 14.3.2. Adversaries

A more general way to model non-uniform failures was proposed by Delporte et al. [28]. Formally, an adversary defined for a set of processes $\Pi$ is a non-empty set of process subsets $\mathcal{A} \subseteq 2^{\Pi}$. We say that an execution is $\mathcal{A}$-compliant if the correct set, i.e., the set of correct processes, in that execution belongs to $\mathcal{A}$. Thus, assuming an adversary $\mathcal{A}$, we only consider the set of $\mathcal{A}$-compliant executions. ${ }^{3}$ By convention, we assume that in every execution, at least one process is correct, i.e., no adversary contains $\emptyset$.

Given a task $T$ and an adversary $\mathcal{A}$, we say that $T$ is $\mathcal{A}$-resiliently solvable if there is a protocol such that in every execution, the outputs match the inputs with respect to the specification of $T$, and in every $\mathcal{A}$-compliant execution, each correct process eventually produces an output.

It is easy to see that the language of survivor sets of [62] describes a special class of superset-closed adversaries. Formally, the set $\mathcal{S C}$ of superset-closed adversaries consists of all $\mathcal{A}$ such that for all $S \in \mathcal{A}$ and $S \subseteq S^{\prime} \subseteq \Pi$, we have $S^{\prime} \in \mathcal{A}$.

For example, consider the $t$-resilient adversary $\mathcal{A}_{t \text {-res }}=\{S \subseteq \Pi,|S| \geq n-t\}$. By definition, $\mathcal{A}_{t-\text {-res }} \in \mathcal{S C}$. The survivor sets of $\mathcal{A}_{t \text {-res }}$ are all sets of $n-t$ processes, and the cores are all sets of $t+1$ processes. The $(n-1)$-resilient adversary $\mathcal{A}_{W F}=\mathcal{A}_{n-1-\text { res }}$ is also called wait-free. An $\mathcal{A}_{W F^{-}}$ resilient task solution must ensure that every process obtains an output in a finite number of its own steps, regardless of the behavior of the rest of the system.

Another example $\mathcal{A}_{L_{p}}=\{S \subseteq \Pi \mid p \in S\} \in \mathcal{S C}$ describing a system in which $p$ never fails. $\mathcal{A}_{L_{p}}$ has one survivor set $\{p\}$ and one core $\{p\}$. Intuitively, $p$ may then act as a correct leader in a consensus protocol. Thus, every task can be solved in the presence of $\mathcal{A}_{L_{p}}$ [48].

The $k$-obstruction-free adversary $\mathcal{A}_{k \text {-OF }}$ is defined as $\{S \subseteq \Pi|1 \leq| S \mid \leq k\}$. In particular, $\mathcal{A}_{O F}=\mathcal{A}_{1-O F}$ allows for solving consensus [33]. Clearly, $\mathcal{A}_{k-O F}$ for $1 \leq k<n$ is not in $\mathcal{S C}$.

The "bimodal" adversary $\{p q r, p, q, r\}$ (Figure 14.1) is not in $\mathcal{S C}$ either: it contains the singleton $p$ but not its supersets $p q$ and $p r$.

### 14.3.3. Failure patterns and environments

An adversary is in fact a special case of a failure environment introduced by Chandra et alii [19]. An environment $\mathcal{E}$ is a set of failure patterns. For a given run, a failure pattern $F$ is a map that associates[^2]each time value $t \in \mathbb{T}$ with a set of processes crashed by time $t$. The set of correct processes, denoted $\operatorname{correct}(F)$ is thus defined as $\Pi-\cup_{t \in \mathbb{T}} F(t)$.

Since an adversary $\mathcal{A}$ only defines sets of correct processes and does not specify the timing of failures, it can be viewed as a specific environment $\mathcal{E}_{\mathcal{A}}$ that is closed under changing the timing of failures. More precisely, $\mathcal{E}_{\mathcal{A}}=\{F \mid \operatorname{correct}(F) \in \mathcal{A}\}$. Clearly, if $F \in \mathcal{E}_{\mathcal{A}}$ and $\operatorname{correct}(F)=\operatorname{correct}\left(F^{\prime}\right)$, then $F^{\prime} \in \mathcal{E}_{\mathcal{A}}$.

Thus, we can rephrase the statement "task $T$ can be solved $\mathcal{A}$-resiliently" as "task $T$ can be solved in environment $\mathcal{E}_{\mathcal{A}}$ ". It is shown in [39] that, with respect to colorless tasks, all environments can be split into $n$ equivalence classes, and each class $j$ agrees on the set of tasks it can solve: namely, tasks that can be solved $(j-1)$-resiliently and not $j$-resiliently. Therefore, by applying [39], we conclude that each adversary belongs to one of such equivalence class. However, this characterization does not give us an explicit algorithm to compute the class to which a given adversary belongs.

### 14.3.4. Asymmetric progress conditions

Imbs et alii [58] introduced asymmetric progress conditions that allow us to specify different progress guarantees for different processes. Informally, for sets of processes $X$ and $Y, X \subseteq Y \subseteq \Pi,(X, Y)$ liveness guarantees that every process in $X$ makes progress regardless of other processes (wait-freedom for processes in $X$ ) and every process in $Y-X$ makes progress if it is eventually the only process in $Y-X$ taking steps (obstruction-freedom for processes in $Y-X$ ).

With respect to solving colorless tasks, it is easy to represent $(X, Y)$-liveness using the formalism of adversaries. The equivalent adversary $\mathcal{A}_{X, Y}$ consists of all subsets of $\Pi$ that intersect with $X$ and all sets $\left\{p_{i}\right\} \cup S$ such that $p_{i} \in Y-X$ and $S \subseteq \Pi-Y$. It is easy to see that a colorless task is (read-write) solvable assuming $(X, Y)$-liveness if and only if it is solvable in the presence of $\mathcal{A}_{X, Y}$.

Taubenfeld [91] introduced a refined condition that associates each process $p_{i}$ with a set $\mathcal{P}_{i}$ of process subsets (each containing $p_{i}$ ). Then $p_{i}$ is expected to make progress (e.g., output a value in a task solution) only if the current set of correct processes is in $\mathcal{P}_{i}$. Similarly, with respect to the question of solvability of colorless tasks, every such progress condition can be modeled as an adversary, defined simply as the union $\cup_{i} \mathcal{P}_{i}$.

### 14.4. Characterizing superset-closed adversaries

Intuitively, the size of a smallest-cardinality core of an adversary $\mathcal{A}$, denoted $\operatorname{csize}(\mathcal{A})$, is related to its ability to "confuse" the processes (preventing them from agreement). Indeed, since in every execution, at least one process in a minimal core $C$ is correct, we can treat $C$ as a collection of leaders. But for a superset-closed adversary, every non-empty subset of $C$ can be the set of correct processes in $C$ in some execution. Therefore, intuitively, the system behaves like a wait-free system on $c=|C|$ processes, where $c$ quantifies the "degree of disagreement" that we can observe among all the processes in the system.

In this section, we show that $\operatorname{csize}(\mathcal{A})$ precisely captures the power of $\mathcal{A}$ with respect to colorless tasks. We overview two approaches to address this question, each interesting in its own right: using combinatorial topology and using shared-memory simulations.

### 14.4.1. A topological approach

Herlihy and Rajsbaum [51] derived a characterization of superset-closed adversaries using the Nerve Theorem of modern combinatorial topology [11]. A set of finite executions is modeled as a simplicial complex, a geometric (or combinatorial) structure where each simplex models a set of local states (views)
of the processes resulting after some execution. This allows for reasoning about the power of a model using topological properties (e.g., connectivity) of simplicial complexes it generates. ${ }^{4}$

The model of [51] is based on iterated computations: each process $p_{i}$ proceeds in (asynchronous) rounds, where every round $r$ is associated with a shared array of registers $M[r, 1], \ldots, M[r, n]$. When $p_{i}$ reaches round $r$, it updates $M[r, i]$ with its current view and takes an atomic snapshot of $M[r,$.$] . In$ the presence of a superset-closed adversary $\mathcal{A}$, the set of processes appearing in a snapshot should be an element of $\mathcal{A}$. We call the resulting set of executions the $\mathcal{A}$-compliant iterated model.

Naturally, given an adversary $\mathcal{A}$, it is easy to implement an iterated model with desired properties in the classical (non-iterated) shared memory model. To implement a round of the iterated model, every process writes its value in the memory and takes atomic snapshots until all processes in some survivor set (minimal element in $\mathcal{A}$ ) are observed to have written their values. The result of this snapshot is then returned. In an $\mathcal{A}$-compliant execution, this allows for simulating infinitely many iterated rounds.

Surprisingly, we can also use the $\mathcal{A}$-compliant iterated model to simulate an $\mathcal{A}$-compliant execution in the read-write model where some participating set of processes in $\mathcal{A}$ takes infinitely many steps (please check the wonderful simulation algorithm proposed recently by Gafni and Rajsbaum [41]). In particular, for the wait-free adversary $\mathcal{A}_{W F}$, the simulation is non-blocking: at least one participating process accepts infinitely many steps in the simulated execution.

Note that if the simulated $\mathcal{A}$-compliant execution is used for an $\mathcal{A}$-resilient protocol solving a given task, then we are guaranteed that at least one process obtains an output. But to solve a colorless task it is sufficient to produce an output for one participating process (all other participants may adopt this output). Thus:

Theorem 40 [41] Let $\mathcal{A}$ be a superset-closed adversary. A colorless task can be solved in the $\mathcal{A}$ compliant iterated model if and only if it can be solved in the $\mathcal{A}$-compliant model.

This result allows us to apply the topological formalism as follows. The set of $r$-round executions of the $\mathcal{A}$-compliant iterated model applied to an initial simplex $\sigma$ generates a protocol complex $\mathcal{K}_{r}(\sigma)$. By a careful reduction to the Nerve Theorem [11], $\mathcal{K}_{r}(\sigma)$ can be shown to be $(c-2)$-connected, i.e., $\mathcal{K}_{r}(\sigma)$ contains no "holes" in dimensions $c-2$ or less (any $(c-2)$-dimensional sphere can be continuously contracted to a point). The Nerve theorem establishes the connectivity of a complex from the connectivity of its components.

Roughly, the argument of [51] is built by induction on $n$, the number of processes. For a given adversary $\mathcal{A}$ on $n$ processes with the minimal core size $c$, the $\mathcal{A}$-compliant protocol complex $\mathcal{K}_{r}(\sigma)$ can be represented as a union of protocol complexes, each corresponding to a sub-adversary of $\mathcal{A}$ on $n-1$ processes with core size $c-1$. By induction, each of these sub-adversaries is at least $(c-3)$-connected. Applying the Nerve theorem, we derive that $\mathcal{K}_{r}(\sigma)$ is $(c-2)$-connected. The base case $n=1$ and $c=1$ is trivial, since every non-empty complex is, by definition, $(-1)$-connected.

Thus, $\mathcal{K}_{r}(\sigma)$ is $(c-2)$-connected. Hence, no task that cannot be solved $(c-1)$-resiliently, in particular $(c-1)$-set consensus, allows for an $\mathcal{A}$-resilient solution [53].

Using the characterization of [53], we can reduce the question of $\mathcal{A}$-resilient solvability of a colorless task $T=(\mathcal{I}, \mathcal{O}, \Delta)$ to the existence of a continuous map $f$ from $\left|s k e l^{c-1}(\mathcal{I})\right|$, the Euclidean embedding of the ( $c-1$ )-skeleton (the complex of all simplexes of dimension $c-1$ and less) of the input complex $\mathcal{I}$, to $|\mathcal{O}|$, the Euclidean embedding of the output complex $\mathcal{O}$, such that $f$ is carried by $\Delta$, i.e., $f(\sigma) \subseteq$ $\Delta(\sigma)$. Indeed, the fact that of $\mathcal{K}_{r}(\sigma)$ is $(c-2)$-connected (and thus $d$-connected for all $0 \leq d \leq c-2$ ) implies that every continuous map from $d$-sphere of $\mathcal{K}_{r}(\sigma)$ extends to the $(d+1)$-disk, for $0 \leq d \leq c-2$.[^3]

Intuitively, we can thus inductively construct a continuous map from $\left|s k e l^{c-1}(\mathcal{I})\right|$ to $|\mathcal{O}|$, starting from any map sending a vertex of $\mathcal{I}$ to a vertex of $\mathcal{O}$ (for $d=0$ ).

On the other hand, it is straightforward to construct an $\mathcal{A}$-resilient protocol solving a colorless task $T$, given a continuous map from the $(c-1)$-skeleton of the input complex of $T$ to the output complex of $T$. Thus:

Theorem 41 [51] An adversary $\mathcal{A} \in \mathcal{S C}$ with the minimal core size $c$ allows for solving a colorless task $T=(\mathcal{I}, \mathcal{O}, \Delta)$ if and only if there is a continuous map from $\mid$ skel ${ }^{c-1}(\mathcal{I}) \mid$ to $|\mathcal{O}|$ carried by $\Delta$.

Therefore, two adversaries in $\mathcal{A}, \mathcal{B} \in \mathcal{S C}$ with the same minimal core size $c$ agree on the set of tasks they allow for solving, which is exactly the set of tasks that can be solved $(c-1)$ )-resiliently (since $\left.\operatorname{csize}\left(\mathcal{A}_{(c-1)-\text { res }}\right)=c\right)$.

### 14.4.2. A simulation-based approach

It is comparatively straightforward to characterize superset-closed adversaries using classical BG-simulation [13, 15], and we present a complete proof below.

Theorem 42 [38] Let $\mathcal{A}$ be a superset-closed adversary. A colorless task $T$ is $\mathcal{A}$-resiliently solvable if and only if $T$ is $(c-1)$-resiliently solvable, where $c$ is the minimal core size of $\mathcal{A}$.

Proof Let a colorless task $T$ be $(c-1)$-resiliently solvable, and let $P_{c}$ be the corresponding algorithm. Let $C=\left\{q_{1}, \ldots, q_{c}\right\}$ be a minimal-cardinality core of $\mathcal{A}(|C|=c)$.

Let the processes in $C$ BG-simulate the algorithm $P_{c}$ running on all processes in $\Pi$. Here each simulator $q_{i}$ tries to use its input value of task $T$ as an input value of every simulated process $[13,15]$. Since $C$ is a core of $\mathcal{A}$, in every $\mathcal{A}$-compliant execution, at most $c-1$ simulators may fail. Since a faulty simulator results in at most one faulty simulated process, the produced simulated execution is $(c-1)$-resilient. Since $P_{c}$ gives a $(c-1)$-resilient solution of $T$, at least one simulated process must eventually decide in the simulated execution. The output value is then adopted by every correct process. Moreover, the decided value is based on the "real" inputs of some processes. Since $T$ is colorless, the decided values are correct with respect to the input values and, thus, we obtain an $\mathcal{A}$-resilient protocol to solve $T$.

For the other direction, suppose, by contradiction that there exists an $\mathcal{A}$-resilient protocol $P_{\mathcal{A}}$ to solve a colorless task $T$, but $T$ is not possible to solve $(c-1)$-resiliently.

We claim that $\mathcal{A}_{(c-1) \text {-res }} \subseteq \mathcal{A}$, i.e., each $(c-1)$-resilient execution is $\mathcal{A}$-compliant. Suppose otherwise, i.e., some set $S$ of $n-c+1$ processes is not in $\mathcal{A}$. Since $\mathcal{A}$ is superset-closed, no subset of $S$ is in $\mathcal{A}$ (otherwise, $S$ would be in $\mathcal{A}$ ). No process in $S$ belongs to any set in $\mathcal{A}$, thus, the smallest core of $\mathcal{A}$ must be a subset of $\Pi-S$. But $|\Pi-S|=c-1-$ a contradiction with the assumption that the size of a minimal cardinality core of $\mathcal{A}$ is $c$.

Thus, every $(c-1)$-resilient execution is also $\mathcal{A}$-compliant, which implies that $P_{\mathcal{A}}$ is in fact a $(c-1)$ resilient solution to $T$-a contradiction with the assumption that $T$ is not $(c-1)$-resiliently solvable.

$\square_{\text {Theorem }} 42$

Theorem ?? implies that adversaries in $\mathcal{S C}$ can be categorized into $n$ equivalence classes, $\mathcal{S C}_{1}, \ldots, \mathcal{S C}_{n}$, where class $\mathcal{S C}_{k}$ corresponds to cores of size $k$. Two adversaries that belong to the same class $\mathcal{S C} \mathcal{C}_{k}$ agree on the set of colorless tasks they are able to solve, and it is exactly the set of all colorless task that can be solved $(k-1)$-resiliently.

### 14.5. Measuring the Power of Generic Adversaries

Let us come back to the "bimodal" adversary $\mathcal{A}_{B M}=\{p q r, p, q, r\}$ (Figure 14.1). Its only core is $\{p, q, r\}$. Does it mean that $\mathcal{A}_{B M}$ only allows for solving trivial (wait-free solvable) tasks? Not really: by splitting $\mathcal{A}_{B M}$ in two sub-adversaries $\mathcal{A}_{F F}=\{p q r\}$ and $\mathcal{A}_{O F}=\{p, q, r\}$ and running two consensus algorithms in parallel, one assuming no failures $\left(\mathcal{A}_{F F}\right)$ and one assuming that exactly one process is correct $\left(\mathcal{A}_{O F}\right)$, gives us a solution to 2 -set consensus.

### 14.5.1. Solving consensus with $\mathcal{A}_{B M}$

But can we solve more in the presence of $\mathcal{A}_{B M}$ ? E.g., is there a protocol Alg that solves consensus $\mathcal{A}_{B M}$-resiliently? We derive that the answer is no by showing how processes, $s_{0}$ and $s_{1}$, can wait-free solve consensus through simulating an $\mathcal{A}_{B M}$-compliant execution of $\mathrm{Alg}$. Initially, the two processes act as BG simulators $[13,15]$ trying to simulate an execution of $\mathrm{Alg}$ on all three processes $p, q$, and $r$. When a simulator $s_{i}(i=0,1)$ finds out that the simulation of some step is blocked (which means that the other simulator $s_{1-i}$ started but has not yet completed the corresponding instance of BG-agreement), $s_{i}$ switches to simulating a solo execution of the next process (in the round-robin order) in $\{p, q, r\}$. If the blocked simulation eventually resolves ( $s_{1-i}$ finally completes the instance of BG-agreement), then $s_{i}$ switches back to simulating all $p, q$ and $r$.

If no simulator blocks a simulated step forever, the simulated execution contains infinitely many steps of every process, i.e., the set of correct processes in it is $\{p, q, r\}$. Otherwise, eventually some simulated process forever runs in isolation and the set of correct processes in the simulated execution is $\{p\},\{q\}$, or $\{r\}$. In both cases, the simulated execution of $A l g$ is $\mathcal{A}_{B M}$-compliant, and the algorithm must output a value, contradicting $[34,77]$. This argument can be easily extended to show that $\mathcal{A}_{B M}$ cannot allow for solving any colorless task that cannot be solved 1-resiliently.

### 14.5.2. Disagreement power of an adversary

Thus, we need a more sophisticated criterion to evaluate the power of a generic adversary $\mathcal{A}$. Delporte et alii [28] proposed to evaluate the "disorienting strength" of an adversary $\mathcal{A}$ via its disagreement power.

Formally, the disagreement power of an adversary $\mathcal{A}$ is the largest $k$ such that $k$-set consensus cannot be solved in the presence of $\mathcal{A}$.

It is shown in [28] that adversaries of the same disagreement power agree on the sets of colorless task they allow for solving. The result is derived via a three-stage simulation. First, it is shown how an adversary can simulate any dominating adversary, where the domination is defined through an involved recursive inclusion property. Second, it is shown that every adversary $\mathcal{A}$ that does not dominate the $k$-resilient adversary ${ }^{5}$ is strong enough to implement the anti $-\Omega_{k}$ failure detector that, in turn, can be used to solve $k$-set consensus [103]. Finally, it is shown that vector- $\Omega_{k}$ (a failure detector equivalent to anti- $\Omega_{k}$ ) can be used to solve any colorless task that can be solved $k$-resiliently. Thus, the largest $k$ such that $k$-set consensus cannot be solved $\mathcal{A}$-resiliently indeed captures the power of $\mathcal{A}$.

The characterization of adversaries proposed in [28] does not give a direct way of computing the disagreement power of an adversary $\mathcal{A}$ and it does not provide a direct $\mathcal{A}$-resilient algorithm to solve a colorless task $T$, when $T$ is $\mathcal{A}$-resiliently solvable.

In the rest of this section, we give a simple algorithm to compute the disagreement power of an adversary. For convenience, we introduce notion of set consensus power, i.e., the smallest $k$ such that $k$-set consensus can be solved in the presence of $\mathcal{A}$. Clearly, the disagreement power of $\mathcal{A}$ is the set consensus power of $\mathcal{A}$ minus 1 .[^4]

### 14.5.3. Defining setcon

Let $\mathcal{A}$ be an adversary and let $S \subseteq P$ be any subset of processes. Then $\mathcal{A}_{S}$ denotes the adversary that consists of all elements of $\mathcal{A}$ that are subsets of $S$ (including $S$ itself if $S \in \mathcal{A}$ ). E.g., for $\mathcal{A}=$ $\{p q, q r, q, r\}$ and $S=q r, \mathcal{A}_{S}=\{q r, q, r\}$. For $S \in \mathcal{A}$ and $a \in S$, let $A_{S, a}$ denote the adversary that consists of all elements of $\mathcal{A}_{S}$ that $d o$ not include $a$. E.g., for $\mathcal{A}=\{p q, q r, q, r\}, S=q r$, and $a=q$, $\mathcal{A}_{S, a}=\{r\}$.

Now we define a quantity denoted $\operatorname{setcon}(\mathcal{A})$, which we will show to be the set consensus power of $\mathcal{A}$. Intuitively, our goal is to split $\mathcal{A}$ into the minimal number $k$ of sub-adversaries, such that every subadversary allows for solving consensus. Then $\mathcal{A}$ allows for solving $k$-set consensus, but not $(k-1)$-set consensus (otherwise, $k$ would not be minimal).

$\operatorname{setcon}(\mathcal{A})$ is defined as follows:

- If $\mathcal{A}=\emptyset$, then $\operatorname{setcon}(\mathcal{A})=0$
- Otherwise, $\operatorname{setcon}(\mathcal{A})=\max _{S \in \mathcal{A}} \min _{a \in S} \operatorname{setcon}\left(\mathcal{A}_{S, a}\right)+1$

Thus, $\operatorname{setcon}(\mathcal{A})$, for a non-empty adversary $\mathcal{A}$, is determined as $\operatorname{setcon}\left(\mathcal{A}_{\bar{S}, \bar{a}}\right)+1$ where $\bar{S}$ is an element of $\mathcal{A}$ and $\bar{a}$ is a process in $\bar{S}$ that "max-minimize" $\operatorname{setcon}\left(\mathcal{A}_{S, a}\right)$. Note that for $\mathcal{A} \neq \emptyset$, $\operatorname{setcon}(\mathcal{A}) \geq 1$.

We say that $S \in \mathcal{A}$ is proper if it is not a subset of any other element in $\mathcal{A}$. Let $\operatorname{proper}(\mathcal{A})$ denote the set of proper elements in $\mathcal{A}$. Note that since for all $S^{\prime} \subset S, \min _{a \in S^{\prime}} \operatorname{setcon}\left(\mathcal{A}_{S^{\prime}, a}\right) \leq$ $\min _{a \in S} \operatorname{setcon}\left(\mathcal{A}_{S, a}\right)$, we can replace $S \in \mathcal{A}$ with $S \in \operatorname{proper}(\mathcal{A})$.

### 14.5.4. Calculating $\operatorname{setcon}(\mathcal{A}):$ examples

Consider an adversary $\mathcal{A}=\{p q r, p q, p r, p, q, r\}$. It is easy to see that $\operatorname{setcon}(\mathcal{A})=2$ : for $S=p q r$ and $a=p$, we have $\mathcal{A}_{S, p}=\{q, r\}$ and $\operatorname{set} \operatorname{con}\left(\mathcal{A}_{S, a}\right)=1$. Thus, we decompose $\mathcal{A}$ into two subadversaries $\{p q r, p q, p r, p\}$ and $\{q, r\}$, each strong enough to solve consensus (Figure 14.2). Intuitively, in an execution where the correct set belongs to $\mathcal{A}-\mathcal{A}_{S, a}=\{p q r, p q, p r, p\}$, process $p$ can act as a leader for solving consensus. If the correct set belongs to $\mathcal{A}_{S, a}=\{q, r\}$ (either $q$ or $r$ eventually runs solo) then $q$ and $r$ can solve consensus using an obstruction-free algorithm. Running the two algorithms in parallel, we obtain a solution to 2 -set consensus. The reader can easily verify that any other choice of $a \in p q r$ results in three levels of decomposition.

As another example, consider the $t$-resilient adversary $\mathcal{A}_{t \text {-res }}=\{S \subseteq \Pi,|S| \geq n-t\}$. It is easy to verify recursively that $\operatorname{setcon}\left(\mathcal{A}_{t \text {-res }}\right)=t+1$ : at each level $1 \leq \leq t+1$ of recursion we consider a set $S$ of $n-j+1$ elements, pick up a process $p \in S$ and delegate the set of $n-j$ processes that do not include $p$ to level $j+1$. At level $t+1$ we get one set of size $n-t$ and stop. Thus, $\operatorname{setcon}\left(\mathcal{A}_{t-\text {-res }}\right)=t+1$.

```
Shared variables:
    $D$, initially $\perp$
    $R_{1}, \ldots, R_{n}$, initially $\perp$
    ropose $(v)$
    est $:=v$
    $r:=0$
    $S:=P$
    repeat
        $r:=r+1$
        $($ flag, est $):=C A_{r}$. propose $($ est $)$
        if $f l a g=$ commit then
            $D:=$ est; return (est) $\quad$ \{Return the committed value\}
        $R_{i}:=(e s t, r)$
        wait until $\exists S \in \mathcal{A}, \forall p_{j} \in S: R_{j}=\left(v_{j}, r_{j}\right)$ where $r_{j} \geq r$ or $D \neq \perp$
            \{Wait until a set in $\mathcal{A}$ moves $\}$
        if $p_{r} \bmod n+1 \in S$ then
            est $:=v_{r} \bmod n+1 \quad$ \{Adopt the estimate of the current leader\}
    until $D \neq \perp$
    return $(D)$
```

More generally, for any superset-closed adversary $\mathcal{A}(\mathcal{A} \in \mathcal{S C})$, setcon $(\mathcal{A})=\operatorname{csize}(\mathcal{A})$, the size of a smallest-cardinality core of $\mathcal{A}$. To show this, we proceed by induction. The statement is trivially true for an empty adversary $\mathcal{A}$ with $\operatorname{csize}(\mathcal{A})=\operatorname{setcon}(\mathcal{A})=0$. Now suppose that for all $0 \leq j<k$ and all $\mathcal{A}^{\prime} \in \mathcal{S C}$ with $\operatorname{csize}\left(\mathcal{A}^{\prime}\right)=j$, we have $\operatorname{setcon}\left(\mathcal{A}^{\prime}\right)=j$. Consider $\mathcal{A} \in \mathcal{S C}$ such that $\operatorname{csize}(\mathcal{A})=k$. Note that the only proper element of $\mathcal{A}$ is the whole set of processes $\Pi$. Thus, setcon $(\mathcal{A})=\min _{a \in \Pi}$ $\operatorname{setcon}\left(\mathcal{A}_{\Pi, a}\right)+1$. By the induction hypothesis and the fact that $\operatorname{csize}(\mathcal{A})=k$, we have $\min _{a \in \Pi}$ $\operatorname{setcon}\left(\mathcal{A}_{\Pi, a}\right)=k-1$. Thus, $\operatorname{setcon}(\mathcal{A})=k$.

Thus, by Theorem ??, setcon () indeed characterizes the disorienting power of adversaries $\mathcal{A} \in \mathcal{S C}$ : a task is $\mathcal{A}$-resiliently solvable if and only if it is $(c-1)$-resiliently solvable, where $c=\operatorname{setcon}(\mathcal{A})$. In the rest of this section, we extend this result from $\mathcal{S C}$ to the universe of all adversaries.

### 14.5.5. Solving consensus with setcon $=1$

Before we characterize the ability of adversaries to solve colorless tasks, we consider the special case of adversaries of setcon $=1$.

Consider an adversary $\mathcal{A}$ and $S \in \mathcal{A}$. Suppose $\operatorname{csize}\left(\mathcal{A}_{S}\right)=1$, and let $\{a\}$ be a core of $\mathcal{A}_{S}$. Obviously, $\mathcal{A}_{S, a}=\emptyset$. On the other hand, if $\mathcal{A}_{S, a}=\emptyset$, then $\{a\}$ is a core of $\mathcal{A}_{S}$. Thus, setcon $(\mathcal{A})=1$ if and only if $\forall S \in \mathcal{A}$, $\operatorname{csize}\left(\mathcal{A}_{S}\right)=1$

Suppose $\operatorname{setcon}(\mathcal{A})=1$. If $S$ is the only proper element of $\mathcal{A}$, then we can easily solve consensus (and, thus, any other task [48]), by deciding on the value proposed by the only member of a core of $\mathcal{A}_{S}$. The process is guaranteed to be correct in every execution.

Now we extend this observation to the case when $\mathcal{A}$ contains multiple proper elements. The consensus algorithm, presented in Figure 14.3, is a "rotating coordinator" algorithm inspired by by Chandra and Toueg $[20]$.

The algorithm proceeds in rounds. In each round $r$, every process $p_{i}$ first tries to commit its current decision estimate in a new instance of commit-adopt $C A_{r}$. If $p_{i}$ succeeds in committing the estimate, the
committed value is written in the "decision" register $D$ and returned. Otherwise, $p_{i}$ adopts the returned value as its current estimate and writes it in $R_{i}$ equipped with the current round number $r$. Then $p_{i}$ takes snapshots of $\left\{R_{1}, \ldots, R_{n}\right\}$ until either a set $S \in \mathcal{A}$ reaches round $r$ or a decision value is written in $D$ (in which case the process returns the value found in $D$ ). If no decision is taken yet, then $p_{i}$ checks if the coordinator of this round, $p_{r} \bmod n$, is in $S$. If so, $p_{i}$ adopts the value written in $R_{r} \bmod n$ and proceeds to the next round.

The properties of commit-adopt imply that no two processes return different values. Indeed, the first round in which some process commits on some value $v$ (line 86) "locks" the value for all subsequent rounds, and no other process can return a value different from $v$.

Suppose, by contradiction, that some correct process never returns in some $\mathcal{A}$-compliant execution $e$. Recall that $\mathcal{A}$-compliant means that some set in $\mathcal{A}$ is exactly the set of correct processes in $e$. If a process returns, then it has previously written the returned value in $D$. Since, in each round, a process performs a bounded number of steps, by our assumption, no process ever writes a value in $D$ and every correct process goes through infinitely many rounds in $e$ without returning.

Let $\bar{S} \in \mathcal{A}$ be the set of correct processes in $e$. After a round $r^{\prime}$ when all processes outside $\bar{S}$ have failed, every element of $\mathcal{A}$ evaluated by a correct process in line 88 is a subset of $\bar{S}$. Finally, since the minimal core size of $\mathcal{A}_{\bar{S}}$ is 1 , all these elements of $\mathcal{A}$ overlap on some correct process $p_{j}$.

Consider round $r=m n+j \geq r^{\prime}-1$. In this round, $p_{j}$ not only belongs to all sets evaluated by the correct processes, but it is also the coordinator $(j=r \bmod n+1)$. Thus, the only value that a process can propose to commit-adopt in round $r+1$ is the value previously written by $p_{j}$ in $R_{j}$. Hence, every process that returns from commit-adopt in round $r+1$ must commit and return-a contradiction. Thus:

Theorem 43 [38] If setcon $(\mathcal{A})=1$, then consensus can be solved $\mathcal{A}$-resiliently.

### 14.5.6. Adversarial partitions

One way to interpret Definition ?? is to say that $\operatorname{set} \operatorname{con}(\mathcal{A})$ captures the size of a minimal-cardinality partitioning of $\mathcal{A}$ into sub-adversaries $\mathcal{A}^{1}, \ldots, \mathcal{A}^{k}$, each of setcon $=1$.

Indeed, for a proper set $S \in \mathcal{A}$, selecting an element $a \in S$ allows for splitting $\mathcal{A}_{S}$ into two subadversaries $\mathcal{A}_{S}-\mathcal{A}_{S, a}$ and $\mathcal{A}_{S, a} . \mathcal{A}_{S}-\mathcal{A}_{S, a}$ is the set of elements of $\mathcal{A}_{S}$ that contain $a$ and, thus, $\operatorname{setcon}\left(\mathcal{A}_{S}-\mathcal{A}_{S, a}\right)=1$ ( $a$ can act as a leader). Moreover, selecting $a$ so that $\operatorname{setcon}\left(\mathcal{A}_{S, a}\right)$ is minimized makes sure that $\mathcal{A}_{S, a}=\operatorname{setcon}\left(\mathcal{A}_{S}\right)-1$.

Intuitively, $\mathcal{A}^{1}$, the first such sub-adversary, is the union of $\mathcal{A}_{S}-\mathcal{A}_{S, a}$, for all such proper $S \in \mathcal{A}$ and $a \in S$. Adversaries $\mathcal{A}_{2}, \ldots, \mathcal{A}_{k}$ are obtained by a recursive partitioning of all $\mathcal{A}-\mathcal{A}^{1}$. (A detailed description of this partitioning can be found in [38].)

Thus, given an adversary $\mathcal{A}$ such that $\operatorname{setcon}(\mathcal{A})=k$, we derive that $\mathcal{A}$ allows for solving $k$-set consensus. Just take the described above partitioning of $\mathcal{A}$ in to $k$ sub-adversaries, $\mathcal{A}^{1}, \ldots, \mathcal{A}^{k}$ such that, for all $j=1, \ldots, k$, setcon $\left(\mathcal{A}^{j}\right)=1$. Then every process can run $k$ parallel consensus algorithms, one for each $\mathcal{A}^{j}$, proposing its input value in each of these consensus instances (such algorithm exist by Theorem 43). Since the set of correct processes in every $\mathcal{A}$-compliant execution belongs to some $\mathcal{A}^{j}$, at least one consensus instance returns. The process decides on the first such returned value. Moreover, at most $k$ different values are decided and each returned value was previously proposed. Thus:

Theorem 44 [38] If setcon $(\mathcal{A})=k$, then $\mathcal{A}$ allows for solving $k$-set consensus.

### 14.5.7. Characterizing colorless tasks

But can we solve $(k-1)$-set consensus in the presence of $\mathcal{A}$ such that $\operatorname{setcon}(\mathcal{A})=k$ ? As shown in [38], the answer is no: $\mathcal{A}$ does not allow for solving any colorless task that cannot be solved $(k-1)$-resiliently. The result is derived by a simple application of BG simulation $[13,15]$.

The intuition here is the following. Suppose, by contradiction, that we are given an adversary $\mathcal{A}$ such that $\operatorname{setcon}(\mathcal{A})=k$ and a colorless task $T$ that is solvable $\mathcal{A}$-resiliently but not $(k-1)$-resiliently. Let Alg be the corresponding $\mathcal{A}$-resilient algorithm. Then we can construct a $(k-1)$-resilient simulation of an $\mathcal{A}$-compliant execution of Alg. Roughly, we build upon BG-simulation, except that the order in which steps of $A l g$ are simulated is not fixed in advance to be round-robin. Instead, the order is determined online, based on the currently observed set of participating processes.

We start with simulating steps of processes in $S \in \mathcal{A}$ such that $\operatorname{set} \operatorname{con}\left(\mathcal{A}_{S}\right)=k$ (by Definition ??, such $S$ exists). If the outcome of a simulated step of some process $a$ cannot be resolved (the corresponding BG-agreement is blocked), we proceed to simulating processes in an element $S^{\prime} \in \mathcal{A}_{S, a}$ with the largest setcon (if there is any). As soon as the blocked BG-agreement on the step of $a$ resolves, the simulation returns to simulating $S$. Since $\operatorname{set} \operatorname{con}(\mathcal{A})=k$, we can obtain exactly $k$ levels of simulation. Therefore, in a $(k-1)$-resilient execution, at most $k-1$ simulated processes (each in a distinct subadversary of $\mathcal{A}$ ) can be blocked forever. Since $\mathcal{A}$ allows for $k$ such sub-adversaries, at least one set in $\mathcal{A}$ accepts infinitely many simulated steps. The resulting execution is thus $\mathcal{A}$-compliant, and we obtain a $(k-1)$-resilient solution for $T$-a contradiction (detailed argument is given in [38]).

In fact, the set of colorless tasks that can be solved given an adversary $\mathcal{A}$ such that $\operatorname{setcon}(\mathcal{A})=k$ is exactly the set of colorless tasks that can be solved $(k-1)$-resiliently, but not $k$-resiliently. Indeed, $\mathcal{A}$ allows for solving $k$-set consensus, and we can employ the generic algorithm of [37] that solves any $(k-1)$-resilient colorless task using the $k$-set consensus algorithm as a black box. Thus:

Theorem 45 [38] Let $\mathcal{A}$ be an adversary such that $\operatorname{setcon}(\mathcal{A})=k$ and $T$ be a colorless task. Then $\mathcal{A}$ solves $T$ if and only if $T$ is $(k-1)$-resiliently solvable.

Recall that the set consensus power of an adversary $\mathcal{A}$ is the smallest $k$ such that $\mathcal{A}$ can solve $k$-set consensus. Theorem 45 implies:

Corollary 8 The set consensus power of $\mathcal{A}$ is $\operatorname{setcon}(\mathcal{A})$, and the disagreement power of $\mathcal{A}$ is setcon $(\mathcal{A})-$ 1.

By Theorem ??, determining setcon $(\mathcal{A})$ may boil down to determining the minimum hitting set size of $\mathcal{A}$, and thus, by $[64]$ :

Corollary 9 Determining the set consensus power of an adversary is NP-complete.

### 14.6. Non-uniform adversaries and generic tasks

This chapter primarily talked about colorless tasks (consensus, set agreement, simplex agreement, et cetera) in the read-write shared memory systems where processes may fail by crashing in a non-uniform (non-identical and correlated) way. We modeled such non-uniform failures using the language of adversaries [28] and we derived a complete characterization of an adversary via its set consensus power [38] (or, equivalently its disagreement power [28]).

The techniques discussed here can be extended to models where processes may also communicate through stronger objects than just read-write registers (e.g., $k$-process consensus objects). In particular, BG-simulation is used in [38] to capture the ability of leveled adversaries of [91] to prevent processes from solving consensus among $n$ processes using $k$-process consensus objects $(k<n)$.

Combinatorial topology proved to be a powerful instrument in analyzing a special class of supersetclosed adversaries and colorless tasks, not only in read-write shared-memory models [51], but also in a variety of other models, including message-passing models and iterated models with $k$-set consensus objects.

However, the power of adversaries with respect to generic (not necessarily) colorless tasks is still poorly understood. Consider, for example, a task $\mathcal{T}_{p q}$ which requires processes $p$ and $q$ (in a system of three processes $p, q$, and $r$ ) to solve consensus and allows $r$ to output any value. The task is obviously not colorless: the output of $r$ cannot always be adopted by $p$ or $q$. The 2 -obstruction-free adversary $\mathcal{A}_{2-O F}=\{p q, p r, q r, p, q, r\}$ does not allow for solving $T_{p q}$ : otherwise, we would get a wait-free 2 process consensus algorithm. On the other hand, $\mathcal{A}_{p q}=\{p q r, p q, p, r\}$ ( $p$ is correct whenever $q$ is correct) allows for solving $T_{p q}$ (just use $p$ as a leader for $p$ and $q$ ). But $\operatorname{setcon}\left(\mathcal{A}_{2-O F}\right)=\operatorname{setcon}\left(\mathcal{A}_{p q}\right)=$ 2 !

One may say that the task $T_{p q}$ is "asymmetric": it prioritizes outputs of some processes with respect to the others. Maybe our result would extend to symmetric tasks whose specifications are invariant under a permutation of process identifiers? Unfortunately, there are symmetric colored tasks that exhibit similar properties [101]. So we need a more fine-grained criterion than set consensus power to capture the power of adversaries with respect to colored tasks.

Finally, this chapter focuses on non-uniform crash faults in asynchronous shared-memory systems. Non-uniform patterns of generic (Byzantine) types of faults are explored in the context of Byzantine quorum systems [79] (see also a survey in [99]) and secure multi-party computations [57]. Both approaches assume that a faulty process can deviate from its expected behavior in an arbitrary (Byzantine) manner. In particular, in [79], Malkhi and Reiter address the issues of non-uniform failures in the Byzantine environment by introducing the notion of a fail-prone system (adversarial structure in [57]): a set $\mathcal{B}$ of process subsets such that no element of $\mathcal{B}$ is contained in another, and in every execution some $B \in \mathcal{B}$ contains all faulty processes. Determining the set of tasks solvable in the presence of a given generic adversarial structure is an interesting open problem.


[^0]:    ${ }^{1}$ For brevity, we simply write $p q r$ when referring to the set $\{p, q, r\}$.

[^1]:    ${ }^{2}$ Formally, let $\operatorname{val}(U)$ denote the set of non- $\perp$ values in a vector $U$. In a colorless task, for all input vectors $I$ and $I^{\prime}$ and all output vectors $O$ and $O^{\prime}$, such that $(I, O) \in \Delta, \operatorname{val}(I) \subseteq \operatorname{val}\left(I^{\prime}\right), \operatorname{val}\left(O^{\prime}\right) \subseteq \operatorname{val}(O)$, we have $\left(I^{\prime}, O\right) \in \Delta$ and $\left(I, O^{\prime}\right) \in \Delta$.

[^2]:    ${ }^{3}$ Note that in the original definition [28], an adversary is defined as a collection of faulty sets, i.e., the sets of processes that can fail in an execution. For convenience, we chose here an equivalent definition based on correct sets.

[^3]:    ${ }^{4}$ For more information on the applications of algebraic and combinatorial topology in distributed computing, check Maurice Herlihy's lectures at Technion [49].

[^4]:    ${ }^{5}$ Recall that the $k$-resilient adversary consists of all subsets of $\Pi$ of size at least $n-k$.

