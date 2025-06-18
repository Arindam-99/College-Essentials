<!-- 25. Write a program in PHP get array key from given array list -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fruit Color Finder</title>
</head>
<body>

    <h2>Select a Fruit to Find Its Color</h2>
    
    <form action="" method="POST">
        <label for="fruit">Choose a fruit:</label>
        <select name="fruit" id="fruit">
        <option value="apple">Chhose the option ! </option>
            <option value="apple">Apple</option>
            <option value="banana">Banana</option>
            <option value="orange">Orange</option>
            <option value="grapes">Grapes</option>
            <option value="watermelon">Watermelon</option>
        </select>
        <br><br>
        <input type="submit" value="Find Color">
    </form>
    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Define fruit colors in an associative array
    $fruitColors = [
        "apple" => "red",
        "banana" => "yellow",
        "orange" => "orange",
        "grapes" => "purple",
        "watermelon" => "green"
    ];

    // Get user-selected fruit
    $selectedFruit = $_POST['fruit'];

    // Check if the selected fruit exists in the array
    if (array_key_exists($selectedFruit, $fruitColors)) {
        $color = $fruitColors[$selectedFruit];
        echo "<h2>The color of " . ucfirst($selectedFruit) . " is " . $color . ".</h2>";
    } else {
        echo "<h2>Fruit not found!</h2>";
    }
} else {
    echo "Invalid Request!";
}
?>

</body>
</html>
