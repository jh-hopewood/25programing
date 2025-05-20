import streamlit as st


def display_multiplication_table(max_num):
    result = []
    for i in range(1, 10):
        row = []
        for j in range(2, max_num + 1):
            row.append(f"{j} × {i} = {j * i}")
        result.append("  \t".join(row))
    return "\n".join(result)


def example_output():
    examples = {
        5: [
            "2 × 1 = 2\t3 × 1 = 3\t4 × 1 = 4\t5 × 1 = 5",
            "2 × 2 = 4\t3 × 2 = 6\t4 × 2 = 8\t5 × 2 = 10",
            "...",
            "2 × 9 = 18\t3 × 9 = 27\t4 × 9 = 36\t5 × 9 = 45",
        ],
        7: [
            "2 × 1 = 2\t3 × 1 = 3\t4 × 1 = 4\t5 × 1 = 5\t6 × 1 = 6\t7 × 1 = 7",
            "2 × 2 = 4\t3 × 2 = 6\t4 × 2 = 8\t5 × 2 = 10\t6 × 2 = 12\t7 × 2 = 14",
            "...",
            "2 × 9 = 18\t3 × 9 = 27\t4 × 9 = 36\t5 × 9 = 45\t6 × 9 = 54\t7 × 9 = 63",
        ],
    }
    return examples


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

# 입력 양식
st.subheader("🖋️ 입력")
max_num = st.number_input("2부터 10까지의 정수를 입력하세요:", min_value=2, max_value=10, step=1)

# 출력 결과
if st.button("출력하기"):
    st.subheader("📤 출력 결과")
    result = display_multiplication_table(max_num)
    st.text_area("구구단 출력", value=result, height=300)

# 출력 예시
st.subheader("📝 출력 예시")
examples = example_output()
for key, lines in examples.items():
    st.write(f"예시 {key} 입력:")
    for line in lines:
        st.text(line)
    st.write("\n")
