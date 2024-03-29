def solution(phone_number):
    answer = ''
    if len(phone_number) < 5:
        answer = phone_number

    for i in range (len(phone_number)-4) :
        phone_number = list(phone_number)
        phone_number[i] = '*'
        answer = ''.join(phone_number)
    return answer
