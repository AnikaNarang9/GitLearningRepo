print("ANIKA NARANG")
print("1/18/FET/BCS/044")
l=[]
sum=0
n=int(input("Enter the size of the array="))
for  i in range (0,n):
  x=int(input())
  l.append(x)
  sum=sum+x
print("Array is :",l)
print("Average of elements =",sum/n)
