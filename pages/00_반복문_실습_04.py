import streamlit as st
import random

# 제목
st.title('🎯 숫자 맞추기 게임')

# 게임 설명
st.write('''
🔢 **게임 설명**
- 프로그램이 랜덤하게 선택한 숫자를 맞추는 게임입니다.
- 1부터 100 사이의 숫자를 맞출 때까지 시도할 수 있습니다.
- 더 큰 수 또는 더 작은 수를 입력하라는 힌트가 제공됩니다.
''')

# 난수 및 상태 초기화
if 'find' not in st.session_state:
    st.session_state.find = random.randint(1, 100)

if 'hints' not in st.session_state:
    st.session_state.hints = []

if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 입력 처리
if not st.session_state.game_over:
    user_input = st.number_input('숫자를 입력하세요 (1 ~ 100):', min_value=1, max_value=100, step=1)

    if st.button('입력하기'):
        if user_input == st.session_state.find:
            st.success(f'🎉 정답입니다! 게임을 종료합니다. ({user_input})')
            st.session_state.game_over = True
        elif user_input < st.session_state.find:
            hint = f"🔺 {user_input}보다 큰 수를 입력해 주세요!"
            st.session_state.hints.append(hint)
        elif user_input > st.session_state.find:
            hint = f"🔻 {user_input}보다 작은 수를 입력해 주세요!"
            st.session_state.hints.append(hint)

# 힌트 출력
if st.session_state.hints:
    st.write("### 📝 힌트 기록")
    for h in st.session_state.hints:
        st.write(h)

# 게임 다시 시작 버튼
if st.session_state.game_over or st.button('게임 다시 시작'):
    st.session_state.find = random.randint(1, 100)
    st.session_state.hints = []
    st.session_state.game_over = False
    st.experimental_rerun()
