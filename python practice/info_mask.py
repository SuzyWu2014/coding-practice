# -*- coding: utf-8 -*-

import re


def info_mask(s):
    typ, info = s.split(":")
    info = info.strip()
    print info
    if typ == 'E' and re.match(r'^[^\.].*', info) and re.match(r'.*[^\.]@.*', info) and re.match(r'.*\.\..*', info) is None and re.match(r'[\w\.!#$%&’*+-/=?^_`{|}~]*@.*\..*', info):
            name, domain = info.strip().split("@")
            name = name[0] + "*****" + name[len(name) - 1]
            print typ + ":" + name + "@" + domain
    elif typ == 'P' and re.match(r"\+?([\d]{0,3})[\s\(\)-]([\d]{3})[\s\(\)-]([\d]{3})[\s\(\)-]([\d]{4})", info):
        nums = info[len(info) - 4:]
        cnt_nums = sum([1 for i in xrange(len(info) - 4) if '0' <= info[i] <= '9'])
        if  6 <= cnt_nums <= 9:
            pre = "*" * (cnt_nums % 3)
            pre = "***-***-" if len(pre) == 0 else pre + "-***-***-"
            if info[0] == '+':
                pre = "+" + pre
            print "P:%s%s" % (pre, nums)

info_mask("E:s..uzy@gmail.com")
info_mask("E:suzy.@gmail.com")
info_mask("E:.suzy@gmail.com")
info_mask("E:!suzy@gmail.com")
# info_mask("P:+1-917-123-2345")
# info_mask("P:+1-917 123-2345")


r'^[^\.].*'
r'.*[^\.]$@.'
r'\.\2'
r'[\w\.!#$%&’*+-/=?^_`{|}~]*@.*\..*'


"\+?[\d\s\(\)-]*$"