-- Write your query below
SELECT name, COALESCE(sum(distance), 0) as travelled_distance
FROM users u
left JOIN rides r
on u.id = r.user_id
group by name order by travelled_distance desc