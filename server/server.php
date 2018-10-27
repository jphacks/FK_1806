<?php
    date_default_timezone_set('Asia/Tokyo');
    $ngrok_url = "http://737facba.ngrok.io";
    $send_url = $ngrok_url . "/cgi-bin/main.py";

    if(isset($_GET['number']) && $_GET['number'] != ''){
        $machine_number = filter_input(INPUT_GET, 'number');
        echo "$machine_number";

        $log_write = "\n[" . date("Y/m/d H:i:s") . "] number:"  . $machine_number . "\n";
        file_put_contents("all.log", $log_write , FILE_APPEND);

        $get_url = $send_url . "?key=" . $machine_number;
        
        $curl = curl_init($get_url);

        curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'GET'); // メソッド指定
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // 証明書の検証を行わない
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); // レスポンスを文字列で受け取る

         $response = curl_exec($curl);

        curl_close($curl);
    }
    else{
        echo 'numberが受け取れません';
    }
?>
