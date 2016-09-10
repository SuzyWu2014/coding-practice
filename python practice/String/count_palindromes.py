def countPalindromes(S):
    count = 0
    for i in range(len(S)):
        count += 1
        k, t = i - 1, i + 1
        if k >= 0 and S[k] == S[i]:
            # hllh
            count += 1
            k -= 1
            count += countPalinInPosition(k, t, S)
        k, t = i - 1, i + 1
        count += countPalinInPosition(k, t, S)
        # print count
    return count

def countPalinInPosition(k, t, S):
    count = 0
    while k >= 0 and t < len(S):
        if S[k] == S[t]:
            count += 1
            k -= 1
            t += 1
        else:
            break
    # print "sub", count
    return count

print countPalindromes("hellolle")
print countPalindromes("wowpurerocks")