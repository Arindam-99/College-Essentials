<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    echo "<h2> Current Date and Time:</h2>";
    $mydate=getDate();
    echo "$mydate[weekday],$mydate[month] $mydate[mday],$mydate[year] $mydate[hours]:$mydate[minutes]:$mydate[seconds]";
    ?>
</body>
</html>