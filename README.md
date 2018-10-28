# SNAP

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### **ジェスチャ** ✖ Tech

### 背景（製品開発のきっかけ、課題等）
私たちの身の回りは、さまざまなモノで溢れています。  
私たちが毎日生活している家も然り。普段の暮らしの中で、「ただいま〜。あれ、リモコンどこだっけ？」なんてことも。

IoTにより、それらのあらゆるモノがインターネットで繋がるようになりました。  
リモコンの代わりに、スマートフォンのアプリや音声認識などのインターフェースを使ったスマート家電も多くあります。  

しかし、音声認識できなかったり、そもそも音声認識してもらうために意識して話すのもちょっと違う...いちいちスマホのアプリ登録するのも大変...  
このように、既存の製品は、インターフェースに課題があると考えました。

**より直感的なインターフェースを作りたい！**  

上記のような課題を解決するプロダクトを作りたいという想いから、今回、人々の**ジェスチャ**にフォーカスした**SNAP**の開発に至りました。

### 製品説明（具体的な製品の説明）
**SNAP**は、WEBカメラであなたの**ジェスチャ**を認識し、あなたの家のさまざま家電製品のON/OFFを操作・管理するデバイスです。

#### 使用方法
①LINEから **SNAP@** を友だちに追加し、操作する家電製品とそれに対応するジェスチャを選択し、学習します。（LINE_botを使用）  

②上記の要領で、複数の家電製品とジェスチャを登録できます。  

③指の「スナップ」が、WEBカメラのトリガーになります。（音声認識を使用）  

④あとは、あなたが動くだけです。あなたのジェスチャが家電製品のスイッチになります。

### 特長

#### 1. 家電製品のON/OFFをあなたのジェスチャで
従来のスマート家電は、スマートフォンアプリや音声認識などのインターフェースを使ったものが多くありますが、SNAPではジェスチャ認識を用いている点で、革新性があります。

||カテゴリー|インターフェース|直感性|操作性|コスト|
|  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |
|**S N A P**|**WEBカメラ**|**ジェスチャ認識**|**◎**|**○**|**○**|
|LINE ClovaFriendsDock|赤外線リモコン|音声認識|○|○|△|
|iRobot ルンバ|掃除機|スマートフォンアプリ|△|○|△|

#### 2. 複数の家電製品とそれに対応するジェスチャを登録
あなたの家の家電製品を直感的に操作し、それらのスイッチを一元的に管理することができます。  

①バイバイ（仮）  
![①バイバイ（仮）](/image/ByeByeHQ.gif)  
②ハンズアップ（仮）  
![②ハンズアップ（仮）](/image/HandUpHQ.gif)  
③セーフ（仮）  
![③セーフ（仮）](/image/SafeHQ.gif)

#### 3. 左右180°内で、指示された家電製品の方向へデバイスが動く

#### 4. IR送受信

### 解決出来ること
もうリモコンを探すことも、音声認識を意識して話すこともありません。  
あなたのジェスチャで、直感的に家電製品のON/OFFを操作し、それらのスイッチを一元的に管理することができます。  
SNAPは、より直感的なインターフェースとして、ジェスチャによる家電製品の操作・管理という新たな価値を提供し、人々の暮らしをより豊かにします。

### 今後の展望
#### 実装予定

- WEBカメラを複数台用いてのジェスチャ認識。  

- ららら。   


今回は、家電製品にフォーカスした開発を行いましたが、「ボディランゲージ」という言葉があるように、ジェスチャは最も直感的でシンプルなコミュニケーションの手段であると考えています。  

このジェスチャ認識の技術を、言語の壁を乗り越えた世界中の人々の更なるコミュニケーションの活性化や、ろう者のような身体の不自由な方がよりストレスなく過ごせる社会環境づくりに発展させたいと考えています。

## 開発内容・開発技術
### 活用した技術
#### API・データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

* 
* 
* 

#### フレームワーク・ライブラリ・モジュール
* OpenPose
* CUDA8
* cuDNN5.1
* LINE_bot
* さくらのレンタルサーバ
* numpy
* pyaudio
* gigpio
* wiringPi

#### デバイス
* RaspbberyPi 
* 

### 研究内容・事前開発プロダクト（任意）
ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

* 
* 


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* スナップ音の認識
* ジェスチャ（３種類）の認識
