<?php
    date_default_timezone_set('Asia/Tokyo');

    if(isset($_GET['number']) && $_GET['number'] != ''){
        $machine_number = filter_input(INPUT_GET, 'number');
        echo "$machine_number";

        $log_write = "\n[" . date("Y/m/d H:i:s") . "] number:"  . $machine_number . "\n";
        file_put_contents("all.log", $log_write , FILE_APPEND);
    }
    else{
        echo 'numberが受け取れません';
    }
?>
