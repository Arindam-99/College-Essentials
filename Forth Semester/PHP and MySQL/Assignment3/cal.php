<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="cal2.php" method="post">
    <label> Enter 1st number :</label>&nbsp;&nbsp;
    <input type = "number" name ="num1" required>
    <br><br>
    <label>Enter 2nd Number :</label>&nbsp;&nbsp;
    <input type ="number" name ="num2" required>
    <br><br>
    <label>Enter choice : </label>&nbsp;&nbsp;
    <select name ="choice" id="choice">
        <option value ="Addition">Addition</option>
        <option value ="Subtraction">Subtraction</option>
        <option value ="Multiplication">Multiplication</option>
        <option value ="Division">Division</option>
</select>
<br><br>
<input type ="reset">&nbsp;&nbsp;
<input type ="submit" value ="submit">
</form>
</body>
</html>
