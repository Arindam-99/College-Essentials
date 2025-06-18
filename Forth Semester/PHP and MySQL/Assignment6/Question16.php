<!-- 16.	 Write a program to create Chess board in PHP using for loop -->
<?php
    echo "<table border='1' width='400px' height='400px' cellspacing='0' cellpadding='0'>";
    for ($row = 0; $row < 8; $row++) {
        echo "<tr>";
        for ($col = 0; $col < 8; $col++) {
            $color = ($row + $col) % 2 == 0 ? "#ffffff" : "#000000";
            echo "<td style='background-color: $color; width: 50px; height: 50px;'></td>";
        }
        echo "</tr>";
    }
    echo "</table>";
?>
