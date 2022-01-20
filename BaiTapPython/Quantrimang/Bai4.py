# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy 
# từ giao diện điều khiểntạo ra một danh sách và một tuple chứa mọi số.

# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

a = input("Nhap chuoi so: ")
b = a.split(",") # Tach cac dau phay
tup = tuple(b)
print(b)
print(tup)