<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel ="stylesheet" type="text/css" href="style/1.css">
<script src="login_page.js"></script>
</head>
<body>

<h2>Login Form</h2>

<form name="rajudai"'
 action="loginpage.php" onsubmit="return validform()" method="post">
 
    <img src="zomato.jpg">
  

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>
<br>
    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>
        
    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw"> <a href="#">Forgot password?</a></span>
  </div>
</form>
<?php
$u_name=$_POST['uname'];
$u_password=$_POST['psw'];

echo $_POST['uname'];
echo "<br>";
echo $_POST['psw'];
if($uname=="aakeshthapa" && $psw="rajeshthapa")
{
  echo 'logged in';
}
else
echo 'sorry';
?>
</body>
</html>
