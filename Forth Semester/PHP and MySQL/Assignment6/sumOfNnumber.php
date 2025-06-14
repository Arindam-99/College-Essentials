<!DOCTYPE html>
<html>
<head>
    <title>Sum of Digits Calculator</title>
</head>
<body>
    <h2>Sum of Individual Digits</h2>
    <form method="post" action="">
        Enter Number: <input type="number" name="number" required>
        <input type="submit" name="submit" value="Calculate">
    </form>
    
    <?php
    if (isset($_POST['submit'])) {
        $number = $_POST['number'];
        $sum = 0;
        
        while ($number != 0) {
            $sum += $number % 10;
            $number = (int)($number / 10);
        }
        echo "<h3>Sum of Digits: " . $sum . "</h3>";
    }
    ?>
</body>
</html>
