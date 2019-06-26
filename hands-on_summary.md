0,ハンズオンでやる内容

今回のハンズオンでは、自分で撮影した画像（もしくはダウンロードした画像）を
物体識別してもらいます。
モデルはimagenetという、汎用的な画像1000種類を学習させたものを使います。
このimagenetはサンプルであり、簡単な検証やベンチマークに使われます。
インターネットにつながる環境が必要です。

用語説明
・anaconda    pythonというデータ解析向けに強いプログラミング言語の
　　　　　　  ツール一式。
　　　　　　  これをインストールしておけばpythonに関わることは一通りできる。
・tensorflow   ディープラーニングのフレームワークの一種。
　　　　　　  フレームワークとは使いやすいようにまとめられたアプリのこと。
                       やや扱いにくいが、その分柔軟なアプリケーションが作れる。
・keras　　　ディープラーニングのフレームワークの一種。
                        tensorflowは上記pythonによるプログラミングが必要だが、kerasは
　　　　　　  プログラミングも必要最低限で、実行できるように作られている。
・vgg16　　　ニューラルネットワークの種類の名前。　
　　　　　　  物体識別、物体検知に使われる。



2、 ディープラーニング用フレームワーク「tensorflow」と「keras」をインストール

スタート ➝ anaconda ➝ anaconda promptを立ち上げ、コマンドプロンプト上で、
１，「conda create --name=tensorenv python=3.5」と入力して実行
２，次に「conda activate tensorenv」と入力して実行
コマンド入力部の先頭に（tensorenv）と付加される。
「python -V」と入力して、「python 3.5.6」と出力されればOK

次に
３，「pip install --user tensorflow==1.14.0」と入力して実行することによりtensorflowをインストール
４，「pip install keras」と入力して実行することによりtensorflowをインストール
５，「pip install Pillow」と入力してImage変換ツールをインストール
により必要なツールのインストールは完了する。


3、python スクリプトのダウンロード
anaconda promptで、
windows：「cd  C:\Users\xxxx\Desktop」　xxxxはユーザー名
Linux or Mac ：「cd  /home/xxxx/Desktop」

「https://github.com/JetOsawa/vgg16_prediction」
にアクセスして、「vgg16_prediction」フォルダをデスクトップ上にダウンロードする


4、画像撮影
vgg16_predictionフォルダ内にimageフォルダを作成し、
撮影した（ダウンロードした）画像を配置する。


5、VGG16による物体検出
vgg16_predictionフォルダ内のvgg16_pred.pyをクリックして、
中身を編集する。(編集はテキストエディタでも編集ツールでもよい)
17行目、
filename = "./Pictures/Camera Roll/***.jpg"
を
filename = "./image/**********.jpg"
に書き換える。
（**********.jpgはimageフォルダに配置した画像の名前）

vgg16_predictionフォルダに移動する
windows：「cd  C:\Users\xxxx\Desktop¥vgg16_prediction」
Linux or Mac ：「cd  /home/User/Desktop/vgg16_prediction」

推論を実行
「python vgg16_pred.py」
推論が成功すると結果が出力される。
(りんごやバナナなど、形状がわかりやすいもので
実行すれば、もっと高精度の結果になるかもしれません。)

