num=int(input("Enter Number: "))

if num%2!=0:
  for i in range(3,int(num/2)+1,2):
      if num%i==0:
          print(num,"Not prime Number")
          break

      else :
          print(num,"prime Number")
else:
     print(num,"not prime Number")





  
