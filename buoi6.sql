-- Read data ----------------------------------
-- select all
select * from customers;
-- select special columns
select city as Customer_City from customers;
-- select distinct (unique data)
select distinct city, country from customers;  
-- select with conditions
select * from customers where customerId = 3;

select * from orders 
where orderDate 
between '1996-07-01' and '1996-07-05';

select * from products 
where productName like '%g%';

-- select with group by
select city from customers
where city like '%i%'
group by city;

-- select with order by 
select * from orderDetails
order by quantity desc; -- lon => nho
-- order by quantity asc -- nho => lon