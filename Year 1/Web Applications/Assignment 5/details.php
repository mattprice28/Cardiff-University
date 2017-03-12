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
							header("location:details.php");
						break;

					}
			?>
			</div>
		</div>
</head>
	<body>
		<div class = container>
		<h2>Product Details</h2>
			<?php

				error_reporting(E_ALL & ~E_NOTICE);
				$product_id = (isset($_GET['id']) ? $_GET['id'] : null); 
				$action = (isset($_GET['action']) ? $_GET['action'] : null);

				switch($action) {

					case "add":
						$_SESSION['cart'][$product_id]++; 
					 
					break;

				}

					$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
					"cywet3", "c0924337");
					if (!$con) {
						die("Failed to connect: " . mysqli_connect_error());
					}

					$retrieve = "SELECT * FROM Products WHERE ID =" . $product_id;
					$result = mysqli_query($con, $retrieve);

					if (mysqli_num_rows($result) > 0) {
						echo "<table>";
						while($row = mysqli_fetch_assoc($result)) {
						$name = $row["Name"];
						$image = $row["Image"];
						$longDescription = $row["Extended Description"];
						$price = $row["Price"];
						$id = $row['ID'];
						echo "<tr><td><h4>" . $name . "</h4></td><td>" . "£" . $price . "</td><td>" . "<a href=\"$_SERVER[PHP_SELF]?page=products&action=add&id=" . $id . "\" onclick=\"return alert('Item added to basket');\">Add to basket</a>" . "</td></tr><tr><td>" . "<img class = 'img' src='" . $image . "'/>" . "</td><td>" . $longDescription . "</td><td><a href='E-Commerce.php'>Back</a></td></tr>";
						}

						echo "</table>";
					
					} 

				else { echo "No results"; }
				mysqli_close($con);
			?>
		</div>
	</body>
</html>