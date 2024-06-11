# Write your MySQL query statement below

WITH feb_orders AS (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
    GROUP BY product_id
    HAVING SUM(unit) >= 100
)

SELECT p.product_name, f.unit FROM feb_orders f JOIN Products p ON f.product_id = p.product_id;
