# SNAP

[![SNAP-MOVIE](/image/snap_logo.jpeg)](https://vimeo.com/297533613)

動画URL(Vimeo) : [https://vimeo.com/297533613](https://vimeo.com/297533613 "VimeoURL")


## 製品概要
### **ジェスチャ** × Tech

### 背景（製品開発のきっかけ、課題等）
私たちの身の回りは、さまざまなモノで溢れています。  
私たちが毎日生活している家も然り。普段の暮らしの中で、「ただいま〜。あれ、リモコンどこだっけ？」なんてことも。

IoTにより、それらのあらゆるモノがインターネットで繋がるようになりました。  
リモコンの代わりに、スマートフォンのアプリや音声認識などのインターフェースを使ったスマート家電も多くあります。  

しかし、音声認識できなかったり、そもそも音声認識してもらうために意識して話すのもちょっと違う...いちいちスマホのアプリ登録するのも大変...。  
このように、既存の製品は、インターフェースに課題があると考えました。

**より直感的なインターフェースを作りたい！**  

上記のような課題を解決するプロダクトを作りたいという想いから、今回、人々の**ジェスチャ**にフォーカスした**SNAP**の開発に至りました。

### 製品説明（具体的な製品の説明）
**SNAP**は、WEBカメラであなたの**ジェスチャ**を認識し、あなたの家のさまざま家電製品の操作・管理するデバイスです。

#### 使用方法
①LINEから **SNAP@** を友だちに追加し、操作する家電製品とそれに対応するジェスチャを選択し、学習します。（LINE_botを使用）  

![Linebotでの家電・ジェスチャ登録](/image/Linebot.gif)  

②上記の要領で、複数の家電製品とジェスチャを登録できます。  

③指の「スナップ」が、WEBカメラのトリガーになります。（音声認識を使用）  

④あとは、あなたが動くだけです。あなたのジェスチャが家電製品のスイッチになります。

### 特長

#### 1. 家電製品の操作をあなたのジェスチャで
従来のスマート家電は、スマートフォンアプリや音声認識などのインターフェースを使ったものが多くありますが、SNAPではジェスチャ認識を用いている点で、直感性・革新性があります。

||カテゴリー|インターフェース|直感性|操作性|コスト|
|  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |
|**S N A P**|**WEBカメラ**|**ジェスチャ認識**|**◎**|**○**|**○**|
|LINE ClovaFriendsDock|赤外線リモコン|音声認識|○|○|△|
|iRobot ルンバ|掃除機|スマートフォンアプリ|△|○|△|

#### 2. 複数の家電製品とそれに対応するジェスチャを登録
あなたの家の家電製品を直感的に操作し、それらのスイッチを一元的に管理することができます。  

①ByeBye  
![①ByeBye](/image/ByeByeHQ.gif)  

②HandUp  
![②HandUp](/image/HandUpHQ.gif)  

③Safe  
![③Safe](/image/SafeHQ.gif)

#### 3. 左右180°内で、指示された家電製品の方向へデバイスが動く
サーボモータを搭載した自作デバイスが、赤外線を送受信するために、操作・管理する家電の方向を向きます。  
エアコンなどの高い位置にある家電にも対応するために、サーボモータを2つ使用して、左右180°に加え上下180°にも動くようにしました。

#### 4. 赤外線送受信による家電操作
家電の操作・管理には赤外線を使用しています。  
Wi-fiやBLE、超音波などを使用するのではなく、赤外線を使用することで、スマート家電のような専用家電でなくても、赤外線を使用する家電なら**SNAP**で操作・管理することを可能としています。


### 解決出来ること
もうリモコンを探すことも、音声認識を意識して話すこともありません。  
あなたのジェスチャで、直感的に家電製品を操作し、それらのスイッチを一元的に管理することができます。  
SNAPは、より直感的なインターフェースとして、ジェスチャによる家電製品の操作・管理という新たな価値を提供し、人々の暮らしをより豊かにします。

### 今後の展望
#### 実装予定

- WEBカメラを複数台用いた多方向からのジェスチャ認識

- オリジナルジェスチャの登録

- 登録をはじめとする機能のインターフェースもジェスチャに一元化する


今回は、家電製品にフォーカスした開発を行いましたが、「ボディランゲージ」という言葉があるように、ジェスチャは最も直感的でシンプルなコミュニケーションの手段であると考えています。  

このジェスチャ認識の技術を、言語の壁を乗り越えた世界中の人々の更なるコミュニケーションの活性化や、ろう者のような身体の不自由な方がよりストレスなく過ごせる社会環境づくりに発展させたいと考えています。

## 開発内容・開発技術
#### システムフロー
![システムフロー](/image/snap_flow.jpeg)

### 活用した技術

#### API・データ

* messaging API

#### フレームワーク・ライブラリ・モジュール
* OpenPose
* CUDA8
* cuDNN5.1
* LINE_bot
* さくらのレンタルサーバ
* numpy
* pyaudio
* pigpio
* wiringPi
* ngrock

#### デバイス
* RaspberryPi
* サーボモータ
* 赤外線受信モジュール
* 赤外線送信LED

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* フーリエ変換を用いたスナップ音の認識 [(Code)](https://github.com/jphacks/FK_1806/blob/master/python/SNAP.py#L15")
* ジェスチャ(3種類)のリアルタイム認識 [(Code)](https://github.com/jphacks/FK_1806/blob/master/python/SNAP.py#L30")
* 自作デバイスの制作
