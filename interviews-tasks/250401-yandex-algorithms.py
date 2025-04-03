# Дана строка (возможно, пустая), содержащая буквы A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию, которая вернет строку вида:
# A4B3C2XYZD4E3F3A6B28

examples = [
    "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    ""
]

def solution(s):
    if len(s) == 0:
        return ""

    ans = ""
    cnt = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += f"{s[i-1]}{cnt if cnt > 1 else ''}"
            cnt = 1

    # Добавляем последний символ с его количеством
    ans += f"{s[-1]}{cnt if cnt > 1 else ''}"

    return ans


if __name__ == "__main__":
    for e in examples:
        print(f"Input: {e} \nOutput: {solution(e)}")