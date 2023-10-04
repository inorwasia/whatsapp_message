import pyautogui
import time
import os


count = int(input("Kaç Adet Mesaj ? : "))
message = input("Başlangıç Mesajı? : ")
endMessage = input("Bitiş Mesajı ?: ")

n = 10

print("Spam Bot Başlatılıyor" , n , "Saniye...")

while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
    os.system("cls")

print("Spam Botu Başlatıldı...")

def send(message):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")


while count:
    send(message)
    time.sleep(0.1)
    count -= 1


send(endMessage)

os.system("cls")

print("Spam Bot Durduruldu ....")
