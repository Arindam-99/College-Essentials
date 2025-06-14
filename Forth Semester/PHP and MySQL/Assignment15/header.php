<!-- header.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Website</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .menu {
            background-color: #333;
            overflow: hidden;
        }
        .menu a {
            float: left;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        .menu a.active {
            background-color: #4CAF50; /* green for active link */
        }
        .menu a:hover {
            background-color: #575757;
        }
    </style>
</head>
<body>
<div class="menu">
    <a href="home.php" class="<?php echo ($currentPage == 'home') ? 'active' : ''; ?>">Home</a>
    <a href="about.php" class="<?php echo ($currentPage == 'about') ? 'active' : ''; ?>">About</a>
</div>
<br>
