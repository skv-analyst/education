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

