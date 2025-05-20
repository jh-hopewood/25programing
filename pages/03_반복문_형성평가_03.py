import streamlit as st

def display_multiplication_table(max_num):
    table = ""
    for i in range(2, max_num + 1):
        for j in range(1, 10):
            table += f"{i} × {j} = {i * j}  \t"
            if j % 5 == 0:
                table += "\n"
        table += "\n"
    return table

# 웹앱 제목
st.title("📊 형성평가2. 구구단 출력하기")

# 문제 제시
st.subheader("📝 문제 제시")
st.write("10이하 양의 정수를 입력 받아, 2단부터 입력 받은 수까지의 구구단을 출력하세요.")

# 입력 조건
st.subheader("📌 입력 조건")
st.write("1이상 10이하의 정수")

# 출력 조건
st.subheader("📌 출력 조건")
st.write("2부터 입력받은 정수까지의 구구단을 화면 출력")

# 사용자 입력
st.subheader("🖋️ 입력")
max_num = st.number_input("2부터 10까지의 정수를 입력하세요:", min_value=2, max_value=10, step=1)

# 출력 결과
if st.button("출력하기"):
    st.subheader("📤 출력 결과")
    result = display_multiplication_table(max_num)
    st.text_area("구구단 출력", value=result, height=300)
