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
							header("location:guestbook.php");
						break;

					}
			?>
			</div>
		</div>
</head>
	<body>
		<div class = container>
		<h2>Guestbook</h2>
			<div class = homepage>

			<?php

			error_reporting(E_ALL & ~E_NOTICE);

				$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
				"cywet3", "c0924337");
				if (!$con) {
					die("Failed to connect: " . mysqli_connect_error());
				}
				
				$retrieve = "SELECT * FROM Guestbook ORDER BY ID DESC";
				$result = mysqli_query($con, $retrieve);

				if (mysqli_num_rows($result) > 0) {
					
					while($row = mysqli_fetch_assoc($result)) {
						$message = $row["Message"];
						$username = $row["Username"];
						$posted = $row["Posted"];
						
						echo "<table class = guestbook>" . $message . "<br><br>" . $username . " - " . $posted ."<hr><br></table>";

					}
				
				} 

				else { echo "No Messages have been posted yet"; }
				mysqli_close($con);
			?>
			<script type="text/javascript">

			function messageValidation() {
	    		
	    		var name = document.forms["guestbook"]["message"].value;
			    if (name == null || name == "") {
			        document.getElementById("error").innerHTML ="Message must not be blank";
			        return false;
			    }
			}

		</script>
			<form name="guestbook" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post" onsubmit="return messageValidation()">
			<label for="message" class= "messagelabel">Write your message here</label><textarea class= "largeInput" type="text" name="message" ></textarea><br>
			<input name="submit" class="submit" type="submit" value="Submit">
			<p id="error" class = "info"></p>
			</form>
				
				<?php

				if(isset($_POST['submit'])){

				if ($_SESSION['username'] == null){
					echo "<p class = info>You must be signed in to post a message</p>";
				}
				
				else{

					$message = (isset($_POST["message"]) ? $_POST["message"] : null);

					$con = mysqli_connect("csmysql.cs.cf.ac.uk", "c0924337",
				"cywet3", "c0924337");
				if (!$con) {
					die("Failed to connect: " . mysqli_connect_error());
				}

			

				if ($message != Null) {
					
					
								
							$addMessage = "INSERT INTO Guestbook (Username, Message) VALUES ('" . $_SESSION['username'] . "', '" . $message . "')";

				if (mysqli_query($con, $addMessage)) {
				    echo "<h4>Message added successfully</h4>";
				    header("location:guestbook.php");
				} 

				else {
				    echo "Error posting message: " . mysqli_error($con);
				}
					
				}
			}
}
			
				?>
			</div>
		</div>
	</body>
</html>