# Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.
from decimal import Decimal
a = float(input("Nhập số cần làm tròn: "))
b = int(input("Nhập chữ số cần làm tròn: "))
print('{0:{1}f}'.format(a, b))