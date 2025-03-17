# %% 387. First Unique Character in a String
examples = [
    "leetcode",
    "loveleetcode",
    "aabb"
]


def solution_1(s):
    # Time: O(n^2)
    # Space: O(1)
    for i in range(len(s)):
        unique = True

        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                unique = False

        if unique:
            return i

    return -1


def solution_2(s):
    # Time: O(n)
    # Space: O(1)
    db = {}
    for c in s:
        if c not in db:
            db[c] = 1
        else:
            db[c] += 1

    for i, c in enumerate(s):
        if db[c] == 1:
            return i

    return -1


def solution_3(s):
    # Time: O(n)
    # Space: O(1)
    db = {}
    for i, c in enumerate(s):
        if c not in db:
            db[c] = i
        else:
            # Если символ не уникальный, то удаляем индекс
            db[c] = None

    return min((idx for idx in db.values() if idx is not None), default=-1)


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(v)}")

# %% 1748. Sum of Unique Elements
from collections import Counter
examples = [
    [1, 2, 3, 2],  # Output: 4
    [1, 1, 1, 1, 1],  # Output: 0
    [1, 2, 3, 4, 5]  # Output: 15
]


def solution_1(nums):
    # Time: O(n)
    # Space: O(n)
    db = {}
    for num in nums:
        if num not in db:
            db[num] = 1
        else:
            db[num] += 1

    return sum([num for num, cnt in db.items() if cnt == 1])


def solution_2(nums):
    # Time: O(n)
    # Space: O(n)
    counter = Counter(nums)
    return sum([num for num, cnt in counter.items() if cnt == 1])


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(v)}")
