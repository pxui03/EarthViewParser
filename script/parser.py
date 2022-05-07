import urllib.request
from json import dumps
from bs4 import BeautifulSoup
result = []
count = 0
file = open('earthview.json','a')
for x in range(1000, 15000): 
	x = str(x)
	try:
		print("Fetching" + x + " ...")
		response = urllib.request.urlopen('https://earthview.withgoogle.com/' + x)
		html = response.read()
		html = BeautifulSoup(html)
		Region = str((html.find("div", class_="location__region")).text)
		Country = str((html.find("div", class_="location__country")).text)
		Everything = html.find("a", class_="location", href=True)
		GMapsURL = Everything['href']
		Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
		result.append({'country': Country, 'region': Region, 'image': Image, 'map': GMapsURL})
		count=count+1
	
	except urllib.request.HTTPError as e:
		continue

meow = dumps(result,indent=3)
file.write(meow)			
file.close()
print('total: '+str(count))
