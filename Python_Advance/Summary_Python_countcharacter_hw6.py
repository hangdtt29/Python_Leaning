#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021
########

"""Wordcount exercise

Hàm main() đã được định nghĩa hoàn chỉnh ở dưới. Bạn phải viết hàm print_words()
và print_top() mà sẽ được gọi từ main().

1. Với đối số --count, viết hàm print_words(filename) đếm số lần xuất hiện của mỗi từ 
trong file đầu vào và in ra theo định dạng sau:
word1 count1
word2 count2
...

In danh sách trên theo thứ tự từ điển các từ (python sẽ sắp xếp dấu câu đứng trước
các chữ cái nên cũng không thành vấn đề). Lưu tất cả các từ dưới dạng chữ thường,
vì vậy 'The' và 'the' được tính là cùng một từ.

2. Với đối số --topcount, viết hàm print_top(filename) tương tự như print_words()
nhưng chỉ in ra 20 từ thông dụng nhất sắp xếp theo từ thông dụng nhất ở trên cùng.

Tùy chọn: định nghĩa một hàm helper để tránh lặp lại code trong các hàm 
print_words() và print_top().

"""

import sys
import re

# +++your code here+++
def dict_words(filename):
    
    with open(filename, 'r') as f:
            chuoidocra = f.read()
      
            new_string = re.sub("[^a-zA-Z0-9]"," ",chuoidocra.lower())
            danhsach = new_string.split()
    danhsach.sort()
    my_dict = dict.fromkeys(danhsach)
    list_unique=list(my_dict)
    for i in list_unique:
        my_dict[i] = danhsach.count(i)
    return my_dict

def print_words(filename):
    
    dict_sx = dict_words(filename)
    for words in dict_sx.items():
        print(words[0],words[1])
    

def print_top(filename):
  dict_top = dict_words(filename)
  words_common = sorted(dict_top.items(), key=lambda value: value[1], reverse=True)
  if len(words_common) <= 20:
    for i in words_common:
            print(i)
  else:
    for i in range(0,20):
      print(words_common[i])

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
