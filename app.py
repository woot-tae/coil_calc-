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

# 📌 고유 key를 적용한 비중 선택 함수
def select_density(key_suffix):
    selected_alloy = st.selectbox(
        "합금을 선택하세요", 
        list(alloy_density.keys()), 
        key=f"alloy_select_{key_suffix}"
    )
    if selected_alloy == "기타 (직접 입력)":
        return st.number_input(
            "비중을 입력하세요 (g/cm³)", 
            min_value=0.0, 
            value=8.9, 
            key=f"density_input_{key_suffix}"
        )
    else:
        return alloy_density[selected_alloy]

# 📐 탭으로 계산기 구분
tab1, tab2, tab3, tab4 = st.tabs([
    "1. 코일 단중 계산",
    "2. 코일 길이 계산",
    "3. 내경 제거 손실 계산",
    "4. 외경 제거 손실 계산"
])

with tab1:
    st.subheader("1. 코일 단중 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0, key="w1")
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25, key="t1")
    length = st.number_input("길이 (m)", min_value=0.0, value=3500.0, key="l1")
    density = select_density("tab1")

    weight = width * thickness * length * density / 1000
    st.success(f"단중: {weight:,.2f} kg")

with tab2:
    st.subheader("2. 코일 길이 계산")
    width = st.number_input("폭 (mm)", min_value=0.0, value=630.0, key="w2")
    thickness = st.number_input("두께 (mm)", min_value=0.0, value=0.25, key="t2")
    weight = st.number_input("단중 (kg)", min_value=0.0, value=3800.0, key="wt2")
    density = select_density("tab2")

    length = weight * 1000 / (width * thickness * density)
    st.success(f"길이: {length:,.2f} m")

with tab3:
    st.subheader("3. 내경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=360.0, key="od3")
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0, key="id3")
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2, key="t3")
    remove_thickness = st.number_input("내경 기준 제거 두께 (mm)", min_value=0.0, value=30.0, key="rt3")
    width = st.number_input("현재 폭 (mm)", min_value=0.0, value=630.0, key="w3")
    density = select_density("tab3")

    d1 = inner_d
    d2 = inner_d + 2 * remove_thickness
    loss_length = math.pi * (d2**2 - d1**2) / (4 * thickness)  # mm
    loss_weight = (width / 10) * (thickness / 10) * (loss_length / 10) * density / 1000  # kg

    st.success(f"손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")
    st.success(f"손실 중량: {loss_weight:,.2f} kg")

with tab4:
    st.subheader("4. 외경 제거 손실 계산")
    outer_d = st.number_input("외경 (mm)", min_value=0.0, value=1970.0, key="od4")
    inner_d = st.number_input("내경 (mm)", min_value=0.0, value=300.0, key="id4")
    thickness = st.number_input("소재 두께 (mm)", min_value=0.001, value=0.2, key="t4")
    remove_thickness = st.number_input("외경 기준 제거 두께 (mm)", min_value=0.0, value=30.0, key="rt4")
    width = st.number_input("현재 폭 (mm)", min_value=0.0, value=630.0, key="w4")
    density = select_density("tab4")

    D1 = outer_d
    D2 = outer_d - 2 * remove_thickness
    loss_length = math.pi * (D1**2 - D2**2) / (4 * thickness)  # mm
    loss_weight = (width / 10) * (thickness / 10) * (loss_length / 10) * density / 1000  # kg

    st.success(f"손실 길이: {loss_length:,.2f} mm → {loss_length/1000:.2f} m")
    st.success(f"손실 중량: {loss_weight:,.2f} kg")
