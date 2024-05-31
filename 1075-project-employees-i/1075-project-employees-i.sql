SELECT p.project_id, round(sum(experience_years) / count(p.project_id), 2) as average_years
FROM Project p JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;