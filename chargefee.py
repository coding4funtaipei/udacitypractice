# 國道收費
# 計算價錢


def price(km):
    if(km <= 20):
        return "0元"
    elif(km <= 200):
        return str((km-20)*1.2) + "元"
    else:
        return str((200*1.2 + (km-200)*0.8)) + "元"


# 將使用者輸入的公里數做計算
print(price(int(input("請輸入你的公里數："))))
