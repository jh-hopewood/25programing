import streamlit as st

def draw_triangle(n):
    triangle = ""
    for i in range(1, n + 1):
        triangle += "*" * i + "\n"
    return triangle

st.title("🔺 삼각형 모양 출력하기")

st.write("10 이하의 양의 정수를 키보드로 입력 받고, 그 수를 참고하여 삼각형을 그리세요.")

# 예시 출력
example_1 = draw_triangle(3)
example_2 = draw_triangle(6)

st.subheader("입출력 예시")
col1, col2 = st.columns(2)
with col1:
    st.text_area("입력: 3", example_1, height=100)
with col2:
    st.text_area("입력: 6", example_2, height=200)

# 입력 및 출력
n = st.number_input("1에서 10 사이의 정수를 입력하세요:", min_value=1, max_value=10, step=1)

if st.button("삼각형 그리기"):
    triangle_shape = draw_triangle(n)
    st.text_area("출력", triangle_shape, height=200)
