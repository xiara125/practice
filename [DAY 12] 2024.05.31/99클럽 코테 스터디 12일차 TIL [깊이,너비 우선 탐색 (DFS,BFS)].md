> 99클럽 코테 스터디 12일차 TIL [깊이/너비 우선 탐색 (DFS/BFS)]
> 

# 오늘의 문제

## [Beginner] 1379. **Find a Corresponding Node of a Binary Tree in a Clone of That Tree**

Given two binary trees `original` and `cloned` and given a reference to a node `target` in the original tree.

The `cloned` tree is a **copy of** the `original` tree.

Return *a reference to the same node* in the `cloned` tree.

**Note** that you are **not allowed** to change any of the two trees or the `target` node and the answer **must be** a reference to a node in the `cloned` tree.

**Example 1:**

!https://assets.leetcode.com/uploads/2020/02/21/e1.png

```
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

```

**Example 2:**

!https://assets.leetcode.com/uploads/2020/02/21/e2.png

```
Input: tree = [7], target =  7
Output: 7

```

**Example 3:**

!https://assets.leetcode.com/uploads/2020/02/21/e3.png

```
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

```

**Constraints:**

- The number of nodes in the `tree` is in the range `[1, 104]`.
- The values of the nodes of the `tree` are unique.
- `target` node is a node from the `original` tree and is not `null`.

**Follow up:** Could you solve the problem if repeated values on the tree are allowed?

# 풀이

## 나의 풀이

```python
-
```

## 좋아요가 가장 많은 풀이

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        
        if original == target:
            return cloned

        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 깊이/너비 우선 탐색 (DFS/BFS)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

## 오늘의 회고

아직도 DFS, BFS를 잘 모르겠다. 시간을 많이 쏟지 못한 부분도 있지만 매우 생소한 개념이다. 내일 확실하게 짚고 넘어가야할 부분이다.

“#깊이/너비 우선 탐색 (DFS/BFS) #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #LeetCode”