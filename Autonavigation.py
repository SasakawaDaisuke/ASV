# 自動航行プログラム

ウェイポイント入力（リスト型にして複数の値を保持しながら帰ってこれるようにする）
for フィードバック制御
    #GPSの値取得 + コンパスの値を取得
    #進む方角取得 + 左右のスラスターの出力を決定
    if ウェイポイントとGPSの距離が〇m以内ならウェイポイントを次のに移動する（ウェイポイントがなくなったら停止）

