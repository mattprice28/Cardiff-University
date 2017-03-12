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
							header("location:Gamers-Guide.php"); 
						break;

					}
			?>
			</div>
		</div>
</head>
	<body>
		<div class = container>
		<h2>About</h2>
			<div class = homepage>
				<p>Gamers guide is an online community, built by gamers for gamers. We welcome anyone across all platforms and of any experience.<br><br>Our aim is to shape and guide those new to gaming and to promote friendly debate and discussion between players. Take a look at our product gallery for consoles and controllers to get you started on your journey. Whichever path you choose.<br><br>Good Luck.<br><br><br>Site Administrator<br><br>Matthew Price</p>
				<?php
				?>
			</div>
		</div>
	</body>
</html>