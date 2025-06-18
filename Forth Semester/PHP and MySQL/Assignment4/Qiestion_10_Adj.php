<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $n=$_POST['num'];
    $s=$n;
    $r=0;
    while($n>0){
        $d=($n%10);
        $r=($r*10)+$d;
        $n=(int)($n/10);
    }
    if($r==$s)
    echo "$s is palindrom:";
    else
    echo "$s is not palindrom:";
    ?>

</body>
</html>