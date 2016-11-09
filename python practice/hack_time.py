def get_key():
    org = list("YourfriendAlice")
    aft = list("AtvthrqgseCnikg")
    res = [ord(i) - ord(j) for (i, j) in zip(aft, org)]

    print res

get_key()

"5122082"

org = "Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg"
def  decrypt(encrypted_message):
    keys, i = [8, 2, 5, 1, 2, 2, 0], 0
    res = []
    for letter in encrypted_message:
        key = keys[i % 7]
        if  (ord('a') <= ord(letter) <= ord('z')) or (ord('A') <= ord(letter) <= ord('Z')):
            decrypted = ord(letter) - key
            if decrypted < ord('A'):
                decrypted = ord('Z') - (ord('A') - decrypted) + 1
            if  ord(letter) >= ord('a') and decrypted < ord('a'):
                decrypted = ord('z') - (ord('a') - decrypted) + 1
            res.append(chr(decrypted))
            i += 1
        else:
            res.append(letter)

    return "".join(res)


print 108 % 7, 108 // 7
print ord('k') - ord('i')
print decrypt(org)
get_key()