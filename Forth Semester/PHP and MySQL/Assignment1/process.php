
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

    $name = $_POST["name"];
    $phone =$_POST["phone"];

    echo "<h2>Hello, $name!</h2>";
    echo "<p>Your phone number is: $phone</p>";
?>
</body>
</html>