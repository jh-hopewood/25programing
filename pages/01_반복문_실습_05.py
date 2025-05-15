import streamlit as st

# 제목
st.title('📝 0 입력될 때까지 숫자 더하기')

# 문제 설명
st.write('''
🔢 **문제 설명**
- 0이 입력될 때까지 사용자가 입력한 숫자를 모두 더하는 프로그램입니다.
- 0을 입력하면 합계를 출력하고 프로그램이 종료됩니다.
''')

# 합계 초기화
if 'sum' not in st.session_state:
    st.session_state.sum = 0

# 숫자 입력 받기
num = st.number_input('숫자를 입력하세요 (0 입력 시 종료):', step=1, key='num_input')

# 버튼으로 입력 처리
if st.button('입력하기'):
    if num != 0:
        st.session_state.sum += num
        st.info('입력되었습니다.')
    else:
        st.success(f'최종 합계는 **{st.session_state.sum}**입니다.')
        # 합계 초기화
        st.session_state.sum = 0
