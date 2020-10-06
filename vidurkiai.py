import csv

from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
from os import listdir

inputfiles = list()
for f in listdir("."):
	filename = f.lower()
	if filename.endswith(".zip"):
		inputfiles.append(f)

inputfiles.sort()
#print (inputfiles)

names = {}
names["111620231"] = "IBM"
names["122588443"] = "ATEA"
names["303246070"] = "Uber Development"
names["304096556"] = "Swedbank"
names["301694694"] = "Danske"
names["302620469"] = "Infare"
names["303332886"] = "Nasdaq"
names["300100651"] = "Bentley Systems"
names["302455964"] = "Barclays"
names["300132841"] = "Devbridge"
names["125756394"] = "Genius Sports"
names["300882953"] = "Trafi"
names["135867375"] = "NFQ"
names["300121962"] = "Euromonitor"
names["121215434"] = "Telia"
names["111445337"] = "Blue Bridge"
names["300067906"] = "Alna"
names["300064148"] = "Elsis"
names["302250087"] = "Softra"
names["110778328"] = "Norfa"
names["111791015"] = "Lidl"
names["111674122"] = "Tieto"
names["300661912"] = "Cognizant"
names["300555649"] = "Adform"
names["302634807"] = "Visma"
names["210316340"] = "CGI"
names["300607099"] = "EIS Group"
names["110320619"] = "Baltic Amadeus"
names["303108774"] = "WIX"
names["302631095"] = "Asseco"
names["125592767"] = "Penki"
names["304633216"] = "Cujo"
names["302350785"] = "Unity"
names["304447756"] = "Helis"
names["301566552"] = "Softera"

if len(inputfiles) == 1:

	resp = open(inputfiles[0])
	zipfile = ZipFile(StringIO(resp.read()))

	print ('%-25s %-10s %-10s %-10s %-10s %-10s' % ("Company", "Average", "Mediana", "25_kv", "75_kv", "std_dev"))
	print ('%-25s %-10s %-10s %-10s %-10s %-10s' % ("-", "-", "-", "-", "-", "-"))

	lines = csv.reader(zipfile.open("VIDURKIAI.CSV"), delimiter=';', quotechar='"')

	for row in lines:

		try:
			company = names [row[0].strip()]
		except KeyError:
			continue

		print('%-25s %-10s %-10s %-10s %-10s %-10s' % ( \
		company,
		row[2].strip(),
		row[3].strip(),
		row[4].strip(),
		row[5].strip(),
		row[6].strip() ))

elif len(inputfiles) > 1:

	averages = {}
	for f in inputfiles:

		resp = open(f)
		zipfile = ZipFile(StringIO(resp.read()))

		lines = csv.reader(zipfile.open("VIDURKIAI.CSV"), delimiter=';', quotechar='"')

		for row in lines:

			try:
				company = names [row[0].strip()]
				value = row[2].strip().replace(",", ".")
			except KeyError:
				continue

			try:
				f = f.replace("Vidurkiai_","")
				f = f.replace(".zip","")
				averages[company][f] = value
			except KeyError:
				averages[company] = dict()
				averages[company][f] = value
	
	months = list()
	for company in averages:
		months = sorted(averages[company])
		break

	results = list()
	for company in averages:
		avg = list()
		avg.append(company)
		for month in months:
			avg.append(averages[company][month])
		results.append(avg)

	print(";"),
	for month in months:
		print (month + ";"),
	print("")

	for res in results:
		for r in res:
			print (r + ";"),
		print("")
