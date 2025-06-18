<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>checking</title>
</head>
<body>
    <?php
    $name=$_POST['name'];
    // $rev=strrev($name)
    // echo "The original String is $name";
    if($name==strrev($name)){
        echo "The string is $name Palindrom: <br>";
    }else{
        echo "The string  $name is not  Palindrom:";
    }
    

    ?>
</body>
</html>