# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
# Tính tổng của dãy số và hiển thị ra màn hình.
a = input()
b = a.split()
c = 0
d = len(b)
for i in range(0, int(d)):
    c += int(b[i])
print("Do dai cua day so la: ", d)
print("Tong cua day so la: ", c)