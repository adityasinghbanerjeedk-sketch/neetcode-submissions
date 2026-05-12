-- Write your query below
SELECT employee_id, 
CASE
    WHEN employee_id % 2 != 0 and left(name, 1) != 'M' then salary
    ELSE 0
END AS bonus 
FROM employees
order by employee_id asc
