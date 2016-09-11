## Deadlock Conditions

In order for a deadlock to occur, you must have the following four conditions met:

1. Mutual Exclusion: Only one process can use a resource at a given time.
2. Hold and Wait: Processes already holding a resource can request new ones.
3. No Preemption: One process cannot forcibly remove another process’ resource.
4. Circular Wait: Two or more processes form a circular chain where each process is waiting on another resource in the chain.

## Deadlock Prevention

Deadlock prevention essentially entails removing one of the above conditions, but many of these conditions are difficult to satisfy. For instance, removing #1 is difficult because many resources can only be used by one process at a time (printers, etc). Most deadlock prevention algorithms focus on avoiding condition #4: circular wait.

## 18.1 What’s the difference between a thread and a process?

Processes and threads are related to each other but are fundamentally different.
A process can be thought of as an instance of a program in execution. Each process is an independent entity to which system resources (CPU time, memory, etc.) are allocated and each process is executed in a separate address space. One process cannot access the variables and data structures of another process. If you wish to access another process’ resources, inter-process communications have to be used such as pipes, files, sockets etc.
A thread uses the same stack space of a process. A process can have multiple threads. A key difference between processes and threads is that multiple threads share parts of their state. Typically, one allows multiple threads to read and write the same memory (no processes can directly access the memory of another process). However, each thread still has its own registers and its own stack, but other threads can read and write the stack memory.
A thread is a particular execution path of a process; when one thread modifies a process resource, the change is immediately visible to sibling threads.

