import re

in_file = open(input("ulazna datoteka? "),"r")

out_file = open("formatirano.csv", "w")

mede = ['MS\n']

#ubaciti kodove za sve ostalo, koje nije 21
#ostalo = []

#string za cijeli red

#string za red bez odrzavanje
#red[0]+red[1]+red[2]+red[3]+red[4]+red[5]+red[6]+red[7]+red[8]+red[9]+red[10]+red[11]+red[12]+red[13]+red[14]+red[15]+red[16]+red[17]


while True:

	linija = in_file.readline()

	if not linija:
		break

	red = re.split(';',linija)
	
	if red[16] in mede:
		out_file.write(red[0]+";"+red[1]+";"+red[2]+";"
		+red[3]+";"+red[4]+";"+red[5]+";"+red[6]+";"+red[7]+";"+red[8]+";"+red[9]+";"+red[10]+";"+red[11]+";"+red[12]
		+";"+red[13]+";"+red[14]+";"+red[15]+";"+red[16])
		#out_file.write("\n")
		

	else:
		out_file.write(red[0]+";"+red[1]+";"+red[2]+";"
		+red[3]+";"+red[4]+";"+red[5]+";"+red[6]+";"+red[7]+";"+red[8]+";"+";"+";"+red[11]+";"+red[12]
		+";"+red[13]+";"+red[14]+";"+red[15]+";"+red[16])
		#out_file.write("\n")


in_file.close()
out_file.close()

#napraviti za ubacivanje 8 tocke

skripta_in = open("formatirano.csv", "r")

skripta_out = open("skripta.scr", "w")

while True:

	linija = skripta_in.readline()
	if not linija:
		break

	red = re.split(';',linija)
		
	if red[16]=='MS\n':
		
		skripta_out.write(
			"-insert o_ab"+"\n"
			+red[9]+","+red[10]+"\n"
			+"1"+"\n"
			+"1"+"\n"
			+"0"+"\n"
			+"elaborat"+"\n"
			+"1"+"\n"
			+"21"+"\n"
			+"6"+"\n"
			+"visina"+"\n"
			+red[0]+"\n"
		)

	else:
		pass


skripta_in.close()
skripta_out.close()