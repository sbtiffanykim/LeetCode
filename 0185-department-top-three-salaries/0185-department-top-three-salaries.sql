# Write your MySQL query statement below
WITH high_earner AS (
    SELECT departmentId, name, salary, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM EMPLOYEE
)

SELECT d.name Department, h.name Employee, h.salary Salary
FROM high_earner h JOIN Department d ON h.departmentId = d.id
WHERE h.salary_rank <= 3;