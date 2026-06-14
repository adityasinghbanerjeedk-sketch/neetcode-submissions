-- Write your query below
SELECT seller_name
FROM seller s
LEFT JOIN orders o
ON s.seller_id=o.seller_id and sale_date between '2020-01-01' and '2020-12-31'
where order_cost is null 
ORDER BY seller_name
