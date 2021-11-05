#Bài 1: Chỉ số BMI: Chỉ số cơ thể

height = float(input("Nhập vào chiều cao theo m: "))
weight = float(input("Nhập vào cân nặng theo kg: "))

BMI = weight / (height * height)

if BMI < 17:
    print("Gầy độ II")
elif 17 <= BMI < 18.5:
    print("Gầy độ 1")
elif 18.5 <=BMI < 25:
    print("Bình thường")
elif 25 <=BMI < 30:
    print("Thừa cân")
elif 30 <=BMI < 35:
    print("Béo phì độ I")
else:
    print("Béo phì độ II")


#Bài 2: Kiểm tra năm nhuận

year = int(input("Nhập vào năm: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print("{} là năm nhuận".format(year))
else:
    print("{} không phải là năm nhuận".format(year))


#Bài 3: Kiểm tra số lớn nhất trong 3 số

a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))
c = int(input("Nhập vào số thứ ba: "))

if a < b:
    if b < c:
        print("Số lớn nhất là: ", c)
    else:
        print("Số lớn nhất là: ", b)
else:
    if a < c:
        print("Số lớn nhất là:", c)
    else:
        print("Số lớn nhất là: ", a)