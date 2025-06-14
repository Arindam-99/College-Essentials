<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vowel Counter</title>
</head>
<body>
    <h1>Vowel Counter</h1>
    <form method="post">
        <label for="inputString">Enter a string: </label>
        <input type="text" id="inputString" name="inputString" required>
        <input type="submit" value="Count Vowels">
    </form>

    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $inputString = $_POST["inputString"];
            countVowels($inputString);
        }

        function countVowels($string) {
            // Convert string to lowercase to handle both uppercase and lowercase vowels
            $string = strtolower($string);
            
            // Vowel characters
            $vowels = ['a', 'e', 'i', 'o', 'u'];
            $vowelCount = [
                'a' => 0,
                'e' => 0,
                'i' => 0,
                'o' => 0,
                'u' => 0
            ];
            
            // Count occurrences of each vowel
            $totalVowels = 0;
            for ($i = 0; $i < strlen($string); $i++) {
                $char = $string[$i];
                if (in_array($char, $vowels)) {
                    $vowelCount[$char]++;
                    $totalVowels++;
                }
            }

            // Display the results
            echo "<h3>Total number of vowels: $totalVowels</h3>";
            echo "<h4>Occurrences of each vowel:</h4>";
            foreach ($vowelCount as $vowel => $count) {
                echo "<p>$vowel: $count</p>";
            }
        }
    ?>
</body>
</html>
