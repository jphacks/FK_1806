<?php
$access_token = 'gcqvTOL50GecC9o9+BYcBqFODfFNrHQJfEc1et/mK8isKswHX36eXYEc5ho8Gm+z0w4+qxhZsWtHsZYEdyx1P1ZtvztHqMLhzNhd/OOEkgQIutiLPv3LSptdeBmtkqtuuX7DM59Xk+ixECMBvxqC5AdB04t89/1O/w1cDnyilFU=';

//APIから送信されてきたイベントオブジェクトを取得
$json_string = file_get_contents('php://input');
$json_obj = json_decode($json_string);

//イベントオブジェクトから必要な情報を抽出
$reply_token = $json_obj->{"events"}[0]->{"replyToken"};
$message = $json_obj->{"events"}[0]->{"message"};
$sent_message = $message->{"text"};//追記分、実際にユーザから送られたメッセージ

//言語処理を行って$best_replyに最適な返答を代入する------------------------------
//使い方
if(strpos($sent_message, "list")!==false){
  sending(reply("リモコンなどの赤外線を登録したい際は「（任意の登録名） （1から3の数字）」とそれぞれ任意の文字を入れて送信してください"));
}


// ブラウザで表示された時のログ表示
print("ちゃっす");

//-------------------------------------------------------------------------
//単純なメッセージを返信する関数
function reply($message){
  global $reply_token;

  $post_data = [
    "replyToken" => $reply_token,
    "messages" => [
    [
      "type" => "text",
      "text" => $message 
    ]
  ]
];
  return $post_data;
}

//curlを使用してメッセージを送信する関数
function sending($poda){
  global $access_token;

  $ch = curl_init("https://api.line.me/v2/bot/message/reply");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($poda));
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json; charser=UTF-8',
    'Authorization: Bearer ' . $access_token
));
$result = curl_exec($ch);
curl_close($ch);
}
