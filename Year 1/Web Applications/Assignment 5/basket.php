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
							header("location:basket.php"); 
						break;

					}
			?>
			</div>
		</div>
</head>
	<body>
		<div class = container>
			<h2>Basket</h2>
				<?php

					error_reporting(E_ALL & ~E_NOTICE);
					$total = 0;
					$totalQuantity = 0;
					$product_id = (isset($_GET['id']) ? $_GET['id'] : null);
					$action = (isset($_GET['action']) ? $_GET['action'] : null);

					switch($action) {	//decide what to do	
		
						case "add":
							$_SESSION['cart'][$product_id]++; //add one to the quantity of the product with id $product_id 
						break;
						
						case "remove":
							$_SESSION['cart'][$product_id]--; //remove one from the quantity of the product with id $product_id 
							if($_SESSION['cart'][$product_id] == 0) unset($_SESSION['cart'][$product_id]); //if the quantity is zero, remove it completely (using the 'unset' function) - otherwise is will show zero, then -1, -2 etc when the user keeps removing items. 
						break;
						
						case "empty":
							unset($_SESSION['cart']); //unset the whole cart, i.e. empty the cart. 
						break;
					
					}

					$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
					"cywet3", "c0924337");
					if (!$con) {
						die("Failed to connect: " . mysqli_connect_error());
					}

					if($_SESSION['cart']) {
						echo "<table class = basket>";
						foreach($_SESSION['cart'] as $product_id => $quantity) {	
				
				 			$retrieve = sprintf("SELECT ID, Name, Image, Description, Price FROM Products WHERE ID =" . $product_id);
							$result = mysqli_query($con, $retrieve);
							if (mysqli_num_rows($result) > 0) {
						
							list($id, $name, $image, $description, $price) = mysqli_fetch_row($result);
							echo "<tr><td><h4>" . $name . "</h4></td><td>" . "£" . $price . "</td><td>" . "<a href='basket.php?page=products&action=remove&id=" . $id . "'>Remove from basket</a>" . "</td></tr><tr><td>" . "<img class = 'img' src='" . $image . "'/>" . "</td><td>" . $description . "</td><td>Quantity: " . $quantity . "</td></tr>";

							$line_cost = $price * $quantity;
							$total = $total + $line_cost;
							$totalQuantity = $totalQuantity + $quantity;

							}
						}
					
						echo "<tr><td></td><td><a href=\"$_SERVER[PHP_SELF]?action=empty\" onclick=\"return confirm('Are you sure?');\">Remove all items</a></td></td><td>£" . $total . "</td></tr>";
					
					} 


					else { 

						echo "<h3>There are no items in your basket</h3>"; 

					}

					mysqli_close($con);
					echo "</table>";

				    $_SESSION['quantity'] = $totalQuantity;
					$_SESSION['total'] = $total;

					if ($totalQuantity != 0) {
						echo "<a href='paymentForm.php'><h5>Proceed to Checkout</h5></a>";
					}
				?>		
		</div>
	</body>
</html>