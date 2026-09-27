# Write your MySQL query statement below
# Write your MySQL query statement below
WITH consecutive AS (
    SELECT num, 
    LAG(num) OVER (ORDER BY id) as prev_num,
    LEAD(num) OVER (ORDER BY id) as next_num
    FROM Logs
)

SELECT DISTINCT(num) AS ConsecutiveNums
FROM consecutive
WHERE num = prev_num and num = next_num