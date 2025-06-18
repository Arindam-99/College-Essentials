<!-- 22.	 Write a PHP program to create an array and store 10 names in the array. Do the following operations.
⮚	Display the contents using for each statement.
⮚	Display the array in a sorted order.
⮚	Display the array without the duplicate elements
⮚	Remove the last element and display
⮚	Display the array in reverse order
⮚	Insert a new element in a specified position
⮚	Search and find out position of an element from array   -->

<!DOCTYPE html>
<html>
<head>
    <title>PHP Array Operations</title>
</head>
<body>

    <form method="post">
        <h3>Enter 10 Names:</h3>
        <?php for ($i = 0; $i < 10; $i++) { ?>
            <input type="text" name="names[]" required><br>
        <?php } ?>
        <input type="submit" name="submit" value="Submit">
    </form>

    <?php
    if (isset($_POST['submit']) || isset($_POST['insert']) || isset($_POST['search'])) {
        $names = isset($_POST['names']) ? $_POST['names'] : [];

        echo "<h3>Original Array:</h3>";
        echo implode(", ", $names);

        // Display sorted array
        $sortedNames = $names;
        sort($sortedNames);
        echo "<h3>Sorted Array:</h3>";
        echo implode(", ", $sortedNames);

        // Display array without duplicates
        $uniqueNames = array_unique($names);
        echo "<h3>Array without duplicates:</h3>";
        echo implode(", ", $uniqueNames);

        // Remove last element and display
        array_pop($names);
        echo "<h3>Array after removing last element:</h3>";
        echo implode(", ", $names);

        // Display array in reverse order
        $reversedNames = array_reverse($names);
        echo "<h3>Reversed Array:</h3>";
        echo implode(", ", $reversedNames);
    ?>

    <form method="post">
        <h3>Insert a new name:</h3>
        <input type="text" name="newName" required>
        <input type="number" name="position" min="0" max="<?php echo count($names); ?>" required>
        <input type="hidden" name="names[]" value="<?php echo implode(',', $names); ?>">
        <input type="submit" name="insert" value="Insert">
    </form>

    <form method="post">
        <h3>Search for a name:</h3>
        <input type="text" name="searchName" required>
        <input type="hidden" name="names[]" value="<?php echo implode(',', $names); ?>">
        <input type="submit" name="search" value="Search">
    </form>

    <?php
    }

    if (isset($_POST['insert'])) {
        $names = explode(',', $_POST['names'][0]); // Retrieve stored names
        $newName = $_POST['newName'];
        $position = intval($_POST['position']);
        array_splice($names, $position, 0, $newName);
        echo "<h3>Array after insertion:</h3>";
        echo implode(", ", $names);
    }

    if (isset($_POST['search'])) {
        $names = explode(',', $_POST['names'][0]); // Retrieve stored names
        $searchName = $_POST['searchName'];
        $pos = array_search($searchName, $names);
        if ($pos !== false) {
            echo "<h3>Name found at position: $pos</h3>";
        } else {
            echo "<h3>Name not found in the array.</h3>";
        }
    }
    ?>

</body>
</html>
