var moreElArr = document.getElementsByClassName("more")

var sleep = false;
var i=0

var processed = {};

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

var savedData = {};
function scrape(){
	console.log("Scrape current element")

	//get the restaraunt name
	var addrEl = document.getElementsByClassName("address")[0];

	var restarauntName = document.getElementsByClassName("name")[0];

	console.log("Found out that ", restarauntName && restarauntName.innerText, " has the address: ", addrEl && addrEl.innerText)
	//get the address
	savedData[restarauntName && restarauntName.innerText] = addrEl && addrEl.innerText;
}


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