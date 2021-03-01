from matplotlib import pyplot as  plt

#v=str(input("enter your label 1 :-"))
#w=str(input("enter your label 2 :-"))
#x=str(input("enter your label 3 :-"))
#y=str(input("enter your label 4 :-"))
#players=[v,w,x,y]
#a=input("enter you value 1 ")
#b=input("enter your value 2 ")
#c=input("enter your value 3 ")
#d=input("enter your value 4 ")
#score=[a,b,c,d]
#explode=(0.1,0,0,0)



a=int(input("enter your number of input :- "))
print(a)
data=[]
value=[]
explode=[]
for i in range (a):
    data.append(input("enter your label :- "))
    value.append(int(input("enter your value :- ")))
    explode.append(float(input("enter your explode :- ")))

print(data)
print(value)
print(explode)
fig1,ax1=plt.subplots()
ax1.pie(value,explode=explode,labels=data,autopct='%1.1f%%',shadow=True,startangle=360 )
ax1.axis()
plt.show()

