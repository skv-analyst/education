/*  Ранжирование    */
-- Составить рейтинг сотрудников по размеру заработной платы.
select
    dense_rank() over w as rank,
    id, name, city, department, salary
from employees
window w as (order by salary desc)
order by rank, id;

-- Составить рейтинг сотрудников по размеру заработной платы независимо по каждому департаменту.
select
    dense_rank() over w as rank,
    id, name, city, department, salary
from employees
window w as (partition by department order by salary desc)
order by department, salary desc, id;

-- Разбить сотрудников на три группы в зависимости от размера зарплаты: высокооплачиваемые, средние, низкооплачиваемые.
-- ntile() всегда старается разбить данные так, чтобы группы были одинакового размера.
-- Поэтому записи с одинаковым значением з/п вполне могут попасть в разные (соседние) группы.
select
    ntile(3) over w as rank,
    id, name, city, department, salary
from employees
window w as (order by salary desc)
order by salary desc;


/*  Сравнение со смещением    */
-- Сравнение с соседями
-- Посчитать процент разницы зарплаты каждого сотрудника относительно предыдущего.
select
    name, department, salary,
    lag(salary, 1) over w as prev,
    round(
        (salary - lag(salary, 1) over w) * 100.0 / lag(salary, 1) over w
    ) as diff_percent
from employees
window w as (order by salary asc)
order by salary, id;

-- Сравнение с границами
-- Соотнести зарплату сотрудника с минимальной и максимальной зарплатой в его департаменте.
-- Всегда помни, что функции first_value() и last_value() работают не просто с секцией окна.
-- Они работают с фреймом внутри секции и конец фрейма не всегда равен концу секции.
-- У каждой записи в секции свой фрейм. По умолчанию начало фрейма совпадает с началом секции, а конец для каждой записи свой.
-- Чтобы last_value() работала как мы ожидаем, придется «прибить» границы фрейма к границам секции.
-- Чтобы границы фрейма совпадали с границами секции (или всего окна, если секция одна) используют конструкцию
-- rows between unbounded preceding and unbounded following в определении окна
select
    name, department, salary,
    first_value(salary) over w as low,
    last_value(salary) over w as high
from employees
window w as (
    partition by department
    order by salary
    rows between unbounded preceding and unbounded following)
order by department, salary, id;