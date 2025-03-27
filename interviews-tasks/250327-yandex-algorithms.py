from string import ascii_letters


def show_result(examples, solution, is_dict=None):
    for i, v in enumerate(examples):
        if is_dict:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")
        else:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")
    print()


# 1. Дана строка вида: "3 7 10 11"
# Надо вывести индекс первого четного числа
examples_1 = [
    "3 7 10 11"  # -> 2
]


def solution_1(s: str) -> int:
    nums = s.split()
    for i, v in enumerate(nums):
        if int(v) % 2 == 0:
            return i
    return -1


# 2. Дана строка, состоящая из букв 'X', 'Y' и 'O'.
# Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y',
# либо вывести 0, если 'X' либо 'Y' отсутствуют.
examples_2 = [
    "XX",  # -> 0
    "YY",  # -> 0
    "XY",  # -> 1
    "YOX",  # -> 2
    "OOOXOOYOXO",  # -> 2
    "OOOXXOY"  # -> 2
]


def solution_2(s: str) -> int:
    x, y = None, None

    dist = []
    for i in range(len(s)):
        if s[i] == "X":
            for j in range(i, len(s)):
                if s[j] == "Y":
                    dist.append(j - i)

        if s[i] == "Y":
            for j in range(i, len(s)):
                if s[j] == "X":
                    dist.append(j - i)

    return min(dist) if len(dist) > 0 else 0


# 3. Есть список (для простоты содержащий буквы).
# Каждая буква может как отсутствовать полностью, так и повторяться любое кол-во раз.
# Нужно посчитать кол-во каждого элемента в списке и вывести одной строкой в формате "{element}:{count}, ..."
# Для каждого уникального элемента, что есть в списке, с сортировкой по элементу.
# l = []


examples_3 = [
    ['c', 'a', 'c', 'd', 'c', 'd']  # -> "a:1, c:3, d:2"
]


def solution_3(arr):
    db = {}

    for i in arr:
        db[i] = db.get(i, 0) + 1

    ans = [f"{ch}:{db[ch]}" for ch in ascii_letters if ch in db.keys()]
    return ", ".join(ans)


# 4. У нас есть набор билетов.
# Из этих билетов можно построить единственный, неразрывный маршрут. Петель и повторов в маршруте нет.
# Нужно написать программу, которая возвращает эти же объекты билетов в порядке следования маршруту.

examples_4 = [
    [{'from': 'London', 'to': 'Moscow'},
     {'from': 'NY', 'to': 'London'},
     {'from': 'Moscow', 'to': 'SPb'}]
]


def solution_4_1(tickets):
    ans = []
    for i in range(len(tickets)):
        if len(ans) == 0:
            ans.append(tickets[i])

        # Если в ans 1 элемент, то для from -> to
        elif len(ans) == 1 and ans[0]['from'] == tickets[i]['to']:
            ans.insert(0, tickets[i])

        # Если в ans 1 элемент, то для to -> from
        elif len(ans) == 1 and ans[0]['to'] == tickets[i]['from']:
            ans.append(tickets[i])

        # Если в ans 2+ элемента, то для from -> to
        elif len(ans) >= 2 and ans[0]['from'] == tickets[i]['to']:
            ans.insert(0, tickets[i])

        # Если в ans 2+ элемента, то для to -> from
        elif len(ans) >= 2 and ans[-1]['to'] == tickets[i]['from']:
            ans.append(tickets[i])

    return ans


def solution_4_2(tickets):
    route = {}
    for t in tickets:
        from_, to_ = t["from"], t["to"]
        route[from_] = to_

    from_set = set(route.keys())
    to_set = set(route.values())

    # Находим начальную точку маршрута (она есть в from_set, но нет в to_set)
    dest = (from_set - to_set).pop()

    ans = []
    # Идём по всем билетам
    for _ in range(len(to_set)):
        # Добавляем текущий билет в маршрут
        ans.append({"from": dest, "to": route[dest]})
        # Переходим к следующему пункту
        dest = route[dest]

    return ans


if __name__ == "__main__":
    show_result(examples_1, solution_1)
    show_result(examples_2, solution_2)
    show_result(examples_3, solution_3)
    show_result(examples_4, solution_4_1)
    show_result(examples_4, solution_4_2)
