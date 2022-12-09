def bai_4(x):
    with open(x,'r') as f:
        z = f.read()
        print(z)
        f.close()
bai_4(r'D:\Data\tap_tin.txt')