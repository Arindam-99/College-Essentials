<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retrieve URL Information</title>
</head>
<body>

    <h2>Enter a URL to Retrieve Information</h2>

    <form action="" method="POST">
        <label for="url">Enter URL:</label>
        <input type="text" id="url" name="url" placeholder="https://www.example.com" required>
        <br><br>
        <input type="submit" value="Get URL Info">
    </form>

    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the user-inputted URL
    $url = trim($_POST['url']);

    // Validate URL
    if (!filter_var($url, FILTER_VALIDATE_URL)) {
        echo "<h2 style='color: red;'>Invalid URL! Please enter a valid URL.</h2>";
        echo "<br><a href='index.html'>Go Back</a>";
        exit;
    }

    // Parse URL components
    $parsedUrl = parse_url($url);

    // Display URL components
    echo "<h2>URL Information</h2>";
    echo "<strong>Full URL:</strong> $url <br><br>";

    echo "<ul>";
    echo "<li><strong>Scheme (Protocol):</strong> " . ($parsedUrl['scheme'] ?? 'N/A') . "</li>";
    echo "<li><strong>Host (Domain):</strong> " . ($parsedUrl['host'] ?? 'N/A') . "</li>";
    echo "<li><strong>Port:</strong> " . ($parsedUrl['port'] ?? 'Default (80/443)') . "</li>";
    echo "<li><strong>Path:</strong> " . ($parsedUrl['path'] ?? 'N/A') . "</li>";
    echo "<li><strong>Query Parameters:</strong> " . ($parsedUrl['query'] ?? 'N/A') . "</li>";
    echo "<li><strong>Fragment (Anchor):</strong> " . ($parsedUrl['fragment'] ?? 'N/A') . "</li>";
    echo "</ul>";

    
} else {
    echo "Invalid Request!";
}
?>

</body>
</html>
