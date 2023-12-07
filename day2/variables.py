a_='bhumi'
b=-10
print(id(a_))
print((b))

name='bn46'
age=26
objective="to learn py"

print(name,age,objective)

x=y=z=46
print(x,y,z)

b,k,ab='bhumi is atheist','kaluyan is partially_religious','abishek isfull_religious'
print(b)
print(k)
print(ab)

#python variable type
#local variables

def add():
    a=46
    b=0
    c=a+b
    print("the sum of two num is",a)
add()

#globalvariables
ex='nithya'
def mylove():
    global ex
    print(ex)
    #changing global variable
    ex=('she is not my ex,she is my forever')
    print(ex)
mylove()
print(ex)

bn=46464646464646464646464646464646464646464646464646464646464
bn=bn+1
print(bn)