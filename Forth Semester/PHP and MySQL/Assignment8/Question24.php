<!-- 24.Write a division table program in PHP using for loop.
<?php
$size = 10; // Define the size of the division table

echo "<h2>Division Table</h2>";
echo "<table border='1' cellpadding='5' cellspacing='0'>";

// Table Header
echo "<tr><th></th>";
for ($i = 1; $i <= $size; $i++) {
    echo "<th>$i</th>";
}
echo "</tr>";

// Generate table rows
for ($i = 1; $i <= $size; $i++) {
    echo "<tr><th>$i</th>";
    for ($j = 1; $j <= $size; $j++) {
        $result = number_format($i / $j, 3); // Format result to 3 decimal places
        echo "<td>$result</td>";
    }
    echo "</tr>";
}

echo "</table>";
?> -->
