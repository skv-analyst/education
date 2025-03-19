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
# %% 383. Ransom Note
examples = [
    {"ransomNote": "a", "magazine": "b"},
    {"ransomNote": "aa", "magazine": "ab"},
    {"ransomNote": "aa", "magazine": "aab"}
]


def solution_1(ransomNote, magazine):
    # Time: O(n+m)
    # Space: O(n+m)
    def count_char(s):
        db = {}
        for c in s:
            if c not in db:
                db[c] = 1
            else:
                db[c] += 1

        return db

    ransom_note_cnt = count_char(ransomNote)
    magazine_cnt = count_char(magazine)

    for c, cnt in ransom_note_cnt.items():
        if magazine_cnt.get(c, 0) < cnt:
            return False

    return True


from collections import Counter


def solution_2(ransomNote, magazine):
    # Time: O(n+m)
    # Space: O(n+m)

    ransom_note_cnt = Counter(ransomNote)
    magazine_cnt = Counter(magazine)

    for c, cnt in ransom_note_cnt.items():
        if magazine_cnt[c] < cnt:
            return False

    return True


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(**v)}")

# %% 242. Valid Anagram
examples = [
    {"s": "anagram", "t": "nagaram"},
    {"s": "rat", "t": "car"}
]


def solution_1(s, t):
    # Time: O(n+m)
    # Space: O(n+m)
    def count_char(string):
        db = {}
        for c in string:
            if c not in db:
                db[c] = 1
            else:
                db[c] += 1
        return db

    s_cnt = count_char(s)
    t_cnt = count_char(t)

    for c, cnt in s_cnt.items():
        if t_cnt.get(c, 0) < cnt:
            return False

    for c, cnt in t_cnt.items():
        if s_cnt.get(c, 0) < cnt:
            return False

    return True


from collections import Counter


def solution_2(s, t):
    # Time: O(n+m)
    # Space: O(n+m)
    return Counter(s) == Counter(t)


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(**v)}")

# %% 1160. Find Words That Can Be Formed by Characters
examples = [
    {"words": ["cat", "bt", "hat", "tree"], "chars": "atach"},
    {"words": ["hello", "world", "leetcode"], "chars": "welldonehoneyr"}
]


def solution_1(words, chars):
    # Time: O(k+n*m)
    # Space: O(k+m)
    def count_char(string):
        db = {}
        for c in string:
            if c not in db:
                db[c] = 1
            else:
                db[c] += 1
        return db

    ans = 0

    chars_cnt = count_char(chars)

    for w in words:
        w_cnt = count_char(w)
        good = True

        for c, cnt in w_cnt.items():
            if chars_cnt.get(c, 0) < cnt:
                good = False

        ans += len(w) if good else 0

    return ans


from collections import Counter


def solution_2(words, chars):
    # Time: O(k+n*m)
    # Space: O(k+m)

    ans = 0
    chars_cnt = Counter(chars)

    def len_of_good_word(w):
        w_cnt = Counter(w)
        for c, cnt in w_cnt.items():
            if chars_cnt[c] < cnt:
                return 0
        return len(w)

    for w in words:
        ans += len_of_good_word(w)

    return ans


def solution_3(words, chars):
    # Time: O(k+n*m)
    # Space: O(k+m)

    ans = 0
    chars_cnt = Counter(chars)

    for w in words:
        ans += len(w) if Counter(w) < chars_cnt else 0

    return ans


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(**v)}")

# %% 1207. Unique Number of Occurrences
examples = [
    [1, 2, 2, 1, 1, 3],
    [1, 2],
    [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
]


def solution_1(arr):
    # Time: O(n)
    # Space: O(n)
    def count_num(nums):
        db = {}
        for n in nums:
            if n not in db:
                db[n] = 1
            else:
                db[n] += 1
        return db

    counter = count_num(arr)
    seen = set()
    for _, value in counter.items():
        if value not in seen:
            seen.add(value)
        else:
            return False

    return True


from collections import Counter


def solution_2(arr):
    # Time: O(n)
    # Space: O(n)
    counter = Counter(arr)
    seen = set()
    for _, value in counter.items():
        if value not in seen:
            seen.add(value)
        else:
            return False

    return True


def solution_3(arr):
    # Time: O(n)
    # Space: O(n)
    counts = Counter(arr).values()
    return len(counts) == len(set(counts))


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(v)}")

# %% 1. Two Sum
examples = [
    {"nums": [2, 7, 11, 15], "target": 9},
    {"nums": [3, 2, 4], "target": 6},
    {"nums": [3, 3], "target": 6},
    {"nums": [3, 2, 3], "target": 6}
]


def solution_1(nums, target):
    # Time: O(n^2)
    # Space: O(1)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

    return None


def solution_2(nums, target):
    # Time: O(n)
    # Space: O(n)

    db = {}
    for i, num in enumerate(nums):
        db[num] = i

    for i, num in enumerate(nums):
        pair = target - num
        if pair in db and db[pair] != i:
            return [i, db[pair]]


def solution_3(nums, target):
    # Time: O(n)
    # Space: O(n)

    db = {}
    for i, num in enumerate(nums):
        pair = target - num
        if pair in db:
            return [i, db[pair]]

        db[num] = i


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(**v)}")

# %% 1365. How Many Numbers Are Smaller Than the Current Number
examples = [
    [8, 1, 2, 2, 3],
    [6, 5, 4, 8],
    [7, 7, 7, 7]
]


def solution_1(nums):
    # Time: O(n^2)
    # Space: O(n)
    ans = []
    for num1 in nums:
        cnt = 0
        for num2 in nums:
            if num2 < num1:
                cnt += 1
        ans.append(cnt)

    return ans


def solution_2(nums):
    # Time: O(n^2)
    # Space: O(n)
    ans = []
    nums_sorted = sorted(nums)  # O(n* log n)

    for num in nums:
        ans.append(nums_sorted.index(num))  # O(n^2)

    return ans


def solution_3(nums):
    # Time: O(n*log_n)
    # Space: O(n)
    ans = []
    nums_sorted = sorted(nums)  # O(n* log_n)

    db = {}  # O(n)
    for i, num in enumerate(nums_sorted):
        if num not in db:
            db[num] = i

    for num in nums:
        ans.append(db[num])  # O(1)

    return ans


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(v)}")

# %% 1512. Number of Good Pairs
examples = [
    [1, 2, 3, 1, 1, 3],
    [1, 1, 1, 1],
    [1, 2, 3]
]


def solution_1(nums):
    # Time: O(n^2)
    # Space: O(1)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] == nums[j]:
                ans += 1

    return ans


def solution_2(nums):
    # Time: O(n)
    # Space: O(n)
    ans = 0
    db = {}

    for num in nums:
        if num not in db:
            db[num] = 1
        else:
            ans += db[num]
            db[num] += 1

    return ans

from collections import Counter
def solution_3(nums):
    # Time: O(n)
    # Space: O(n)
    ans = 0
    db = Counter()

    for num in nums:
        ans += db[num]
        db[num] += 1

    return ans

for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(v)}")
