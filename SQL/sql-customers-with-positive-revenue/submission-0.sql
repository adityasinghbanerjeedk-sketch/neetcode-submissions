-- Write your query below
with cust_table AS (
    SELECT customer_id, sum(revenue) as total_rev FROM customers
    where year = 2020 GROUP BY customer_id
)
select customer_id from cust_table where total_rev > 0
