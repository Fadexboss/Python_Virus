import webbrowser
from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ, CloseKey, CreateKey, OpenKey, SetValueEx
#Bu fonksiyonu çalıştırırsanız chromeda vermiş olduğunuz link açılır ve explorer ana sayfa düğmesini kendi linkinizle değiştirebilirsiniz
def q1():
    url = 'https://i.ytimg.com/vi/WuUW-DGV6wc/maxresdefault.jpg'
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new_tab(url)
#explorerın registrydeki ana sayfa kaydına kendi sitemi atıyorum 
    keyVal = r'Software\Microsoft\Internet Explorer\Main'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "Start Page", 0, REG_SZ, "https://i.ytimg.com/vi/WuUW-DGV6wc/maxresdefault.jpg")
    CloseKey(key)
