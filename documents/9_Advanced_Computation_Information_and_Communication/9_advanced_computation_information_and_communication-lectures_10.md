Estimating run times of algorithms. Suppose we want to sort a list of integers, and that we write a computer program to do so. Suppose that, given our program, we observe that to sort lists of some large number of integers, say $\ell$ integers, our program takes at most $T_{\ell}$ seconds per list. How can we approximate the time it will take at most to sort a list of $n$ items for some $n$ that is not necessarily equal to $\ell$, in particular when $n$ gets much larger than $\ell$ ? Before we can give a sensible answer to this question, we have to understand the time complexity of the sorting method used by our computer program. Very informally, the time complexity of an algorithm is an expression for the maximal number of operations (or "steps") carried out by the algorithm as a function of the "input size". In our sorting example the input size could be the number $n$ of integers to be sorted, and the time complexity would be a function $f$ of $n$ that specifies the largest number of "steps" to be taken to sort $n$ integers (using our program). Here is "step" consists of a small constant number of operations that is relevant for the context being analysed; in the context of sorting a step could be a comparison between two elements (this includes accessing those elements, cf. below) or swapping the values of two variables (swapping the values of variables $x$ and $y$ means that after the swap the "new" $x$ has the value of the "old" $y$ and the "new" $y$ has the value of the "old" $x$, so if $x=5, y=3$ before the swap then $x=3, y=5$ after the swap).

Figuring out precisely how many steps an algorithm will take is not only quite cumbersome, in this paragraph we informally show that it is also (mostly) useless. Suppose that we have found, after a lengthy and careful analysis, that the time complexity of our sorting algorithm can be expressed as $f(n)=36 n^{2}+128 n+75$ (or some other crazy expression). This allows easy calculation of the maximum number of steps to be carried out for any input size $n$. Given that we know that it apparently takes at most $T_{\ell}$ seconds to perform $f(\ell)$ steps, we may calculate the time at most required to sort $n$ integers as $\frac{f(n)}{f(\ell)} T_{\ell}=\frac{36 n^{2}+128 n+75}{36 \ell^{2}+128 \ell+75} T_{\ell}$ seconds: if it takes $T_{\ell}$ seconds to perform $f(\ell)$ steps it means that we spend $\frac{T_{\ell}}{f(\ell)}$ seconds per step, so the time required for $f(n)$ steps may be estimated as $f(n) \frac{T_{\ell}}{f(\ell)}$ seconds ${ }^{1}$. Using that $\ell$ is large and that $n$ can be expected to be even larger, to get a good approximation of the expression $\frac{36 n^{2}+128 n+75}{36 \ell^{2}+128 \ell+75}$ the two constants 75 are insignificant, the two terms[^0]$128 n$ and $128 \ell$ are mostly insignificant, and in the "remaining" fraction $\frac{36 n^{2}}{36 \ell^{2}}$ the two constants 36 cancel: all that is relevant to know about $f(n)$ is that it is a quadratic function in $n$. For large $\ell$ it follows that sorting $n>\ell$ integers using our program takes at most approximately $\left(\frac{n}{\ell}\right)^{2} T_{\ell}$ seconds.

This argument that only the most significant terms of time complexities are relevant is made more precise in the paragraphs below.

Big- $O$. When talking about algorithms and their run times it is essential to understand what big- $O$ is about. Thus a quick introduction to this subject (with the more interesting results postponed to a later lecture). Big- $O$ allows us to focus on "what is most important" when analysing algorithms (as illustrated in the paragraphs above). In the 1970s this led to the re-popularization of the Landau big-O symbol from the late 1800s, now commonly referred to as just big- $O$ (pronounced as "big-oh", not as "big-zero").

Let $f$ and $g$ be two functions from $\mathbf{R}_{>0}$ to $\mathbf{R}$. In our context the function $f$ should be thought of as some (often overly complicated) expression for the number of operations carried out by an algorithm when solving a problem of a certain size, and the function $g$ should be thought of as a more insightful "simple" function that conveys all information that we really care about (in the example above, $f(x)$ would be the function $36 x^{2}+128 x+75$ and $g(x)=x^{2}$ ). We say that " $f$ is big-oh of $g$ " and write " $f(x)$ is $O(g(x))$ " or simply " $f$ is $O(g)$ " if

$$
\exists C, k \quad \forall x>k|f(x)| \leq C|g(x)|
$$

where the domain for $C, k$, and $x$ is $\mathbf{R}_{>0}$. Thus if there is a positive constant $(C)$ such that for all large enough ( $>k$ ) problem sizes $x$ the value $|f(x)|$ is dominated by that constant times $|g(x)|$ then $f$ is big-oh of $g$.

Constants $C$ and $k$ such that $|f(x)| \leq C|g(x)|$ for all $x>k$ are witnesses to the fact that $f(x)$ is $O(g(x))$. Once you have done it a couple of times, finding explicit values for the witnesses is not something you're ever going to do again; it makes sense though to make some of the exercises in Section 3.2 to make sure you understand how this works.

The following basic examples should be obvious:

- If $T(n)=12 n+31$ then $T(n)$ is $O(n)$ : what we really care about is to know that $T$ is at most "linear".
- If $S(n)=2 n^{2}+120 n+4325$ then $S(n)$ is $O\left(n^{2}\right)$ : what we really care about is to know that $S$ is at most "quadratic".
- If $U(n)=666$ then $U(n)$ is $O(1)$ : what we really care about is to know that $U$ is at most "constant".
- If $V(n)=\log _{10}\left(n^{4}\right)$ then $V(n)$ is $O(\log (n))$ : what we really care about is to know that $V$ is at most "logarithmic".
- With the above functions, it is also true that $T$ is $O(S)$ and thus $O\left(n^{2}\right)$, that $U$ is $O(T)$ and thus $O(n)$, and that $U$ is $O(S)$ and thus $O\left(n^{2}\right)$. These big-oh estimates are however much less informative than the ones given in the first four bullets: we always like to go for the "tightest" estimate that we can find and avoid using upper bounds that are too loose.


## Big- $O$ related definitions.

Big-omega and big-theta. Where $f$ is $O(g)$ provides an "upper bound" for $f$ in terms[^1]of $g$, a "lower bound" for $f$ in terms of $h$ is provided by big-omega: we say that " $f(x)$ is big-omega of $h(x)$ " (and write " $f(x)$ is $\Omega(h(x)$ )" or " $f$ is $\Omega(h)$ ") if

$$
\exists C, k \forall x>k|f(x)| \geq C|h(x)|
$$

where the domain for $C, k$, and $x$ is $\mathbf{R}_{>0}$, and $C$ must be strictly positive for the definition to make sense. It follows that $f$ is $\Omega(h)$ if and only if $h$ is $O(f)$.

If $f$ is $O(g)$ and $f$ is $\Omega(g)$ (where the latter is equivalent to $g$ is $O(f))$, then we say that " $f(x)$ is big-theta of $g(x)$ " (and write " $f(x)$ is $\Theta(g(x))$ " or " $f$ is $\Theta(g)$ "); in this case we also say that $f$ is of order $g$ and that $f$ and $g$ are of the same order. For the examples $T, S, U, V$ above it follows that $T(n)$ is $\Theta(n)$ ( $T$ is linear), $S(n)$ is $\Theta\left(n^{2}\right)$ ( $S$ is quadratic), $U(n)$ is $\Theta(1)$ ( $U$ is constant), and $V(n)$ is $\Theta(\log (n))(V$ is logarithmic) ${ }^{3}$. In the exercises we will also see little-o ("little-oh").

Three basic problems given a list of items. Let $L$ be some non-empty list containing $n$ unspecified items $\ell_{1}, \ell_{2}, \ldots, \ell_{n}$. We do not care what the $\ell_{i}$ contain or consist of (numbers, apples, oranges, other type of data, movies, books, people, cars, ...) but we assume that the $\ell_{i}$ can be compared to each other (so a "largest" item makes sense) and to other items (not necessarily in $L$ ) of a comparable data type. We also assume that the data structure used to store $L$ allows random access: for any $1 \leq i \leq n$ the item $\ell_{i}$ can be accessed at more or less the same (constant) cost that does not depend on $i$ (more on random access below). Assuming this is done on a computer using some programming language a list $L$ of this sort could be represented by an "array" of an appropriate data type. The data type of the items in $L$ is irrelevant for our purposes, except that we assume that a question such as " $\ell_{i}<\ell_{j}$ " makes sense and has a yes/no answer. Note that a so-called "linked list" would not allow the type of access as specified above (i.e., random access).

Thus, given an "array" $L$ (that allows random access), we are interested in three problems:

- deciding if some given item $x$ (of the right type) is among the items of $L$.
- computing the largest item of $L$.
- (assuming $L$ consists of real values) computing the average of the values assigned to the items of $L$.

If no additional information about $L$ or its items is known, all we can do to solve each of these problems is consecutively inspecting all items, starting for instance at $\ell_{1}$ (but in principle any order will do, as long as all items will be inspected, if necessary), and taking for each item under inspection some appropriate action that depends on the problem addressed:
- ("find $x$ ") compare $x$ to the item under inspection, stop with "yes, found $x$ in $L "$ if it is equal, otherwise move to the next item to be inspected, etc., and stop with "no, $x$ is not in $L$ " after all items have been inspected but $x$ was not found (note that, if $x$ has been found in $L$, the location (or index) where it has been found may be reported as well);
- ("largest") replace the candidate largest item (initialized as a smallest possible item, or as the first item on the list) by the item under inspection if the latter is larger than the candidate largest value, then move to the next item to be inspected, etc., and, after all items have been inspected, report the candidate largest item as the largest item (note that a location where the largest item occurred may be reported as well at little extra effort);[^2]- ("average") add the value of the item under inspection to some accumulator (initialized as zero), then move to the next item to be added to the accumulator, etc., and, after all items have been processed, divide the accumulator by the number $n$ of items in the list and report the resulting number as the average.

You should not have trouble programming either of these three variants in the programming language of your choice.

Each of the three variants takes, essentially, $n$ or at most $n$, "steps": although the details of the "step" that must be taken may be quite different for the three variants, each of the three step-variants takes at most some non-zero constant number of operations: "if $x$ equals item then print("yes, found $x$ in $L$ "); "if item is larger than current_max then replace current_max by item"; "add item to accumulator". Similarly, the action taken at the end is different for the three variants, but consists of some non-zero constant number of operations. Note that we use the fact that each item in $L$ can be accessed at unit cost, but also note that the items may be accessed sequentially - truly random access (i.e., wildly jumping around among the items in $L$ ) is not required. For any non-outrageous implementation cache-misses (as discussed below) will not cause noticeable inefficiencies.

So, up to some non-zero constant factor, the total effort that is at most required by each of our three variants is comparable, namely some non-zero constant times $n$. We say that all three methods run in time $O(n)$, i.e., linear in the size of the list, and the above search for $x$ is referred to as linear search. The major distinction between the three variants is that the linear search may stop earlier (if $x$ is found somewhere in the list: if at the first location, for instance, the total search takes only a non-zero constant number of operations) but may require - in the worst case - inspection of all $n$ items in $L$. For the "largest" and "average" calculations all items must be inspected: they run in time $\Theta(n)$.

Same three problems, but now the list is sorted. For two of our three problems the solution changes entirely if we assume that the items in $L$ are sorted (say in increasing order) with respect to the ordering under consideration (how that is achieved, i.e., sorting $L$, will be discussed next time):

- Deciding if $x$ is in $L$ or not can now be done using binary search: compare $x$ to the item $y$ (approximately) in the middle of $L$ and decide based on the outcome if the bottom-half of $L$ can be discarded (this is the case if $y<x$ ) or if the top-half of $L$ can be discarded (this is the case if $y>x$ ) or if we happen to be lucky $(y=x)$. In either case the original search space of $n$ items is reduced to at most about $\left\lfloor\frac{n}{2}\right\rfloor$ items at the cost of a single comparison. After a second comparison (comparing $x$ to the item in the middle of the remaining part of the list) the number of items in the then remaining part of the list is at most $\left\lfloor\frac{n}{4}\right\rfloor ; \ldots ;$ until the final remaining part of the list contains about $\frac{n}{2^{k}}$ items after in total $k$ comparisons. Because the final "yes" or "no" decision can, at the latest, be made when $\frac{n}{2^{k}} \approx 1$ (i.e., the remaining part of the list contains a single item) we find that $n \approx 2^{k}$ and thus that $k \approx \log _{2}(n)$.

This means that at most only logarithmically many comparisons have to be made before one is sure whether or not $x$ is in $L$. Because for any reasonably large $n$ the value of $\log _{2}(n)$ is quite a bit smaller than $n$, binary search (which exploits the fact that $L$ is sorted) is much faster than linear search (which is all one can do if $L$ is not sorted): for instance, if $n=10^{6}$, linear search may require up to $10^{6}$ comparisons (requiring just sequential access to the items of $L$, though), whereas for binary search about $\log _{2}\left(10^{6}\right) \approx 20$
comparisons suffice (but requiring random access to the items of $L$, because the items in $L$ are not inspected consecutively: it requires quite some jumping around in $L$ ).

Using the big- $O$ notation, we say that "binary search works in $O(\log (n))$ " or "in the worst case binary search requires logarithmic time" (where the size is implicit). Note that, as above, this logarithmic time bound is an upper bound only and that the base of the logarithm is no longer relevant as soon as the big- $O$ is applied.

- The largest item will now be at the last position in $L$ (it would have been at the first position if $L$ would have been in decreasing order). Retrieving the largest item thus requires just constant effort (cf. random access). So "it works in time $\Theta(1)$ ", but this is a bit uncommon, and normally people say "it works in $O(1)$ " because a constant lower bound is more or less unavoidable.
- The calculation of the average of the items in $L$ cannot profit from the new situation where the items in $L$ are sorted: the required effort is still linear in $n$ and the earlier $\Theta(n)$ still applies.

Because searching is an important and very common problem and the gain per search is considerable (for large $n$ the difference between $\log _{2}(n)$ versus $n$ comparisons is substantial: even for the modest value $n=10^{3}$ we get $\approx 10$ versus 1024), it may be worth the effort to sort a list of items before (many) searches are conducted - if just a single or a few searches are required sorting of course does not make sense. But, this also depends on the effort that would be required to sort a list of items (which will be discussed next time). First, however, an informal summary of our discussion on the selection of a random $x$ to search for in a list $L$.

Comment on random access: the memory hierachy. This subject is treated in the course ICC, and should therefore be included in AICCI too (I do so occasionally). It is not in the book.

Random access to array elements means that given any array $a$ the time it takes to read or write the array element $a[i]$ (or $a_{i}$ ) is "mostly" independent of the index $i$ and that, when requested by the processing unit, the value $a[i]$ is "more or less instantaneously" available to the processor - if this sounds vague, that is intentional. In theory random access is very nice, and it may even have some practical value if the array is small. In practice, however, it is entirely unrealistic, and no one knows how to achieve this in all circumstances: access times easily become quite noticeable, or even annoyingly noticeable, and in particular when one constantly tries to truly "randomly access" elements in huge arrays (or other data structures) program easily grind to a halt, and the programmer will have to take conscious action to prevent mishaps. This is not just the case for array elements but for any type of variable that you may be using in your programs; below the two cases (array element versus any type of variable) are not necessarily distinguished, but they often turn out to behave quite differently with respect to fast access.

Taking appropriate action requires insight in the memory hierarchy of one's hardware and in particular of its so-called cache; in practice it is extra challenging because the programmer can exercise only little control over what the cache does. Below a severely oversimplified big picture is sketched which is meant to give you only a vague idea of the myriad of complications involved in moving data back and forth between the place where the data is stored and where the data is used (i.e., read or written or both).

Some of the data that your program requires (the program itself, its variables, its input) may be stored in on-chip memory, so close to the processor that the data can read (or written) in a single clock-cycle (or thereabouts: in any case, very
efficiently, and on the order of a single nanosecond). (Part of) this on-chip memory is called the cache (this cache may itself be divided in several levels, not for us to worry about in this high level description, and the non-cache part of on-chip memory we won't worry about at all). There is only a limited amount of cache, due to cost constraints, manufacturing limitations, the desire to make available on-chip all kinds of other useful functionalities, and what have you. The main point is that on-chip, fast memory is very limited.

Because on-chip, fast memory is limited, there is a good chance that at least part of your data will have to be stored somewhere off-chip, in a part of the memory that is called "RAM", for Random Access Memory. Assume our piece of data called $x$ is not stored in on-chip memory, but in RAM. When $x$ needs to be operated upon, $x$ will be retrieved from RAM and put in the cache, but this can only be done much slower (on the order of one hundred nanoseconds) and only as part of a "chunk" that we call a cache line and that normally contains some fixed amount of other data as well (i.e., besides $x$ ). The good news is that you do not have to worry about this data-retrieval from RAM (except that it takes time), but the bad news is that generally speaking you have no control over which other data (than $x$ ) will be included in the chunk that contains $x$. More about this later, first a little more about RAM and the other parts of the memory hierarchy. In the description below we imagine that the cache is at the top of the memory hierarchy and that the RAM is at the highest level below the cache.

If your amount of data is huge (or the amount of RAM is small), your data may have to reside on a lower level than RAM such as the disk drive - or on an even lower level such as on magnetic tapes: the further away one gets from the processor the more one can store, but the slower it becomes to access the data and the bigger the chunks are that are moved between the different consecutive levels (to be put in, or received from, the one level higher storage medium): huge chunks are copied rather slowly between magnetic tape and your disk drive; medium size chunks are copied at medium speed between the disk drive and RAM, smallish chunks take about one hundred nanoseconds to reach cache from RAM (or back); and once in cache the processor can access or write the data almost instantaneously, at the order of a single nanosecond. Here we will only consider RAM and cache, because their interaction is mostly invisible to regular users and can normally not directly be influenced by the user.

The reason to have a cache is so that it may be possible to serve future requests for data from memory in a fast manner. If your program needs data that are indeed available in cache at the moment the data is required it is called a cache hit. If the data required is not readily available in the cache, your program faces a cache miss: the program issues an instruction to retrieve the proper data from RAM and to put it in cache, and then stalls until the data is (finally) available (i.e., once it has been put in cache). If there is no space left in cache, "old" data sitting in cache will first have to be evicted from cache (and returned to their proper place in RAM); once space is available the proper data are pulled in, but always (as described above) in chunks that fill a "line of cache". How many data per chunk and how it is decided which data to evict all depends on the caching and memory policies of the processor (the different levels of cache play a role too - not our concern here) and is closely tied to two types of "locality" that can often be found in programs: spatial locality and temporal locality, as sketched below.

This process of getting a cache line from memory and putting it in cache takes a while (as mentioned above: on the order of one hundred nanoseconds), during which the processor is just twiddling its thumbs. Pulling in an entire cache line from RAM to cache should decrease the chance that one of the next instructions will have to
wait again due to a cache miss $^{4}$, if a wise decision is made about what to include in the chunk (cache line) retrieved from RAM. But what is a "wise decision"? That all depends on the type of program you are writing. Very often it turns out to be the case that programs can profit from spatial locality: if your piece of data $x$ as above is needed at moment $t$, then it is not unlikely that something that is stored "close" to $x$ in memory (such as RAM) is needed at a moment close to $t$. For instance, your $x$ may be the $i$-th element $a_{i}$ of some array. Often, when programmers are processing array-data, it is the case that when $a_{i}$ is needed, then $a_{i+1}$ is needed shortly later (and who knows $a_{i+2}, a_{i+3}$, etc. too): so it makes sense to retrieve $a_{i+1}$ (and who knows $a_{i+2}, a_{i+3}$, etc. too) at the same time that your $x=a_{i}$ is put in cache. So, even though you had to wait a while for the proper $x$ to be loaded from RAM into cache, this is to some extent compensated for by the fact that the "neighbors" of $x$ are instantanously accessible as soon as $x$ is accessible. This "pulling in of neighbors" happens more or less automatically due to the way arrays are laid out in memory: consecutive array elements are normally speaking stored at consecutive memory locations so that if a chunk containing $a_{i}$ is pulled in (i.e., a chunk is copied from RAM into cache), the next element $a_{i+1}$ (etc., but obviously only up to a very finite limit, i.e., $a_{i+j}$ for all $j \in[1, B]$ for some modest value of $B$ - "bit boundaries" normally play a role too, namely that an interval of length $\ell$ around $a_{i}$ is retrieved, where $\ell$ is some smallish power of two) is often also pulled in. This works great if $x$ is always operated on along with its "neighbors" (i.e., spatial locality applies to $x$ ), but it is useless if the operations to be applied to $x$ are completeley independent from what happens to the values that are stored close to $x$.

The more "surrounding" data are pulled in, the better the program can profit from spatial locality. But, due to the limited cache space, "pulling in more surrounding data" also means that more other data will have to be evicted which makes it harder to profit from another type of locality that is often also relevant for programs, namely temporal locality: if some piece of data $y$ is used at moment $t$, then most likely the same $y$ will be used again at a moment close to $t$ (typically something that is applicable to data not part of an array, such as all kinds of control variables); this implies that once $y$ has been put in the cache and has been operated upon it makes sense to keep it there for a while, because other operations involving $y$ may be imminent. Optimization to best profit from both types of locality puts conflicting demands on the length of cache lines: they need to be long (large $B$ as above, or large $\ell$ as above) to profit from spatial locality, but quite a bit shorter to profit from temporal locality, so in practice some type of compromise is used that works acceptably.

Most commonly the compromises that industry has settled for work great for most middle of the road programming tasks, to the extent that the required waiting times to copy data from RAM to cache (and back, when data are evicted from cache back to RAM) do not interfere with a program's normal functionality. But if your program requires you to jump around at random in your data, then it can become very inefficient. And worse: if you are sharing the processor with another user, caching effects can become disastrous. Both issues are explained below.

Cache inefficiences. You don't have to write outrageous programs to run into serious cache inefficiencies: there are very common circumstances where the delays quickly become substantial and where proper understanding of how memory is organized and how data are loaded from RAM into cache can help to make programs much more efficient. In class this was illustrated using the way the elements of a[^3]two-dimensional $n \times n$ array

$$
A=\left(\begin{array}{cccc}
a_{1,1} & a_{1,2} & \ldots & a_{1, n} \\
a_{2,1} & a_{2,2} & \ldots & a_{2, n} \\
\cdot & \cdot & & \cdot \\
\cdot & \cdot & & \cdot \\
\cdot & \cdot & & \cdot \\
a_{n, 1} & a_{n, 2} & \ldots & a_{n, n}
\end{array}\right)
$$

are laid out in memory. Either all such arrays are laid out in row-major order

$$
a_{1,1}, a_{1,2}, \ldots, a_{1, n}, a_{2,1}, a_{2,2}, \ldots, a_{2, n}, \ldots, a_{n, 1}, a_{n, 2}, \ldots, a_{n, n}
$$

or they are all laid out in column-major order

$$
a_{1,1}, a_{2,1}, \ldots, a_{n, 1}, a_{1,2}, a_{2,2}, \ldots, a_{n, 2}, \ldots, a_{1, n}, a_{2, n}, \ldots, a_{n, n}
$$

For large $n$ this has unpleasant consequences if your program is organized in such a way that it accesses the array elements in an order that does not correspond to the order in which they are laid out in memory. As an example, this commonly happens when matrices are multiplied. Let $A$ be as above and let $B$ be another $n \times n$ matrix, with entries $b_{i, j}$ (and thus laid out in memory in the same manner as $A$ is laid out). To compute $A \times B$ one typically ${ }^{5}$ writes a piece of code that does something similar to

$$
\begin{aligned}
& \text { for } i=1 \text { to } n \text { do } \\
& \text { for } j=1 \text { to } n \text { do } \\
& c_{i, j}=0 \\
& \text { for } k=1 \text { to } n \text { do } \\
& c_{i, j}=c_{i, j}+a_{i, k} \cdot b_{k, j}
\end{aligned}
$$

and that thus runs in time $O\left(n^{3}\right)$. If row-major order is used to store $A$ and $B$ then the elements of $A$ are nicely accessed in the same order in which they are stored in memory, namely in the order

$$
a_{1,1}, a_{1,2}, \ldots, a_{1, n}, a_{2,1}, a_{2,2}, \ldots, a_{2, n}, \ldots, a_{n, 1}, a_{n, 2}, \ldots, a_{n, n}
$$

But the elements of $B$ are not at all accessed in the order

$$
b_{1,1}, b_{1,2}, \ldots, b_{1, n}, b_{2,1}, b_{2,2}, \ldots, b_{2, n}, \ldots, b_{n, 1}, b_{n, 2}, \ldots, b_{n, n}
$$

in which they are stored: for $i=1$ and $j=1$, for instance the underlined nonconsecutively stored entries are accessed for $k=1,2, \ldots, n$ :

$$
\underline{b_{1,1}}, b_{1,2}, \ldots, b_{1, n}, \underline{b_{2,1}}, b_{2,2}, \ldots, b_{2, n}, \ldots, \underline{b_{n, 1}}, b_{n, 2}, \ldots, b_{n, n}
$$

As a consequence, if $n$ is large compared to the length of a cache line, the code will suffer from constant cache misses ${ }^{6}$. If column-major order is used, then $B$ will not suffer from cache misses, but $A$ will, with the non-consecutively stored underlined entries accessed for $k=1,2, \ldots, n$ :

$$
\underline{a_{1,1}}, a_{2,1}, \ldots, a_{n, 1}, \underline{a_{1,2}}, a_{2,2}, \ldots, a_{n, 2}, \ldots, \underline{a_{1, n}}, a_{2, n}, \ldots, a_{n, n}
$$[^4]

To solve this problem, and assuming row-major order is used for matrix storage,the matrix $B$ may be replaced by its transpose before doing the matrix multiplication. Assuming $B$ has been transposed implies that the matrix multiplication code fragment above must be replaced by the odd-looking piece of code

```
for $i=1$ to $n$ do
    for $j=1$ to $n$ do
        $c_{i, j}=0$
        for $k=1$ to $n$ do
            $c_{i, j}=c_{i, j}+a_{i, k} \cdot b_{j, k}$
```

and that, after the matrix multiplication, the matrix $B$ must be transposed back to its original state. (Obviously, transpose and back-transpose $A$ instead if storage is column-major; how to change the piece of code is left as a simple exercise. And what is one supposed to do to compute $A^{2}$ efficiently?)

Straightforward transposition will suffer from cache-misses, but at most once per matrix-entry, whereas there would be multiple cache misses per matrix-entry during a matrix multiplication, so the transposition overhead should be relatively small. Also, if the transposition is done a bit smarter than just by "for $i=1$ to $n$ do for $j=1$ to $i-1$ do swap $a_{i, j}$ and $a_{j, i}$ " some of the ill cache effects can quite easily be avoided; how?

The slowdown caused by constant cache-misses during matrix multiplication is easily an order of magnitude (i.e, a slowdown by a factor of ten, and actually quite a bit more for large matrices). Similar effects can be observed when doing other elementary matrix operations that access the matrix-entries in the "correct" versus the "wrong" order, from the cache's point of view. An example is computing the sum of all matrix entries.

Cache disasters. (This uplifting story was not told in class.) There may be circumstances where different parties share the same processor (such as virtual machines). Although memory can be segmented so users will not be able to peek at each others' data, and the processing unit will be time sliced to either work for one party or for another, but not for both at the same time, there is nevertheless a resource that is shared between the parties: the cache. This does not imply that users can look at each others' data in the cache - the problem is more subtle. What any party can do, is observe how much time is required to operate on its data: if a piece of data that was recently used turns out to have been evicted from cache (which may be observable because it takes a while to work on it again), information may be inferred about what type of data was pulled into cache by some other party with whom the cache is shared. From a security point if view this is "not good" - indeed, this simple observation has been used to break otherwise very secure cryptographic schemes in a matter of milliseconds (just type "shamir tromer osvik cache attacks" in DuckDuckGo). The fix turned out to be nontrivial.

Next class. We will discuss sorting methods, followed by more big-O related results.


[^0]:    ${ }^{1}$ If the logic still escapes you, do an example: say $f(\ell)=100$ for some $\ell$ and that performing those 100 steps took $T_{\ell}=5$ seconds. If $n$ is such that $f(n)=1000$, then $\frac{f(n)}{f(\ell)}=\frac{1000}{100}=10$ times more steps must be taken (compared to what was required for $\ell$ ), which thus takes 10 times more time, namely $10 * 5=50$ seconds. Or: 100 steps in 5 seconds, thus $\frac{5}{100}=\frac{1}{20}$ seconds per step, thus $\frac{1}{20} * 1000=50$ seconds for 1000 steps.

[^1]:    ${ }^{2}$ We use that $\log \left(n^{k}\right)=k \log (n)$ (where we have $k=4$ ). This should not be confused with $(\log (n))^{k}$ which is in general not equal to $k \log (n)$. Note that for constants $k$ and $\ell$ with $0<$ $k<\ell$ we have that $\log \left(n^{k}\right)$ is $O\left(\log \left(n^{\ell}\right)\right)$, that $\log \left(n^{\ell}\right)$ is $\left.O\left(\log \left(n^{k}\right)\right)\right)$ (and thus that $\log \left(n^{k}\right)$ is $\Theta\left(\log \left(n^{\ell}\right)\right)$ and $\log \left(n^{\ell}\right)$ is $\Theta\left(\log \left(n^{k}\right)\right)$, cf. below), that $(\log (n))^{k}$ is $O\left((\log (n))^{\ell}\right)$, and that $(\log (n))^{\ell}$ is $\Omega\left((\log (n))^{k}\right)$ (cf. below), but that $(\log (n))^{\ell}$ is not $O\left((\log (n))^{k}\right)$.

[^2]:    ${ }^{3}$ You will see that in the computer science literature the symbols $O$ and $\Theta$ are often used in an incorrect manner, leading to incorrectly stated results the correct version of which can only be inferred from the context (a similar remark is made in the book right before the exercises of Section 3.2).

[^3]:    ${ }^{4}$ Reflecting the purpose of the cache, as mentioned above: "The reason to have a cache is so that it may be possible to serve future requests for data from memory in a fast manner."

[^4]:    ${ }^{5}$ Unless one likes Karatsuba a lot and decides to apply similar ideas to speed up matrix multiplication: $O\left(n^{\log _{2}(7)}\right)$ can relatively easily be achieved using Strassen's algorithm (which is "Karatsuba inspired"). More painful, but much faster, are the Coppersmith-Winograd algorithms: on Wikipedia you can find the latest matrix multiplication exponent. It is still not known if the value of the matrix multiplication exponent can be lowered further.

    ${ }^{6}$ This may be compared to reading a book: accessing the $a_{i, k}$ values is comparable to reading the consecutive sentences, accessing the $b_{k, j}$ values is comparable to first reading the first word of each sentence, than the second word of each sentence, then the third, etc.

