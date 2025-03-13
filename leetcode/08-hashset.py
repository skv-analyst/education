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
# %% 2395. Find Subarrays With Equal Sum
examples = [
    [4, 2, 4],
    [1, 2, 3, 4, 5],
    [0, 0, 0]
]


def solution(nums):
    # Time: O(n)
    # Space: O(n)

    seen = set()
    ans = False

    for i in range(len(nums) - 1):
        # sum_now = nums[i - 1] + nums[i]
        sum_now = nums[i] + nums[i + 1]
        if sum_now in seen:
            ans = True
            break
        seen.add(sum_now)

    return ans


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Result: {solution(v)}")

# %% 2729. Check if The Number is Fascinating
examples = [192, 100, 783]


def solution(n):
    n_str = str(n) + str(n * 2) + str(n * 3)

    if len(n_str) > 9 or '0' in n_str:
        return False

    unique_digits = set(n_str)
    return len(unique_digits) == 9


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")

# %% 2956. Find Common Elements Between Two Arrays
examples = [
    {"nums1": [2, 3, 2], "nums2": [1, 2]},
    {"nums1": [4, 3, 2, 3, 1], "nums2": [2, 2, 5, 2, 3, 6]},
    {"nums1": [3, 4, 2, 3], "nums2": [1, 5]}
]


def solution(nums1, nums2):
    # Time: O(n)
    # Space: O(n)
    def check(nums, nums_set):
        ans = 0
        for n in nums:
            if n in nums_set:
                ans += 1
        return ans

    ans1 = check(nums1, set(nums2))
    ans2 = check(nums2, set(nums1))

    return [ans1, ans2]


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")

# %% 2965. Find Missing and Repeated Values
examples = [
    [[1, 3], [2, 2]],
    [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
]


def solution_1(grid):
    rows = cols = len(grid)
    grid_digits = {i for i in range(1, rows ** 2 + 1)}

    # Time: O(n^2). Space: O(n)
    grid_flat = []
    for r in range(rows):
        for c in range(cols):
            grid_flat.append(grid[r][c])

    # Time: O(n). Space: O(n)
    seen = set()
    repeat = 0
    for d in grid_flat:
        if d not in seen:
            seen.add(d)
        else:
            repeat = d

    # Time: O(n). Space: O(n)
    missing = 0
    for d in grid_digits:
        if d not in grid_flat:
            missing = d

    return [repeat, missing]


def solution_2(grid):
    n = len(grid)
    grid_digits = {i for i in range(1, n ** 2 + 1)}
    seen = set()
    repeat = 0
    for row in grid:
        for d in row:
            if d in seen:
                repeat = d
            seen.add(d)

    missing = (grid_digits - seen).pop()
    return [repeat, missing]


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(v)}")

