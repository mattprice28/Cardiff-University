<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="../css/style.css"> 
	<title>E-Commerce</title>
	<meta charset="utf-8" />			
</head>
	<body>
		<div class = container>
			<h1>
			<img class = banner src="http://www.endlessicons.com/wp-content/uploads/2013/03/game-controller-icon-614x460.png"/>	
			Gamers Guide
			<img class = banner src="http://www.endlessicons.com/wp-content/uploads/2013/03/game-controller-icon-614x460.png"/>
			</h1>
			<h2>Product Gallery</h2>
				<?php
					$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
					"cywet3", "c0924337");
					if (!$con) {
					// Connection failed
					die("Failed to connect: " . mysqli_connect_error());
					}
					// Success
					$retrieve = "SELECT * FROM Products";
					$result = mysqli_query($con, $retrieve);
					if (mysqli_num_rows($result) > 0) {
						echo "<table>";
					while($row = mysqli_fetch_assoc($result)) {
					$name = $row["Name"];
					$image = $row["Image"];
					$description = $row["Description"];
					$price = $row["Price"];
					echo "<tr><td>" . $name . "</td><td>" . "<img class = 'img' src='". $image . "'/>" . "</td><td>" . $description . "</td><td>" . "£" . $price . "</td></tr>";
					}
					echo "</table>";
					} else { echo "No results"; }
					mysqli_close($con);
				?>
		</div>
	</body>
</html>