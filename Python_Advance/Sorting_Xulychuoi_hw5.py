# Bài 1: Sorting - Sắp xếp điểm thi

sort_list_last = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1), (3,2,0)]

def sapxep(list):
    return list[::-1]

print(sorted(sort_list_last, key=sapxep))

#Bài 2: Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường

str_first = input("Nhập vào chuỗi phân cách nhau bởi dấu cách: ")

chuoiconvert = str_first.swapcase()
str_second = chuoiconvert.split(" ")
danhsach = list(str_second)
listsx = danhsach[::-1]

# Hàm join() để ghép các phần tử của mảng --> str
chuoidao = " ".join(listsx)
print(chuoidao)
