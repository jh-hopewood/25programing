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

# 난수 생성
random.seed(42)  # 재현성을 위한 시드 설정
find = random.randint(1, 100)
user_input = -1  # 초기값 설정

# 게임 로직
while find != user_input:
    user_input = st.number_input('숫자를 입력하세요 (1 ~ 100):', min_value=1, max_value=100, step=1)
    
    if find > user_input:
        st.warning('🔺 더 큰 수를 입력해 주세요!')
    elif find < user_input:
        st.warning('🔻 더 작은 수를 입력해 주세요!')
    else:
        st.success('🎉 정답입니다! 게임을 종료합니다.')
