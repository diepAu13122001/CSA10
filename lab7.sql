use northwindfulldata;

-- Cau 1 ---
select min(orderdate) as EarliestDate 
from orders;

-- Cau 2 ---
select count(orderid) as TotalOrders
from orders;

-- Cau 3 ---
create view totalItems_by_OrderID as
select  OrderID, sum(Quantity) as TotalItems
from orderdetails group by orderId;

-- Cau 4 ---
select avg(TotalItems) * 1.0 as AvgItems
from totalItems_by_OrderID;

select sum(quantity) * 1.0/ count(distinct orderId) 
as AvgItems from orderDetails;

-- Cau 5 ---
select orderId, count(productId) as distinctItems 
from orderdetails group by orderID;

-- Cau 6 ---
select category, avg(price) as avgPrice 
from products group by category 
having avgPrice between 20 and 30;

-- Cau 7 ---
select country, count(customerId) as CustomerCount
from customers group by country 
having CustomerCount > 10;

-- Cau 8 ---
select customerid, count(orderID) as Ordered 
from orders group by customerid
order by ordered desc; 

-- Cau 9 ---
select productID, count(orderID) as Ordered
from orderdetails group by productId;

-- Cau 10 ---
select productID, sum(quantity) as TotalItems
from orderdetails where productId = 1
group by productId;
