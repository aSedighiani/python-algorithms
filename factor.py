def print_factors(a):
   print("The factors of",a,"are:")
   for i in range(1, a + 1):
       if a % i == 0:
           print(i)

num = int(input("enter a number: "))
print_factors(num)