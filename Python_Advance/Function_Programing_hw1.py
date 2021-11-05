#Bài 1: Function - Chỉ số thống kê mô tả

# Nhập vào phần từ của list từ bàn phím
num = int(input("Nhập số phần tử của list : "))
mylist = []
for i in range(1,num + 1):

   val = int(input('Nhập giá trị điểm thi thứ {}: '.format(i)))
   mylist.append(val)

# Hàm sắp xếp theo thứ tự tăng dần 
def sapxep(args):
   
   for i in range(0,len(args)+1):
      for j in range(i+1,len(args)):
        
         if args[i] > args[j]:
          trunggian = args[i]
          args[i] = args[j]
          args[j] = trunggian
   return args

# Hàm tinhs trung bình của 1 list
def mean(args):
   
   sum = 0
   for v in args:
      sum += v
   return sum/len(args)


# Hàm tính giá trị trung vị
def median(list):

   if (len(list)%2 != 0):
      stt = int((len(list)-1)/2)
      median = list[stt]
   else:
      stt1 = int(len(list)/2)
      stt2 = int(len(list)/2+1)
      median = (list[stt1] + list[stt2])/2
   return median

'''Hàm tìm mode của 1 dãy list []
   Chuyển dãy thành 1 dict {}
   Add value thành 1 list riêng --> Tìm giá trị max nhất của list đó
   Run từng phần tử của 1 dict --> map giá trị max với key tương ứng trả về 1 list mode
'''
def mode(listDs):
    my_dict = dict.fromkeys(listDs)
    list_unique=list(my_dict)

    count = []
    
    for i in list_unique:
        my_dict[i] = listDs.count(i)
        count.append(my_dict[i])
        
    maxgt = max(count)
    resultMode = []

    for point, count in my_dict.items():  
        if count == maxgt:
            resultMode.append(point)

    return resultMode

mean,median,mode = mean(mylist),median(mylist),mode(mylist)
print("Mean, Median, mode of list {}==".format(mylist), (mean,median,mode) )

# Bài 2: Function - Đếm loại ký tự

words_first = input("Nhập vào một chuỗi đầu vào: ")

def demkitu(words):

    letter = 0
    digitals = 0
    other = 0
    upper = 0
    lower = 0
    dict_kitu = {"LETTERS":None, "CASE": {"UPPER CASE":None, "LOWER CASE":None}, "DIGITS":None}
    
    for i in words :
        if i.isalpha():
            letter+=1
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
        elif i.isdigit():
            digitals+=1
        else:
            other+=1
    
    dict_kitu["LETTERS"] = letter
    dict_kitu["DIGITS"] = digitals
    dict_kitu["CASE"]["UPPER CASE"] = upper
    dict_kitu["CASE"]["LOWER CASE"] = lower
    return dict_kitu

print(demkitu(words_first))