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
