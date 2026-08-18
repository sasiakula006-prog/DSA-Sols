SELECT s.user_id, ROUND(AVG(IF(c.action = 'confirmed',1.00,0)),2) AS confirmation_rate
FROM signups AS s
LEFT JOIN Confirmations as c
ON s.user_id = c.user_id
GROUP BY s.user_id