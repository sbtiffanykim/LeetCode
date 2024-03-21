SELECT name From SalesPerson s LEFT JOIN (SELECT o.sales_id FROM Company c JOIN Orders o ON c.com_id = o.com_id WHERE c.name = 'RED') AS n 
ON s.sales_id = n.sales_id
WHERE n.sales_id IS NULL
