def solution(sizes):
        
    answer = 0
    w = 0
    h = 0
    for size in sizes:
        if w < max(size):
            w = max(size)
        if h < min(size):
            h = min(size)
    answer = w*h
    return answer