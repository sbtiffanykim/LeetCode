# Write your MySQL query statement below
(SELECT u.name AS results
FROM MovieRating r JOIN (SELECT * FROM Users) u ON r.user_id = u.user_id
GROUP BY r.user_id
ORDER BY COUNT(r.movie_id) DESC, u.name
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM MovieRating r JOIN (SELECT * FROM Movies) m ON r.movie_id = m.movie_id
WHERE DATEDIFF(created_at, '2020-02-01') >= 0 AND DATEDIFF(created_at, '2020-02-01') <= 28
GROUP BY r.movie_id
ORDER BY AVG(rating) DESC, m.title
LIMIT 1);