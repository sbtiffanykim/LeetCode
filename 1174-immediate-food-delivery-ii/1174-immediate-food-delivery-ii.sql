# Write your MySQL query statement below

SELECT round(avg(if(order_date = customer_pref_delivery_date, 100, 0)), 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN
    (select customer_id, min(order_date) from Delivery group by customer_id);