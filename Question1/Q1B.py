print("This Program calculate (a+b) or (a-b) or (a*b) or (a/b)")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Enter the operation: ")
if operation=="+":
    res=a+b
elif operation=="-":
    res=a-b
elif operation=="*":
    res=a*b
elif operation=="/":
    res=a/b
else:
    res='error'
if res!='error':
    print("{0}{1}{2}={3}".format(a,operation,b,res))
else:
    print(res)
