class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def parentheses(l, r, p):
            if l == 0 and r == 0:
                result.append(''.join(p))
            if l > 0:
                p.append('(')
                parentheses(l - 1, r, p)
                p.pop()
            if l < r:
                p.append(')')
                parentheses(l, r - 1, p)
                p.pop()
        parentheses(n, n, [])
        return result


