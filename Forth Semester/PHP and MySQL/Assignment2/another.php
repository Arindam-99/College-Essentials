<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Largest Number</title>
</head>
<body>
    <h1>Here the answer is:</h1>
    <?php

        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $num3 = $_POST['num3'];

        if ($num1 > $num2 && $num1 > $num3) {
            echo "<h2>$num1 is the largest number.</h2>";
        } elseif ($num2 > $num1 && $num2 > $num3) {
            echo "<h2>$num2 is the largest number.</h2>";
        } elseif ($num3 > $num1 && $num3 > $num2) {
            echo "<h2>$num3 is the largest number.</h2>";
        } else {
            echo "<h2>There is a tie among the largest numbers.</h2>";
        }
?>
</body>
</html>
