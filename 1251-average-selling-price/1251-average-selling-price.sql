# Write your MySQL query statement below
select  distinct Prices.product_id,round(sum(Prices.price*UnitsSold.units)/sum(UnitsSold.units),2) as  average_price 
from Prices 
join UnitsSold on Prices.product_id=UnitsSold.product_id 
where UnitsSold.purchase_date between Prices.start_date and Prices.end_date 
group by Prices.product_id 
order by Prices.product_id

