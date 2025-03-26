from collections import Counter


def show_result(examples, solution, is_dict=None):
    for i, v in enumerate(examples):
        if is_dict:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")
        else:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")


# 345. Reverse Vowels of a String
examples_354 = [
    "IceCreAm",
    "leetcode"
]


def solution_345(s):
    # Time: O(n)
    # Space: O(n)
    s = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    l, r = 0, len(s) - 1

    while l < r:
        if s[l].lower() not in vowels:
            l += 1
            continue

        if s[r].lower() not in vowels:
            r -= 1
            continue

        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return ''.join(s)


# 125. Valid Palindrome
examples_125 = [
    "hello",
    "ama",
    "A man, a plan, a canal: Panama",
    "race a car",
    " "
]


def solution_125(s: str) -> bool:
    # Time: O(n)
    # Space: O(1)

    s = s.lower()
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


# 2108. Find First Palindromic String in the Array
examples_2108 = [
    ["abc", "car", "ada", "racecar", "cool"],
    ["notapalindrome", "racecar"],
    ["def", "ghi"]
]


def solution_2108(words):
    # Time: O(n)
    # Space: O(1)
    def is_palindrome(word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    for word in words:
        if is_palindrome(word):
            return word

    return ""


# 283. Move Zeroes
examples_283 = [
    [0, 1, 0, 3, 12],
    [0]

]


def solution_283(nums):
    # Time: O(n)
    # Space: O(1)

    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


# 26. Remove Duplicates from Sorted Array
examples_26 = [
    [1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
]


def solution_26(nums):
    # Time: O(n)
    # Space: O(1)

    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]

    return j + 1


# 977. Squares of a Sorted Array
examples_977 = [
    [-4, -1, 0, 3, 10],
    [-7, -3, 2, 3, 11]
]


def solution_977_1(nums):
    # Time: O(n * log_n)
    # Space: O(n)
    return sorted([n ** 2 for n in nums])


def solution_977_2(nums):
    # Time: O(n)
    # Space: O(1)

    ans = [0] * len(nums)
    k = len(ans) - 1
    l, r = 0, len(nums) - 1

    while l <= r:
        l2, r2 = nums[l] ** 2, nums[r] ** 2

        if l2 > r2:
            ans[k] = l2
            l += 1
        else:
            ans[k] = r2
            r -= 1
        k -= 1

    return ans


# 167. Two Sum II - Input Array Is Sorted
examples_167 = [
    {"numbers": [2, 7, 11, 15], "target": 9},  # [1,2]
    {"numbers": [2, 3, 4], "target": 6},  # [1,3]
    {"numbers": [-1, 0], "target": -1}  # [1,2]
]


def solution_167(numbers, target):
    # Time: O(n)
    # Space: O(1)
    l, r = 0, len(numbers) - 1

    while numbers[l] + numbers[r] != target:
        if numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] < target:
            l += 1

    return [l + 1, r + 1]


# 541. Reverse String II
examples_541 = [
    {"s": "abcdefg", "k": 2},
    {"s": "abcd", "k": 2}
]


def solution_541_1(s, k):
    # Time: O(n)
    # Space: O(n+k)
    ans = ''
    rev = True
    for i in range(0, len(s), k):
        if rev:
            ans += s[i:i + k][::-1]
        else:
            ans += s[i: i + k]

        rev = not rev
    return ans


def solution_541_2(s, k):
    # Time: O(n)
    # Space: O(1)
    s = list(s)

    for i in range(0, len(s), 2 * k):
        l, r = i, min(i + k - 1, len(s) - 1)

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return ''.join(s)


# 5. Longest Palindromic Substring
examples_5 = [
    "babad",
    "cbbd"
]


def solution_5_1(s):
    # Time: O(n^3)
    # Space: O(n)

    ans = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]

            if sub == sub[::-1] and len(sub) > len(ans):
                ans = sub

    return ans


if __name__ == "__main__":
    # show_result(examples_354, solution_345)
    # show_result(examples_125, solution_125)
    # show_result(examples_2108, solution_2108)
    # show_result(examples_283, solution_283)
    # show_result(examples_26, solution_26)
    # show_result(examples_977, solution_977_1)
    # show_result(examples_977, solution_977_2)
    # show_result(examples_167, solution_167, is_dict=True)
    # show_result(examples_541, solution_541_1, is_dict=True)
    # show_result(examples_541, solution_541_2, is_dict=True)
    show_result(examples_5, solution_5_1)
