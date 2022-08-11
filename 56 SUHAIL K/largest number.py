a = [1,2,3,4,5,6,7,8]
max = a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
print("the greatest number is: " ,max)
