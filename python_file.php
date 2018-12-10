<?php

$file_tmp =$_FILES['file']['tmp_name'];

move_uploaded_file($file_tmp,"logs_file.txt");

echo "Success";

?>