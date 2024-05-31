# Write your MySQL query statement below

SELECT contest_id, round(count(user_id) / (Select count(user_id) From Users) * 100, 2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;