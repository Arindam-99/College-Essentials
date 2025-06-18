<!-- 33.  Write a PHP program to upload an image file within “upload” 	folder. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload Image</title>
</head>
<body>
    <h2>Upload Image</h2>
    <form action="/Assignment12/Question33Adj.php" method="post" enctype="multipart/form-data">
        Select image to upload:<br><br>
        <input type="file" name="fileToUpload" id="fileToUpload"><br><br>
        <input type="submit" value="Upload Image" name="submit">
    </form>
</body>
</html>
