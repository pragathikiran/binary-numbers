number = int( input("enter a number"))
binary  = bin(number)[2:]
print("binary is" ,binary)


n = int(input("enter a number"))
if 1 <= n <=len(binary):
    bit = binary[n - 1]
    print("that bit is",bit)

else:
    print("ohhhhhhh! no big number 😒")