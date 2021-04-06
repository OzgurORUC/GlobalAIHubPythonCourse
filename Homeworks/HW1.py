#Explain your work

#Question 1
mylist=[0,1,2,3,4,5,6,7]
mylist=mylist[4:8]+mylist[0:4]
print(mylist)

#Question 2 basit cevap
n=int(input('tek basamaklı bir sayı giriniz:'))
print(list(range(0,n+1,2)))

#Question 2 diğer cevap
#while uygulaması ile tek basamaklı sayı girdisine zorluyoruz
n=10
while n>9 or n<0:
  n=int(input('tek basamaklı bir sayı giriniz:'))
print(list(range(0,n+1,2)))