import csv

from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen

resp = urlopen("http://sodra.is.lt/Failai/Vidurkiai.zip")
zipfile = ZipFile(StringIO(resp.read()))

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

