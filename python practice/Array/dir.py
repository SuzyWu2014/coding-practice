

def solution(S):
    res = []
    dir_dict = dict()
    str_list = S.split('\n')
    print str_list
    for i in range(len(str_list)):
        level = len(str_list[i]) - len(str_list[i].lstrip())
        dir_dict[str_list[i]] = level
    print dir_dict

    def dfs(start, str_list, pre_path, up_level):
        if start >= len(str_list):
            return
        if 'jpeg' in str_list[start]:
            print pre_path
            res.append(pre_path + "/" + str_list[start].lstrip())
            dfs(start + 1, str_list, pre_path, up_level)
        elif '.' in str_list[start]:
            pass
        elif dir_dict[str_list[start]] >= up_level:
            # TO-DO up level path
            pre_path = pre_path - "/*"
            dfs(start + 1, str_list, pre_path, dir_dict[str_list[start]])
        else:
            pre_path += "/" + str_list[start].lstrip()
            print pre_path
            dfs(start + 1, str_list, pre_path, up_level + 1)

    dfs(0, str_list, "", 1)
    print res
    return sum([len(i) - 2 for i in res])


S = """
dir1
 dir2
  image.jpeg
  r.jpeg
 dir3
  two.jpeg
    """
print solution(S)
