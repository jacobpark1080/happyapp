Advertisement video was too large to push to repository. Follow this link to view: https://youtu.be/XIay1TTXlt0 

HappyApp Description:
Have you ever wondered what happy hours are happening at the exact moment you have that exact moment?
Well, now there is a website that you can go to HappyApp. When you log in, the website takes in your
current time and gives you the happy hours available at all the bars in Boulder, CO. The bars are
organized such that the soonest ending happy hour is displayed first. It is also shown in a color
that descibes the urgency necessary to make it to this bar for happy hours. Now, you can find the
best deals whenever you need them. Enjoy your night!


1) Repo Organization:
Master Branch - Contains most updated version of code
		Only functional code stored here
V1.0	      - Manually built SQL statements for Restaraunts and Specials
		Project Proposal
		MYSQL ER diagram
V1.1	      - Included scrape functionality for individual days
	      - Origins of the .php website file
V2.0	      - Scrape Function for all days
		Improved website design
		fixed bugs in scrape outputs
V2.1	      -	Click for address functionality added
		Testing files included for scrape and database
		Improved Website Design

2) How to Build and Run HappyApp
**FIRST DOWNLOAD NECESSARY PACKAGES**

	a) clone the repo		git clone https://github.com/sniemeyer13/HappyApp	b) Open MySQL			mysql -u root -p
	c) Source our database:		source happyappv2.1.sql
	c) Update files to connect to your DB
		in addressesToSQL.py (line 72)
		in specials_scrape_to_SQL.py (line 50)
		update to: 
		conn = MySQLdb.connect(host="localhost",user=“FILL IN YOUR USERNAME”,passed = “FILL IN YOUR PASSWORD”,db="HappyApp")
	d) Load info into your database
		python addressesToSQL.py 
		python sepcials_scrape_to_SQL.py
	e) Start a php server in the HappyApp folder
		php -S localhost:8000
	f) Open HappyApp in internet browser
		localhost:8000/happy2.php

3) Testing
	a) clone the repo		git clone https://github.com/sniemeyer13/HappyApp	b) Open MySQL			mysql -u root -p
	c) Source our database:		source happyappv2.1.sql
	c) Update files to connect to your DB
		in addressesToSQL.py (line 72)
		in specials_scrape_to_SQL.py (line 50)
		in happy2.php (line 6)
		update to: 
		conn = MySQLdb.connect(host="localhost",user=“FILL IN YOUR USERNAME”,passed = “FILL IN YOUR PASSWORD”,db="HappyApp")
	d) Load info into your database
		python addressesToSQL.py 
		python sepcials_scrape_to_SQL.py
	e) Run the tests
		python Scrape_test.py		python DBTest.py

	  	
