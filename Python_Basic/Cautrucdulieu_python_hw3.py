# Bài 1: Find Pair

listA = [3, 6, 7, 9, 11, 12] 
sum = int(input("Nhập vào tổng sum: "))
list_result = []

for i in range(0,len(listA)-1):
    for j in range (i+1,len(listA)):
        if listA[i] + listA[j] == sum:
            my_set = (listA[i],listA[j])
            list_result.append(my_set)
          
print("Với tổng bằng {0} thì có số cặp thỏa mãn: {1}".format(sum,list_result))

#Bài 2: Unique value Dictionary

############ Ví dụ 1 ########

value_dict_1 = dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)

value_list = []

for i in value_dict_1:
    value_list.append(value_dict_1[i])

unique_value_dict = set(list(value_list))
print(unique_value_dict)

############ Ví dụ 2 ########

value_dict_2 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

value_list_2 = set()

for i in value_dict_2:
   value_list_2.update(list(i.values()))

print(value_list_2)


#Bài 4: Đếm số

my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
my_dict = dict.fromkeys(my_list)
list_unique=list(my_dict)

for i in list_unique:
    my_dict[i] = my_list.count(i)
print(my_dict)


# Bài 5: Print Star

############ Ví dụ 1 ########

n = int(input("Nhap vao so dong: "))

for i in range(1,n+1):
    #print(i*'\t*')
    print((n-i)*"\t", i*'\t*')


############ Ví dụ 2 ########

so_dong = int(input("Nhap vao so dong: "))

for i in range(1,so_dong+1):
    #print(i*'\t*')
    n = i*'*'
    if i == so_dong:
         print(i*'\t*', end = '')
         break
    print((so_dong-i)*"\t", i*'\t*')

for i in range(so_dong, 0, -1):
    if(i == so_dong):
        print(i*'\t*')
        continue
    print( (so_dong)*"\t", i*'\t*')


#Bài 3: Đếm ngược tới Xmas sau thời gian second giây 

import datetime
import time

xmas = datetime.datetime(2021, 12, 25)
second = int(input("Nhập vào số giây đếm ngược: "))

while True:
   
   today = datetime.datetime.now()
   dem_nguoc = xmas - today
   print("Countdown to Xmas 2021: ",dem_nguoc)
   time.sleep(second)