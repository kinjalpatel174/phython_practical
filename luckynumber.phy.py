import random



#print(random.randit(1000,999))
#print(random.choice[1,2,1.1,2.2,"tops","phython",true,false]))

l=[]
lucky=[]


for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)



print(l)
print(lucky)
