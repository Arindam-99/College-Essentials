<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
    
        $number = $_POST['num1'];

        if ($number % 2 == 0) {
            echo "<h3>$number is an Even number.</h3>";
        } else {
            echo "<h3>$number is an Odd number.</h3>";
        }
    
    ?>
</body>
</html>