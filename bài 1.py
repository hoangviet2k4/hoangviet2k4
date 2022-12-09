a = str(input("Nhập một chuỗi kí tự từ bàn phím : "))
def tep_tin(x):
    with open(x,'w') as f:
        f.write(a)
        f.close()
tep_tin(r'D:\Data\tep_tin.txt')