number = int(input("Enter a number: "))
binary=[]
mask=1
while mask<=number:
    if mask & number >0:
        binary.append(1)
    else:
        binary.append(0)
    mask*=2
binary_res='';
for i in binary:
    binary_res=str(i)+binary_res
print('{0} in binary is: {1}'.format(number,binary_res))
