> 99클럽 코테 스터디 16일차 TIL [탐욕법]
> 

# 오늘의 문제

## [Beginner] 체육복

### **문제 설명**

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 전체 학생의 수는 2명 이상 30명 이하입니다.
- 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

### 입출력 예

| n | lost | reserve | return |
| --- | --- | --- | --- |
| 5 | [2, 4] | [1, 3, 5] | 5 |
| 5 | [2, 4] | [3] | 4 |
| 3 | [3] | [1] | 2 |

### 입출력 예 설명

예제 #1

1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2

3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

# 풀이

## 나의 풀이

```python
# 실패한 풀이

def solution(n, lost, reserve):
    answer = 0
    lost, reserve = sorted(lost), sorted(reserve)
    
    if lost == reserve:
        return n
    
    for los in lost:
        if los in reserve:
            reserve.remove(los)
            lost.remove(los)
            print("los", los, reserve, lost)
    
    for reser in reserve:
        print(reser)
        if reser-1 in lost:
            lost.remove(reser-1)

        elif reser+1 in lost:
            lost.remove(reser+1)

            
    answer = n-len(lost)
    return answer
```

```python
# 성공한 풀이

def solution(n, lost, reserve):
    
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for reser in sorted(new_reserve):
        if reser-1 in new_lost:
            new_lost.remove(r-1)
        elif reser+1 in new_lost:
            new_lost.remove(r+1)
    
    return n - len(new_lost)
```

## 좋아요가 가장 많은 풀이

```python
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
```

## 생각해볼 풀이

```python
def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        for x in range(l-1, l+2):
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved
```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 탐욕법(Greedy)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

1. 체육복을 잃어버렸지만 여유 체육복을 가지고 있는 학생을 체육복을 빌려줄 수 있는 학생 목록에서 지우기위해 for문을 사용했는데 remove()를 통해 지우는 반복중 반복하는 리스트를 수정하게 되므로 오류가 발생할 수 있다. 
→ 그 문제는 set()을 이용해 중복된 요소를 정리해주었다
: 훨씬 간단하면서 깔끔해지는 코드다
2. 시간복잡도 : 프로그램이나 알고리즘이 실행되는데 걸리는 시간을 표현하는 방식(컴퓨터가 문제를 해결하는데 얼마나 시간이 걸리는가?)
O(1) : 상수 시간 복잡도
- 문제의 크기와 상관 없이 항상 일정한 시간이 걸리는 경우
O(n) : 선형 시간 복잡도
- 문제의 크기에 비례해서 시간이 걸리는 경우
O(n^2) : 이차 시간 복잡도
- 문제의 크기에 대해 시간이 제곱으로 증가하는 경우
O(log n) : 로그 시간 복잡도
- 문제의 크기가 커질수록 시간이 느리게 증가하는 경우
시간복잡도가 중요한 이유 : 프로그램을 빨리 실행시키기 위해. 프로그램 시간을 줄이기 위해
3. 탐욕법(진짜 그 탐욕스럽다 할 때 탐욕) : 문제해결을 위해 형재 순간에서 가장 좋은 선택을 반복해서 최종 해결책을 찾는 방법
- 각 단계에서 최선의 선택을 해서 문제를 해결하는 방법이다. 단순하고 빠르게 해결책을 찾을 수 있지만 항상 최적의 해결책을 보장하지는 않는다. 따라서 적합한 때를 잘 찾는것이 중요하다.

## 오늘의 회고

생각이 갇히면 비효율적인 방식에서 벗어날 수 없다. 작성한 코드가 아깝더라도 새롭게 시작하는 마음으로 시간을 좀 가진 뒤 다시 문제를 바라보면 새로운 관점으로 더 나은 풀이를 얻을 수 있다.

“#탐욕법 #Greedy #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #Programmers”