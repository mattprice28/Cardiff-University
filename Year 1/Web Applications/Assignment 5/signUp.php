<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
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

			?>
			</div>
		</div>
</head>
	<body>
		<div class = container>
		<h2>Sign Up</h2>
			<div class = homepage>
			<script type="text/javascript">

			function accountValidation() {

				var illegalUsernameChars = /\W/;
				var illegalPasswordChars = /[\W_]/;
	    		
	    		var name = document.forms["signUpForm"]["username"].value;
			    if (name == null || name == "" || name.length < 5 || name.length > 15 || illegalUsernameChars.test(name)) {
			        document.getElementById("error").innerHTML ="Username invalid, must  be between 5 and 15 characters and can only contain letters, numbers and underscores";
			        return false;
				}

				var password = document.forms["signUpForm"]["password"].value;
				if (password == null || password == "" || password.length < 6 || password.length > 20 || illegalPasswordChars.test(password) || !(password.search(/(a-z)+/)) || !(password.search(/(0-9)/)) ) {
					document.getElementById("error").innerHTML ="Password must be between 6 and 20 characters and must contain at least one number";
					return false;
				}

				var confirmPassword = document.forms["signUpForm"]["confirmPassword"].value;
				if (confirmPassword != password){
					document.getElementById("error").innerHTML = "Passwords do not match";
				return false;
				}
			}

		</script>
			<form name="signUpForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post" onsubmit="return accountValidation()">
			<label for="username">Choose a username</label><input type="text" name="username"><br>
			<label for="password">Choose a password</label><input type="password" name="password"><br>
			<label for="password">Confirm password</label><input type="password" name="confirmPassword"><br><br>
			<input class="submit" type="submit" value="Sign Up">
			<p id="error" class = "info"></p>
			</form>
				
				<?php

				$username = (isset($_POST["username"]) ? $_POST["username"] : null);
				$password = (isset($_POST["password"]) ? $_POST["password"] : null);
				$confirmPassword = (isset($_POST["confirmPassword"]) ? $_POST["confirmPassword"] : null);

					$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
				"cywet3", "c0924337");
				if (!$con) {
					die("Failed to connect: " . mysqli_connect_error());
				}

				$retrieve = "SELECT * FROM UserAccounts";
				$result = mysqli_query($con, $retrieve);

				if (mysqli_num_rows($result) > 0) {
					
					while($row = mysqli_fetch_assoc($result)) {
						$savedUserName = $row["Username"];
						$savedPassword = $row["Password"];
						}
					}

						if($username == Null){
							echo "<p class = message>Please enter your details</p>";
						}

						else if($username == $savedUserName){	
							echo "<p class = info>Username is already taken</p>";
						}

						else if ($password == $confirmPassword){
								
							$addUser = "INSERT INTO UserAccounts (Username, Password) VALUES ('" . $username . "', '" . $password . "')";

				if (mysqli_query($con, $addUser)) {
				    echo "<h4>User account created successfully, Welcome</h4>";
				    $_SESSION['username'] = (isset($_POST["username"]) ? $_POST["username"] : null);
				} 

				else {
				    echo "Error creating account: " . mysqli_error($con);
				}
					
				}
		
				?>
			</div>
		</div>
	</body>
</html>