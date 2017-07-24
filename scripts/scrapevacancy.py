import requests
from bs4 import BeautifulSoup as bs


def getDetails(college_code):

	res = requests.post("https://www.tnea.ac.in/tnea_aca_vacancy.php", data = {'cname': college_code,'btncname': 'Find', 'ccode': 0, 'bname': 0})
	
	# print res.content

	soup_obj = bs(str(res.text))

	tables  = soup_obj.findAll('table')
	
	print len(tables) 

	# for table in tables:
	# 	if table.findParent("table") is None:
	# 		# print str(table)
	# 		pass
	
	# print tables[2]

	for tr in tables[2]:
		if len(tr) == 30:
			cells = tr.findAll("td")
			# print len(cells)
			count = 0
			for index, td in enumerate(cells):
				if index == 0:
					print "Department: ",td.get_text()
					continue
				if index%2 == 0:
					if td.get_text().strip() == "":
						print "-1"
					else:
						print td.get_text().strip()
				count = count + 1
			print "Total count : ", count	



getDetails(2706)

#kct 2172, PSG 2006 