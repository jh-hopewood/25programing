import streamlit as st

# App Title
st.title("📊 형성평가 1. 1부터 ?까지 합 계산하기")

# Input Section
number = st.number_input("🔢 10이상 100이하의 정수를 입력하세요:", min_value=10, max_value=100, step=1)

# Calculate and Display Sum
if number > 0:
    total_sum = sum(range(1, number + 1))
    st.write(f"🎯 **결과:** 1부터 {number}까지의 합은 **{total_sum}**입니다.")

# Example Table
st.subheader("📝 입력 예시")
example_data = {
    "예시번호": [1, 3],
    "입력": [10, 100],
    "출력": [sum(range(1, 11)), sum(range(1, 101))],
    "비고": ["", ""]
}
st.table(example_data)
