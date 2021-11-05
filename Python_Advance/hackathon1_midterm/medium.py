def anagram_number(number):
    raw_number = number
    revert_str = ""
    while (number != 0):
        revert_str += str(number % 10)
        number = number // 10  
    number_revert = int(revert_str)
    if (raw_number == number_revert):
        return True
    else:
        return False
        
   
'''
Viết hàm in ra số với chuỗi số la mã nhập vào
Định nghĩa 1 dictionary cho kí tự La mã
Cộng từ kí tự cuối cùng
Run for chuỗi nhập vào --> tính tổng giá trị 
So sanh kí tự đứng trước với kí tự đứng sau
    Nếu kí tự đứng trước >= kí tự đứng sau --> cộng 
    Else: Cộng với số âm của nó
'''

def roman_to_int(s):
    dict_roman = {'I':1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
    mang_roman = list(s)
    final = len(mang_roman)
    number_final = mang_roman[final-1]

    sum = dict_roman[number_final]

    for i in range(0, len(mang_roman)-1):
        number_first = mang_roman[i]
        number_second = mang_roman[i+1]
        if (dict_roman[number_first] >= dict_roman[number_second]):
            sum = sum + dict_roman[number_first]
        else:
            sum = sum + (dict_roman[number_first])*-1
    return sum
