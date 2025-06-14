<!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill Calculator</title>
</head>
<body>
    <h2>Electricity Bill Calculator</h2>
    <form method="post" action="">
        Enter Units Consumed: <input type="number" name="units" required>
        <input type="submit" name="submit" value="Calculate">
    </form>
    
    <?php
    if ($_POST['submit']) {
        $units = $_POST['units'];
        $bill = 0;
        
        if ($units <= 50) {
            $bill = $units * 3.50;
        } elseif ($units <= 150) {
            $bill = (50 * 3.50) + (($units - 50) * 4.00);
        } elseif ($units <= 250) {
            $bill = (50 * 3.50) + (100 * 4.00) + (($units - 150) * 5.20);
        } else {
            $bill = (50 * 3.50) + (100 * 4.00) + (100 * 5.20) + (($units - 250) * 6.50);
        }
        
        echo "<h3>Total Electricity Bill: Rs. " . number_format($bill, 2) . "</h3>";
    }
    ?>
</body>
</html>
