class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []
        for comp in components:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        return '/' + '/'.join(stack)
