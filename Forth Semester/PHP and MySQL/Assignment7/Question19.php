<!-- 19.	 Write a PHP Script to find the factorial of a given number -->
<!DOCTYPE html>
<html>
<head>
    <title>Factorial Calculator</title>
</head>
<body>
    <h2>Factorial Calculator</h2>
    <form method="post" action="">
        Enter Number: <input type="number" name="number" required>
        <input type="submit" name="submit" value="Calculate">
    </form>
    
    <?php
    if ($_POST['submit']) {
        $number = $_POST['number'];
        $factorial = 1;
        
        for ($i = 1; $i <= $number; $i++) {
            $factorial *= $i;
        }
        
        echo "<h3>Factorial of $number is: " . $factorial . "</h3>";
    }
    ?>
</body>
</html>
