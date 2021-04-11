# Final Project
# Knowledge competition (case sensitive istenmiş ama ben şıklı yaptım)
sorulist = [{"Türkiye’nin uluslararası otomatik telefon kod numarası kaçtır?":["00","90","80","09"]},
            {"Pusulada ( N ) harfi hangi yönü ifade eder?":["Güney","Doğu","Batı","Kuzey"]},
            {"Gece gündüz eşitliği (ekinoks) bir yılda kaç kez gerçekleşir?":["1","2","3","4"]},
            {"Türkiye’de Erozyonla mücadele amacıyla kurulan vakfın kısa adı nedir?":["TMO","DSİ","Tema","TKK"]},            
            {"Altın Palmiye sinema ödülü hangi film festivalinde verilmektedir?":["Londra","Paris","Cannes","Barcelona"]},            
            {"Dünyanın ilk haritasını çizen ünlü Türk denizcisi kimdir?":["İbni Sina","Oruç Reis","Piri Reis","Barbaros Hayrettin"]},
            {"Çocuk hakları günü hangi tarihte kutlanmaktadır?":["23 Nisan","20 Kasım","28 Eylül","26 Nisan"]},            
            {"Nobel ödülleri hangi ülkede verilmektedir?":["Almanya","İsveç","Norveç","Danimarka"]},
            {"Amerika kıtasını 2’ye ayıran önemli su geçidinin adı nedir?":["Süveyş","CebeliTarık","Panama","Berink"]},
            {"İlk Türk kadın dağcı kimdir?":["İlmiye Bergman","Nasuh Mahruki","Gülnur Tumbat","Burçak Özoğlu Poçan"]}];
cevaplist=["b","d","b","c","c","c","b","b","c","a"]
soruno=0
dogrucevapsay=0
hatasiklar={}
hatalist=[]
print(str(len(cevaplist)) + " soruluk bilgi yarışmasına hoşgeldiniz\n")
for k in sorulist:
    soruno+=1    
    for s,v in k.items():
        print("Soru " + str(soruno) + " : ", s, "\n a) ", v[0],"\n b) ", v[1], "\n c) ", v[2],"\n d) ", v[3])    
        cevap = input("Cevap şıkkını giriniz (a,b,c,d): ")
        if cevap == cevaplist[soruno-1]:
            dogrucevapsay+=10
        else:
            hatasiklar[soruno]=cevap
    print("*****************************************************\n")
if dogrucevapsay<60:
    print("Sonucunuz (100 üzerinden): " + str(dogrucevapsay) + ", başarısız oldunuz, tekrar deneyiniz\n")
    for k,v in hatasiklar.items():
           print(str(k) + ".soruyu " + str(v) + " diyerek hatalı cevapladınız, dogru cevap: " + cevaplist[k-1] + "\n")    
else:
    print("Sonucunuz (100 üzerinden): " + str(dogrucevapsay) + ", başarılı oldunuz, tebrikler\n")
    if dogrucevapsay<100:
        for k,v in hatasiklar.items():
           print(str(k) + ".soruyu " + str(v) + " diyerek hatalı cevapladınız, dogru cevap: " + cevaplist[k-1] + "\n")
input("Herhangi bir tuşa basarak çıkabilirsiniz!")