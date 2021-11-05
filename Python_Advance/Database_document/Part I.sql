
# Chỉ định CSDL
# Có thể double-click vào 1 CSDL
# Hoặc chỉ định rõ CSDL trong truy vấn
USE sql_store;

# SELECT
# Lấy tất cả các cột trong bảng customers
SELECT *
FROM customers;

# Lấy các cột name, quantity_in_stock trong bảng products
# Nên chỉ định rõ ràng các cột cần lấy
SELECT name, quantity_in_stock
FROM products;

# Có thể sử dụng toán tử, hàm trong mệnh đề SELECT
# Đặt tên (bí danh) cho cột với AS
SELECT 
	concat(first_name, " ", last_name) as fullname,
    points,
    points * 0.1 as bonus_points
FROM customers;

# SELECT không có FROM
SELECT 1 + 2 + 3;

# WHERE
# Lấy ra customer trong bảng customers có points > 3000
SELECT *
FROM customers
WHERE points > 3000;

# Các toán tử so sánh > >= < <= = != <>

# Lấy ra customer trong bảng customers có first_name là "Babara"
SELECT *
FROM customers
WHERE first_name = "babara";


# Lấy ra customer trong bảng customers có birth_date > 1990
# Giá trị ngày tháng có định dạng YYYY-MM-DD
SELECT *
FROM customers
WHERE birth_date > "1990-01-01";

# Lấy tất cả customer có state là MA và points > 2000
SELECT *
FROM customers
WHERE state = "ma" AND points > 2000; 

# Lấy tất cả customer có first_name là Babara hoặc Levy
SELECT *
FROM customers
WHERE first_name = "babara" OR first_name = "levy";

# Sử dụng toán tử IN
SELECT *
FROM customers
WHERE first_name IN ("babara", "levy");

# Lấy tất cả customers có state không phải FL
SELECT *
FROM customers
WHERE NOT state = "fl";

# Lấy tất cả product có unit_price trong khoảng 3 - 5
SELECT *
FROM products
WHERE unit_price BETWEEN 3 AND 5;

# Lấy ra tất cả customer có last_name bắt đầu bằng B
SELECT *
FROM customers
WHERE last_name LIKE "b%";

# Lấy ra tất cả customer có last_name có ký tự thứ 2 là a
SELECT *
FROM customers
WHERE last_name LIKE "_a%";

# Với REGEXP
SELECT *
FROM customers
WHERE last_name REGEXP "^\.a";

# Lấy ra tất cả customer có last_name chứa từ mac hoặc field
SELECT *
FROM customers
WHERE last_name REGEXP "mac|field";

# Lấy ra tất cả customer có last_name chứa e, và trước e là g hoặc i
SELECT *
FROM customers
WHERE last_name REGEXP "[gi]e";

# Lấy ra tất cả customer không có phone
SELECT *
FROM customers
WHERE phone IS NULL;

# ORDER BY
# Lấy ra tất cả customer
# Sắp xếp tập kết quả theo first_name, thứ tự alphabet
SELECT *
FROM customers
ORDER BY first_name ASC;

# Lấy ra tất cả customer
# Sắp xếp theo state, thứ tự alphabet
# Sau đó sắp xếp theo first_name, thứ tự alphabet ngược
SELECT *
FROM customers
ORDER BY state ASC, first_name DESC;

# Lấy ra 5 product trong bảng products
SELECT *
FROM products
LIMIT 5;

# Lấy ra 5 product trong bảng products
# Tính từ product thứ 6
SELECT *
FROM products
LIMIT 5 OFFSET 5;

