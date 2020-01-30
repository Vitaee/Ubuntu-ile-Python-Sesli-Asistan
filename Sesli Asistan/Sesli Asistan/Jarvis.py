from gtts import gTTS #google yazıdan sese yazılı olan bir kelimeyi veya cümleyi
#bize sesli olarak yansıtır ve çalışması için internet gereklidir.
#https://pypi.org/project/gTTS/

import speech_recognition as sr #sesimizi tanıyıp algılıyor,
#https://pypi.org/project/SpeechRecognition/

import os
from os import system as komut

import wikipedia #wikipedia ulaşımımızı sağlayan modül
#https://pypi.org/project/wikipedia/

import webbrowser #bu modül ile istenilen bir web sitesini açtırıyoruz
#https://www.pythondersleri.com/2014/01/webbrowser-modulu.html (türkçe kaynak)

import smtplib #gmail göndermek için kullanılan modül
#https://docs.python.org/3/library/smtplib.html

import datetime #bilgisayarımızdan anlık tarih çekmemize yarıyor
import time #anlık saat gösterimi
import sys

import cv2 #opencv modülü kameramıza erişimimizi sağlayıp yüzümüzü odaklatıyoruz
#ve istersek anlık görüntü kayıt edebiliyoruz.
#https://pypi.org/project/opencv-python/

import random

import pyowm #hava durumu bu projemde sıcaklık , nem ve rüzgar hızını ele aldım.
#https://pypi.org/project/pyowm/

import psutil #sistemimiz hakkında bilgi edinebiliyoruz.Bu projemde disk,ram ve
#işlemci sıcaklığı hakkında bilgiler alıyorum. https://pypi.org/project/psutil/

import fbchat #facebook hesabımıza giriş yapıp mesaj gönderebiliyoruz bu
#modülümüzle, https://pypi.org/project/fbchat/
from getpass import getpass #Bizden şifremimizi istiyor ve şifremimizi yazıp
#hesabımıza giriş yapabiliyoruz. https://docs.python.org/2/library/getpass.html

from pygame import mixer #Bu projemde belirtilen bir müziği oynatmak ve
#durdurmak için kullanıyorum, https://www.pygame.org/docs/ref/mixer.html

from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys


from googletrans import Translator #google translate modülü, bu projemde
#söylenen ingilizce kelimeyi türkçeye çeviriyoruz veya türkçe den ingilizceye.
#https://pypi.org/project/googletrans/

from googlesearch import search #google arama motorunu bu modül ile kullanıyoruz
#projemde bir fonksiyon kullanarak herhangi bir konuyu sesli olarak
#arayabiliyoruz.
#https://pypi.org/project/google-search/

from youtube_search import YoutubeSearch #youtube modülünü kullanarak şarkı /
#video araması yapıyoruz


from pydub import AudioSegment #pip install pydub
from pydub.playback import play # bu 2 modül için daha önce burdaki adımlar -
#yapılmalı.
#https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg



buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
#verilen komut içerisindeki büyük harfleri(varsa) bulup küçük harfe çeviriyoruz

def lower(command:str): #türkçe alfabesini entegre ettik, küçük veya büyük harf sorununu kaldırmış olduk.
    newText = str()
    for i in command:
        if i in command:
            if i in buyukAlfabe:
                index = buyukAlfabe.index(i)
                newText += kucukAlfabe[index]
            else:
                newText += i
    return newText

def konusBenle(audio): #bu fonksiyon ile bilgisayarımızın konuşma dilini belirledik
    print(audio)
    tts = gTTS(text=audio, lang="tr")
    tts.save("audio.mp3") #mp3 formatında kayıt ettik
    sound = AudioSegment.from_file("audio.mp3", format="mp3")  #kayıt ettiğimiz dosyamızı pydub modülü ile oynatıyoruz.
    play(sound)

#komutlar için dinle

def komutlar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        komut("clear") #gereksiz yazıları temizliyoruz
        print("Diğer komut için hazırım") #ekranda yazılı kalacak metnimiz
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) #ortam sesini azaltıp sesimize yoğunlaşıyor
        audio = r.listen(source) #source yani mikrofonumuzun algıladığı ses bizim sesimiz


    print("Dur.")
    try:
        command = r.recognize_google(audio,language="tr")
        command = lower(command)

        print("Söylenen: " + command + "\n") #ekrana sesli komutumuzu yazdırdık
        #time.sleep(2)
    #sesimizi tekrar dinlesin
    except sr.UnknownValueError:
        #konusBenle("Son komutunuz anlaşılmadı")
        print("Son komutunuz anlaşılmadı.")
        command = komutlar();


    return command

def searchOnGoogle(command,outputList): #google arama motorunu kullanarak internette gezinmemizi sağladık. sesli arama yapma
    konusBenle("İlk beş sonuç")
    for output in search(command,tld = "co.in",lang = "tr", num = 10, stop = 5 , pause = 2):   #bir maddeyi konuyu aradığımızda başta çıkan ilk 5 sayfayı ele aldık
        print(output)
        outputList.append(output)   #çıkan 5 sonucu listemize append ettik
    return outputList

def openLink(outputList):
    konusBenle("İlk sayfa açılıyor")
    webbrowser.open(outputList[0])  #ilk sayfanın açılmasını sağladık [0] = 1.sayfa


def get_size(bytes, suffix="B"):   #Bilgisayar hakknda bilgi amaçlı yazılan fonks
# https://www.thepythoncode.com/article/get-hardware-system-information-python

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# komutlarımız;

insta = ["instagram","aç instagram","instagram aç","Instagram","İnstagram","ınsta","insta"]
face = ["facebook","facebook aç","aç facebook","Facebook","face","feys"]
facemesaj = ["mesaj gönder","facebook ile mesaj gönder","facebooktan mesaj gönder"]
twitt = ["twitter","twitter aç","aç twitter","Twitter","twitt","twit","twitt","tvit","tvitt","tivit","tivitter","tivitt"]
gthb = ["github","aç github","aç githab","aç githap","githap aç","github aç","gitab","gitap","githab","githap","git hap"]
hıztest = ["hız","hız testi","internet hızı","internet durumu","internet hızı","internet hız testi","internetin hızı"]
webcm = ["kamera","kamerayı aç","kamerayu açar mısın","aç kamera","beni göster","kendimi göster","yüzümü tanı","tanı yüzümü"]
meraba = ["merhaba","selam","merhabalar","alo","selamlar","merhaba selam"]
merbdonus = ["merhaba","selam","heyy","merhaba hoşgeldin"]
e_mail = ["e-posta gönder","posta gönder","mail gönder","email gönder","e-mail gönder","gmail gönder","g-mail gönder"]
kapatma = ["sistemi kapat","uyu","kendini kapat","uyu uyu"]
tarayıcı = ["tarayıcımı aç","web tarayıcımı aç","tarayıcı","tarayıcı aç","tarayıcımı aç","tarayıcıyı aç","tarayıcımı aç","google aç","google'ı aç"]
site = ["reddit aç","web sitemi aç","favori sitemi aç","favori web sitesini aç","favori web sitemi aç","favori sayfamı aç","favori web sayfasını aç","favori web sayfamı aç","reddit sayfasını aç","reddit'i aç"]
kimsin = ["seni kim yarattı","sen kimsin","seni kim oluşturdu","kimsin","nesin","nesin sen","yaratıcın kim","kendini tanıt","tanıt"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
donus = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
iltifat = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","teşekkür ederim","çok","iyi","çok iyi"]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
nasilsincumeleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon","ne yapıyorsun",]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın","ayın kaçı"]
mzik = ["müzik","müzik oynat","müzik çal","çal müzik","müzik aç","aç müzik"]
mzik_kes = ["müzik kes","müziği kes","kes","dur","müziği durdur","kes müziği","dur dur müziği","dur dur","dur dur"]
islemci = ["işlemci hakkında bilgi","işlemci kullanımı","işlemci","işlemcim","işlemcim hakkında bilgi","işlemci durumu","işlemcimin durumu"]
ramm = ["ram hakkında bilgi","rem hakkında bilgi","ram","rem","bellek kullanımı","bellek","belleğin durumu","bellek hakkında bilgi"]
dsk = ["disk kullanımı","disk hakkında bilgi","diskim nasıl","disk durumu","disk ne kadar dolu","disk","diskim","harddisk","harddiskim","harddisk hakkında bilgi","harddisk durumu"]
blgs_kapat = ["bilgisayarımı kapat", "kapat bilgisayarı","kapat bilgisayarımı","bilgisayar kapan"]
blgs_ynden = ["bilgisayırımı yeniden başlat","yeniden başlat","başlat yeniden"]
blgs_otrm = ["oturumu kapat","oturumumu kapat","bilgisayar oturumunu kapat","uykuya al","bilgisayarı uykuya al","bilgisayar oturumumu kapat"]
yttube = ["youtube","aç youtube","youtube aç","you tube","aç you tube","you tube aç"]
srki_ytbe = ["şarkı aç","aç şarkı","youtube ile şarkı aç","you tube ile şarkı aç","şarkı"]
arstr = ["araştır","google ile araştır","google araştır"]

def asistan(command):
    if command in tarayıcı:
        webbrowser.open("www.google.com.tr")

    elif command in kimsin:
        a = """Ben Can İlgu tarafından geliştirilmekte olan bir sesli asistan projesiyim sizin hayatınızı kolaylaştırmak
        istiyorum"""
        konusBenle(a)

    elif command in meraba:
        konusBenle(random.choice(merbdonus))

    elif command in mzik:
        mixer.init()
        mixer.music.load('/home/can/Downloads/Ezhel - LOLO.mp3') #müziğin konumunu belirledik
        mixer.music.play() #çalmasını sağladık
    elif command in mzik_kes:
        mixer.music.stop() #durdurma komutu , mixer.music.pause() o anki saniyede durdurur.

    elif command in facemesaj: #"mesaj gönder" in command:
        username = "facebook kullanıcı adınız" #örnek: https://www.facebook.com/can.ilgu  , can.ilgu benim kullanıcı adım.
        konusBenle("Merhaba " + username)
        konusBenle("Lütfen facebook şirenizi giriniz.")
        client = fbchat.Client(username, getpass()) # facebook şifreniz.
        no_of_friends = 1
        for i in range(no_of_friends):
            konusBenle("Arkadaşınızın adını giriniz.")
            name = str(input("Name: ")) # arkadaşınızın kullanıcı adı.
            friends = client.searchForUsers(name)
            friend = friends[0] #oluşturulan listediki ilk isim zaten 1 isim diye ayarladık
            konusBenle("Lütfen mesajınızı yazınız.")
            msg = str(input("Message: ")) #mesajımızı yazıyoruz
            sent = client.sendMessage(msg, thread_id=friend.uid)
            if sent:
                konusBenle("Mesajınız başarıyla gönderilmiştir.") #mesaj gönderildiyse bu yazı ekrana basılacak.

    elif command in iltifat:
        msg1 = ["Rica ederim","beni utandırıyorsun","utandım","Rica","yardımcı olabildiysem ne mutlu bana"] #teşekkürler dediğimizde bu 3 cümleden bir tanesini seçip bizle konuşacak.
        konusBenle(random.choice(msg1))


    elif command in islemci:
        print("="*20, "CPU Info", "="*20) #Cpu İnfo yazısını yazdırdık soluna ve sağına 20şer tane = işareti koydum
        #print("Physical cores:", psutil.cpu_count(logical=False))
        print("Toplam çekirdek:", psutil.cpu_count(logical=True)) #İŞlemci de bulunan çekirdek sayısı
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz") #anlık işlemci Ghz
        print("CPU Usage Per Core:") #Cpu kullanımının yüzdelik görünümü
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%") #totalde kullanılan işlemci yüzdeliği
        time.sleep(5) #bu bilgileri gösterdikten 5 saniye sonra bekletiyoruz

    elif command in ramm:
        svmem = psutil.virtual_memory()
        print("="*20, "RAM Kullanımı", "="*20)
        print(f"Toplam: {get_size(svmem.total)}") #totalde sahip olunan ram
        print(f"Kullanılan: {get_size(svmem.used)}")  #kullanılan ram
        print(f"Yüzdelik: {svmem.percent}%") #kullanılan ramin yüzdeliği
        time.sleep(5)

    elif command in dsk:
        partition_usage = psutil.disk_usage('/') #() içinde '/' koyduğumuz bu işaret disk'in konumunu gösterir ve onun hakkında bilgi almamımızı sağlar
        print(f"  Toplam alan: {get_size(partition_usage.total)}")
        print(f"  Kullanılan: {get_size(partition_usage.used)}")
        print(f"  Boşta: {get_size(partition_usage.free)}")
        print(f"  Yüzdelik: {partition_usage.percent}%")

        time.sleep(5)

    elif command in blgs_kapat:
        konusBenle("Bilgisayarınız 5 saniye içinde kapanacak")
        time.sleep(5)
        os.system("shutdown now -h") #ubuntudaki bilgisayar kapatma kodu

    elif command in blgs_ynden:
        konusBenle("Bilgisayarınız yeniden başlatılacak")
        time.sleep(3)
        os.system("shutdown -r now") #yeniden başlatma komutu

    elif command in blgs_otrm:
        konusBenle("Bilgisayarınız uykuya alınıyor")
        time.sleep(3)
        #os.system("gnome-session-quit") #eminmisiniz diye soruyor
        os.system("gnome-session-quit --no-prompt") #direkt olarak oturumu kapatıyor.
    elif "tarayıcımı kapat" in command:
        os.system("pkill firefox")

    elif command in webcm:
        konusBenle("Kameranız açılıyor")
        print("Çıkış için ESC")
        print("Kayıt etmek için SPACE") # o an ki görüntüyü kayıt etmek istersek SPACE tuşuna basabiliriz
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        video_capture = cv2.VideoCapture(0) #opencv kullanarak yüzümüzü tanıtıyoruz

        img_counter = 0

        while True:

            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            k = cv2.waitKey(1)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )


            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


            cv2.imshow('FaceDetection', frame)

            if k%256 == 27: #ESC
                break

            elif k%256 == 32: #SPACE

                img_name = "facedetect_webcam_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1


        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()



    elif "nerede" in command or "nerededir" in command or "neresi" in command: #Türkiye nerede diye seslendiğimizde google haritaları açıp türkiyenin nerde olduğunu gösterecek
        konusBenle("Hemen gösteriyorum")
        command = command.replace("nerede","")
        location = command #konumu command a eşitleyip hangi ülke veya şehrin nerde olduğunu görebiliyoruz
        #konusBenle(location + " burada")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;") #google mapsi açarak türkiyenin nerde olduğunu öğrenebiliyoruz.
        #webbrowser.open("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif command in yttube:
        webbrowser.open("youtube.com")

    elif command in srki_ytbe:
        konusBenle("Hangi şarkıyı açmamı istersiniz?")
        cevap1 = komutlar()
        results = YoutubeSearch(cevap1, max_results=1).to_dict() #youtube dan şarkımızı aratıp (tek sonuçlu arama yaptık)
        for v in results: #ilk sonucu alıp açtırıyoruz.
            print('https://www.youtube.com.tr' + v['link'])
            time.sleep(2)
        konusBenle("Bu şarkıyı açmamı istermisiniz?")
        cevap2 = komutlar()
        if "aç" in cevap2 or "evet" in cevap2 or "evet aç" in cevap2:
            konusBenle("Açılıyor")
            webbrowser.open('https://www.youtube.com.tr' + v['link'])
        if "hayır" in cevap2:
            konusBenle("Tamam, işlemi iptal ediyorum")


    elif command in site:
        konusBenle("Web sitesi açılıyor")
        webbrowser.open("www.stackoverflow.com")


    elif command in nasilsincumeleleri:
        msg = donus
        konusBenle(random.choice(msg))

    elif command in saat:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") #H = hour , M = minute , S = Second
        konusBenle(f"Efendim, şuan saat {strTime} ")

    elif command in gun:
        strDay = datetime.datetime.now().strftime("%B %d %A")
        konusBenle(f"Bugün günlerden {strDay} ")


    elif "wikipedia" in command:
        konusBenle("Aranıyor")
        command = command.replace("wikipedia", "")
        wikipedia.set_lang("tr") #wikipedia dilini ayarladık
        results = wikipedia.summary(command, sentences = 2) #vikipediadaki ilk 2 cümleyi alıyoruz
        #print(results)
        konusBenle(results) #türkçe olarak okuttuk

    elif command in arstr:
        outputList = []
        konusBenle("Ne araştırmalıyım?")
        cevap = komutlar()
        searchOnGoogle(cevap,outputList)
        konusBenle("İlk sayfayı açmalımıyım?")
        ikinciCevap = komutlar()
        if "aç" in ikinciCevap or "evet" in ikinciCevap or "evet aç" in ikinciCevap:
            openLink(outputList)
        if "hayır" in ikinciCevap:
            konusBenle("Tamam")

    elif "nasıl yapılır" in command or "nasıl yapılmalı" in command or "nasıl yapılıyor" in command:
        konusBenle("Gösteriyorum")
        command = command.replace("nasıl yapılır", "")
        outputList = []
        searchOnGoogle(command,outputList)
        konusBenle("Tarayıcınızda gösteriyorum")
        openLink(outputList)


    elif "aç discord" in command:  #for whatsapp /snap/bin/whatsdesk
        #/snap/bin/discord
        konusBenle("Discord açılıyor")
        komut("discord")

    elif command in kapatma:
        konusBenle("Tamam")
        konusBenle("Hoşçakal, iyi günler")
        sys.exit()

    elif command in tempature:
        owm = pyowm.OWM("") #API KEY
        sf = owm.weather_at_place("Kyrenia, CY") #bulunduğumuz konumu bu methodda giriyoruz
        #tomorrow = pyowm.timeutils.tomorrow()
        weather = sf.get_weather() #weather methodunu tanımladık ki  get_temperature gibi methodları çağırabilelim.
        w = sf.get_weather()
        a = int(weather.get_temperature("celsius")["temp"]) #sıcaklığı celsius olarak ayarlayıp sadece anlık sıkcalığı istedik onun yanında min ve max sıcaklıklarda var.
        wind = w.get_wind() #rüzgarı aldık hızı ve açısı var ben sadece hızı aldım
        h = weather.get_humidity() #nem oranını aldık.
        konusBenle("Hava sıcaklığı " + str(a) + " derece")
        konusBenle("Rüzgar " + str(wind["speed"]) + " kilometre hızında")
        konusBenle("Nem oranı ise %" + str(h))

    elif command in face:
        mailname = ""
        password1 = ""
        class Facebook:
            def __init__(self,mailname,password1):
                self.browser = webdriver.Chrome()
                self.mail = mailname
                self.password = password1

            def singIn(self):
                self.browser.get("https://www.facebook.com/login/")
                time.sleep(3)
                mailnameInput = self.browser.find_element_by_xpath("//*[@id='email']")
                password1Input = self.browser.find_element_by_xpath("//*[@id='pass']")

                mailnameInput.send_keys(self.mail)
                password1Input.send_keys(self.password)
                password1Input.send_keys(Keys.ENTER)
                time.sleep(2)
        facbk = Facebook(mailname,password)
        facbk.singIn()

    elif command in gthb:
        gitname = ""
        gitpass = ""
        class Github:
            def __init__(self,gitname,gitpass):
                self.browser = webdriver.Chrome()
                self.gitname = gitname
                self.gitpass = gitpass

            def singn(self):
                self.browser.get("https://github.com/login")
                time.sleep(3)
                gitnameInput = self.browser.find_element_by_xpath("//*[@id='login_field']")
                gitpassInput = self.browser.find_element_by_xpath("//*[@id='password']")

                gitnameInput.send_keys(self.gitname)
                gitpassInput.send_keys(self.gitpass)
                gitpassInput.send_keys(Keys.ENTER)
                time.sleep(2)

        githb = Github(gitname, gitpass)
        githb.singn()

    elif command in hıztest:
        class Speed:
            def __init__(self):
                self.browser = webdriver.Chrome()

            def pressButon(self):
                self.browser.get("https://www.speedtest.net/")
                time.sleep(2)
                butonPress = self.browser.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[2]/div[3]/div[1]/a")
                butonPress.click()
                time.sleep(2)

        sped = Speed()
        sped.pressButon()


    elif command in insta:
        email = ""
        password = ""
        class Instagram:
            def __init__(self,email,password):
                self.browser = webdriver.Chrome()
                self.email = email
                self.password = password

            def signIn(self):
                self.browser.get("https://www.instagram.com/accounts/login/")
                time.sleep(3)
                emailInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
                passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

                emailInput.send_keys(self.email)
                passwordInput.send_keys(self.password)
                passwordInput.send_keys(Keys.ENTER)
                time.sleep(2)
        instgrm = Instagram(email,password)
        instgrm.signIn()

    elif command in twitt:
        usernm = ""
        password = ""
        class Twitter:
            def __init__(self, usernm, password):
                self.browser = webdriver.Chrome()
                self.usernm = usernm
                self.password = password

            def singInn(self):
                self.browser.get("https://twitter.com/login")
                time.sleep(2)

                usernameInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
                passwordInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

                usernameInput.send_keys(self.usernm)
                passwordInput.send_keys(self.password)

                btnSubmit = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
                btnSubmit.click()
                time.sleep(2)
        twitterr = Twitter(usernm,password)
        twitterr.singInn()



    elif "çevir" in command or "çeviri" in command or "çevirsene" in command:
        translator = Translator()
        command = command.replace("çevir", "")
        translated = translator.translate(command,src = "tr", dest = "en")
        konusBenle("Söylediğiniz kelimenin ingilizcede karşığılı " + str(translated.text))

    elif command in e_mail:
        konusBenle("Alıcı kim?")
        alıcı = komutlar()

        if "Sedat" in alıcı:
            konusBenle("Ne yazmalıyım?")
            content = komutlar()

            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("canilguu@gmail.com", "şifreniz")
            mail.sendmail("İsim Soyisim","KişininGmaili@gmail.com", content)
            mail.close()

            konusBenle("Posta gönderildi")

        if "Salih" in alıcı:
            konusBenle("Ne yazmalıyım?")
            content = komutlar()

            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login()
            mail.sendmail("İsim Soyisim","KişininGmaili@gmail.com",content)
            mail.close()

            konusBenle("Posta gönderildi")
        if "Sema" in alıcı:

            konusBenle("Ne yazmalıyım?")
            content = komutlar()

            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("canilguu@gmail.com", "şifreniz")
            mail.sendmail("İsim Soyisim", "KişininGmaili@gmail.com",content) #Maili alacak  kişinin bilgileri
            mail.close()

            konusBenle("Posta gönderildi")
    else:
        print("Algılanan: " + command)
        konusBenle("Komut listemde böyle bir komut yok.")
        time.sleep(2)


hour = int(datetime.datetime.now().hour)
if hour >= 1 and hour <12:
    konusBenle("Günaydınn, size nasıl yardımcı olabilirim")
elif hour >= 12 and hour < 16:
    konusBenle("Tünaydın, size nasıl yardımcı olabilirim")
else:
    konusBenle("iyi akşamlar, size nasıl yardımcı olabilirim")


while True:
    command = komutlar();
    command = command.lower()
    asistan(command)

