def info_mask():
    typ, info = raw_input().strip().split(":")
    if typ == 'E':
        name, domain = info.strip().split("@")
        name = name[0] + "*****" + name[len(name) - 1]
        print typ + ":" + name + "@" + domain
    else:
        nums = info[len(info) - 4:]
        cnt_nums = sum([1 for i in xrange(len(info) - 4) if '0' <= info[i] <= '9'])
        pre = "*" * (cnt_nums % 3)
        pre = "***-***-" if len(pre) == 0 else pre + "-***-***-"
        if info[0] == '+':
            pre = "+" + pre
        print typ + ":" + pre + nums

info_mask()