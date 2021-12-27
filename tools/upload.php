<?php
if (isset($_POST['submit'])) {
    $file = $_FILES['file'];
    print_r($file);
    $fileName = $file['name'];
}