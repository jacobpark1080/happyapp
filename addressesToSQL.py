import requests
import re
import MySQLdb

data = {
"28th Street Tavern": "2690 28th Street, Boulder CO ",
"Absinthe House": "1109 Walnut St., Boulder, CO 80302 ",
"Agave": "2845 28th Street, Boulder, CO 80301 ",
"Aji": "1601 Pearl Street, Boulder, CO 80302 ",
"Alba": "2480 Canyon Boulevard, Boulder, CO 80302 ",
"Arugula Bar & Ristorante": "2785 Iris Ave., Boulder, CO 80304 ",
"Bacco Trattoria & Mozzarella Bar": "1200 Yarmouth Ave, Boulder, CO 80304 ",
"Backcountry Pizza & Tap House": "2319 Arapahoe Ave, Boulder, CO 80302 ",
"Black Pepper Pho": "2770 Pearl Street, Boulder, CO 80302 ",
"Boulder Chophouse & Tavern": "921 Walnut Street, Boulder, CO 80302 ",
"Boulder Cork": "3295 30th Street Boulder, CO 80301 (303) 443-9505 ",
"Brasserie Ten Ten": "1011 Walnut Street, Boulder, CO 80302 ",
"Cafe Aion": "1235 Pennsylvania Avenue, Boulder, CO 80302 ",
"Cantina Laredo": "1680 29th Street, Boulder, CO 80301 ",
"Centro Latin Kitchen": "950 Pearl St., Boulder, CO 80302 ",
"Cheesecake Factory": "1401 Pearl Street, Boulder, CO 80302 ",
"Conor O'Neills": "1922 13th St, Boulder, CO 80302 ",
"Corner Bar": "2115 13th Street, Boulder, CO 80302 ",
"Dagabi Cucina": "3970 N Broadway St, Boulder, CO 80305 ",
"Dark Horse": "2922 Baseline Rd, Boulder, CO 80303 ",
"Eggloo Delights": "3033 28th Street, Boulder, CO 80301 ",
"Foolish Craig's": "1611 Pearl Street Boulder, CO 80302 ",
"George's": "2028 14th St, Boulder, CO 80302 ",
"Half Fast Subs": "1215 13th Street, Boulder, CO 80302 ",
"Hapa on Pearl": "1117 Pearl Street Boulder, CO 80302 ",
"Illegal Pete's": "1447 Pearl Street, Boulder, CO ",
"Japango": "1136 Pearl Street, Boulder CO ",
"Jax Fish House": "928 Pearl Street, Boulder, CO 80302 ",
"Jill's Restaurant": "900 Walnut St, Boulder, CO 80302 ",
"Kasa Japanese": "1468 Pearl St, Boulder, CO 80302 ",
"Lazy Dog": "1346 Pearl Street, Boulder, CO 80302 ",
"Leaf Vegetarian Restaurant": "2010 16th St, Boulder, CO 80303 ",
"Mateo": "1837 Pearl Street, Boulder, CO 80302 ",
"Moongate Asian Bistro": "1628 Pearl Street Boulder, CO 80302 ",
"Mountain Sun Pub & Brewery": "1535 Pearl Street, Boulder, CO 80302 ",
"Murphy's Grill": "2731 Iris Ave, Boulder, Co 80304 ",
"Old Chicago": "1102 Pearl Street, Boulder, CO 80302 ",
"Pasta Jay's": "1001 Pearl Street, Boulder, CO 80302 ",
"Pearl Street Pub": "1108 Pearl Street ",
"Pizzeria Locale": "1730 Pearl St, Boulder, CO 80302 ",
"Press Play": "1005 Pearl Street, Boulder CO 80302 ",
"Rio Grande Mexican Restaurant Boulder": "1101 Walnut Street Boulder, CO 80302 ",
"Rueben's Burger Bistro": "1800 Broadway, Boulder, CO 80302 ",
"Salt": "1047 Pearl Street, Boulder, CO 80302 ",
"Sherpa's": "825 Walnut Street, Boulder, CO 80302 ",
"Sushi Hana": "1220 Pennsylvania Ave Boulder, CO 80302 ",
"Sushi Tora": "2014 10th St, Boulder, CO 80302 ",
"Sushi Zanmai": "1221 Spruce Street, Boulder CO ",
"Taco Junky": "1149 13th St, Boulder, CO 80302 ",
"Tahona Tequlia Bistro": "1035 Pearl Street, Boulder, CO 80304 ",
"Ted's Montana Grill": "1701 Pearl Street, Boulder, CO 80302 ",
"The Attic Bar & Bistro": "949 Walnut St, Boulder, CO 80302 ",
"The Bitter Bar": "835 Walnut Street, Boulder CO ",
"The Hungry Toad": "2543 Broadway St, Boulder, CO 80304 ",
"The Kitchen": "1039 Pearl St., Boulder, CO 80302 ",
"The Med": "1002 Walnut Street, Boulder, CO 80302 ",
"The Rib House": "1801 13th Street, Suite 180 Boulder, CO 80302 ",
"The Sink": "1165 13th Street, Boulder, CO 80302 ",
"The Walrus": "1911 11th Street Boulder, CO 80302 ",
"Turley's": "2805 Pearl St, Boulder, CO 80301 ",
"Wahoo's Fish Taco": "2790 Pearl Street, Boulder, CO 80302 ",
"Walnut Brewery": "1123 Walnut Street, Boulder, CO 80302 ",
"West End Tavern": "926 Pearl Street, Boulder, CO 80302 ",
"Zolo": "2525 Arapahoe Ave, Boulder, CO 80302 "
}

conn = MySQLdb.connect(user="root",db="HappyApp")
x = conn.cursor()



addrest = ("INSERT INTO Restaurant"
			  "(restname, address)" 
			  "VALUES (%s, %s)")



for key, value in data.iteritems():
	try:
		datarest = (str(key), str(value))
		x.execute(addrest, datarest)

	except:
		pass

x.close()
conn.commit()
conn.close()