-- Write your query below
with cte as(
select s.sales_id, s.name, string_agg(o.com_id::text, ',') as com_list
from sales_person s
left join orders o
on o.sales_id=s.sales_id
group by s.sales_id
having string_agg(o.com_id::text, ',') not like '%1%' or string_agg(o.com_id::text, ',') is null
)
select name from cte

