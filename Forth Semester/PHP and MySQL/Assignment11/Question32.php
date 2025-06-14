<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload in PHP</title>
</head>
<body>

    <h2>Upload a File</h2>

    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose File:</label>
        <input type="file" name="file" id="file" required>
        <br><br>
        <input type="submit" value="Upload File">
    </form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    $uploadDir = "uploads/"; // Directory to store uploaded files
    $fileName = basename($_FILES["file"]["name"]);
    $uploadFilePath = $uploadDir . $fileName;
    
    // Check if the directory exists, if not, create it
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    // Check if file was uploaded successfully
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $uploadFilePath)) {
        echo "<h2>File Uploaded Successfully!</h2>";
        echo "<ul>";
        echo "<li><strong>File Name:</strong> " . $_FILES["file"]["name"] . "</li>";
        echo "<li><strong>File Type:</strong> " . $_FILES["file"]["type"] . "</li>";
        echo "<li><strong>File Size:</strong> " . ($_FILES["file"]["size"] / 1024) . " KB</li>";
        echo "<li><strong>Temporary Location:</strong> " . $_FILES["file"]["tmp_name"] . "</li>";
        echo "<li><strong>Saved Location:</strong> " . $uploadFilePath . "</li>";
        echo "</ul>";
    } else {
        echo "<h2 style='color: red;'>File upload failed. Please try again.</h2>";
    }
}
?>
</body>
</html>






