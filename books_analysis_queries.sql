
--1. Average price for each rating

select rating ,
round(avg(price),2) as avg_price
from books
group by rating
order by rating desc


--2. The 5 most expensive books rated 4 or 5

select top 5
  title,
  round (price,2) As price,
  rating
from books
where rating in (4, 5)
order by price desc


--3. How many books are out of stock, per rating
select
  rating,
  sum(case when in_stock = 0 then 1 else 0 end ) As out_of_stock_count
from books
group by rating
order by rating desc



