<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="../Assignment 5/css/style.css">
		<title>Gamers-Guide</title>
		<meta charset="utf-8" />
		<div class = header-cont>
			<div class = header>
			<h1>
				<img class = banner src="https://openclipart.org/image/800px/svg_to_png/204910/joypad.png"/>	
				G a m e r s - G u i d e
				<img class = banner src="https://openclipart.org/image/800px/svg_to_png/204910/joypad.png"/>
			</h1>
			<ul>
				<li><a href="Gamers-Guide.php">Home</a></li>
				<li><a href="E-Commerce.php">Gallery</a></li>
				<li><a href="basket.php">Basket</a></li>
				<li><a href="guestbook.php">Guestbook</a></li>
				</ul>
				<?php

			error_reporting(E_ALL & ~E_NOTICE);


			if ($_SESSION['username'] == null){
				echo "<h6><a href='SignIn.php'>Sign in</a></h6>";
			}

			else{
				echo"<a href=\"Gamers-Guide.php?action=signOut\" onclick=\"return confirm('Are you sure you wish to sign out?');\"><h6>Welcome " . $_SESSION['username'] . "</h6></a>"; 
				
			}

			$action = (isset($_GET['action']) ? $_GET['action'] : null);

					switch($action) {

			case "signOut":
							unset($_SESSION['username']);
							header("location:paymentForm.php"); 
						break;

					}
			?>
			</div>
		</div>
				<script type="text/javascript">

				var ck_name = /^[A-Za-z ] {3,20}$/;
				var ck_cardNumber = /^[0-9] {16}$/;
				var ck_security = /^[0-9] {3}$/;

			function validateForm() {
	    		
	    		var name = document.forms["paymentForm"]["name"].value;
			    if (name == null || name == "" || ck_name.test(name)) {
			        document.getElementById("message").innerHTML ="Name must be filled out";
			        return false;
			    }

			 	var number = document.forms["paymentForm"]["cardNumber"].value;
			    if (ck_cardNumber.test(number)) {
			    	document.getElementById("message").innerHTML ="Card Number must contain 16 digits";
			    	return false;
			    }

			    var security = document.forms["paymentForm"]["securityCode"].value;
			    if (ck_security.test(security)) {
			    	document.getElementById("message").innerHTML ="Security Code must contain 3 digits";
			    	return false;
			    }

			    var month = document.forms["paymentForm"]["expiryMonth"].value;
			    if (isNaN(month) || month < 1 || month > 12) {
        			document.getElementById("message").innerHTML ="Month must be a number between 1 and 12";
        			return false;
    			}

    			var year = document.forms["paymentForm"]["expiryYear"].value;
			    if (isNaN(year) || year == null || year == "") {
        			document.getElementById("message").innerHTML ="Year must be a number";
        			return false;
    			}
			}

			function displayMessageA() {

			document.getElementById("helpMessage").innerHTML ="Please enter the 16 digit number on the front of your card.";

			}

			function displayMessageB() {

			document.getElementById("helpMessage").innerHTML ="Please enter the month your card expires.";

			}

			function displayMessageC() {

			document.getElementById("helpMessage").innerHTML ="Please enter the year your card expires.";

			}

			function displayMessageD() {

			document.getElementById("helpMessage").innerHTML ="Please enter your name as it appears on the front of your card.";

			}

			function displayMessageE() {

			document.getElementById("helpMessage").innerHTML ="Please enter the 3 digit security code on the back of your card.";

			}

		</script>
	</head>
	<body>
	<div class = container>
	<h2>Payment Form</h2>
	<?php
	if ($_SESSION['total'] > 0){
		if ($_SESSION['quantity'] == 1){
		echo "<h3>There is " . $_SESSION['quantity'] . " item in your basket</h3>";
}
else{
	echo "<h3>There are " . $_SESSION['quantity'] . " items in your basket</h3>";
}
		echo "<h3>Your total is: £" . $_SESSION['total'] . "</h3>";	
	}
	
	?>
		<form name="paymentForm" action="paymentSubmitted.html" method="post" onsubmit="return validateForm()">
			<label for="cardNumber">Card Number</label> <input type="int" id="cardNumber" onfocus="displayMessageA()"><br>
			<label for="expiryDate">Expiry Date</label> <input class="date" type="int" name="expiryMonth" id="expiryDate" onfocus="displayMessageB()"> <input class="date" type="int" name="expiryYear" id="expiryDate" onfocus="displayMessageC()"><br>
			<label for="name">Name on Card</label> <input type="text" id="name" onfocus="displayMessageD()"><br>
			<label for="securityCode">Security Code</label> <input class="date" type="int" id="securityCode" onfocus="displayMessageE()"><br><br>
			<input class="submit" type="submit" value="Submit">
			<p id="helpMessage" class = "help"></p><p id="message" class = "info"></p>
		</form>
	</div>
	</body>
</html>