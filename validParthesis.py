
def validParthesis(s):
    
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
                
    return stack == []

s = "[()[]{}]"
s = '()'
