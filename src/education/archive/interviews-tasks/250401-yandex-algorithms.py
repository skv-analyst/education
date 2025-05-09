# Дана строка (возможно, пустая), содержащая буквы A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию, которая вернет строку вида:
# A4B3C2XYZD4E3F3A6B28

examples = [
    "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    ""
]


def solution_1(s):
    if len(s) == 0:
        return ""

    ans = ""
    cnt = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += f"{s[i - 1]}{cnt if cnt > 1 else ''}"
            cnt = 1

    # Добавляем последний символ с его количеством
    ans += f"{s[-1]}{cnt if cnt > 1 else ''}"

    return ans


def solution_2(s):
    if len(s) == 0:
        return ""

    ans = []

    s += '1'
    start, stop = 0, 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            stop += 1

        else:
            cnt = stop - start
            ans.append(f"{str(s[i])}{cnt if cnt > 1 else ''}")

            start = stop
            stop = start

    return ''.join(ans)


if __name__ == "__main__":
    for e in examples:
        print(f"Input: {e} \nOutput: {solution_2(e)}")
