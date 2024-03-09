# Stack question - 

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# explain my thought :
# stack: is that first in last out: so checking variable, if I find '(', get ')', ...
# how to compare ???


def findMatch(string):
    new_string = ""
    for i in string:
        if i == '(':
            new_string += ')'
        if i == ')':
            new_string += '('
        if i == '[':
            new_string += ']'
        if i == ']':
            new_string += '['
        if i == '{':
            new_string += '}'
        if i == '}':
            new_string += '{'

    print(new_string)
    # print(len(new_string))
    # compare = len(new_string) - len(string)
    # print(compare)
    # if (len(new_string) - len(string)) %2 == 0:
    #     # print(True)
    #     return True
    # return False
    return

s = '()'
findMatch(s)

s = '()[]{}'
findMatch(s)

s = '(]'
findMatch(s)