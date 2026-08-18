SELECT name
FROM (SELECT managerId, count(managerId) FROM employee GROUP BY managerId HAVING count(managerId)>=5) AS B 
JOIN employee as A
ON A.id = B.managerId;