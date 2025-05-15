import streamlit as st
import random

# 제목

st.title('🎯 숫자 맞추기 게임')

# 게임 설명

st.write('''
🔢 **게임 설명**

* 프로그램이 랜덤하게 선택한 숫자를 맞추는 게임입니다.
* 1부터 100 사이의 숫자를 맞출 때까지 시도할 수 있습니다.
* 더 큰 수 또는 더 작은 수를 입력하라는 힌트가 제공됩니다.
  ''')

# 난수 생성 (세션 상태를 사용하여 매번 다른 숫자)

if 'find' not in st.session\_state:
st.session\_state.find = random.randint(1, 100)

# 사용자 입력 받기

user\_input = st.number\_input('숫자를 입력하세요 (1 \~ 100):', min\_value=1, max\_value=100, step=1)

# 버튼 추가

if st.button('입력하기'):
if user\_input == st.session\_state.find:
st.success('🎉 정답입니다! 게임을 종료합니다.')
\# 새로운 난수 생성 옵션
if st.button('게임 다시 시작'):
st.session\_state.find = random.randint(1, 100)
st.experimental\_rerun()
elif user\_input < st.session\_state.find:
st.warning('🔺 더 큰 수를 입력해 주세요!')
elif user\_input > st.session\_state.find:
st.warning('🔻 더 작은 수를 입력해 주세요!')
