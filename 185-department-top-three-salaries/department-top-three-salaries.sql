# Write your MySQL query statement below
WITH NewTable AS 
(SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e LEFT JOIN Department d
ON e.departmentId = d.id),

NewTable2 AS 
(SELECT Department, Employee, Salary,
DENSE_RANK() OVER (PARTITION BY Department
ORDER BY Salary DESC) AS rnk
FROM NewTable)

SELECT Department, Employee, Salary
FROM NewTable2
WHERE rnk <= 3;


