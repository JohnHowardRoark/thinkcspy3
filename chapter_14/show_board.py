def print_layout(a):
    for x in range(len(a)):
        for i in range(len(a)):
            if a[i] == x:
                print("x ", end = "")
            else:
                print("o ", end = "")
        print()
    print()


b = [0,4,7,5,2,6,1,3]
print("layout of ", b)
print_layout(b)
