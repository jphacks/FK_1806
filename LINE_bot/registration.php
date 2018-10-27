<?php
$fp = fopen('access_token.txt', 'r');
$access_token = fgets($fp);
$channelSecret = fgets($fp);

// APIから送信されてきたイベントオブジェクトを取得
$json_string = file_get_contents('php://input');
$json_obj = json_decode($json_string);

// イベントオブジェクトから必要な情報を抽出
$reply_token = $json_obj->{"events"}[0]->{"replyToken"};
$message = $json_obj->{"events"}[0]->{"message"};
$sent_message = $message->{"text"};   // 追記分、実際にユーザから送られたメッセージ
//postbackの"data"の取得
$postback_data = $json_obj->{"events"}[0]->{"postback"}->{"data"};
//クエリ文字列を通常の変数に変換
parse_str($postback_data);

/*
// HTTPヘッダーを取得
$headers = getallheaders();
print_r($headers);
// HTTPヘッダーから、署名検証用データを取得
$headerSignature = $headers["X-Line-Signature"];
// Channel secretを秘密鍵として、JSONデータからハッシュ値を計算
$httpRequestBody = $json_string;
$hash = hash_hmac('sha256', $httpRequestBody, $channelSecret, true);
$signature = base64_encode($hash);
// HTTPヘッダーから得た値と、計算したハッシュ値を比較
if($headerSignature !== $signature)
{
  print($headerSignature . "//////////". $signature);
  exit;
}
*/

// 絵文字
$kirara          = toEmoji('100080');   // きらら
$brown           = toEmoji('100084');   // Brown
$cony_cute_smile = toEmoji('10009D');   // cony cute smile


// 言語処理を行って$best_replyに最適な返答を代入する------------------------------
// 使い方
if(strpos($sent_message, "使い方")!==false or $how_to==1){
  sending(reply("使い方ここで説明できればなと"));
}

// IR機器登録用
if(strpos($sent_message, "機器の登録")!==false){
  sending(buttons(
  "登録番号を選択してください\nすでに登録されている番号は上書きされます",
  "登録番号を選択してください\nすでに登録されている番号は上書きされます",
  "1:ByeBye",
  "gesture_index=1&mode=1",
  "2:HandUp",
  "gesture_index=2&mode=1",
  "3:Safe",
  "gesture_index=3&mode=1"
  ));
}

// ジェスチャ登録用
if(strpos($sent_message, "ジェスチャ")!==false or $how_to==1){
  sending(reply("ジェスチャ登録は後日実装予定です！\nしばしお待ちください"));
}

// ラズパイ送信用
if($mode==1){
  $content = file_get_contents("http://73161605.ngrok.io/cgi-bin/main.py");
  if ($content){
    sending(reply("SNAPが赤外線登録モードになりました！${kirara}\n赤外線受信部に向かって登録する赤外線を送信してください"));
  } else{
    sending(reply("問題が生じたためSNAPを赤外線登録モードにできませんでした（泣）\nもうしばらく経ってからお試しください\n${content}"));
  }
}


// ブラウザで表示された時のログ表示
print("Hello");

// -------------------------------------------------------------------------
// 16進数から絵文字に変換する関数
function toEmoji($code){
  $bin = hex2bin(str_repeat('0', 8 - strlen($code)) . $code);
  $emoticon =  mb_convert_encoding($bin, 'UTF-8', 'UTF-32BE');

  return $emoticon;
}

// 単純なメッセージを返信する関数
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

// confirmの型(postback専用)
function confirm($altText, $text, $label1, $data1, $label2, $data2){
  global $reply_token;

  $post_data = [
    "replyToken" => $reply_token,
    "messages" => [
    [
      "type"=>"template",
      "altText"=>$altText,
      "template"=>[
          "type"=>"confirm",
          "text"=>$text,
          "actions"=>[
          [
            "type"=>"postback",
            "label"=>$label1,
            "data"=>$data1
          ],
          [
            "type"=>"postback",
            "label"=>$label2,
            "data"=>$data2
          ]
        ]
      ]
    ]
    ]
  ];
  return $post_data;
}

// 画像なしbuttonsの型(postback専用)
function buttons($altText, $text, ...$template){
  global $reply_token;

  $post_data = [
      "replyToken" => $reply_token,
      "messages" => [
      [
          "type"=>"template",
          "altText"=>$altText,
          "template"=>[
            "type"=>"buttons",
            "text"=>$text,
            "actions"=>[]
          ]
        ]
        ] 
    ];
    for($i=0; $i<count($template); $i=$i+2){
      array_push($post_data["messages"][0]["template"]["actions"],
        [
          "type"=>"postback",
          "label"=>$template[$i],
          "data"=>$template[$i+1]
        ]);
    }
    return $post_data;
}

// curlを使用してメッセージを送信する関数
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
