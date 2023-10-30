# lekcia 3

x=float(input('ներմուծեք առաջին թիվը  '))
y=float(input('ներմուծեք երկրորդ թիվը  '))
op=input('ներմուծեք գործողությունը  ')
if op=='+':
    res=x+y
    print(x,'+',y,'=',res)

if op=='-':
    res=x-y
    print(x,'-',y,'=',res)

if op=='/':
    if y==0:
        print('Թիվը 0-ի վրա բաժանել չի կարելի') 
    else:
        res=x/y
        print(x,'/',y,'=',res)
    
if op=='*':
    res=x*y
    print(x,'*',y,'=',res)