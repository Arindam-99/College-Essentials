<!-- 2.	To write a program gets the name of the user from a form and show greeting text. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Form</title>
</head>
<body>
    <h2>Enter Your Details</h2>
    <form action="/Assignment1/Question_2_Adj.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
