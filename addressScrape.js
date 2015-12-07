
/**
* moreElArr is where we search for the detailed data about each restaraunt, which includes the address
* @property moreElArr
* @type array
*/
var moreElArr = document.getElementsByClassName("more")

/**
* @property i
* @type int
* @default 0
*/
var i=0

/**
* processed keeps track of which restaraunts have been processed
* @property processed
* @type hashtable
* @default {}
*/
var processed = {};

/**
* processCurrentEl goes through and scrapes the restaraunt name and address for each restaraunt
* @event processCurrentEl
*/

function processCurrentEl(){
	if(processed[i]) i++;
	if(i >= moreElArr.length) return;

	console.log("Processing current element ", i)

	var el = moreElArr[i];
	
	//click
	el.click();

	//wait
	setTimeout(function(){
		scrape();
		clickExit();

		

		setTimeout(function(){
			//finished with this one
			processed[i] = true;
			i++;
			//queue another click and scrape
			processCurrentEl();
		}, 1000)
		
		
	}, 5000);

}

/**
* savedData stores all the restaraunt and address data we've found
* @property savedData
* @type hashtable
* @default {}
*/
var savedData = {};

/**
* scrape extracts the restaraunt name and address from a particular restaraunt
* @event scrape
*/
function scrape(){
	console.log("Scrape current element")

	//get the restaraunt name
	/**
	@property addrEl
	@type String
	*/
	var addrEl = document.getElementsByClassName("address")[0];

	/**
	@property restarauntName
	@type String
	*/
	var restarauntName = document.getElementsByClassName("name")[0];

	console.log("Found out that ", restarauntName && restarauntName.innerText, " has the address: ", addrEl && addrEl.innerText)
	//get the address
	savedData[restarauntName && restarauntName.innerText] = addrEl && addrEl.innerText;
}

/**
* clickExit exits the current restaraunt screen
* @event clickExit
*/

function clickExit(){
	console.log("Clicking exit")

	//find exit button
	//fire click
	document.getElementsByClassName("close")[0].click()

	//spin for a bit
	a = 3;
	for(var i =0; i < 1000; i++)
		 a = 2 * a;
}

processCurrentEl()