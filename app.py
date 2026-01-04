import streamlit as st

st.title("🎂 ケーキデコレーション")

st.write("自分だけのケーキを作ろう！")

cake_type = st.radio(
    "ケーキの種類",
    ["チョコレートケーキ 🍫", "いちごケーキ 🍓", "チーズケーキ 🧀"]
)

st.write("### トッピングをえらんでね！")

topping1 = st.checkbox("いちご 🍓")
topping2 = st.checkbox("チョコレート 🍫")
topping3 = st.checkbox("クリーム 🍦")
topping4 = st.checkbox("キャンディ 🍬")
topping5 = st.checkbox("ほし ⭐")

candle = st.slider("ろうそくの数", 0, 10, 5)

if st.button("ケーキかんせい！🎉"):
    st.success("✨ ステキなケーキができたよ！ ✨")
    st.write(f"## {cake_type}")
    
    toppings = []
    if topping1:
        toppings.append("🍓")
    if topping2:
        toppings.append("🍫")
    if topping3:
        toppings.append("🍦")
    if topping4:
        toppings.append("🍬")
    if topping5:
        toppings.append("⭐")
