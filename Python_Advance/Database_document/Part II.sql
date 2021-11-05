-- INNER JOIN

-- Lấy toàn bộ records từ 2 bảng orders và customers
-- theo cột customer_id
SELECT *
FROM orders AS o
INNER JOIN customers as c 
    ON o.customer_id = c.customer_id;

-- Khi cột chỉ định ở cả 2 bảng trùng tên
-- có thể sử dụng USING
SELECT *
FROM orders AS o
INNER JOIN customers as c 
    USING(customer_id);

-- Lấy toàn bộ records từ 2 bảng orders và orders_statuses, customers
-- theo cột status và order_status_id
-- bao gồm các cột order_id, order_date, customer full name và status name
-- chỉ lấy các records có status name là 'Shipped'
SELECT 
    o.order_id, 
    o.order_date, 
    CONCAT(c.first_name, ' ', c.last_name) AS customer, 
    s.name 
FROM orders AS o 
INNER JOIN customers AS c 
    USING(customer_id)
INNER JOIN order_statuses AS s 
    ON o.status = s.order_status_id
WHERE s.name = 'Shipped';

-- JOIN dữ liệu trong các CSDL khác nhau
-- Lấy toàn bộ records trong bảng orders, order_items trong sql_store
-- và products trong sql_inventory
SELECT 
    o.order_id, 
    p.name, i.quantity, 
    i.unit_price, 
    (i.quantity * i.unit_price) as total
FROM sql_store.orders AS o 
INNER JOIN sql_store.order_items AS i
    USING(order_id)
INNER JOIN sql_inventory.products AS p 
    USING(product_id);

-- Trong một số trường hợp, chúng ta cần so sánh dữ liệu trong một hàng
-- với các hàng trong chính bảng đó (dữ liệu phân cấp)
-- khi đó, các bảng cần join với chính nó (self join)

-- Lấy tất cả records trong bảng employees từ CSDL sql_hr
-- bao gồm employee_id, employee_name và reports_to
-- reports_to là Employee có id tương ứng
SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    CONCAT(ee.first_name, ' ', ee.last_name) AS reports_to
FROM sql_hr.employees AS e 
INNER JOIN sql_hr.employees AS ee
    ON e.reports_to = ee.employee_id;


-- LEFT JOIN

-- Lấy toàn bộ dữ liệu trong bảng orders và shipper tương ứng

-- Với INNER JOIN sẽ chỉ trả về các orders có thông tin shipper
SELECT *
FROM sql_store.orders AS o 
INNER JOIN sql_store.shippers AS s 
    USING(shipper_id);

-- Với LEFT JOIN trả về toàn bộ records từ orders
-- Record nào có shipper_id sẽ khớp với dữ liệu từ bảng shippers
-- Records nào không có sẽ trả về NULL
SELECT *
FROM sql_store.orders AS o 
LEFT JOIN sql_store.shippers AS s 
    USING(shipper_id);

-- CROSS JOIN
-- CROSS JOIN thường được sử dụng để kết hợp mọi dữ liệu từ 2 bảng
-- Một trường hợp ví dụ là tạo ra các mục kết hợp như kích thước, màu sắc sản phẩm
SELECT *
FROM customers 
CROSS JOIN products;

-- UNION
-- Lấy tất cả name (first_name và name) từ 2 bảng customers và shippers
SELECT first_name AS name
FROM sql_store.customers
UNION
SELECT name
FROM sql_store.shippers;