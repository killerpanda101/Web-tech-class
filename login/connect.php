<?php
$se = getenv("DB_HOST") ?: "localhost";
$un = getenv("DB_USER") ?: "root";
$pw = getenv("DB_PASS") ?: "";
$db = getenv("DB_NAME") ?: "vit";

$conn = mysqli_connect($se,$un,$pw,$db);


