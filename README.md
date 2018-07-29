# Scanner01

カメラ画像から矩形検出と顔認識を行うコード

scanner01.pyの説明

opencvを用いてカメラで取得した画像に次の3つの画像処理を行った。

1. 射影変換をして矩形検出

2. 顔認識

3. BGR色調の各色の調整


使い方

名刺等の長方形の形をしたものをカメラに写す。

矩形の検出結果を表示する緑色の枠、顔の検出結果を表示する白色の枠が表示される。

好みで色を変えて、キーボード入力で画像を保存。

3はスイッチをON(1)にしてトラックバーを操作してパラメータを変えられる。

終了はqを入力。

依存ライブラリとバージョン

Opencv cv2 や from numpy 

Opencvバージョン:'3.4.1'

参考文献1(スイッチのコードで参考)

https://sites.google.com/site/lifeslash7830/home/hua-xiang-chu-li/opencvniyoruhuaxiangchulitorakkubatoka?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1

参考文献2(射影変換)
https://qiita.com/mix_dvd/items/5674f26af467098842f0

参考文献3(顔認識)

https://gist.github.com/kurozumi/04a75695dc32c46586be0d69e6a8243f

参考文献4(顔をトリミングして保存)

http://famirror.hateblo.jp/entry/2015/12/19/180000



実行の様子

youtube: https://youtu.be/-4XYudxH7k4

