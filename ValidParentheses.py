"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:

        # Check is even number of brackets
        if len(s)%2 != 0:
            return False
     
        # Set of opening brackets
        opening = set('([{') 
     
        # Matching Pairs
        matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
     
        # Use a list as a "Stack"
        stack = []
     
        # Check every parenthesis in string
        for paren in s:
         
            # If its an opening, append it to list
            if paren in opening:
                stack.append(paren)
         
            else:
             
                # Check that there are parentheses in Stack
                if len(stack) == 0:
                    return False
             
                # Check the last open parenthesis
                last_open = stack.pop()
             
                # Check if it has a closing match
                if (last_open,paren) not in matches:
                    return False
             
        return len(stack) == 0