class Solution:
    def isValid(self, s: str) -> bool:
        bc = ['(',')','{','}','[',']']
        result = []
        open_count = 0
        close_count = 0
        for i in s:
            if i in ['(', '{', '[']:
                result.append(i)
                close_count += 1
            if i in [')', '}', ']']:
                open_count += 1
            if len(result) > 0:
                if i == ')' and result[-1] == '(':
                    result.pop()
                if i == '}' and result[-1] == '{':
                    result.pop()
                if i == ']' and result[-1] == '[':
                    result.pop()
        if open_count != close_count:
            return False
        if len(result) == 0:
            return True
        else:
            return False
