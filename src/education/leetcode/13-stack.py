import string


def show_result(examples, solution, is_dict=None):
    for i, v in enumerate(examples):
        if is_dict:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")
        else:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")


# 1047. Remove All Adjacent Duplicates In String
examples_1047 = [
    "abbaca",
    "azxxzy"
]


def solution_1047(s):
    # Time: n/2 * 26 * n = n*n = n^2
    # Space: O(1)
    pairs = [letter * 2 for letter in string.ascii_lowercase]

    cur_len, prev_len = len(s), None

    while cur_len != prev_len:  # Time: O(n/2)
        prev_len = cur_len

        for pair in pairs:  # Time: O(1) 26 pairs
            s = s.replace(pair, '')  # Time: O(n)

        cur_len = len(s)

    return s


def solution_1047_2(s):
    # Time: O(n)
    # Space: O(n)
    stack = []

    for l in s:
        if stack and stack[-1] == l:
            stack.pop()
        else:
            stack.append(l)

    return "".join(stack)


# 1544. Make The String Great
examples_1544 = [
    "leEeetcode",
    "abBAcC"
]


def solution_1544(s):
    stack = []

    for l in s:
        if stack and stack[-1].lower() == l.lower():
            first_lower_second_upper = stack[-1].islower() and l.isupper()
            first_upper_second_lower = stack[-1].isupper() and l.islower()

            if first_lower_second_upper or first_upper_second_lower:
                stack.pop()
            else:
                stack.append(l)
        else:
            stack.append(l)

    return "".join(stack)


# 844. Backspace String Compare
examples_844 = [
    {"s": "ab#c", "t": "ad#c"},
    {"s": "ab##", "t": "c#d#"},
    {"s": "a#c", "t": "b"}
]


def solution_844(s, t):
    # Time: O(n)
    # Space: O(n)
    def typing(s):
        stack = []
        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    return typing(s) == typing(t)


# 1614. Maximum Nesting Depth of the Parentheses
examples_1614 = [
    "(1+(2*3)+((8)/4))+1",
    "(1)+((2))+(((3)))",
    "()(())((()()))"
]


def solution_1614_pointer(s):
    max_, cnt = 0, 0
    for c in s:
        if c == "(":
            cnt += 1
            max_ = max(max_, cnt)
        elif c == ")":
            cnt -= 1

    return max_


def solution_1614_stack(s):
    ans = 0
    stack = []

    for c in s:
        if c == "(":
            stack.append("(")
            ans = max(ans, len(stack))
        elif c == ")":
            stack.pop()

    return ans


# 20. Valid Parentheses
examples_20 = [
    "()",
    "()[]{}",
    "(]",
    "([])"
]


def solution_20(s):
    stack = []

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if stack:
                last = stack.pop()

                if c == ")" and last != "(":
                    return False
                if c == "]" and last != "[":
                    return False
                if c == "}" and last != "{":
                    return False
            else:
                return False

    return len(stack) == 0


# 739. Daily Temperatures
examples_739 = [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90]
]


def solution_739(temperatures):
    # Time: O(n^2)
    # Space: O(1)
    ans = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):

            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break

    return ans

def solution_739_2(temperatures):
    # Time: O(n)
    # Space: O(n)
    ans = [0] * len(temperatures)
    stack = []

    for day, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            last_day = stack.pop()
            ans[last_day] = day - last_day

        stack.append(day)

    return ans

if __name__ == "__main__":
    # show_result(examples_1047, solution_1047, is_dict=False)
    # show_result(examples_1047, solution_1047_2, is_dict=False)
    # show_result(examples_1544, solution_1544, is_dict=False)
    # show_result(examples_844, solution_844, is_dict=True)
    # show_result(examples_1614, solution_1614_pointer, is_dict=False)
    # show_result(examples_1614, solution_1614_stack, is_dict=False)
    # show_result(examples_20, solution_20, is_dict=False)
    # show_result(examples_739, solution_739, is_dict=False)
    show_result(examples_739, solution_739_2, is_dict=False)