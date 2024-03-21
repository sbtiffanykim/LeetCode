SELECT day, emp_id, SUM(total_time) AS total_time 
FROM (SELECT event_day "day", emp_id, out_time - in_time "total_time" FROM Employees) AS R GROUP BY emp_id, day
