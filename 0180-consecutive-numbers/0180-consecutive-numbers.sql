# Write your MySQL query statement below
WITH Cte AS(SELECT num,
            LEAD(num, 1) OVER() num1,
            LEAD(num, 2) OVER() num2,
            id,
            LEAD(id, 1) OVER() id1,
            LEAD(id, 2) OVER() id2
            FROM Logs
            ORDER BY id
           )

SELECT DISTINCT(num) ConsecutiveNums FROM Cte 
WHERE num = num1 AND num = num2 AND id + 1 = id1 AND id + 2 = id2
