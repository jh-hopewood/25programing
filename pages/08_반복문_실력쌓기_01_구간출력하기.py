import streamlit as st

def main():
    st.title('구간의 수 출력하기')
    st.write('두 수를 입력하여 해당 범위의 모든 정수를 출력하는 프로그램입니다.')
    
    # 사용자 입력
    a = st.number_input('첫 번째 수를 입력하세요:', min_value=1, max_value=100, step=1)
    b = st.number_input('두 번째 수를 입력하세요:', min_value=1, max_value=100, step=1)
    
    # 숫자 순서 정리
    if a > b:
        a, b = b, a
        st.write(f'입력 순서가 바뀌어 {a}부터 {b}까지 출력합니다.')
    
    # 범위 출력
    if st.button('출력하기'):
        numbers = ' '.join(map(str, range(a, b+1)))
        st.text_area('출력 결과:', numbers)

if __name__ == '__main__':
    main()
