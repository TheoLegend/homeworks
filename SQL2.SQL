SELECT 
    c.name AS customer_name,
    p.product_name,
    e.country AS export_country
FROM 
    Customers c
JOIN 
    Products p ON c.customer_id = p.customer_id
JOIN 
    Exports e ON p.product_id = e.product_id
WHERE 
    LOWER(c.name) LIKE 'a%' AND
    LOWER(c.name) LIKE '%or%';
