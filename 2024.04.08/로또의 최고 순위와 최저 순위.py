def solution(lottos, win_nums):
    answer = []
    
    # 당첨번호와 확실하게 일치하는 번호
    def_num = set(lottos) & set(win_nums)
    
    # 로또 번호 중 모르는 번호
    indef_num = 0
    for i in lottos :
        if i == 0 :
            indef_num += 1
    
    # 최소,최대 당첨번호 개수를 담은 리스트
    my_num = [len(def_num), len(def_num) + indef_num]
    print(my_num)
    min = len(def_num)
    max = min + indef_num
    
    # 당첨내용
    prize = [6, 5, 4, 3, 2, 1]
    
    # 당첨 내용
	  # 1-5등
    for idx, num in enumerate(prize):
        for j in my_num :
            print(idx, num, j)
            if j==num:
                answer.append(idx+1)
                print(answer)
    # 6등
    for i in range(2):
	    if len(answer) < 2 :
	        answer.append(6)
    return answer