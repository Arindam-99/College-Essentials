<!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body>
    <h2>Age Calculator</h2>
    <form method="post" action="">
        Enter Date of Birth: <input type="date" name="dob" required>
        <input type="submit" name="submit" value="Calculate Age">
    </form>
    
    <?php
    if ($_POST['submit']) {
        $dob = $_POST['dob'];
        $dobObject = new DateTime($dob);
        $currentDate = new DateTime();
        $age = $currentDate->diff($dobObject)->y;
        
        echo "<h3>Your Age is: " . $age . " years</h3>";
    }
    ?>
</body>
</html>
