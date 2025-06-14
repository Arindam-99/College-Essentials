<?php
if(preg_match('/Mobile|Android|iphone|ipad|blackberry|windows Phone/',$_SERVER['HTTP_USER_AGENT'])){
  echo "<h1>This is a mobile device</h1>";
}else{
  echo "<h1>This is a desktop device</h1>";
}
?>
