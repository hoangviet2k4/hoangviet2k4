def bai_2(x):
    with open(x,'r') as f:
        a = f.read()
        print(a)
        f.close()
bai_2(r'D:\Data\tep_tin.txt')