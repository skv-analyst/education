from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):

        root = self

        if not root:
            return "[]"
        output = []
        queue = [root]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output.append("null")
                continue

            output.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        while output[-1] == "null":
            output.pop()

        return "[" + ",".join(output) + "]"


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(",")]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


# 144. Binary Tree Preorder Traversal
root = stringToTreeNode("[1,2,5,3,4]")


class Solution_144:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            cur = stack.pop()
            ans.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return ans


# 104. Maximum Depth of Binary Tree
class Solution_104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [(root, 1)]
        ans = 0

        while stack:
            cur, depth = stack.pop()
            ans = max(ans, depth)

            if cur.left:
                stack.append((cur.left, depth + 1))
            if cur.right:
                stack.append((cur.right, depth + 1))

        return ans


# 404. Sum of Left Leaves
class Solution_404:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ans = 0
        stack = [(root, False)]

        while stack:
            cur, is_left = stack.pop()

            if is_left and not cur.left and not cur.right:
                ans += cur.val

            if cur.left:
                stack.append((cur.left, True))
            if cur.right:
                stack.append((cur.right, False))

        return ans


# 112. Path Sum
class Solution_112:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            cur, cur_sum = stack.pop()
            cur_sum -= cur.val

            if not cur.left and not cur.right and cur_sum == 0:
                return True

            if cur.left:
                stack.append((cur.left, cur_sum))
            if cur.right:
                stack.append((cur.right, cur_sum))

        return False


# 100. Same Tree
class Solution_100:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p, q)]

        while stack:
            p, q = stack.pop()

            if p and not q:
                return False

            if not p and q:
                return False

            if not p and not q:
                pass

            if p and q:
                if p.val == q.val:
                    pass

                if p.val != q.val:
                    return False

                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True


# 226. Invert Binary Tree
class Solution_226:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        stack = [root]

        while stack:
            cur = stack.pop()

            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root


# 700. Search in a Binary Search Tree
class Solution_700:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        # Time: O(n)
        # Space: O(h)
        # while stack:
        #     cur = stack.pop()

        #     if cur.val == val:
        #         return cur

        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)

        # Time: O(log_n)
        # Space: O(1)
        while stack:
            cur = stack.pop()

            if cur.val == val:
                return cur

            if val < cur.val:
                if cur.left:
                    stack.append(cur.left)
            else:
                if cur.right:
                    stack.append(cur.right)


# 98. Validate Binary Search Tree
class Solution_98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, -float("inf"), float("inf"))]

        while stack:
            cur, lo, hi = stack.pop()

            if not lo < cur.val < hi:
                return False

            if cur.left:
                stack.append((cur.left, lo, cur.val))
            if cur.right:
                stack.append((cur.right, cur.val, hi))

        return True


# 257. Binary Tree Paths
class Solution_257:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        stack = [(root, "")]

        while stack:
            cur, path = stack.pop()
            path += str(cur.val) + "->"

            if not cur.left and not cur.right:
                ans.append(path[:-2])

            if cur.left:
                stack.append((cur.left, path))
            if cur.right:
                stack.append((cur.right, path))

        return ans


class Solution_257_2:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        stack = [(root, [])]

        while stack:
            cur, path = stack.pop()
            path.append(str(cur.val))

            if not cur.left and not cur.right:
                ans.append("->".join(path))

            if cur.left:
                stack.append((cur.left, path.copy()))
            if cur.right:
                stack.append((cur.right, path.copy()))

        return ans


# 113. Path Sum II
class Solution_113:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        ans = []

        stack = [(root, [])]

        while stack:
            cur, path = stack.pop()
            path.append(cur.val)

            if not cur.left and not cur.right and sum(path) == targetSum:
                ans.append(path)

            if cur.left:
                stack.append((cur.left, path.copy()))
            if cur.right:
                stack.append((cur.right, path.copy()))

        return ans


if __name__ == "__main__":
    # print(Solution_144().preorderTraversal(root))
    # print(Solution_104().maxDepth(root))
    # print(Solution_404().sumOfLeftLeaves(root))
    # print(Solution_112().hasPathSum(root, 10))
    # print(Solution_100().isSameTree(root, root))
    # print(Solution_226().invertTree(root))
    # print(Solution_700().searchBST(root, 3))
    # print(Solution_98().isValidBST(root))
    # print(Solution_257().binaryTreePaths(root))
    print(Solution_113().pathSum(root, 10))
