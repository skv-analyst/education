# %% 2544. Alternating Digit Sum
examples = [521, 111, 886996]


def solution(n):
    ans = 0
    arr = list(map(int, str(n)))

    for i in range(len(arr)):
        if (i + 1) % 2:
            ans += arr[i]
        else:
            ans += arr[i] * -1

    return ans


for e in examples:
    print(solution(e))

# %% 2535. Difference Between Element Sum and Digit Sum of an Array
examples = [[1, 15, 6, 3], [1, 2, 3, 4]]


def solution(nums):
    elements_sum = sum(nums)

    digits = ''.join([str(d) for d in nums])
    digits_sum = 0

    for d in digits:
        digits_sum += int(d)

    return abs(elements_sum - digits_sum)


for e in examples:
    print(solution(e))

# %% 1869. Longer Contiguous Segments of Ones than Zeros
examples = ["1101", "111000", "110100010"]


def solution(s):
    # one_max = 0
    # one_max_total = 0
    # zero_max = 0
    # zero_max_total = 0
    #
    # for i in range(len(s)):
    #     if s[i] == '1':
    #         one_max += 1
    #         one_max_total = max(one_max_total, one_max)
    #         zero_max = 0
    #     elif s[i] == '0':
    #         zero_max += 1
    #         zero_max_total = max(zero_max_total, zero_max)
    #         one_max = 0
    #     print(f"i:{i}, s[i]:{s[i]}, one_max:{one_max}, zero_max:{zero_max}, one_max_total:{one_max_total}, zero_max_total:{zero_max_total}")
    #
    # return one_max_total > zero_max_total

    one_arr = s.split('0')
    one_max = max([len(i) for i in one_arr])

    zero_arr = s.split('1')
    zero_max = max([len(i) for i in zero_arr])

    return one_max > zero_max


for e in examples:
    print(solution(e))

# %%

