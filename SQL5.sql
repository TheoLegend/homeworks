-- Overall Salary and Department Summary
SELECT 
    COUNT(*) AS total_employees,
    COUNT(DISTINCT department) AS total_departments,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM 
    Employees;

-- Breakdown of Salary by Department
SELECT 
    department,
    COUNT(*) AS employee_count,
    SUM(salary) AS department_total_salary,
    AVG(salary) AS department_average_salary,
    MIN(salary) AS department_min_salary,
    MAX(salary) AS department_max_salary
FROM 
    Employees
GROUP BY 
    department
ORDER BY 
    department;

-- Optional: List of Employees with Their Details
SELECT 
    employee_id,
    name,
    position,
    department,
    salary,
    hire_date
FROM 
    Employees
ORDER BY 
    department, salary DESC;
