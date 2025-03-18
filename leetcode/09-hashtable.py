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
