import streamlit as st
import pandas as pd
import plotly.express as px

# データの読み込み（例として、CSVファイルから読み込む場合
df = pd.read_csv('.venv/data.csv', encoding='sjis')

# NaN値を列の平均値で置換
df = df.fillna(df.mean(numeric_only=True))
df['年月日'] = pd.to_datetime(df['年月日'], dayfirst=False)

# Streamlitアプリケーションの設定
st.title("三木市の過去の天気")

# グラフの色を指定
colors = ['orange', 'blue']

# 折れ線グラフの描画
fig = px.line(df, x='年月日', y=['最大風速(m/s)', '10分間降水量の最大(mm)'],
              title='雨量の折れ線グラフ', color_discrete_sequence=colors)
st.plotly_chart(fig)

# ユーザーに日付を入力させる
selected_date = st.date_input("日付を選択してください(2021/06/27~2024/06/17)", pd.to_datetime('2021-06-27'))

# 入力された日付に対応するデータを検索
selected_date_str = selected_date.strftime('%Y-%m-%d')
selected_data = df[df['年月日'] == selected_date_str]

# 検索結果を表示
if not selected_data.empty:
    st.write(f"### {selected_date_str} の気象データ")
    st.write(f"最大風速: {selected_data['最大風速(m/s)'].values[0]} m/s")
    st.write(f"10分間降水量の最大: {selected_data['10分間降水量の最大(mm)'].values[0]} mm")
    st.write(f"平均気温: {selected_data['平均気温(℃)'].values[0]} ℃")
    st.write(f"最高気温: {selected_data['最高気温(℃)'].values[0]} ℃")
    st.write(f"最低気温: {selected_data['最低気温(℃)'].values[0]} ℃")
else:
    st.write("選択された日付のデータは存在しません。")
