class Solution:
    def isValid(self, s: str) -> bool:
        for i, myS in enumerate(s):
            if i%2 == 0 :
                print("2", i)
                if (ord(myS) == (ord(s[i+1])-1) and ord(myS) == 40) or ord(myS) == (ord(s[i+1])-2):
                    print(i, ord(myS), (ord(s[i+1])-2))
                    answer = True
                else:
                    return False
        return answer