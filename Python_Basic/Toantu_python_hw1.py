#Chuyển đổi nhiệt đồ từ độ C sang độ F,K,R
tempC = float(input("Nhap nhiet do C: "))
tempF = tempC * 9 / 5 + 32
tempK = tempC + 273.15
tempR = (tempC + 273.15) * 9 / 5
print ("Nhiet do theo do F: ", tempF)
print ("Nhiet do theo do K: ", tempK)
print ("Nhiet do theo do R: ", tempR)


# Chuyển đổi độ dài km sang m,mm,cm,..
lengthKm = float(input("Nhap vao gia tri do dai theo km: "))
print ("Giá trị theo m = %.2f" %(lengthKm*1000))
print ("Do dai theo dm = %.2f " %(lengthKm*10000))
print ("Do dai theo cm = %.2f " %(lengthKm*100000))
print ("Do dai theo mm = %.2f " %(lengthKm*1000000))
print ("Do dai theo mile = %.2f " %(lengthKm*1.609344))
print ("Do dai theo inch = %.2f " %(lengthKm*39370.1))


#Chuyển đổi thời gian từ giây sang giờ, phút, giây
sec = int(input("Nhập vào số giây: "))
hour = sec // 3600
minutes = (sec % 3600) // 60
sec_real = (sec % 3600) % 60
print("Với {} giây thì giờ hiện tại là: {} giờ, {} phut, {} giây".format(sec,hour,minutes,sec_real))
