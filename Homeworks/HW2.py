# HW1 DAY.3

# Question 1
# User login Application
# - get username and password values from user.
# - check the values in an if statement and tell the user if they were successful.
username = "Ozgur"
password = "sifreozgur123"
hataligiris=0;
while True:
    if hataligiris == 3:
        print("Şifreniz bloke olmuştur, bir süre sonra tekrar deneyiniz, hatalı giris sayınız: " + str(hataligiris))
        break  
    username1 = input("Lütfen kullanıcı adınızı giriniz: ")
    password1 = input("Lütfen parolanızı giriniz: ")        
    if (username != username1 and password == password1):
        hataligiris +=1
        print("Kullanıcı adınız hatalı, hatalı giriş sayısı: " + str(hataligiris) + " kalan hakkınız: " + str(3-hataligiris))
    elif (username == username1 and password != password1):
        hataligiris +=1    
        print("Parolanız hatalı, hatalı giriş sayısı: " + str(hataligiris) + " kalan hakkınız: " + str(3-hataligiris))
    elif (username != username1 and password != password1):
        hataligiris +=1    
        print("Kullanıcı adınız ve parolanız hatalı, hatalı giriş sayısı: " + str(hataligiris) + " kalan hakkınız: " + str(3-hataligiris))
    else:
        print("Tebrikler, Başarıyla giriş yaptınız")
        if hataligiris>0:
            print("Bilginize, hatali giris sayınız: " + str(hataligiris))                
            hataligiris=0
        break
input("Herhangi bir tuşa basarak devam edebilirsiniz!")

# Question 2
# Extra try building the same user login application but this time, use a dictionary!
NamePass = {"Ozgur":"sifreozgur123", "Ahmet":"ahmet135", "Mehmet":"147mehmet"}
hataligiris=0;
girisdurum=False;
while True:
    if hataligiris == 3:
        print("Şifreniz bloke olmuştur, bir süre sonra tekrar deneyiniz, hatalı giris sayınız: " + str(hataligiris))
        break  
    username1 = input("Lütfen kullanıcı adınızı giriniz: ")
    password1 = input("Lütfen parolanızı giriniz: ")  
    for u,p in NamePass.items():    
        if (u == username1 and p == password1):
            girisdurum = True
    if  girisdurum:  
        print("Tebrikler, Başarıyla giriş yaptınız")
        if hataligiris>0:
            print("Bilginize, hatali giris sayınız: " + str(hataligiris))                
            hataligiris=0
        break
    else:
        hataligiris +=1    
        print("Giriş bilgileriniz hatalı, hatalı giriş sayısı: " + str(hataligiris) + " kalan hakkınız: " + str(3-hataligiris))
input("Herhangi bir tuşa basarak çıkabilirsiniz!")       