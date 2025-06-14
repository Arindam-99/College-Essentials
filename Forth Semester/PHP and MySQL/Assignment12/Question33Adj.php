<?php
$message = "";
$imageHTML = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $targetDir = "upload/";
    
    // Create directory if it doesn't exist
    if (!is_dir($targetDir)) {
        mkdir($targetDir, 0755, true);
    }

    $targetFile = $targetDir . basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

    // Check if file is an actual image
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if ($check !== false) {
        $message .= "File is an image - " . $check["mime"] . ".<br>";
    } else {
        $message .= "File is not an image.<br>";
        $uploadOk = 0;
    }

    // Check if file already exists
    if (file_exists($targetFile)) {
        $message .= "Sorry, file already exists.<br>";
        $uploadOk = 0;
    }

    // Check file size (limit: 5MB)
    if ($_FILES["fileToUpload"]["size"] > 5000000) {
        $message .= "Sorry, your file is too large.<br>";
        $uploadOk = 0;
    }

    // Allow only specific formats
    $allowedFormats = ["jpg", "jpeg", "png", "gif"];
    if (!in_array($imageFileType, $allowedFormats)) {
        $message .= "Sorry, only JPG, JPEG, PNG & GIF files are allowed.<br>";
        $uploadOk = 0;
    }

    // Attempt to upload file
    if ($uploadOk == 1) {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
            $message .= "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded.<br>";
            $imageHTML = "<h3>Uploaded Image:</h3><img src='$targetFile' style='max-width:500px;'><br>";
        } else {
            $message .= "Sorry, there was an error uploading your file.<br>";
        }
    } else {
        $message .= "Sorry, your file was not uploaded.<br>";
    }
}
?>
