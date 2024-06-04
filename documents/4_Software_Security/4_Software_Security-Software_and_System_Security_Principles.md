
## Software And System Security Principles

The goal of software security is to allow any intended use of software but prevent any unintended use. Any unintended use may cause harm as in unintended use of compute resources outside of a defined allowed use. In this chapter, we discuss several system principles that are essential when building secure software systems. Confidentiality, *Integrity*, and *Availability* enable reasoning about different properties of a secure system. Isolation enforces the separation between components such that interaction is only possible along a well-defined interface that allows reasoning about access primitives. *Least privilege* ensures that each software component executes with the minimum amount of privileges. During *compartmentalization*, a complex piece of software is broken into smaller components. Isolation and compartmentalization play together, a large complex system is compartmentalized into small pieces that are then isolated from each other. The *threat model* specifies the environment of the software system, outlining the capabilities of an attacker. Distinguishing between *software bugs* and *vulnerabilities* helps us to decide about the risks of a given flaw.

## 2.1 Authentication

Authentication is the process of verifying if someone is who they claim to be. Through authentication, a system learns who you are based on what you know, have, or are. During authentication, a user verifies that they have the correct credentials. For example, to login on a system a user has to authenticate with their username and password. The username may either have to be entered or selected from a drop down list and the password has to be typed.

Authenticating through username and password is the most common form of verifying someones credential but alternate forms are possible too. Common classes of authentication forms are passwords (what you know), biometric (what you are), or demonstration of property (what you have).

Passwords are the classic approach towards authentication.

During authentication, the user has to type their password or PIN (personal identification number) to login. The password is generally kept secret. Most systems provide usernames and password as the default authentication method. Limitations are the lack of replay resistance: an attacker that steals the raw biometric data can replay that data to authenticate as the user. This risk can be mitigated by a reasonable password update policy where, after a break, the users may be urged to update their passwords.

Another risk is that passwords can be brute-forced. During such a brute force attack, the attacker tries every single possible password combination. Over the years password policies have become highly restrictive and on some systems users have to create new passwords every few months, they are not allowed to repeat passwords, and passwords must contain a set of unique character types (e.g., upper case letters, lower case letters, numbers, and special characters) to ensure sufficient entropy. Current best practices are to allow users freedom in providing sufficiently long passwords. It is easier to achieve good entropy with longer passwords than having users forget their complex short passwords.

Biometric logins may target fingerprints, Iris scans, or behavioral patterns (e.g., how you swipe across your screen). Using biometric factors for authentication is convenient as users cannot (generally) neither lose nor forget them. Their key limitation is the lack of replay resistance. Different to passwords, biometrics cannot be changed, so a loss of data means that this authentication form loses its utility. For example, if someone's fingerprints are known by the attacker, they can no longer be used for authentication.

Property can be anything the user owns that can be presented to the authentication system such as smartcards, smartphones, or USB keys. These devices have some internal key generation mechanism that can be verified. An advantage is that they are easily replaceable. The key disadvantage is that they should not be used by itself as, e.g., the smartphone may be stolen. Instead of just using a single username and password pair, many authentication systems nowadays rely on two or more factors. For example, a user may have to log in with username, password, and a code that is sent to their phone via text message.

## 2.2 Access Rights

Access rights encode what entities a user has access to. For example, a user may be allowed to execute certain programs but not others. They may have access to their own files but not to files owned by another user. The Unix philosophy introduced a similar access right matrix consisting of user, group, and other rights. Each file has an associated user which may have read, write, or execute rights. In addition to the user who is the primary owner, there may be a group with corresponding read, write, or execute rights, and all others that are not part of the group with the same set of rights. A user may be member of an arbitrary number of groups. The system administrator organizes group membership and may create new users. Through privileged services, users may update their password and other sensitive data. More information about access rights, access control (both mandatory and discretionary) along with role based access control can be found in many books on Usenix system design or generally system security.

## 2.3 Confidentiality, Integrity, And Availability

Information security can be summarized through the three key concepts: confidentiality, integrity, and availability. The three concepts are often called the CIA triad. These concepts are sometimes called security mechanisms, fundamental concepts, properties, or security attributes.

While the CIA triad is somewhat dated and incomplete, it is an accepted basis when evaluating the security of a system or program.

The CIA
triad serves as a good basis for refinement and covers the core principles. *Secrecy* as a generic property ensures that data is kept hidden (secret) from an unintended receiver.

Confidentiality of a service limits access of information to privileged entities. In other words, confidentiality guarantees that an attacker cannot recover protected data. The confidentiality property requires authentication and access rights according to a policy. Entities must be both named and identified and an access policy determines the access rights for entities. Privacy and confidentiality are not equivalent. Confidentiality is a component of privacy that prevents an entity from viewing privileged information. For example, a software flaw that allows unprivileged users access to privileged files is a violation of the confidentiality property. Alternatively, encryption, when implemented correctly, provides confidentiality. Note that confidentiality ensures that someone else's data is being kept secret For example, the OS ensures confidentiality of a process' address space by hiding it from other processes.

Integrity of a service limits the modification of information to privileged entities. In other words, integrity guarantees that an attacker cannot modify protected data. Similar to confidentiality, the integrity property requires authentication and access rights according to a policy. For example, a software flaw that allows unauthenticated users to modify a privileged file is a violation of the integrity policy. For example, a checksum that is protected against adversarial changes can detect tampering of data. Another aspect of integrity is replay protection. An adversary could record a benign interaction and replay the same interaction with the service. Integrity protection detects replayed transactions. In software security, the integrity property is often applied to data or code in a process. For example, the OS ensures integrity of a process' address space by prohibiting other processes from writing to it.

Availability of a service guarantees that the service remains accessible. In other words, availability prohibits an attacker from hindering computation. The availability property guarantees that legitimate uses of the service remain possible. For example, allowing an attacker to shut down the file server is a violation of the availability policy.

For example, the OS ensures availability by scheduling each process a "fair" amount of time, alternating between processes that are ready to run.

The three concepts build on each other and heavily interact.

For example, confidentiality and integrity can be guaranteed by sacrificing availability. A file server that is not running cannot be compromised or leak information to an attacker. For the CIA triad, all properties must be guaranteed to allow progress in the system. Several newer approaches extend these three basic concepts by introducing orthogonal ideas. The two most common extensions are *accountability* and *non-repudiation*, referring that a service must be accountable and cannot redact a granted access right or service. For example, a service that has given access to a file to an authorized user cannot claim after the fact that access was not granted. Non-repudiation is, at its core, a concept of law. Non-repudiation allows both a service to prove to an external party that it completed a request and the external party to prove that the service completed the request. Orthogonally, *privacy* ensures confidentiality properties for the data of a person. *Anonymity* protects the identity of an entity participating in a protocol. Each property covers one separate aspect of information security. Policies provide concrete instantiations of any of the policies while mechanisms further refine a policy into an actual implementation. In practice, we will be working with policies that provide certain guarantees, following the core properties defined here. Policies themselves define the high level goals and the concrete mechanisms then enforce a given policy.

## 2.4 Isolation

Isolation separates two components from each other and confines their interactions to a well-defined API. There are many different ways to enforce isolation between components, all of them require some form of abstraction and a security monitor.

The security monitor runs at higher privileges than the isolated components and ensures that they adhere to the isolation. Any violation to the isolation is stopped by the security monitor and, e.g., results in the termination of the violating component. Examples of isolation mechanisms include the process abstraction, containers, or SFI [33,34].

The *process abstraction* is the most well known form of isolation: individual processes are separated by the operating system from each other. Each process has its own virtual memory address space and can interact with other processes only through the operating system which has the role of a security monitor in this case. An efficient implementation of the process abstraction requires support from the underlying hardware for virtual memory and privileged execution. Virtual memory is an abstraction of physical memory that allows each process to use the full virtual address space. Virtual memory relies on a hardware-backed mechanism that translates virtual addresses to physical addresses and an operating system component that manages physical memory allocation. The process runs purely in the virtual address space and cannot interact with physical memory. The code in the process executes in non-privileged mode, often called user mode. This prohibits process code from interacting with the memory manager or side-stepping the operating system to interact with other processes. The CPU acts as a security monitor that enforces this separation and guarantees that privileged instructions trap into supervisor mode. Together privileged execution and virtual memory enable isolation. Note that similarly, a hypervisor isolates itself from the operating system by executing at an even higher privileged mode and mapping guest physical memory to host physical memory, often backed through a hardware mechanism to provide reasonable performance.

Containers are a lightweight isolation mechanism that builds on the process abstraction and introduces namespaces for kernel data structures to allow isolation of groups of processes. Normally, all processes on a system can interact with each other through the operating system. The container isolation mechanism separates groups of processes by virtualizing operating system mechanisms such as process identifiers (pids), networking, inter process communication, file system, and namespaces. Software-based Fault Isolation (SFI) [33,34] is a software technique to isolate different components in the same address space.

The security monitor relies on static verification of the executed code and ensures that two components do not interact with each other. Each memory read or write of a component is restricted to the memory area of the component. To enforce this property, each instruction that accesses memory is instrumented to constrain the pointer to the memory area. To prohibit the isolated code from modifying its own code, controlflow transfers are carefully vetted and all indirect control-flow transfers must target well-known locations. The standard way to enforce SFI is to mask pointers before they are dereferenced
(e.g., anding them with a mask: and %reg, 0x00ffffff) and by aligning control-flow targets and enforcing alignment. Generally, lower levels of abstractions trust the isolation guarantees of higher levels.

For example, a process trusts the operating system that another process cannot suddenly read its memory. This trust may be broken through side channels which provide an indirect way to recover (partial) information through an unintended channel. Threat models and side channels will be discussed in detail later. For now, it is safe to assume that if a given abstraction provides isolation that this isolation holds. For example, the process trusts the operating system (and the underlying hardware which provides privilege levels) that it is isolated from other processes.

## 2.5 Least Privilege

The principle of least privilege guarantees that a component has the least amount of privileges needed to function. Different components need privileges (or permissions) to function. For example, an editor needs read permission to open a particular file and write permissions to modify it. Least privilege requires isolation to restrict access of the component to other parts of the system. If a component follows least privilege then any privilege that is further removed from the component removes some functionality. Any functionality that is available can be executed with the given privileges. This property constrains an attacker to the privileges of the component. In other words, each component should *only* be given the privilege it requires to perform its duty and no more. Note that privileges have a temporal component as well. For example, a web server needs access to its configuration file, the files that are served, and permission to open the corresponding TCP/IP port. The required privileges are therefore dependent on the configuration file which will specify, e.g., the port, network interface, and root directory for web files. If the web server is required to run on a privileged port (e.g., the default web ports 80 and 443) then the server must start with the necessary privileges to open a port below 1024. After opening the privileged port, the server can drop privileges and restrict itself to only accessing the root web directory and its subdirectories.

## 2.6 Compartmentalization

The idea behind compartmentalization is to break a complex system into small components that follow a well-defined communication protocol to request services from each other. Under this model, faults can be constrained to a given compartment. After compromising a single compartment, an attacker is restricted to the protocol to request services from other compartments. To compromise a remote target compartment, the attacker must compromise all compartments on the path from the initially compromised compartment to the target compartment. Compartmentalization allows abstraction of a service into small components.

Under compartmentalization, a system can check permissions and protocol conformity across compartment boundaries. Note that this property builds on least privilege and isolation. Both properties are most effective in combination: many small components that are running and interacting with least privilege.

A good example of compartmentalization is the Chromium web browser. Web browsers consist of multiple different components that interact with each other such as a network component, a cache, a rendering engine that parses documents, and a JavaScript compiler. Chromium first separates individual tabs into different processes to restrict interaction between them.

Additionally, the rendering engine runs in a highly restricted sandbox to limit any bugs in the parsing process to an unprivileged process.

## 2.7 Threat Model

A threat model is used to explicitly list all threats that jeopardize the security of a system. Threat modeling is the process of enumerating and prioritizing all potential threats to a system.

The explicit motion of identifying all weaknesses of a system allows individual threats to be ranked according to their impact and probability. During the threat modeling process, the system is evaluated from an attacker's view point. Each possible entry vector is evaluated, assessed, and ranked according to the threat modeling system. Threat modeling evaluates questions such as:

- What are the high value-assets in a system? - Which components of a system are most vulnerable? - What are the most relevant threats?
As systems are generally large and complex, the first step usually consists of identifying individual components. The interaction between components is best visualized by making any data flow between components explicit, i.e., drawing the flow of information and the type of information between components.

This first step results in a detailed model of all components and their interactions with the environment. Each component is then evaluated based on its exposure, capabilities, threats, and attack surface. The analyst iterates through all components and identifies, on a per-component basis, all possible inputs, defining valid actions and possible threats. For each identified threat, the necessary preconditions are mapped along with the associated risk and impact.

A threat model defines the environment of the system and the capabilities of an attacker. The threat model specifies the clear bounds of what an attacker can do to a system and is a precondition to reason about attacks or defenses. Each identified threat in the model can be handled through a defined mitigation or by accepting the risk if the cost of the mitigation outweighs the risk times impact. Let us assume we construct the threat model for the Unix
"login" service, namely a password-based authentication service. Our application serves three use-cases: (i) the system can authenticate a user based on a username and password through a trusted communication channel, (ii) regular users can change their own password, and (iii) super users can create new users and change any password. We identify the following components: data storage, authentication service, password changing service, and user administration service according to the use-cases above.

The service must be privileged as arbitrary users are allowed to use some aspects of the service depending on their privilege level. Our service therefore must distinguish between different types of users (administrators and regular users). To allow this distinction, the service must be isolated from unauthenticated access. User authentication services are therefore an integral part of the operating system and privileged, i.e., run with administrator capabilities.

The data storage component is the central database where all user accounts and passwords are stored.

The database must be protected from unprivileged modification, therefore only the administrator is allowed to change arbitrary entries while individual users are only allowed to change their own entry. The data storage component relies on the authentication component to identify who is allowed to make modifications.

To protect against information leaks, passwords are encrypted using a salt and one-way hash function. Comparing the hashed input with the stored hash allows checking equivalence of a password without having to store the plaintext (or encrypted version) of the password.

The authentication service takes as input a username and password pair and queries the storage component for the corresponding entry. The input (login request) must come from the operating system that tries to authenticate a user. After carefully checking if the username and password match, the service returns the information to the operating system. To protect against brute-force attacks, the authentication service rate limits the number of allowed login attempts.

The password changing service allows authenticated users to change their password, interfacing with the data storage component. This component requires a successful prior authorization and must ensure that users can only change their own password but not passwords of other users. The administrator is also allowed to add, modify, or delete arbitrary user accounts. Such an authentication system faces threats from several directions, providing an exhaustive list would go beyond the scope of this book. Instead, we provide an incomplete list of possible threats:

- Implementation flaw in the authentication service allowing either a user (authenticated or unauthenticated) to
authenticate as another user or privileged user without supplying the correct password.

- Implementation flaw in privileged user management
which allows an unauthenticated or unprivileged user to
modify arbitrary data entries in the data storage.
- Information leakage of the password from the data storage, allowing an offline password cracker to probe a large
amount of passwords1
- A brute force attack against the login service can probe
different passwords in the bounds of the rate limit.
- The underlying data storage can be compromised through
another privileged program overwriting the file, data corruption, or external privileged modification.

## 2.8 Bug Versus Vulnerability

A "bug" is a flaw in a computer program or system that results in an unexpected outcome. A program or system executes computation according to a specification.

The term "bug"
comes from a moth that deterred computation of a Harvard Mark II computer in 1947. Grace Hopper noted the system crash in the operation log as "first actual case of bug being found", see 2.1, [10]. The bug led to an unexpected termination of the current computation. Since then the term bug was used for any unexpected computation or failure that was outside of the specification of a system or program.

As a side note, while the term bug was coined by Grace Hopper, the notion that computer programs can go wrong goes back to Ada Lovelace's notes on Charles Babbage's analytical machine where she noted that "an analysing process must equally have been performed in order to furnish the Analytical Engine with the necessary operative data; and that herein may also lie a possible source of error. Granted that the actual mechanism is unerring in its processes, the cards may give it wrong orders."
A software bug is therefore a flaw in a computer program that causes it to misbehave in an unintended way while a hardware bug is a flaw in a computer system. Software bugs are due to human mistake in the source code, compiler, or runtime system. Bugs result in crashes and unintended program state. Software bugs are triggered through specific input (e.g., console input, file input, network input, or environmental input). If the bug can be controlled by an adversary to escalate privileges, e.g., gaining code execution, changing the system state, or leaking system information then it is called a vulnerability.

A vulnerability is a software weakness that allows an attacker to exploit a software bug. A vulnerability requires three key components (i) system is susceptible to flaw, (ii) adversary has access to the flaw (e.g., through information flow), and (iii) adversary has capability to exploit the flaw.

Vulnerabilities can be classified according to the flaw in the source code (e.g., buffer overflow, use-after-free, time-of-checkto-time-of-use flaw, format string bug, type confusion, or missing sanitization). Alternatively, bugs can be classified according to the computational primitives they enable (e.g., arbitrary read, arbitrary write, or code execution).

## 2.9 Summary

Software security ensures that software is used for its intended purpose and prevents unintended use that may cause harm. Security is evaluated based on three core principles: confidentiality, integrity, and availability. These principles are evaluated based on a threat model that formally defines all threats against the system and the attacker's capabilities. Isolation and least privilege allow fine-grained compartmentalization that breaks a large complex system into individual components where security policies can be enforced at the boundary between components based on a limited interface. Security relies on abstractions to reduce complexity and to protect systems [17].