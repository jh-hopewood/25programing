import streamlit as st

# 제목
st.title('🏟️ 가장 큰 운동장 찾기')

# 문제 설명
st.write('''
🏟️ **문제 설명**
- 학교 근처에 있는 3개의 운동장의 넓이를 비교하여 가장 넓은 운동장을 찾는 프로그램입니다.
- 각 운동장의 가로와 세로 길이를 입력하면 가장 넓은 운동장의 넓이를 출력합니다.
- 각 길이는 1,000 이하의 정수입니다.
''')

# 입력 필드 생성
fields = []
for i in range(1, 4):
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input(f'운동장 {i}의 가로 길이', min_value=1, max_value=1000, step=1, key=f'width_{i}')
    with col2:
        height = st.number_input(f'운동장 {i}의 세로 길이', min_value=1, max_value=1000, step=1, key=f'height_{i}')
    fields.append(width * height)

# 가장 넓은 운동장 계산 및 출력
if st.button('가장 큰 운동장 찾기'):
    max_area = max(fields)
    st.success(f'가장 큰 운동장의 넓이는 **{max_area}**입니다.')
