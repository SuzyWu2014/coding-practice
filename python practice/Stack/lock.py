def varifyLog(lines):
    stack = []
    threads = set()
    for i, line in enumerate(lines):
        words = line.split()
        action = words[0]
        thread_id = int(words[1])
        if action == "ACQUIRE":
            if thread_id not in threads:
                stack.append(thread_id)
                threads.add(thread_id)
            else:
                return i + 1
        else:
            pop_thread = stack.pop()
            if pop_thread != thread_id:
                return i + 1
            else:
                threads.remove(thread_id)
    if len(stack) == 0:
        return 0
    else:
        return len(lines) + 1


log = ["ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364"]
log = ["ACQUIRE 364", "ACQUIRE 84", "RELEASE 364", "RELEASE 84"]
log = ["ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 456"]
log = ["ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 789", "RELEASE 456", "RELEASE 123"]
log = ["ACQUIRE 364", "ACQUIRE 84", "ACQUIRE 364","RELEASE 364", "ACQUIRE 789", "RELEASE 456", "RELEASE 123"]
print(varifyLog(log))
