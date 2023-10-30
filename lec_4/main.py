# lekcia 4
user_input=input('Ներմուծեք դրական թվեր առանձնացված բացատներով։')
arr=[int(num) for num in user_input.split()]
Even=[]
Odd=[]

for i in range(0,len(arr)):
    if arr[i]%2==0:
        Even.append(arr[i])
    else:
        Odd.append(arr[i])

print('Even numbers:',Even)
print('Odd numbers',Odd)