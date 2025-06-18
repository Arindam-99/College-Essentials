<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
        $num =$_POST['num'];
        for ($i = 1; $i <= 10; $i++) { 
            $result = $num * $i;
            echo "$num X $i = $result <br>";
        }
  
?>


</body>
</html>