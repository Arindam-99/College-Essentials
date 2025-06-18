<!-- 23.	Write a PHP program to create a String and store value on that string “php Program - the complete SOLUTION for WEB development”. Do the following operations.
⮚	convert lowercase string to uppercase
⮚	convert uppercase string to lowercase
⮚	convert first character uppercase
⮚	convert first character of all the words uppercase
⮚	get the last 11 characters of string
⮚	replace the first ‘the’ of the following string with ‘best’
⮚	get the Second word of a sentence
⮚	insert a string at the specified position in a given string -->

<!DOCTYPE html>
<html>
<head>
    <title>PHP String Operations</title>
</head>
<body>
    <form method="post">
        <label>Enter a String:</label><br>
        <input type="text" name="user_string" required><br><br>
        <label>Enter a String to Insert:</label><br>
        <input type="text" name="insert_string" required><br><br>
        <label>Enter Position to Insert:</label><br>
        <input type="number" name="position" min="0" required><br><br>
        <input type="submit" name="submit" value="Perform Operations">
    </form>

    <?php
    if (isset($_POST['submit'])) {
        $user_string = $_POST['user_string'];
        $insert_string = $_POST['insert_string'];
        $position = intval($_POST['position']);

        echo "<h3>Original String:</h3>" . $user_string;

        // Convert lowercase to uppercase
        echo "<h3>Uppercase:</h3>" . strtoupper($user_string);
        
        // Convert uppercase to lowercase
        echo "<h3>Lowercase:</h3>" . strtolower($user_string);
        
        // Convert first character to uppercase
        echo "<h3>First Character Uppercase:</h3>" . ucfirst(strtolower($user_string));
        
        // Convert first character of all words to uppercase
        echo "<h3>Title Case:</h3>" . ucwords(strtolower($user_string));
        
        // Get the last 11 characters of string
        echo "<h3>Last 11 Characters:</h3>" . substr($user_string, -11);
        
        // Replace the first occurrence of 'the' with 'best'
        echo "<h3>Replace 'the' with 'best':</h3>" . preg_replace('/\bthe\b/', 'best', $user_string, 1);
        
        // Get the second word of the sentence
        $words = explode(" ", $user_string);
        echo "<h3>Second Word:</h3>" . ($words[1] ?? 'N/A');
        
        // Insert a string at a specified position
        $modified_string = substr_replace($user_string, $insert_string, $position, 0);
        echo "<h3>String After Insertion:</h3>" . $modified_string;
    }
    ?>
</body>
</html>
