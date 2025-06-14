<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Self-Processing Form</title>
</head>
<body>

    <h2>Enter Your Details</h2>

    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>

        <input type="submit" value="Submit">
    </form>
    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize variables
    $name = $email = "";
    $nameErr = $emailErr = "";

    // Validate Name
    if (empty($_POST["name"])) {
        $nameErr = "Name is required";
    } else {
        $name = htmlspecialchars($_POST["name"]);
    }

    // Validate Email
    if (empty($_POST["email"])) {
        $emailErr = "Email is required";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $emailErr = "Invalid email format";
    } else {
        $email = htmlspecialchars($_POST["email"]);
    }

    // If no errors, show success message
    if (empty($nameErr) && empty($emailErr)) {
        echo "<h2>Form Submitted Successfully</h2>";
        echo "Name: $name <br>";
        echo "Email: $email <br>";
    } else {
        // Show errors
        echo "<h2>Form Submission Failed</h2>";
        echo "<p style='color:red;'>$nameErr</p>";
        echo "<p style='color:red;'>$emailErr</p>";
    }

  
}else{

  echo "Invalid";
} 
?>

</body>
</html>
