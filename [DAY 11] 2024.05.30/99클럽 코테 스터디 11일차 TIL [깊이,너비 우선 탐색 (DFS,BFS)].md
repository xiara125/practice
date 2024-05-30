> 99클럽 코테 스터디 11일차 TIL [깊이/너비 우선 탐색 (DFS/BFS)]
> 

# 오늘의 문제

## [Beginner] 938.Range Sum of BST

Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range* `[low, high]`.

**Example 1:**

!https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

```

**Example 2:**

!https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 2 * 104]`.
- `1 <= Node.val <= 105`
- `1 <= low <= high <= 105`
- All `Node.val` are **unique**.

# 풀이

## 나의 풀이

```python
# Runtime 114ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]        
        range_sum = 0
        
        while stack:
            node = stack.pop()
            
            if node:
                if low < node.val:
                    stack.append(node.left)
                
                if node.val < high:
                    stack.append(node.right)
                
                if low <= node.val <= high:
                        range_sum += node.val
                        
        return range_sum
```

## 좋아요가 가장 많은 풀이

```python
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```

## 생각해볼 풀이

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)
```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 깊이/너비 우선 탐색 (DFS/BFS)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

1. DFS : 깊이 우선 탐색
< 설명 >
1. 루트노드에서 시작하여 다음 분기로 넘어가기 전, 해단 분기를 완벽하게 탐색하는 방법(자식 우선)
2. 스택이나 재귀함수로 구현
3. 한 노드에서 제일 마지막 자식까지 탐색하고 돌아오는 과정을 “백트리킹”이라고 한다
< 장점 >
1. 현재 경로상의 노드들만 기억하면 되므로 저장 공간의 사용률이 비교적 적음
2. 목표 노드가 깊은 단계에 있는 경우 BFS보다 해를 빨리 구할 수 있음
3. BFS보다 구현이 간단함
< 단점 >
1. 단순 검색 속도가 BFS보다 느림
2. 해가 없는 경우에 빠질 수 있어 사전에 한계점을 기정할 필요가 있음

2. BFS : 넓이 우선 탐색
< 설명 >
1. 루트노드에서 시작하여 인접한 노드부터 탐색하는 방법
2. 큐를 이용하여 구현
3. 최단거리를 구하는 문제에서 자주 사용
< 장점 >
1. 단순 검색 속도가 DSF보다 빠름
2. 최단거리를 구하는데 최적화
< 단점 >
1. 가까운 정점을 모두 저장해놓고 순서대로 방문하므로 저장 공간의 사용이 비교적 많다.

## 오늘의 회고

오늘 처음 배우는 개념이라 문제를 푸는데 어려움을 겪어가며 문제를 마주했다. DFS와 BFS의 차이는 이해했지만 구체적으로 어떻게 적용해야하는지가 미지수이다. 
코딩테스트에 통과하려면 무조건 풀어야 하는 문제 유형이라고 하는데;… 힘내자.

“#깊이/너비 우선 탐색 (DFS/BFS) #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #Leetcode”