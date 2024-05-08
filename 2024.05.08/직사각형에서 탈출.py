# x, y, w, h = map(int, input().split())
x, y, w, h = 161, 181, 762, 375

if (abs(x-w) > min(x,w) and min(abs(x-w), abs(y-h)) > min(x,w)) or (abs(y-h) > min(y,h) and min(abs(x-w), abs(y-h)) > min(y,h)):
    print(min(min(x,w), min(y,h)))
else:
    print(min(abs(x-w), abs(y-h)))
