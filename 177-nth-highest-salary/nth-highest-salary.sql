CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    WITH ranked AS (
        SELECT DISTINCT salary,
        DENSE_RANK() over (ORDER BY salary DESC) AS rnk
        FROM employee
    )

    SELECT CASE
        WHEN COUNT(*) = 0 THEN NULL
        ELSE MAX(salary) 
        END AS getNthHighestSalary
        FROM ranked
        WHERE rnk = N
      # Write your MySQL query statement below.

  );
END