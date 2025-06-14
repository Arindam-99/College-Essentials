<?php
$currentDirectory = __DIR__;

$currentFile = __FILE__;

$currentLine = __LINE__;

echo "<h2>PHP File Information</h2>";
echo "Current Directory: $currentDirectory <br>";
echo "Current File: $currentFile <br>";
echo "Current Line Number: $currentLine <br>";

echo "This is printed on line: " . __LINE__ . "<br>";
?>
