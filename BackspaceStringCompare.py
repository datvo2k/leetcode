"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in s:
            if i != "#":
                s_stack.append(i)
            else:
                if len(s_stack) > 0:
                    s_stack.pop()

        for i in t:
            if i != "#":
                t_stack.append(i)
            else:
                if len(t_stack) > 0:
                    t_stack.pop()

        return ''.join(s_stack) == ''.join(t_stack)
        
