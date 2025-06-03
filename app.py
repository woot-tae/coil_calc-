import streamlit as st
import math

st.set_page_config(page_title="코일 계산기", layout="centered")
st.title("📦 압연 코일 계산기")

menu = st.sidebar.selectbox("계산기 종류를 선택하세요", [
    "1. 코일 단중 계산", 
    "2. 코일 길이 계산", 
    "3. 내경 제거 손실 계산", 
    "4. 외경 제거 손실 계산"])

if menu == "1. 코일 단중 계산":
    st.header("1. 코일 단중 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0)
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25)
    length = st.number_input("길이 (m)", min_value=0.0, value=3500.0)
    density = st.number_input("비중 (g/cm³)", min_value=0.0, value=8.9)

    weight = width * thickness * length * density / 1000
    st.success(f"단중: {weight:,.2f} kg")

elif menu == "2. 코일 길이 계산":
    st.header("2. 코일 길이 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0)
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25)
    weight = st.number_input("단중 (kg)", min_value=0.0, value=3800.0)
    density = st.number_input("비중 (g/cm³)", min_value=0.0, value=8.9)

    length = weight * 1000 / (width * thickness * density)
    st.success(f"길이: {length:,.2f} m")

elif menu == "3. 내경 제거 손실 계산":
    st.header("3. 내경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=360.0)
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0)
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2)
    remove_thickness = st.number_input("내경 기준 제거 두께 (mm)", min_value=0.0, value=30.0)

    d1 = inner_d
    d2 = inner_d + 2 * remove_thickness
    loss_length = math.pi * (d2**2 - d1**2) / (4 * thickness)
    st.success(f"제거 손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")

elif menu == "4. 외경 제거 손실 계산":
    st.header("4. 외경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=1970.0)
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0)
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2)
    remove_thickness = st.number_input("외경 기준 제거 두께 (mm)", min_value=0.0, value=30.0)

    D1 = outer_d
    D2 = outer_d - 2 * remove_thickness
    loss_length = math.pi * (D1**2 - D2**2) / (4 * thickness)
    st.success(f"제거 손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")
