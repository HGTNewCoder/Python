# Viết một method tính giá trị bình phương của một số.
value = int(input("Nhap so can binh phuong: "))
def square(num):
    return num ** 2

print("Binh phuong cua so do la: ", square(value))