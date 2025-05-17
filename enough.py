from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

while 1:
    system("cls||clear")
    # Güncellenmiş ASCII art (HEC)
    print("""{}
┏━━━━┳━━━┓
┃┏┓┏┓┃┏━┓┃
┗┛┃┃┗┫┗━┛┃
╋╋┃┃╋┃┏┓┏┛
╋╋┃┃╋┃┃┃┗┓
╋╋┗┛╋┗┛┗━┛
┏┓╋┏┳━━━┳━━━┳┓┏━┓
┃┃╋┃┃┏━━┫┏━┓┃┃┃┏┛
┃┗━┛┃┗━━┫┃╋┗┫┗┛┛╋
┃┏━┓┃┏━━┫┃╋┏┫┏┓┃╋
┃┃╋┃┃┗━━┫┗━┛┃┃┃┗┓
┗┛╋┗┻━━━┻━━━┻┛┗━┛
Sms: {}           {}by {}@TR WILD CRAFT XSS\n

""".format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        # Menü seçenekleri düzeltildi (\n kullanıldı)
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş. Lütfen bir sayı girin.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        for i in range(len(servisler_sms)):
            print(Fore.LIGHTCYAN_EX + f"{i+1}-{servisler_sms[i]}")
        print(Fore.LIGHTYELLOW_EX + "İstediğiniz servislerin numarasını aralarına virgül koyarak yazınız (Örnek: 1,2,3) veya hepsini seçmek için 'all' yazınız: " + Fore.LIGHTGREEN_EX, end="")
        secim = input()
        servis_secim = []
        if secim.lower() == "all":
            servis_secim = servisler_sms
        else:
            try:
                secim = secim.split(",")
                for s in secim:
                    servis_secim.append(servisler_sms[int(s)-1])
            except:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş. Tekrar deneyiniz.")
                sleep(3)
                continue
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsunuz?: " + Fore.LIGHTGREEN_EX, end="")
        adet = input()
        try:
            adet = int(adet)
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı adet girişi. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        for i in range(adet):
            for servis in servis_secim:
                try:
                    getattr(send_sms, servis)()
                    print(Fore.LIGHTGREEN_EX + f"{servis} -> SMS gönderildi")
                except:
                    print(Fore.LIGHTRED_EX + f"{servis} -> SMS gönderilemedi")
            sleep(5) # Servisler arasında 5 saniye bekleme

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuşuna basıldı. Program sonlandırılıyor.")
            sleep(3)
            break

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Çıkılıyor...")
        sleep(3)
        break
    else:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Geçersiz seçim. Tekrar deneyiniz.")
        sleep(3)
