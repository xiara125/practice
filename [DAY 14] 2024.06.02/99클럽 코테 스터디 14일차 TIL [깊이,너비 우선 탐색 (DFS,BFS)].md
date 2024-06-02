> 99클럽 코테 스터디 14일차 TIL [깊이/너비 우선 탐색 (DFS/BFS)]
> 

# 오늘의 문제

## [Beginner] 226. Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

**Example 2:**

!https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg

```
Input: root = [2,1,3]
Output: [2,3,1]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

# 풀이

## 나의 풀이

```python
# << Fail >>  
```

## 좋아요가 가장 많은 풀이

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #Base Case
            return root
        self.invertTree(root.left) #Call the left substree
        self.invertTree(root.right)  #Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root # Return the root
```

## 생각해볼 풀이

```python
class Solution(object):
    def invertTree(self, root):
        # Base case...
        if root == None:
            return root
        # swapping process...
        root.left, root.right = root.right, root.left
        # Call the function recursively for the left subtree...
        self.invertTree(root.left)
        # Call the function recursively for the right subtree...
        self.invertTree(root.right)
        return root     # Return the root...
```

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root and TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
```

---

# 결론

## 오늘의 학습 키워드

<aside>
💡 깊이/너비 우선 탐색 (DFS/BFS)

</aside>

## 새롭게 배운 것, 다시금 깨달은 것

1. `root.left, root.right = root.right, root.left` 이 코드는 풀이가 제대로 되고
`root.left = root.right`
`root.right - root.left` 이 코드는 풀이가 제대로 되지 않는다.
swap연산을 위해서이다. 파이썬을 제외한 다른 많은 언어들은 서로의 값을 바꾸기 위해서는 바꿀 두 개의 변수와 또 다른 하나의 변수를 사용해 바꿀 두 개의 변수를 바꿀 수 있지만 파이썬은 파이썬스럽게 한줄로 적으면 두 개의 값이 서로 바뀌게 되는것이다.
그러므로 첫번째 코드는 `root.left`와 `root.right`의 값을 서로 바꾼다 다른 뜻이고 두번째 코드는 `root.left`에 `root.rifgt`값을 넣고 `root.right`에 `root.right`가 입력된 `root.left`가 대입되기에 결국 변하는게 없는 것이다.

## 오늘의 회고

새로운 개념에 이해도가 낮아 시간이 없다는 핑계로 계속 미루고 있는 기분이다. 지난 4개의 문제들을 내 힘으로 스스로 풀 수 있을 정도가 되도록 노력해보자.
LeetCode도 조금 익숙해져야 할 것같다. 프로그래머스가 아주 익숙해지고 백준이 이제 조금 익숙해지나 싶었는데 새로운게 튀어나왔다. 자주 볼 것 같은 곳인데 우리 좀 친해지자.

“#DFS #BFS #99클럽 #코딩테스트 준비 # 개발자 취업 #항해99 #TIL #LeetCode”