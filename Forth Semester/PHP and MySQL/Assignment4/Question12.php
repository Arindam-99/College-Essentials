<!-- 12.	PHP Program to display digital clock with current time of the Server. -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
   
    <meta http-equiv="refresh" content="1"> <!--it is refresh the page -->
    <title>Digital Clock</title>
</head>
<body>
    <h3>Current Time</h3>
    <?php
    $cur=date('h:i:s');
    echo $cur;
    ?>
</body>
</html>