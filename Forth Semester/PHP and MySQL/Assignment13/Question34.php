 <!-- 34. Create a form of four field as name, address, age and password. Input name, address, age and password through form. Then create a file with name and write name, address, age, password in that file. is_file() function  check the existence of file in “data” directory. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submit User Details</title>
</head>
<body>
    <h2>Enter Your Details</h2>
    <form action="/Assignment13/Question34Adj.php" method="post">
        Name: <input type="text" name="name" required><br><br>
        Address: <input type="text" name="address" required><br><br>
        Age: <input type="number" name="age" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" name="submit" value="Submit">
    </form>
</body>
</html>
