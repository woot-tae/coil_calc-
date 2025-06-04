import streamlit as st
import math

st.set_page_config(page_title="코일 계산기", layout="centered")
st.title("📦 압연 코일 계산기")

# 🧪 합금 비중 데이터
alloy_density = {
    "OFC": 8.94,
    "T/P": 8.91,
    "DLP": 8.94,
    "RB": 8.8,
    "B1": 8.53,
    "BA": 8.47,
    "B2": 8.44,
    "B3": 8.39,
    "PB1": 8.86,
    "PB2": 8.83,
    "PBSS": 8.78,
    "키양백": 8.7,
    "P102": 8.91,
    "P90": 8.9,
    "P194": 8.91,
    "P425": 8.78,
    "P26": 8.9,
    "P1000": 8.89,
    "P70": 8.82,
    "기타 (직접 입력)": None
}

menu = st.sidebar.selectbox("계산기 종류를 선택하세요", [
    "1. 코일 단중 계산", 
    "2. 코일 길이 계산", 
    "3. 내경 제거 손실 계산", 
    "4. 외경 제거 손실 계산"
])

# 📌 공통 비중 선택 함수
def select_density():
    selected_alloy = st.selectbox("합금을 선택하세요", list(alloy_density.keys()))
    if selected_alloy == "기타 (직접 입력)":
        return st.number_input("비중을 입력하세요 (g/cm³)", min_value=0.0, value=8.9)
    else:
        return alloy_density[selected_alloy]

if menu == "1. 코일 단중 계산":
    st.header("1. 코일 단중 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0)
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25)
    length = st.number_input("길이 (m)", min_value=0.0, value=3500.0)
    density = select_density()

    weight = width * thickness * length * density / 1000
    st.success(f"단중: {weight:,.2f} kg")

elif menu == "2. 코일 길이 계산":
    st.header("2. 코일 길이 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0)
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25)
    weight = st.number_input("단중 (kg)", min_value=0.0, value=3800.0)
    density = select_density()

    length = weight * 1000 / (width * thickness * density)
    st.success(f"길이: {length:,.2f} m")

elif menu == "3. 내경 제거 손실 계산":
    st.header("3. 내경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=360.0)
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0)
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2)
    remove_thickness = st.number_input("내경 기준 제거 두께 (mm)", min_value=0.0, value=30.0)
    width = st.number_input("현재 폭 (mm)", min_value=0.0, value=630.0)
    density = select_density()

    d1 = inner_d
    d2 = inner_d + 2 * remove_thickness
    loss_length = math.pi * (d2**2 - d1**2) / (4 * thickness)  # mm
    loss_weight = (width / 10) * (thickness / 10) * (loss_length / 10) * density / 1000  # kg

    st.success(f"손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")
    st.success(f"손실 중량: {loss_weight:,.2f} kg")

elif menu == "4. 외경 제거 손실 계산":
    st.header("4. 외경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=1970.0)
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0)
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2)
    remove_thickness = st.number_input("외경 기준 제거 두께 (mm)", min_value=0.0, value=30.0)
    width = st.number_input("현재 폭 (mm)", min_value=0.0, value=630.0)
    density = select_density()

    D1 = outer_d
    D2 = outer_d - 2 * remove_thickness
    loss_length = math.pi * (D1**2 - D2**2) / (4 * thickness)  # mm
    loss_weight = (width / 10) * (thickness / 10) * (loss_length / 10) * density / 1000  # kg

    st.success(f"손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")
    st.success(f"손실 중량: {loss_weight:,.2f} kg")
