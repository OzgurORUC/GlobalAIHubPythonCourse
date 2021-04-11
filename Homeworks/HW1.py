# HW1 DAY.2

# Question 1
# Create a list and swap the second half of the list with the first half of the list 
# and print this list on the screen
mylist=[0,1,2,3,4,5,6,7]
mylist=mylist[int(len(mylist)/2):len(mylist)]+mylist[0:int(len(mylist)/2)]
print(mylist)

# Question 2 
# Ask the user to input a single digit integer to a variable 'n'.
# Then, print out all of even numbers from 0 to n (including n)
n=10
while n>9 or n<0:
  n=int(input('tek basamaklı pozitif bir sayı giriniz:'))
  if  n>9:
    print("Hatalı giriş: " + str(len(str(n))) + " basamaklı sayı girdiniz")
  elif n<0:
    print("Hatalı giriş: negatif sayı girdiniz")
print(list(range(0,n+1,2)))