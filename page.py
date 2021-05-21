import streamlit as st

st.set_page_config(page_title='McDonald EDA', page_icon = "https://img.icons8.com/color/452/mcdonalds.png", layout = 'wide', initial_sidebar_state = 'expanded')

with st.sidebar:
    st.image(
        "https://img.icons8.com/color/452/mcdonalds.png",
        width=300,
    )
    st.markdown("# Mcdonald EDA")
    st.markdown("## 맥도날드 데이터셋을 사용한 EDA 프로젝트")
    st.markdown("[Github Repo](https://github.com/Team-M1/M1_macdonald_EDA)")

st.markdown("# Mcdonald EDA")