b = str(input("Nhập một chuỗi kí tự từ bàn phím: "))
def bai_3(x):
    with open(x,'b') as f:
        f.write('\n')
        f.write(b)
        f.close()
bai_3(r'D:\Data\tep_tin.txt')