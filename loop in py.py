for j in range(1,5):
    for i in range(1,5):
        if j<=5-i:
            print("*@*",end=' ')

    print("  ")
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print("*#@",end=' ')

    print("  ")



for i in range(1,i+1):
    for j in range(1,j-1):
       if j>=4-i and j<=2+i:
            print("* ", end=' ')

    print(" ")
# trangle code is start from here with expalaintion
height = 5


for i in range(1, height + 1):
    # Print spaces before the stars
    for j in range(height - i):
        print(" " "#", end="")

    # Print stars
    for k in range(2 * i - 1):
        print("@", end="")

    # Move to the next line after printing each row
    print()
j=0
i=5
while i>=j:
    j+=1
    i-=1
    print("@#"*i)

for i in range(1,i+1):
    for j in range(1,j-1):
        if j>=4-i and j<=2+i:
            print(" " "*",end=' ')

    print(" ")
