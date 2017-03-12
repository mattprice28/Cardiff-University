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
			</div>
		</div>
</head>
	<body>
		<div class = container>
		<h2>Sign In</h2>
			<div class = homepage>
				<form name="signInForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
			<label for="username">Enter username</label><input type="text" name="username"><br>
			<label for="password">Enter password</label><input type="password" name="password"><br><br>
			<input name= "submit" class="submit" type="submit" value="Sign In">
			</form>	
			<?php
				
				error_reporting(E_ALL & ~E_NOTICE);

				$username = (isset($_POST["username"]) ? $_POST["username"] : null);
				$password = (isset($_POST["password"]) ? $_POST["password"] : null);

				if(isset($_POST['submit'])){

				$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
				"cywet3", "c0924337");
				if (!$con) {
					die("Failed to connect: " . mysqli_connect_error());
				}

				$retrieve = "SELECT * FROM UserAccounts WHERE Username ='" . $username . "'";
				$result = mysqli_query($con, $retrieve);

				if (mysqli_num_rows($result) > 0) {
					
					while($row = mysqli_fetch_assoc($result)) {
						$savedUserName = $row["Username"];
						$savedPassword = $row["Password"];
				
				} 
			}

				
				mysqli_close($con);

				if ($savedUserName == $username){

					if ($savedPassword == $password){

						echo "<h4>Sign in successful, welcome</h4>";
						$_SESSION['username'] = $username;
					
				}

				else{
				echo "<h4>Username or Password incorrect</h4>";

			}
		}
			else{
				echo "<h4>Username or Password incorrect</h4>";
			}
		}
		else{
			echo "<h4>Please sign in</h4>";
		}

				?>
				<h4><a href = "signUp.php">New to the site? Sign up here</a></h4>
			</div>
		</div>
	</body>
</html>