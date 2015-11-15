import requests
import re
import MySQLdb

data = {
"28th Street Tavern": "2690 28th Street, Boulder CO | (303) 444-1562",
"Absinthe House": "1109 Walnut St., Boulder, CO 80302 | (303) 443-8600",
"Agave": "2845 28th Street, Boulder, CO 80301 | (303) 444-2922",
"Aji": "1601 Pearl Street, Boulder, CO 80302 | (303) 442-3464",
"Alba": "2480 Canyon Boulevard, Boulder, CO 80302 | (303) 938-8800",
"Arugula Bar & Ristorante": "2785 Iris Ave., Boulder, CO 80304 | (303) 443-5100",
"Bacco Trattoria & Mozzarella Bar": "1200 Yarmouth Ave, Boulder, CO 80304 | (303) 442-3899",
"Backcountry Pizza & Tap House": "2319 Arapahoe Ave, Boulder, CO 80302 | (303) 449-4285",
"Black Pepper Pho": "2770 Pearl Street, Boulder, CO 80302 | (303) 440-1948",
"Boulder Chophouse & Tavern": "921 Walnut Street, Boulder, CO 80302 | (303) 443-1188",
"Boulder Cork": "3295 30th Street Boulder, CO 80301 (303) 443-9505 | (303) 443-9505",
"Brasserie Ten Ten": "1011 Walnut Street, Boulder, CO 80302 | (303) 998-1010",
"Cafe Aion": "1235 Pennsylvania Avenue, Boulder, CO 80302 | (303) 993-8131",
"Cantina Laredo": "1680 29th Street, Boulder, CO 80301 | (303) 444-2260",
"Centro Latin Kitchen": "950 Pearl St., Boulder, CO 80302 | (303) 442-7771",
"Cheesecake Factory": "1401 Pearl Street, Boulder, CO 80302 | (303) 546-0222",
"Conor O'Neills": "1922 13th St, Boulder, CO 80302 | (303) 449-1922",
"Corner Bar": "2115 13th Street, Boulder, CO 80302 | (303) 442-4880",
"Dagabi Cucina": "3970 N Broadway St, Boulder, CO 80305 | (303) 786-9004",
"Dark Horse": "2922 Baseline Rd, Boulder, CO 80303 | (303) 442-8162",
"Eggloo Delights": "3033 28th Street, Boulder, CO 80301 | (303) 444-3133",
"Foolish Craig's": "1611 Pearl Street Boulder, CO 80302 | (303) 247-9383",
"George's": "2028 14th St, Boulder, CO 80302 | (303) 998-9350",
"Half Fast Subs": "1215 13th Street, Boulder, CO 80302 | (303) 449-0404",
"Hapa on Pearl": "1117 Pearl Street Boulder, CO 80302 | (303) 473-4730",
"Illegal Pete's": "1447 Pearl Street, Boulder, CO | (303) 444-3055",
"Japango": "1136 Pearl Street, Boulder CO | (303) 938-0330",
"Jax Fish House": "928 Pearl Street, Boulder, CO 80302 | (303) 444-1811",
"Jill's Restaurant": "900 Walnut St, Boulder, CO 80302 | (720) 406-7399",
"Kasa Japanese": "1468 Pearl St, Boulder, CO 80302 | (303) 938-8888",
"Lazy Dog": "1346 Pearl Street, Boulder, CO 80302 | (303) 440-3355",
"Leaf Vegetarian Restaurant": "2010 16th St, Boulder, CO 80303 | (303) 442-1485",
"Mateo": "1837 Pearl Street, Boulder, CO 80302 | (303) 443-7766",
"Moongate Asian Bistro": "1628 Pearl Street Boulder, CO 80302 | (720) 406-8888",
"Mountain Sun Pub & Brewery": "1535 Pearl Street, Boulder, CO 80302 | (303) 546-0886",
"Murphy's Grill": "2731 Iris Ave, Boulder, Co 80304 | (303) 449-4473",
"Old Chicago": "1102 Pearl Street, Boulder, CO 80302 | (303) 443-5031",
"Pasta Jay's": "1001 Pearl Street, Boulder, CO 80302 | (303) 444-5800",
"Pearl Street Pub": "1108 Pearl Street | 303 939 9900",
"Pizzeria Locale": "1730 Pearl St, Boulder, CO 80302 | (303) 442-3003",
"Press Play": "1005 Pearl Street, Boulder CO 80302 |",
"Rio Grande Mexican Restaurant Boulder": "1101 Walnut Street Boulder, CO 80302 | (303) 444-3690",
"Rueben's Burger Bistro": "1800 Broadway, Boulder, CO 80302 | (303) 443-5000",
"Salt": "1047 Pearl Street, Boulder, CO 80302 | (303) 444-7258",
"Sherpa's": "825 Walnut Street, Boulder, CO 80302 | (303) 440-7151",
"Sushi Hana": "1220 Pennsylvania Ave Boulder, CO 80302 |",
"Sushi Tora": "2014 10th St, Boulder, CO 80302 | (303) 444-2280",
"Sushi Zanmai": "1221 Spruce Street, Boulder CO | (303) 440-0733",
"Taco Junky": "1149 13th St, Boulder, CO 80302 | (303) 443-2300",
"Tahona Tequlia Bistro": "1035 Pearl Street, Boulder, CO 80304 | (303) 938-9600",
"Ted's Montana Grill": "1701 Pearl Street, Boulder, CO 80302 | (303) 449-5546",
"The Attic Bar & Bistro": "949 Walnut St, Boulder, CO 80302 | (303) 415-1300",
"The Bitter Bar": "835 Walnut Street, Boulder CO | (303) 442-3050",
"The Hungry Toad": "2543 Broadway St, Boulder, CO 80304 | (303) 442-5012",
"The Kitchen": "1039 Pearl St., Boulder, CO 80302 | (303) 544-5973",
"The Med": "1002 Walnut Street, Boulder, CO 80302 | (303) 444-5335",
"The Rib House": "1801 13th Street, Suite 180 Boulder, CO 80302 | (303) 442-7427",
"The Sink": "1165 13th Street, Boulder, CO 80302 | (303) 444-7465",
"The Walrus": "1911 11th Street Boulder, CO 80302 | (303) 443-9902",
"Turley's": "2805 Pearl St, Boulder, CO 80301 | (303) 442-2800",
"Wahoo's Fish Taco": "2790 Pearl Street, Boulder, CO 80302 | 303-473-9072",
"Walnut Brewery": "1123 Walnut Street, Boulder, CO 80302 | (303) 447-1345",
"West End Tavern": "926 Pearl Street, Boulder, CO 80302 | (303) 444-3535",
"Zolo": "2525 Arapahoe Ave, Boulder, CO 80302 | (303) 449-0444",
}

conn = MySQLdb.connect(user="root",db="mydb")
x = conn.cursor()

rests = data.keys()
adds = data.values()

rest_info = (str(rests), str(adds))


add_data = ("INSERT INTO Restaurant" 
			 "(restname, address)" 
			  "VALUES (%s, %s)")

x.execute(add_data, rest_info)
x.close()
conn.commit()
conn.close()