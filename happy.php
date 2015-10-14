<!DOCTYPE html>

<?php

// Create a MySQL user named: HappyApp with password: password and source the HappyApp database to it
$conn = new mysqli("localhost", "HappyApp", "password", "HappyApp");

if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}

// Variable to select the current day of the week from the database
$today = 'Tuesday';

// Select the current day of the week table and store it in a 2D array
$sql = "SELECT * FROM  $today ";
$result = $conn->query($sql);
$row = $result->fetch_all();

// Count the number of entries in the table and store it in as a 1D array
$count_sql = "SELECT COUNT(*) FROM $today ";
$count_result = $conn->query($count_sql);
$count_row = $count_result->fetch_row();

$conn->close();
?>


<!-- CSS styling parameters for display and text. NOTE: Parameters have been calibrated for a 13" Mac screen; May need adjusting to look proper on other computers -->
<style>
body {
    background-image: url(http://www.arcotelhotels.com/images/uploads/arcotel_hotel_kaiserwasser_vienna/AKW-U-ONE-Bar-130626.jpg);
}

.title {
    position: absolute;
    margin: auto;
    background-color: green;
    left: 15%;
    width: 1000px;
    height: 100px;
    border: 1px solid blue;
}

.info {
    display: block;
    position: absolute;
    background-color: yellow;
    padding: 1% 2%;
    left: 6%;
    width: 1200px;
    height: 200px;
    border: 1px solid blue;
}

h1 {
    position: relative;
    color: pink;
    font-size: 50px;
    font-style: oblique;
    text-align: center;
    top: -20%;
}

.rest_name {
    font-weight: bold;
    color: blue;
    text-align: left;
    float: left;
    font-size: 30px; 
}

.rest_food {
    color: purple;
    text-align: left;
    float: left;
    font-size: 20px;
}

.rest_hour {
    color: red;
    text-align: right;
    float: right; 
    font-size: 30px;
    font-weight: bold;
}

.rest_drank {
    position: absolute;
    color: purple;
    text-align: left;
    float: left;
    font-size: 20px;
}
</style>


<!-- HTML display code -->
<html>
<body>
    <div class="title">
        <h1>Happy App!</h1>
    </div>

<!-- PHP script to display current data collected from the database -->
<?php

// while() loop counter variable
$x = 0;

// while() loop to create a display 'card' for each happy hour event going on
while($x < $count_row[0]){
	$h = 250*$x+150;
	echo   '<div class="info" style="top:'.$h.'px">';
	echo     '<a class="rest_name">' . $row[$x][4] . '</a>';
	echo     '<a class="rest_hour">Get Happy At: ' . $row[$x][0] . ' - ' . $row[$x][1] . '</a>';
	echo   '<br style="line-height: 600%">';
	echo	 '<a class="rest_food">Food: ' . $row[$x][2] . '</a>';
	echo   '<br style="line-height: 300%" >';
	echo	 '<a class="rest_drank">Drinks: ' . $row[$x][3] . '</a>';     
	echo   '</div>';
	$x = $x + 1;
}
?>

</body>
</html>
