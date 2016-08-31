def countPalindromes(string):
    count = 0
    for i in range(len(string)):
        count += 1
        k, t = i - 1, i + 1
        if k >= 0 and string[k] == string[i]:
            # hllh
            count += 1
            k -= 1
            count += countPalinInPosition(k, t, string)
        k, t = i - 1, i + 1
        count += countPalinInPosition(k, t, string)
        # print count
    return count

def countPalinInPosition(k, t, string):
    count = 0
    print k, t
    while k >= 0 and t < len(string):
        if string[k] == string[t]:
            count += 1
            k -= 1
            t += 1
        else:
            break
    # print "sub", count
    return count

print countPalindromes("hellolle")
print countPalindromes("wowpurerocks")