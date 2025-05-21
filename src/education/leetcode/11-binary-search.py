from string import ascii_lowercase


def show_result(examples, solution, is_dict=None):
    for i, v in enumerate(examples):
        if is_dict:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")
        else:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")


# 704. Binary Search
examples_704 = [
    {"nums": [-1, 0, 3, 5, 9, 12], "target": 9},
    {"nums": [-1, 0, 3, 5, 29, 12], "target": 2}
]


def solution_704(nums, target):
    # Time: O(log n)
    # Space: O(1)
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            l = mid + 1

        else:
            r = mid - 1

    return -1


# 374. Guess Number Higher or Lower
examples_374 = [

]


def solution_374(n):
    # Time: O(log n)
    # Space: O(1)
    def guess():
        pass

    l, r = 1, n

    while l <= r:
        mid = (l + r) // 2

        if guess(mid) == 0:
            return mid

        if guess(mid) == -1:
            r = mid - 1

        else:
            l = mid + 1

    return -1


# 278. First Bad Version
examples_278 = [

]


def solution_278(n):
    # Time: O(log n)
    # Space: O(1)
    def isBadVersion(mid):
        pass

    l, r = 1, n

    while l <= r:
        mid = (l + r) // 2

        if isBadVersion(mid):
            r = mid - 1
        else:
            l = mid + 1

    # Когда пройдем весь цикл, то левый указатель остановится на первой плохой версии
    return l


# 35. Search Insert Position
examples_35 = [
    {"nums": [1, 3, 5, 6], "target": 5},
    {"nums": [1, 3, 5, 6], "target": 2},
    {"nums": [1, 3, 5, 6], "target": 7}
]


def solution_35(nums, target):
    # Time: O(log n)
    # Space: O(1)

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1

    return l


# 2529. Maximum Count of Positive Integer and Negative Integer
examples_2529 = [
    [-2, -1, -1, 1, 2, 3],
    [-3, -2, -1, 0, 0, 1, 2],
    [5, 20, 66, 1314]
]


def solution_2529(nums):
    # Time: O(log n)
    # Space: O(1)

    # negative
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] >= 0:
            r = mid - 1
        else:
            l = mid + 1
    neg = l

    # positive
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] <= 0:
            l = mid + 1
        else:
            r = mid - 1
    pos = len(nums) - l

    return max(neg, pos)


# 367. Valid Perfect Square
examples_367 = [16, 14]


def solution_367(num):
    # Time: O(log n)
    # Space: O(1)

    l, r = 0, num

    while l <= r:
        mid = (l + r) // 2

        if mid * mid == num:
            return True

        if mid * mid > num:
            r = mid - 1
        else:
            l = mid + 1

    return False


# 69. Sqrt(x)
examples_69 = [4, 8]


def solution_69(x):
    # Time: O(log n)
    # Space: O(1)

    l, r = 0, x

    while l <= r:
        mid = (l + r) // 2

        if mid * mid == x:
            return mid

        if mid * mid > x:
            r = mid - 1
        else:
            l = mid + 1

    return r


# 744. Find Smallest Letter Greater Than Target
examples_744 = [
    {"letters": ["c", "f", "j"], "target": "a"},
    {"letters": ["c", "f", "j"], "target": "c"},
    {"letters": ["x", "x", "y", "y"], "target": "z"},
    {"letters": ["c", "f", "j"], "target": "d"}
]


def solution_744(letters, target):
    l, r = 0, len(letters) - 1
    while l <= r:
        mid = (l + r) // 2

        if letters[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1

    return letters[l] if l < len(letters) else letters[0]


if __name__ == '__main__':
    # show_result(examples_704, solution_704, is_dict=True)
    # show_result(examples_374, solution_374)
    # show_result(examples_278, solution_278)
    # show_result(examples_35, solution_35, is_dict=True)
    # show_result(examples_2529, solution_2529)
    # show_result(examples_367, solution_367)
    # show_result(examples_69, solution_69)
    show_result(examples_744, solution_744, is_dict=True)
