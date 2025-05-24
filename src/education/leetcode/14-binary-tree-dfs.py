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


if __name__ == "__main__":
    # print(Solution_144().preorderTraversal(root))
    # print(Solution_104().maxDepth(root))
    # print(Solution_404().sumOfLeftLeaves(root))
    print(Solution_112().hasPathSum(root, 10))
