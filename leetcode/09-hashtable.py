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

# %% 2006. Count Number of Pairs With Absolute Difference K
examples = [
    {"nums": [1, 2, 2, 1], "k": 1}
]


def solution_1(nums, k):
    # Time: O(n^2)
    # Space: O(1)
    ans = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j] and abs(nums[i] - nums[j]) == k:
                ans += 1

    return ans


def solution_2(nums, k):
    # Time: O(n)
    # Space: O(1)
    ans = 0
    db = {}

    for num in nums:
        pair1 = num - k
        pair2 = num + k

        if pair1 in db:
            ans += db[pair1]

        if pair2 in db:
            ans += db[pair2]

        if num in db:
            db[num] += 1
        else:
            db[num] = 1
    return ans


from collections import Counter


def solution_3(nums, k):
    # Time: O(n)
    # Space: O(n)
    ans = 0
    db = Counter()

    for num in nums:
        pair1 = num - k
        pair2 = num + k

        ans += db[pair1]
        ans += db[pair2]

        db[num] += 1

    return ans


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_3(**v)}")

# %% 49. Group Anagrams
examples = [
    ["eat", "tea", "tan", "ate", "nat", "bat"]
]


def solution_1(strs):
    # Time: O(n * k * log_k)
    # Space: O(n * k)
    db = {}
    for s in strs:
        key = tuple(sorted(s))

        if key in db:
            db[key].append(s)
        else:
            db[key] = [s]

    return list(db.values())


from collections import defaultdict


# from dataclasses import List
def solution_2(strs):
    # Time: O(n * k * log_k)
    # Space: O(n * k)
    db = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        db[key].append(s)

    return list(db.values())


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(v)}")

# %% 2283. Check if Number Has Equal Digit Count and Digit Value
examples = [
    "1210",
    "030"
]


def solution_1(num):
    # Time: O(n^2)
    # Space: O(1)
    for i in range(len(num)):
        n_await = int(num[i])
        n_fact = 0

        for j in range(len(num)):
            if str(i) == num[j]:
                n_fact += 1

        if n_fact != n_await:
            return False
    return True


def solution_2(num):
    # Time: O(n)
    # Space: O(n)

    db = {}
    for n in num:
        db[n] = db.get(n, 0) + 1

    for i in range(len(num)):
        n_await = int(num[i])
        n_fact = db.get(str(i), 0)
        if n_fact != n_await:
            return False

    return True


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(v)}")

# %% 2325. Decode the Message
import string

examples = [
    {"key": "the quick brown fox jumps over the lazy dog", "message": "vkbs bs t suepuv"},
    {"key": "eljuxhpwnyrdgtqkviszcfmabo", "message": "zwx hnfx lqantp mnoeius ycgk vcnjrd"}
]


def solution_1(key, message):
    # Time: O(n)
    # Space: O(n)
    alphabet = string.ascii_lowercase
    alphabet_code = []
    ans = ''
    for k in key.replace(' ', ''):
        if k not in alphabet_code:
            alphabet_code.append(k)

    db = {}
    for ac, a in zip(alphabet_code, alphabet):
        db[ac] = a

    for m in message:
        if m != ' ':
            ans += db[m]
        else:
            ans += ' '

    return ans


def solution_2(key, message):
    db = {}
    alphabet_index = 0

    for char in key:
        if char == ' ':
            continue
        if char not in db:
            db[char] = string.ascii_lowercase[alphabet_index]
            alphabet_index += 1

    result = []
    for char in message:
        if char != ' ':
            result.append(db[char])
        else:
            result.append(' ')

    return ''.join(result)


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(**v)}")

# %%2404. Most Frequent Even Element
examples = [
    [0, 1, 2, 2, 4, 4, 1],
    [4, 4, 4, 9, 2, 4],
    [29, 47, 21, 41, 13, 37, 25, 7]
]


def solution_1(nums):
    # Time: O(n)
    # Space: O(n)
    ans = -1
    db = {}

    for n in nums:
        if n % 2 == 0:
            db[n] = db.get(n, 0) + 1

    if db.values():
        max_cnt = max(db.values())
        ans = min([key for key, value in db.items() if value == max_cnt])
        return ans

    else:
        return ans


def solution_2(nums):
    db = {}
    max_freq = 0
    min_num = float('inf')

    for n in nums:
        if n % 2 == 0:
            db[n] = db.get(n, 0) + 1
            if db[n] > max_freq or (db[n] == max_freq and n < min_num):
                max_freq = db[n]
                min_num = n

    return min_num if min_num != float('inf') else -1


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(v)}")

# %% 2068. Check Whether Two Strings are Almost Equivalent
import string

examples = [
    {"word1": "aaaa", "word2": "bccb"},
    {"word1": "abcdeef", "word2": "abaaacc"},
    {"word1": "cccddabba", "word2": "babababab"}
]


def solution_1(word1, word2):
    # Time: O(n)
    # Space: O(n)
    db1, db2 = {}, {}
    alphabet = {c: 0 for c in string.ascii_lowercase}

    for c1, c2 in zip(word1, word2):
        db1[c1] = db1.get(c1, 0) + 1
        db2[c2] = db2.get(c2, 0) + 1

    for c in alphabet:
        if abs(db1.get(c, 0) - db2.get(c, 0)) > 3:
            return False
    return True


from collections import defaultdict


def solution_2(word1, word2):
    # Time: O(n)
    # Space: O(n)
    diff = defaultdict(int)

    for c1, c2 in zip(word1, word2):
        diff[c1] += 1  # Увеличиваем частоту для символа из word1
        diff[c2] -= 1  # Уменьшаем частоту для символа из word2

    # Проверяем, что разница частот для всех символов не превышает 3
    for count in diff.values():
        if abs(count) > 3:
            return False

    return True


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_2(**v)}")

# %% 1189. Maximum Number of Balloons
examples = [
    "balloon",
    # "nlaebolko",
    # "loonbalxballpoon",
    # "leetcode"
]

from collections import Counter
def solution_1(text):
    text_cnt = Counter(text)
    balloon_cnt = Counter("balloon")
    max_instances = float('inf')

    for char in balloon_cnt:
        if char not in text_cnt:
            return 0
        max_instances = min(max_instances, text_cnt[char] // balloon_cnt[char])
    return max_instances


for i, v in enumerate(examples):
    print(f"Example: {i + 1}. Values: {v}. Result: {solution_1(v)}")

# text_cnt = Counter(text)
# balloon_cnt = Counter("balloon")
# max_instances = float('inf')
#
# for char in balloon_cnt:
#     if char not in text_cnt:
#         return 0
#     max_instances = min(max_instances, text_cnt[char] // balloon_cnt[char])
#
# return max_instances