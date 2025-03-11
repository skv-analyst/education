# %% 771. Jewels and Stones
examples = [
    {"jewels": "aA", "stones": "aAAbbbb"},
    {"jewels": "z", "stones": "ZZ"}
]


def solution(jewels, stones):
    ans = 0

    # Time: O(n * m)
    # Space: O(1)
    # for s in stones:
    #     if s in jewels:
    #         ans += 1

    # Time: O(n + m)
    # Space: O(m)
    jewels_set = set(jewels)
    for s in stones:
        if s in jewels_set:
            ans += 1

    return ans


for e in examples:
    print(solution(**e))

# %% 217. Contains Duplicate
examples = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]


def solution_1(nums):
    # Time: O(n^2)
    # Space: O(1)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False


def solution_2(nums):
    # Time: O(n * log(n) + n)
    # Space: O(n)

    nums.sort()  # O(n * Log(n))

    for i in range(1, len(nums)):  # O(n)
        if nums[i] == nums[i - 1]:
            return True
    return False


def solution_3(nums):
    # Time: O(n)
    # Space: O(n)
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def solution_4(nums):
    # Time: O(n)
    # Space: O(n)

    return True if len(set(nums)) < len(nums) else False


for e in examples:
    print(solution_4(e))

# %% 268. Missing Number
examples = [
    [3, 0, 1],  # Output: 2
    [0, 1],  # Output: 2
    [9, 6, 4, 2, 3, 5, 7, 0, 1]  # Output: 8
]


def solution_1(nums):
    # Time: O(n)
    # Space: O(n)

    nums_set = set(nums)

    for num in range(len(nums) + 1):
        if num not in nums_set:
            return num


def solution_2(nums):
    # Time: O(n)
    # Space: O(1)
    return sum(range(len(nums) + 1)) - sum(nums)


for e in examples:
    print(solution_2(e))

# %% 1496. Path Crossing
examples = ["NES", "NESWW"]


def solution(path):
    # Time: O(n)
    # Space: O(n)

    x, y = 0, 0
    visited = {(x, y)}

    for s in path:
        if s == 'N':
            dx, dy = 0, 1
        elif s == 'S':
            dx, dy = 0, -1
        elif s == 'E':
            dx, dy = 1, 0
        elif s == 'W':
            dx, dy = -1, 0

        x += dx
        y += dy

        if (x, y) in visited:
            return True

    return False


for e in examples:
    print(solution(e))

# %% 1684. Count the Number of Consistent Strings
examples = [
    {"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]},  # Output: 2
    {"allowed": "abc", "words": ["a", "b", "c", "ab", "ac", "bc", "abc"]},  # Output: 7
    {"allowed": "cad", "words": ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]}  # Output: 4
]


def solution(allowed, words):
    # Time: O(n)
    # Space: O(n)
    ans = 0
    allowed_set = set(allowed)

    for w in words:
        ans += 0 if set(w) - allowed_set else 1

    return ans


for e in examples:
    print(solution(**e))

# %% 2351. First Letter to Appear Twice
examples = [
    "abccbaacz",  # Output: "c"
    "abcdd",  # Output: "d"
    "nwcn"  # Output: "n"
]


def solution(s):
    # Time: O(n)
    # Space: O(n)
    seen = set()
    ans = str()

    for char in s:
        if char in seen:
            ans += char
            break
        seen.add(char)

    return ans


for e in examples:
    print(solution(e))

