WITH final_id AS (
    SELECT MIN(id) FROM Person GROUP BY email
)

DELETE FROM Person WHERE id NOT IN (SELECT * FROM final_id);