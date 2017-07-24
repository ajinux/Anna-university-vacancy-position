import requests
from bs4 import BeautifulSoup as bs
import csv

def getCollege():

	res = requests.get("https://www.tnea.ac.in/tnea_aca_vacancy.php")

	soup_obj = bs(str(res.text))

	tables  = soup_obj.findAll('table')
	
	for indx, tr in enumerate(tables):
		if indx == 1:
			optns = tr.findAll("option"), "\n"
			print len(optns)
			with open('tncolleges.csv', 'w') as csvfile:
				fieldnames = ['Code', 'College_Name']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				for opt in optns[0][:519]:
					print opt['value'], opt.text
					writer.writerow({'Code': opt['value'], 'College_Name': opt.text}) 

		 
getCollege()