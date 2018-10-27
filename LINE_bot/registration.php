<?php
$access_token = 'gcqvTOL50GecC9o9+BYcBqFODfFNrHQJfEc1et/mK8isKswHX36eXYEc5ho8Gm+z0w4+qxhZsWtHsZYEdyx1P1ZtvztHqMLhzNhd/OOEkgQIutiLPv3LSptdeBmtkqtuuX7DM59Xk+ixECMBvxqC5AdB04t89/1O/w1cDnyilFU=';

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

// 絵文字
$kirara          = toEmoji('100080');   // きらら
$brown           = toEmoji('100084');   // Brown
$cony_cute_smile = toEmoji('10009D');   // cony cute smile


// 言語処理を行って$best_replyに最適な返答を代入する------------------------------
// 使い方
if(strpos($sent_message, "使い方")!==false or $how_to==1){
  sending(reply("使い方ここで説明できればなと"));
}
// IR機器登録
if(strpos($sent_message, "登録")!==false){
  sending(confirm(
    "〇〇 という名前で赤外線の登録を始めますか？${cony_cute_smile}",
    "〇〇 という名前で赤外線の登録を始めますか？${cony_cute_smile}",
    "はい",
    "IRregister=yes",
    "いいえ",
    "IRregister=no"
    ));
}
// 上記のIR機器登録のconfirmに対する返答に対して
if($IRregister=="yes"){
  $content = file_get_contents("http://73161605.ngrok.io/cgi-bin/main.py");
  if ($content){
    sending(reply("SNAPが赤外線登録モードになりました！${kirara}\n赤外線受信部に向かって登録する赤外線を送信してください"));
  } else{
    sending(reply("問題が生じたためSNAPを赤外線登録モードにできませんでした（泣）\nもうしばらく経ってからお試しください\n${content}"));
  }
}if($IRregister=="no"){
  sending(buttons(
    "中止しました\n使い方を知りたい場合は以下のボタンを押してみてください${brown}",
    "中止しました\n使い方を知りたい場合は以下のボタンを押してみてください${brown}",
    "使い方を見る",
    "how_to=1"
  ));
}


// ブラウザで表示された時のログ表示
print("ちゃっす");

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
