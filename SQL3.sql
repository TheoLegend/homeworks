-- Part 1: Filtered Customer Info with Products and Export Countries
SELECT 
    'Customer' AS record_type,
    c.name AS name,
    p.product_name AS detail_1,
    e.country AS detail_2,
    NULL AS detail_3
FROM 
    Customers c
JOIN 
    Products p ON c.customer_id = p.customer_id
JOIN 
    Exports e ON p.product_id = e.product_id
WHERE 
    LOWER(c.name) LIKE 'a%' AND
    LOWER(c.name) LIKE '%or%'

UNION ALL

-- Part 2: Full Employee Info
SELECT 
    'Employee' AS record_type,
    e.name AS name,
    e.position AS detail_1,
    CAST(e.salary AS VARCHAR) AS detail_2,
    e.department AS detail_3
FROM 
    Employees e;
