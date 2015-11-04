#figure out what to do with multiple stimes and etimes
#get address information


import requests
from bs4 import BeautifulSoup
import re
import MySQLdb


gmap = {}
timemap = {}
drinkmap = {}
foodmap = {}
# THURSDAY
url = "http://www.therooster.com/happyhours/boulder#d=thursday"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

Info = soup.find_all("div", {"class" : "details"})
i = 0
for item in Info:
	try:
		restname = item.contents[1].text
		gmap[i] = restname
	except:
		pass
	timemap[i] = item.contents[5].find_all("div", {"class" : "time"})[0].text
	drinkmap[i] = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[0].text.replace('Drinks:', '')
	try:
		foodmap[i] = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[1].text.replace('Food:', '')
	except:
		pass
	i=i+1

add_special = ("INSERT INTO Thursday" 
			"(Restaurant_restname, stime, etime,food,drink)"
			"VALUES (%s, %s, %s, %s, %s)")
addrest = ("INSERT INTO Restaurant"
			  "(restname, address)" 
			  "VALUES (%s, %s)")



conn = MySQLdb.connect(host="localhost",user="root",db="mydb")
x = conn.cursor()

for key in gmap.keys():
	
	name = gmap[key]
	add = "temp"
	try:
		x.execute(addrest, datarest)
	except:
		pass

	time = timemap[key]
	drink = drinkmap[key]
	drink = drink.encode('ascii','ignore')
	Drinks = drink.replace('/n', '')
	Drinks = Drinks.replace('[ ]\+', '')
	try:
		food = foodmap[key]
		food = food.encode('ascii','ignore')
		Foods = food.replace('/n', '')
		Foods = Foods.replace('[ ]\+', '')
	except:
		pass
	time_flag = False
	times = time.split(',',1)
	print name
	if len(times) > 1:
		time_flag = True
		time1 = times[0]
		time2 = times[1]
		time1 = time1.split('-',1)
		time2 = time2.split('-',1)
                stime1 = time1[0]
		stime2 = time2[0]
                # ALL DAY CASE CASE SHOULD NEVER BE REACHED
		#try:
                #        etime1 = time1[1]
		#	etime2 = time2[1]
                #except:
                #        stime = "0:00"
                #        etime = "24:00"
		etime1 = time1[1]
		etime2 = time2[1]
                if (name != "Eggloo Delights "):
                        st1 = stime1
                        et1 = etime1
			st1 = st1.replace(":00"," ")
                        st1 = st1.replace(":30",".5")
                        st1 = st1.replace("am", "")
                        st1 = float(st1.replace("pm","")) + 12
                        et1 = et1.replace(":00"," ")
                        et1 = et1.replace(":30",".5")
                        et1 = et1.replace("am","")
                        et1 = float(et1.replace("pm","")) + 12
                        data_special1 = (str(name), str(st1), str(et1), str(Drinks), str(Foods))
			st2 = stime2
                        et2 = etime2
                        st2 = st2.replace(":00"," ")
                        st2 = st2.replace(":30",".5")
                        st2 = st2.replace("am", "")
                        st2 = float(st2.replace("pm","")) + 12
                        et2 = et2.replace(":00"," ")
                        et2 = et2.replace(":30",".5")
                        et2 = et2.replace("am","")
                        et2 = float(et2.replace("pm","")) + 12
                        data_special2 = (str(name), str(st2), str(et2), str(Drinks), str(Foods))
			
                        print st1, "to", et1
                        print st2, "to", et2
	else:
		time = time.split('-',1)
		print time
	        stime = time[0] 
        	try:
               		etime = time[1]
        	except:
               		stime = "0:00"
               		etime = "24:00"
			st = float(stime[0])
			et = float(etime[0] + etime[1])
			print st, "to", et
        	if (name != "Eggloo Delights ")	and etime != "24:00":
			st = stime
               		et = etime
			print st, et
               		st = st.replace(":00"," ")
               		st = st.replace(":30",".5")
               		
			am_flag = st.replace("am", "")
			if st == am_flag + "am":
				st = st.replace("am","")
			else:
               			st = float(st.replace("pm","")) + 12
               		et = et.replace(":00"," ")
               		et = et.replace(":30",".5")
               		am_flag = et.replace("am","")
			if et == am_flag + "am":
				et = et.replace("am","")
			else:
              			et = float(et.replace("pm","")) + 12
               		data_special = (str(name), str(st), str(et), str(Drinks), str(Foods))
                        print st, "to", et
		else:
               		pass

	try:
		if time_flag == True:
			x.execute(add_special,data_special1)
			x.execute(add_special,data_special2)
		else:
			x.execute(add_special,data_special)
	except:
		pass
	print

x.close()
conn.commit()
conn.close()
