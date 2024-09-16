# 2024/09/13 TeamTrashBox

import streamlit as st
import torch
from PIL import Image
import numpy as np
import io

# YOLOv5モデルの読み込み
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Streamlit UIの設定
st.title("YOLOv5物体検出アプリ")

# ユーザーに画像をアップロードさせる
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # アップロードされた画像を読み込む
    image = Image.open(uploaded_file)

    # 画像を表示
    st.image(image, caption='アップロードされた画像', use_column_width=True)

    # YOLOv5で物体検出を行う
    st.write("物体検出中...")

    # 画像をYOLOv5が扱える形式に変換
    img_array = np.array(image)

    # YOLOv5で検出
    results = model(img_array)

    # 検出結果の描画
    results_img = results.render()[0]  # 結果を描画した画像を取得

    # 検出結果の画像を表示
    st.image(results_img, caption="物体検出結果", use_column_width=True)

    # 検出された物体をテキストで表示
    st.write("検出された物体:", results.pandas().xyxy[0])
