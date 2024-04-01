def solution(price, money, count):
    answer = 0

    total_prise = 0
    for i in range (count):
        total_prise += price*(i+1)

        if money-total_prise < 0:
            answer = total_prise - money
        else:
            answer = 0

    return answer