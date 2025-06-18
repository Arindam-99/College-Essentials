<!--13. write a program that displays a different message based on time of day,for example,page should display : "Good morning" if it is assessed in the morning" -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $d=date('H');
    if($d>5 && $d<12){
        echo "<B>Good morning";
    }elseif($d>12 && $d<16){
    echo "<B>Good Afternoon!";
    }elseif($d>16 && $d<19){
        echo "<B>Good Evening!";
    }
    else{
        echo "Good night!";
    }

    ?>
</body>
</html>