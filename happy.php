<!DOCTYPE html>

<?php
$conn = new mysqli("localhost", "HappyApp", "password", "happyapp");

if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM monday";
$result = $conn->query($sql);
$row = $result->fetch_row();

$conn->close();
?>

<style>
body {
    background-image: url(http://www.arcotelhotels.com/images/uploads/arcotel_hotel_kaiserwasser_vienna/AKW-U-ONE-Bar-130626.jpg);
}

.title {
    position: absolute;
    margin: auto;
    background-color: green;
    left: 10%;
    width: 1000px;
    height: 100px;
    border: 1px solid blue;
}

.info {
    position: absolute;
    background-color: Yellow;
    top: 30%;
    left: 10%;
    width: 1000px;
    height: 150px;
    border: 1px solid blue;
}

h1 {
    position: relative;
    color: pink;
    text-align: center;
}

.rest_name {
    color: purple;
    text-align: left;
    float: left;
    font-size: 20px; 
}

.rest_add {
    color: purple;
    text-align: left;
    float: left;
    font-size: 20px;
}

.rest_hour {
    color: red;
    text-align: right;
    float: right; 
    font-size: 20px;
}

.rest_deal {
    color: purple;
    text-align: right;
    float: right;
    font-size: 20px;
}

</style>

<html>
<body>
    <div class="title">
        <h1>Happy App!</h1>
    </div>
    <div class="info">
        <h1 Class="rest_name">Restaurant Name: <?php echo $row[1];?></h1>
    	<h1 Class="rest_hour"><?php echo "Get Happy At: " .$row[3]. "-" . $row[4];?></h1> 
	<h1 class="rest_add">Restaurant Address: <?php echo $row[2];?></h1>
	<h1 class="rest_deal"> <?php echo "Food: " . $row[6] . "<br> Drink: " . $row[5];?></h1>     
</div>
</body>
</html>

