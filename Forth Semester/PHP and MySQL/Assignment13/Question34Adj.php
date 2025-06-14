<?php
if (isset($_POST['submit'])) {
    // Collect form data
    $name = trim($_POST['name']);
    $address = trim($_POST['address']);
    $age = trim($_POST['age']);
    $password = trim($_POST['password']);

    // Directory to save the file
    $dir = "data/";

    // Create "data" folder if it doesn't exist
    if (!is_dir($dir)) {
        mkdir($dir, 0777, true);
    }

    // Clean the filename (optional but safe)
    $safeName = preg_replace("/[^a-zA-Z0-9]/", "_", $name);

    // Filename will be like: Arindam.txt
    $filename = $dir . $safeName . ".txt";

    // Prepare content to write
    $content = "Name: $name\n";
    $content .= "Address: $address\n";
    $content .= "Age: $age\n";
    $content .= "Password: $password\n";

    // Save the content into the text file
    if (file_put_contents($filename, $content)) {
        echo "✅ User details saved successfully into <b>'$filename'</b>.<br><br>";

        // Check using is_file() if it really exists
        if (is_file($filename)) {
            echo "<h3>Stored User Details:</h3>";
            echo nl2br(htmlspecialchars($content));
        } else {
            echo "Error: File not found after saving.";
        }
    } else {
        echo "❌ Failed to save user details.";
    }
} else {
    echo "Form not submitted.";
}
?>
