def right_triangle(n):
    for i in range(1,n+1):
        print("".join(str(j) for j in range(1,i+1)))

def pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i) + "".join(str(j) for j in range(1,i)) + str(i) + "".join(str(j) for j in range(i-1,0,-1)))

def inverted(n):
    for i in range(n,0,-1):
        print("".join(str(j) for j in range(1,i+1)))

while True:
    print("\n1. Right Triangle\n2. Pyramid\n3. Inverted\n4. Exit")
    ch = input("Choice: ")
    if ch in ["1","2","3"]:
        n = int(input("Rows: "))
        if ch=="1": right_triangle(n)
        elif ch=="2": pyramid(n)
        else: inverted(n)
    elif ch=="4":
        break
    else:
        print("Invalid")