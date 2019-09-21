#    https://leetcode.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/

Q. You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.




sol:-->
class Solution:
    def reverseParentheses(self, s: str) -> str:
        idx = []
        pos = 0
        tmp = ""
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                idx.append(i)
            elif s[i] == ")":
                pos = idx.pop()
                tmp = s[pos + 1:i]
                s = s[:pos + 1] + tmp[::-1] + s[i:]
        print(s)
        for i in s:
            if i.isalpha():
                res += i
        return res
