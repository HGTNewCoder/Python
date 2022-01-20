# Định nghĩa một class có ít nhất 2 method:

# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

# printString: in chuỗi vừa nhập sang chữ hoa.

# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

class Chuoi():
    def __init__(self):
        self.user = ""
        pass
    def getString(self):
        self.user = input("Enter your String: ")
    def printString(self):
        print(self.user.upper())

bailam = Chuoi()
bailam.getString()
bailam.printString()