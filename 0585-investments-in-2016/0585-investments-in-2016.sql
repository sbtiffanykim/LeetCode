# Write your MySQL query statement below

WITH tiv_2015_val AS (
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1
),
unique_lat_lon AS (
    SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(tiv_2016), 2) tiv_2016 FROM Insurance 
WHERE tiv_2015 IN (SELECT * FROM tiv_2015_val) AND (lat, lon) IN (SELECT * FROM unique_lat_lon);