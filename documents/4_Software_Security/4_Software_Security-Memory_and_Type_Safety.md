# Memory and Type Safety

A set of core security principles covers the security of system software. If these security principles hold then the software is secure. Memory safety ensures that pointers always point to a valid memory object, i.e., each memory access is in bounds and to a live object. Type safety ensures that objects are accessed with their corresponding types and casts observe the type hierarchy according to the true runtime type of an object. Under memory and type safety, all memory accesses adhere to the memory and type semantics defined by the source programming language. Bugs that cause the program to violate memory or type safety can be used to change the runtime state of the program. This modified runtime state leads to an execution that would not be possible under a benign execution of the program. For example, instead of encoding an image into a different format, an image program may connect to the internet and upload personal documents. Memory and type safety restrict the program behavior to what is specified in the source code. Bugs in the program logic may still allow arbitrary actions but no action that does not conform to a valid execution path in the program is possible.

For software written in high-level languages such as Java, core principles such as memory safety and type safety guarantee the absence of low-level flaws that violate the high-level abstractions of the programming language and therefore limit possible attacks to bugs inherent to the program such as logic flaws.

To be precise, memory and type safety limit attackers to a given specification and constraints of the implementation, not constraints of an underlying abstract machine. Memory unsafe languages like C/C++ do not enforce memory or type safety and data accesses can occur through stale/illegal pointers and an object may be reinterpreted under an illegal type.

The gap between the operational semantics of the programming language and the instructions provided through the underlying Instruction Set Architecture (ISA - e.g., the Intel x86 ISA defines the available instructions and their encoding on an x86 CPU) allow an attacker to step out of the restrictions imposed by the programming language and access memory out of context. If memory safety or type safety are violated, the program must no longer follow the well-defined control-flow graph and turns into a so-called weird machine [3]. You can think of a weird machine as a snapshot of the program state that was modified at a point in time. This modified memory snapshot may reuse the existing code sequences (e.g., individual instructions or short sequences of instructions) in unintended ways and out of context. Repurposing existing code snippets out of context turns a program into a weird machine. For example, in the code below, the weird machine could transfer control to notcalled by overwriting the function pointer ptr with the address of notcalled and the variable flag with a non-null value.

```
// this function is never called
**void** notcalled();

**void** addrtaken();

**int** flag = 0; 7 **void** (*ptr)() = &addrtaken;

**void** func() {
    if (flag != 0) {
        // under attack, this may call notcalled
        ptr();
    }
}
```
The need for memory or type safety checks depends on the programming language. Some languages inherently enforce memory and type safety (e.g., functional languages generally do not expose pointers to the programmer) and therefore do not require runtime checks. A low-level systems language such as C requires explicit checks to guarantee memory and type safety as the programmer is not required to add sufficient checks.

## 4.1 Pointer Capabilities

Pointers are unstructured addresses to memory and a way to reference data or code. A pointer has an associated type and a value, the address it points to. Under C/C++ pointer arithmetic allows modification of a pointer through increments and decrements. The validity of the pointer is not enforced through the programming language but must be checked by the programmer. For example, after a pointer increment the programmer must ensure that the pointer still points into a valid array. When dereferencing, the programmer is responsible to guarantee that the pointed-to object is still valid. Memory safety is a program property which guarantees that memory objects can only be accessed with the corresponding capabilities. At an abstract level, a pointer is a capability to access a certain memory object or memory region [9,21]. A pointer receives capabilities whenever it is assigned and is then allowed to access the pointed-to memory object. The capabilities of a memory object describe the size or area, validity, and potentially the type of the underlying object. Capabilities are assigned to a memory object when it is created. The initial pointer returned from the memory allocator receives these capabilities and can then pass them, through assignment, to other pointers. Memory objects can be created explicitly by calling the allocator, implicitly for global data by starting the program, or implicitly for the creation of a stack frame by calling a function. The capabilities are valid as long as that memory object remains alive. Pointers that are created from this initial pointer receive the same capability and may only access the object inside the bounds of that object, and only as long as that object has not been deallocated. Deallocation, either through an explicit call to the memory allocator or through removal of the stack frame by returning to the caller, destroys the memory object and invalidates all capabilities. Pointer capabilities cover three areas: bounds, validity, and type. The bounds of a memory object encode spatial information of the memory object. *Spatial memory safety* ensures that pointer dereferences are restricted to data *inside* of the memory object. Memory objects are only valid as long as they are allocated. *Temporal safety* ensures that a pointer can only be dereferenced as long as the underlying object *stays allocated*. Memory objects can only be accessed if the pointer has the correct type. *Type safety* ensures that the object's type is correct
(according to the type system of the programming language)
and matches one of the *compatible types* according to type inheritance. The C/C++ family of programming languages allows invalid pointers to exist, i.e., a pointer may point to an invalid memory region that is out of bounds or no longer valid.

A memory safety violation only occurs when such an invalid pointer is dereferenced.

## 4.2 Memory Safety

Memory corruption, the absence of memory safety, is the root cause of many high-profile attacks and the foundation of a plethora of different attack vectors. Memory safety is a general property that can apply to a program, a runtime environment, or a programming language. A program is memory safe, if all possible *executions* of that program are memory safe. A runtime environment is memory safe, if all runnable programs are memory safe. A programming language is memory safe, if all expressible programs are memory safe. Memory safety prohibits, e.g., buffer overflows, NULL pointer dereferences, use after free, use of uninitialized memory, or double frees. So while the C programming language is not memory safe, a C
program can be memory safe if all possible executions of the C program enforce memory safety due to sufficient memory safety checks by the programmer. Memory safety can be enforced at different layers. Languagebased memory safety makes it impossible for the programmer to violate memory safety by, e.g., checking each memory access and type cast (Java, C#, or Python) or by enforcing a strict static type system (Rust). Systems that retrofit memory safety to C/C++ are commonly implemented at the compiler level due to the availability of pointer and type information. Techniques that retrofit memory safety for C/C++ must track each pointer and its associated bounds for spatial memory safety, validity for temporal memory safety, and associated type for type safety.

## 4.2.1 Spatial Memory Safety

Spatial memory safety is a property that ensures that all memory dereferences of an application are within the bounds of their pointer's valid objects. A pointer references a specific address in an application's address space. Memory objects are allocated explicitly by calling into the memory allocator (e.g., through malloc) or implicitly by calling a function for local variables. An object's bounds are defined when the object is allocated and a pointer to the object is returned. Any computed pointer to that object inherits the bounds of the object. Pointer arithmetic may change the pointer to outside the object. Only pointers that point inside the associated object may be dereferenced. Dereferencing a pointer that points outside of the associated object results in a spatial memory safety error and undefined behavior. Spatial memory safety violations happen if a pointer is (i) incremented past the bounds of the object, e.g., in a loop or through pointer arithmetic and (ii) dereferenced:
```
**char** *c = (**char***)malloc(24); 
for (int i = 0; i < 26; ++i) {
    // 1.) buffer overflow for i >= 24
    c[i] = 'A' + i;
} 
// 2.) violation through a direct write
c[26] = 'A'; 
c[-2] = 'Z'; 
// 3.) invalid pointers: OK if not dereferenced
**char** *d = c+26;
d -= 3; 
*d = 'C';
```
This example shows a classic overflow where an array is sequentially accessed past its allocated length. The iterator moves past the end of the allocated object and as soon as the pointer is dereferenced (to write), memory safety is violated, corrupting an adjacent memory object. In the second case, memory safety is violated through a direct overwrite where the index points outside of the bounds of the object. The third case is fine as the invalid pointer is never dereferenced. The C standard allows pointers to become invalid as long as they are not used. For example, a pointer can be incremented past the bounds of the object. If it is decremented, it may become valid again. Note that a pointer may only become valid again for spatial safety. If the underlying object has been freed, the pointer cannot become valid again.

## 4.2.2 Temporal Memory Safety

Temporal memory safety is a property that ensures that all memory dereferences are valid at the time of the dereference, i.e., the pointed-to object is the same as when the pointer was created. When an object is freed (e.g., by calling free for heap objects or by returning from a function for stack objects), the underlying memory is no longer associated to the object and the pointer is no longer valid. Dereferencing such an invalid pointer results in a temporal memory safety error and undefined behavior.

Various forms of temporal memory safety violations exist. After allocation, memory of an object can be read before it is written, returning data from the previously allocated object in that area.

A stale pointer can be used after the underlying object has been returned to the memory allocator and even after that memory has been reused for a different object. Temporal memory safety violations happen if the underlying memory object was freed as shown in the following example:
```
**char** *c = malloc(26);
**char** *d = c;
free(d);
// violation as c no longer points to a valid object
c[23] = 'A';
```

## 4.2.3 A Definition Of Memory Safety

Memory safety is violated if undefined memory is accessed, either out of bounds or the underlying memory was returned to the allocator. When evaluating memory safety, pointers become capabilities, they allow access to a well-defined region of allocated memory. A pointer becomes a tuple of address, lower bound, upper bound, and validity. Pointer arithmetic updates the tuple. Memory allocation updates validity. Dereference checks capability. These capabilities are implicitly added and enforced by the compiler. Capability-based memory safety enforces type safety for two types: pointer-types and scalars. Pointers (and their capabilities) are only created in a safe way. Pointers can only be dereferenced if they point to their assigned, still valid region.

## 4.2.4 Practical Memory Safety

In *Java*, memory safety is enforced by the programming language and the runtime system. The programming language replaces pointers with references and direct memory access is not possible. There is no way to explicitly free and return data to the runtime system, memory is implicitly reclaimed through garbage collection. The runtime system enforces memory through additional checks (e.g., bounds checks) and leverages a garbage collector to passively reclaim unused memory. Note that Java also enforces type safety with explicit type safety checks. For *Rust*, a strict type system and ownership implements memory and type safety. References are bound to variables and clear ownership protects against data races: single mutable reference or zero or more immutable references. Memory is reclaimed when variables go out of scope. Interestingly, many of these guarantees can be enforced by the compiler resulting in zero-cost abstractions. Non-system functional languages such as Haskell or OCaml are oblivious to memory violations as they do not require the concept of references but pass data and control in other forms. See Section 6.2 for a short discussion on language-based security. For *C/C++* there are two approaches to achieve memory safety: either removing unsafe features by creating a dialect or to protect the use of unsafe features through instrumentation. Dialects extend C/C++ with safe pointers and enforce strict propagation rules. Cyclone [12] restricts the C programming language to a safe subset by limiting pointer arithmetic, adding NULL checks, using garbage collection for heap and region lifetimes for the stack (one of the inspirations for Rust's lifetimes), tagged unions to restrict conversions, splitting pointers into the three classes normal, never NULL, fat pointers, and replacing setjmp (setjmp provides an archaic form of handling special cases, allowing the developer to record a return point and then jump to that point on demand) with exceptions and polymorphism. Cyclone enforces both spatial and temporal memory safety. CCured [23] follows a similar idea and introduces a pointer inference system to reduce the overhead of pointer tagging and pointer tracking. Similarly, modern C++ variants such as C++1X support a memory safe subset that uses references and strict ownership for memory objects to track lifetimes. Whenever only the safe subsets are used, C++ can be memory (and type) safe. Protecting the use of unsafe features requires a runtime system to keep track of all live objects and pointers, associating bounds with each pointer and liveness with each memory object. For each pointer dereference a bounds and liveness check ensures that the memory access is valid. For pointer assignments, the pointer inherits the bounds of the assigned reference. SoftBound [21] is a compiler-based instrumentation to enforce spatial memory safety for C/C++. The general idea is to keep information about all pointers in *disjoint* metadata, indexed by pointer location. The downside of the approach is an overhead of 67% for SPEC CPU2006.
```
**struct** BankAccount {
    char acctID[3]; **int** balance;
} b;
b.balance = 0;
**char** *id = &(b.acctID);
// Instrumentation: store bounds 
lookup(&id)->bse = &(b.acctID); 
lookup(&id)->bnd = &(b.acctID)+3; 
// --
**char** *p = id; // local, remains in register
// Instrumentation: propagate information
**char** *p_bse = lookup(&id)->bse; 
**char** *p_bnd = lookup(&id)->bnd;
// --
do {
    char ch = readchar();
    // Instrumentation: check bounds
    check(p, p_bse, p_bnd);
    // --
    *p = ch;
    p++;
} **while** (ch);
```
The code example shows the instrumentation for SoftBound.

Allocated memory is instrumented to return bounds (allocated on a per-pointer basis). Pointer assignment propagates bounds.

Whenever the pointer is dereferenced for reading or writing, the bounds are checked. CETS [22], an extension for SoftBound, enforces temporal memory safety by storing validity for each object and pointer. CETS leverages memory object versioning. The code instrumentation allocates a unique version to each allocated memory area and stores this version in the pointer metadata as well. Each deallocation is instrumented to destroy the version in the object's memory area, causing the pointer and object version to become out of sync. Upon dereference, CETS checks if the pointer version is equal to the version of the memory object.

There are two failure conditions: either the area was deallocated and the version is smaller (0) or the area was reallocated to a new object and the version is bigger. Both error conditions result in an exception and terminate the program.

The instrumentation and metadata can be carried out with different trade-offs regarding performance, memory overhead, and hardware extensions [5,15,20].

## 4.3 Type Safety

Well-typed programs cannot "go wrong".
(Robin Milner)

Type-safe code accesses only well-typed objects it is authorized to access. The literature groups type safety into different classes: strongly typed or weakly typed (with implicit type conversion).

The type system can orthogonally be either static or dynamic.

Despite a lot of research in type safety, C/C++ which are not type safe remain popular languages. Note that full type safety does not imply memory safety. The two properties are distinct.

A C++ program can be type safe but not memory safe, e.g., an array index may point outside of the bounds of an array in a perfectly type safe program, resulting in a memory safety violation. Similarly, memory safety does not imply type safety as a char * array may be wrongly interpreted as an object of a specific type.

Type safety is a programming language concept that assigns each allocated memory object an associated type. Typed memory objects may only be used at program locations that expect the corresponding type. Casting operations allow an object to be interpreted as having a different type. Casting is allowed along the inheritance chain. Upward casts (upcasts) move the type closer to the root object, the type becomes more generic, while downward casts (downcasts) specialize the object to a subtype. For C, the type lattice is fully connected, any pointer type can be cast to any other pointer types with the validity of the cast being the responsibility of the programmer. In C++ there are several casting operations.

The most common ones are static and dynamic casts.

A static cast static_cast<ToClass>(Object) results in a compile time check where the compiler guarantees that the type of Object is somehow related to ToClass, without executing any runtime check.

A dynamic_cast<ToClass>(Object) results in a runtime check but requires Runtime Type Information (RTTI) and is only possible for polymorphic classes (i.e., they must have a vtable pointer in the object itself that uniquely identifies the class). Due to the runtime check, this type of cast results in performance overhead.
```
class Base { **int** base; };

class Exec: public Base {

    public:
        virtual **void** exec(**const char** *prg) {
        system(prg);
    }
};
class Greeter: public Base {
    public:
        int loc;
        virtual **void** sayHi(**const char** *str) {
            std::cout << str << std::endl;
    }
};
**int** main() {
    Base *b1 = new Greeter();
    Base *b2 = new Exec();
    Greeter *g;

    g = static_cast<Greeter*>(b1);
    g->sayHi("Greeter says hi!");

    // Type confusion
    g = static_cast<Greeter*>(b2);

    // execute Exec::exec instead of Greeter::sayHi
    // Low-level implementation: g[0][0](str);
    g->sayHi("/usr/bin/xcalc");
    g->loc = 12; // memory safety violation

    delete b1;
    delete b2;
}
```
In the code example above, an object of type Greeter is allocated and then upcast to a Base type. Later, the Base type is downcast into Exec. As the runtime type of the object is Greeter, this downcast is illegal and results in type confusion
- a violation of type safety.

In low-level languages like C or C++, type safety is not explicit and a memory object can be reinterpreted in arbitrary ways. C++ provides a complex set of type cast operations. Static casts are only checked at compile time to check if the two types are compatible. Dynamic casts execute a slow runtime check, which is only possible for polymorphic classes with virtual functions as otherwise, no vtable pointer - to identify the object's type - is available in the memory object layout. Reinterpret casts allow reclassification of a memory object under a different type. Static casts have the advantage that they do not incur any runtime overhead but are purely checked at compile time. Static casts lack any runtime guarantees and objects of the wrong type may be used at runtime. For example, the figure below shows a type violation where an object of the base type can be used as a subtype after an illegal downcast. Reinterpretation of casts allows the programmer to explicitly break the underlying type assumptions and reassign a different type to the pointer or underlying memory object. Due to the low-level nature of C++, a programmer may write to the raw memory object and change the underlying object directly. Ideally, a program can statically be proven type safe. Unfortunately, this is not possible for C/C++ due to the generalicity of the underlying type system and the opportunity to handle raw memory. Defenses therefore have to resort to runtime Greeter *g = new Greeter(); Base *b = static_cast<Base*>(g); Exec *e = static_cast<Exec*>(b);
Example of a type confusion vulnerability due to an illegal downcast. checks. By making all casts in the program explicit and checking them for correctness at runtime, we ensure that the runtime type conforms to the statically assumed type at compile time [8,11,18,28]. Such a solution must keep metadata for all allocated memory objects, similarly to memory safety. Instead of bounds, a type safety mechanism records the true type of each allocated object. All cast types in C++ are then replaced with a runtime check.

## 4.4 Summary

Memory and type safety are the root cause of security vulnerabilities. Memory safety defines spatial and temporal capabilities for pointers. Spatial memory safety guarantees that pointers can only access objects in the corresponding bounds. Temporal memory safety checks for liveness of the underlying object.

When both spatial and temporal memory safety are enforced then a pointer is locked to a given memory object and can only dereference the area inside the object as long as that object is valid. Type-safe code accesses only the memory locations it is authorized to access. Type safety ensures that each object is only used with its correct type.