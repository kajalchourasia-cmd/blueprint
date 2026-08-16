import streamlit as st
from blueprint.state import reset

st.set_page_config(page_title="Blueprint", page_icon="⌖", layout="centered")
reset()
st.markdown("<style>main .block-container{max-width:650px;padding-top:12vh} .stButton button{border-radius:8px}</style>", unsafe_allow_html=True)
st.caption("BLUEPRINT")
st.title("You have an idea. Blueprint gives you the shortest honest path to make it real.")
st.write("No cheerleading. No scores. Just the plan, the true cost, and the truths every founder misses.")
idea = st.text_area("What's your idea?", value=st.session_state.get("idea", ""), placeholder="e.g., I want to open a specialty coffee shop in Austin", height=130)
if st.button("Get my plan →", type="primary", use_container_width=True):
    if idea.strip():
        st.session_state["idea"] = idea.strip(); st.switch_page("pages/1_📝_Questions.py")
    else: st.warning("Enter the idea you want to test.")

