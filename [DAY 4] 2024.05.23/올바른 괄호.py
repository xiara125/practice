def solution(s):
    answer = True
    mapping = {")":"("}
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack or mapping[i] != stack.pop():
                return False
                    
    return not stack