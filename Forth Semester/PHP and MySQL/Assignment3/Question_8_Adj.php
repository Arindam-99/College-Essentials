<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
$n1=$_POST['num1'];
$n2=$_POST['num2'];
$choice=$_POST['choice'];
switch($choice)
{
    case "Addition":
        echo "Addition  of $n1 and $n2 is:".($n1+$n2);
        break;
        case "Subtraction":
            echo "Subtraction $n1 and $n2  is:".($n1-$n2);
            break;
            case "Multiplication":
                echo "Multiplication $n1 and $n2  is:".($n1*$n2);
                break;
                case "Division":
                    echo "Division $n1 and $n2  is:".($n1/$n2);
                    break;
                    default:
                    echo "Wrong Choice";
                }
  ?>
</body>
</html>