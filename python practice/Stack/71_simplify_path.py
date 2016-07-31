# 71. Simplify Path
# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        sub_paths = path.split('/')
        for path in sub_paths:
            if path == '.' or path == '':
                pass
            elif path == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(path)
        if stack == []:
            return '/'
        else:
            path = ''
            for item in stack:
                path += "/" + item
            return path

print Solution().simplifyPath("/a/./b/../../c/")
print Solution().simplifyPath("/../")
