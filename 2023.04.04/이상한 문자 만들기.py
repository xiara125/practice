# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    answer = ''
    # 단어별로 자르기
    words = s.split(" ")
    # 단어의 개수만큼 반복
    for i in range(len(words)):
        word = words[i]
        # 각 단어의 길이만큼 반복
        for j in range(len(word)):
            if j%2 == 0 :
                answer += word[j].upper()
            else :
                answer += word[j].lower()
        answer += " "
    # 맨 마지막 공백을 없애기위해 사용
    return answer[:-1]