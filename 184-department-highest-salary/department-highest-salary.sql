# Write your MySQL query statement below
WITH rank_salary AS (
    SELECT d.name AS Department, 
    e.name AS Employee, e.salary AS Salary,
    DENSE_RANK() over (partition by e.departmentId order by e.salary DESC) as rnk
    FROM Employee e left join Department d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary 
FROM rank_salary
where rnk = 1
