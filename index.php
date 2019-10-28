<?php
session_start();

$db=mysqli_connect("localhost", "root","","submit");
if (isset($_POST['register_btn'])){
  session_start();
  $username=mysql_real_escape_string($_POST['username']);
  $email=mysql_real_escape_string($_POST['email']);
  $password=mysql_real_escape_string($_POST['password']);
  $sql="select * from users where username='".$username."' AND email='".$email."' AND password='".$password."' 
  limit 1";
  $result=mysqli_query($sql);
  if( mysqli_num_rows($result)==1){
    echo 'you have sucessfully login';
    exit();
  }
  else{
    echo 'you have endered wrong password';
  }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
 
<link rel="stylesheet" href="style/1.css">
</head>
<body>
 <div class="header">
   <h1>login page</h1>
</div>
<form method="post" action="index.php">
  <table>
    <tr>
      <td>username:</td>
      <td><input type="text" name="username" class="textInput"></td>
</tr><tr>
<td>Email:</td>
      <td><input type="email" name="email" class="textInput"></td>
</tr><tr>
<td>password:</td>
      <td><input type="password" name="password" class="textInput"></td>
</tr><tr>
  <td></td>
<td><input type="submit" name="register-btn" value="login"></td>
</tr>
</table>
</form>
</body>
</html>