> 99클럽 코테 스터디 13일차 TIL [깊이/너비 우선 탐색 (DFS/BFS)]
> 

# 오늘의 문제

## [Beginner] 2331. Evaluate Boolean Binary Tree

You are given the `root` of a **full binary tree** with the following properties:

- **Leaf nodes** have either the value `0` or `1`, where `0`represents `False` and `1` represents `True`.
- **Non-leaf nodes** have either the value `2` or `3`, where `2` represents the boolean `OR` and `3`represents the boolean `AND`.

The **evaluation** of a node is as follows:

- If the node is a leaf node, the evaluation is the **value** of the node, i.e. `True` or `False`.
- Otherwise, **evaluate** the node's two children and **apply** the boolean operation of its value with the children's evaluations.

Return *the boolean result of **evaluating** the* `root` *node.*

A **full binary tree** is a binary tree where each node has either `0` or `2` children.

A **leaf node** is a node that has zero children.

**Example 1:**

!https://assets.leetcode.com/uploads/2022/05/16/example1drawio1.png

```
Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
```

**Example 2:**

```
Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 3`
- Every node has either `0` or `2` children.
- Leaf nodes have a value of `0` or `1`.
- Non-leaf nodes have a value of `2` or `3`.

# 풀이

## 나의 풀이

```python
-
```

## 좋아요가 가장 많은 풀이

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root.val==0 or root.val==1:
            return root.val == 1
        elif root.val == 2:
            return self.helper(root.left) or self.helper(root.right)
        elif root.val == 3:
            return self.helper(root.left) and self.helper(root.right)
        return False

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
        
```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 깊이/너비 우선 탐색 (DFS/BFS)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

1. BFS : 큐(Queue), 선입선출(First In First Out or Last In Last Out), 큐가 나간 순서→탐색순서
2. DFS : 스택(Stack), 선입후출,후입선출(접시)

## 오늘의 회고

이제 조금씩 감이 오기 시작한다. 주말에 많은 공부를 하라고 주말에 어렵고 새로운 개념들을 적용할 수 있는 문제를 많이 받는데.. 시간을 내기가 쉽지 않다. 내일은 시간을 내서 마무리를 지을 수 있기를 바란다.

“#DFS #BFS #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #LeetCode”