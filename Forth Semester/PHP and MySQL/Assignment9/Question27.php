<!-- 27. Write a program in PHP to read from directory. -->
<?php
$directory = "."; 


if (is_dir($directory)) {
    
    $files = scandir($directory);
    
    echo "<h2>Contents of Directory: $directory</h2>";
    echo "<ul>";
    
    foreach ($files as $file) {
        
        if ($file != "." && $file != "..") {
            echo "<li>$file</li>";
        }
    }
    
    echo "</ul>";
} else {
    echo "<h2>Directory not found!</h2>";
}
?>
