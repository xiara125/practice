> 99클럽 코테 스터디 15일차 TIL [깊이/너비 우선 탐색 (DFS/BFS)]
> 

# 오늘의 문제

## [Beginner] 104.Maximun Depth of Binary

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

!https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `100 <= Node.val <= 100`

# 풀이

## 나의 풀이

```python
# DFS(깊이우선탐색)
class Solution:
     def maxDepth(self, root: Optional[TreeNode]) -> int:
         if not root:
             return 0
         max_depth = 0
         my_stack = [(root,1)]
         while my_stack:
             node,depth = my_stack.pop()
             max_depth = max(depth,max_depth)
             if node.left:
                 my_stack.append((node.left,depth+1))
             if node.right:
                 my_stack.append((node.right,depth+1))
         return max_depth
```

```python
# 재귀
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
```

## 좋아요가 가장 많은 풀이

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 깊이/너비 우선 탐색 (DFS/BFS)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

1. 재귀함수(Recursive Function) : 자기 자신을 다시 호출하는 함수
- 종료 조건을 반드시 명시해야한다. 하지않으면 무한 루프! (if문이나 while문 사용하여 종료 조건을 만들자)
- 내부적으로 스택 자료구조와 동일하다
2. DFS(Depth-First Search) : 깊이우선탐색
- Recursion - Call Stack
- Interation - Stack
(Stack : First In First Out)
3. BFS(Breadth-First Search) : 너비우선탐색
- Queue
(Queue : First In Last Out)

## 오늘의 회고

재귀함수를 많이 보아왔지만 코드를 이해하는데 그쳤고 많이 사용하지 못했다. 문제를 해결하는 참 멋있는 방법이다. 적절한 곳에 적절하게 쓰일 수 있도록 더 많은 이해와 노력이 필요하다.

“#DFS #BFS #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #LeetCode #104”