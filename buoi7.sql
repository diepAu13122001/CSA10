-- sum: tong so luong mon hang theo product_id (orderdetails)
create view product_quantity_view as
select ProductID, sum(quantity) as sum_of_quantity
from orderdetails
group by ProductID;

drop view product_quantity_view;

-- operators: thong tin product(name, unit, price),
-- price * quantity
select productName as name, unit, 
price * table_a.sum_of_quantity as total
from products join (
	select ProductID, sum(quantity) as "sum_of_quantity"
	from orderdetails
	group by ProductID) as table_a
on products.ProductID = table_a.ProductID;

select productName as name, unit, 
price * table_a.sum_of_quantity as total
from products join product_quantity_view as table_a
on products.ProductID = table_a.ProductID;

-- max: order cuoi cung (gan nhat)
select max(OrderDate) as max_orderDate from orders;
-- toan bo thong tin trong order
select * from orders
where OrderDate = (
	select max(OrderDate) as max_orderDate from orders
);

-- select OrderID, max(OrderDate) as max_orderDate, OrderDate
-- from orders
-- group by OrderDate
-- having OrderDate = max_orderDate;

-- avg: lay product co price > avg
select * from products where price > (
	select avg(price) as avg_price from products);

-- gia trung binh tung loai sp > 30
select category, avg(price) as avg_price
from products group by category 
having avg_price > 30;

-- union: lien ket du lieu 2 bang
-- union: lay du lieu khong trung lap
select max(price) as range_price from products
union
select min(price) from products;
