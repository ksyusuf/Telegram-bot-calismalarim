# from instagramUserInfo import username, password
from selenium import webdriver                                      # Browser'ı başlatmak vb işlemler için gerekli kütüphane
from selenium.webdriver.support.ui import WebDriverWait             # Sayfanın yüklenmesini bekleyen kütüphane
from selenium.webdriver.common.by import By                         # Sayfadaki elementlere ulaşmak için gerekli kütüphane
from selenium.webdriver.support import expected_conditions as EC    # Belli bir koşulun oluşmasını bekleyen kütüphane
from selenium.webdriver.common.keys import Keys                     # Tuşları seçtirmek için
import time
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from pyvirtualdisplay import Display
import pickle


baslangic_zaman = time.time()


class Telegram:
    def __init__(self):

        self.browserProfile = webdriver.ChromeOptions()
        # self.browserProfile.add_argument('--user-data-dir=./User_Data')
        self.browser = webdriver.Chrome('chromedriver_v_91.0.4472.101.exe', chrome_options=self.browserProfile)
        # pickle.dump(self.webdriver.get_cookies(), open("cookies.pkl", "wb"))

        mycookies = self.browser.get_cookies()
        print(mycookies)


    def giris(self):
        self.browser.get("https://web.telegram.org/#/im")
        print("Giriş Bekleniyor... (25 saniye)")
        self.browser.get("https://web.telegram.org/k/")
        kontrol_inputu = "//*[@id='column-left']/div/div/div[1]/div[2]/input"
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located((By.XPATH, kontrol_inputu)))
        print("Giriş Başarılı")
        # şimdilik elle giriş sağlayalım


        # pickle.dump(self.browser.get_cookies(), open("C:/Users/ksyus/Documents/GitHub/Telegram-bot-calismalarim/cerezler.txt", "wb"))
        # deneme_cerez = {'name': 'Selenium', 'value': 'Java'}
        # self.browser.add_cookie(deneme_cerez)
        # time.sleep(3)
        # mycookies = self.browser.get_cookies()
        # print(mycookies)

    def kisi_cekme(self):
        self.browser.get("https://web.telegram.org/k/")
        kontrol_inputu = '//*[@id="folders-container"]/div/div[1]/ul/li[1]/div[1]'
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.XPATH, kontrol_inputu)))
        self.browser.find_element_by_xpath(kontrol_inputu).click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="column-center"]/div/div/div[2]/div[1]/div').click()
        sayac = 2
        gelen_kullanıcı_listesi = []
        while(sayac < 40):
            try:
                print("kullanıcı username alınıyor...")
                time.sleep(1)
                self.browser.find_element_by_xpath('//*[@id="column-right"]/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/ul/li[%s]' %sayac).click()
                time.sleep(1)
                sayac += 1
                username = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]').text
                print("----->>> "+username)
                gelen_kullanıcı_listesi.append(username)
                self.browser.back()
            except:
                print("username yok")
                self.username_yok()
                sayac += 1

        print(list(set(gelen_kullanıcı_listesi))) # listei benzersiz hale getiriyor
        self.nickleri_kaydet(gelen_kullanıcı_listesi)

    def nickleri_kaydet(self, gelen_kullanıcı_listesi):
        with open("C:/Users/ksyus/Documents/GitHub/Telegram-bot-calismalarim/kisi_listesi.txt","r+") as kisiler:  # dosyamıza okuma+yazma eriştik
            kayitli_kisiler =[]
            for kisi in kisiler:  # bununla mesaj atılmışları düzenli liste içine alıyorun  \n dizesi olmadan
                kayitli_kisiler.append(kisi[:-1])  # kaçış dizesini siliyor.
            for gelen_kullanıcı in gelen_kullanıcı_listesi:
                if gelen_kullanıcı in kayitli_kisiler:  # mesaj atılanlar listesinde varsa kullanıcı, o kullanıcıyı pas geçiyor
                    continue
                kisiler.write(gelen_kullanıcı + "\n")  # write() fonksiyonundan farklı olarak liste yazdırabiliyouz bu şekilde writelines()

    def username_yok(self):
        self.browser.back()

telegram = Telegram()

telegram.giris()

sayac = 0
while(sayac < 10):
    telegram.kisi_cekme()
    sayac += 1

telegram.browser.close()