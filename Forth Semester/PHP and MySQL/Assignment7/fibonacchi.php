<!DOCTYPE html>
<html>
<head>
    <title>Fibonacci Series Generator</title>
</head>
<body>
    <h2>Fibonacci Series Generator</h2>
    <form method="post" action="">
        Enter Number of Terms: <input type="number" name="terms" required>
        <input type="submit" name="submit" value="Generate">
    </form>
    
    <?php
    if ($_POST['submit']) {
        $terms = $_POST['terms'];
        $num1 = 0;
        $num2 = 1;
        
        echo "<h3>Fibonacci Series: </h3>";
        echo "<p>";
        
        for ($i = 0; $i < $terms; $i++) {
            echo $num1 . " ";
            $next = $num1 + $num2;
            $num1 = $num2;
            $num2 = $next;
        }
        
        echo "</p>";
    }
    ?>
</body>
</html>
