<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Swapping 2 number Adj: </title>
</head>
<body>
    <?php
    $a=$_POST['first_num'];
    $b=$_POST['second_num'];
    echo "Before swapping the first Number is $a <br>";
    echo "Before swapping the second number is $b <br>";

    $a=$a+$b;
    $b=$a-$b;
    $a=$a-$b;
    echo "<h2>Perform the swapping the final result is:</h2>";
    echo "After swapping the first Number is $a <br>";
    echo "After swapping the second number is $b <br>";
    ?>
</body>
</html>