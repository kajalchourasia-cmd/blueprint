import streamlit as st
from blueprint.schemas import UserProfile
from blueprint.state import reset

st.set_page_config(page_title="Questions · Blueprint", page_icon="📝")
reset(); st.session_state.setdefault("answers", {})
questions = st.session_state["answers"]
idx = st.session_state["question_index"]
st.progress((idx + 1) / 7, text=f"Question {idx + 1} of 7")
st.title("Build your context")
idea = st.session_state.get("idea", "")
if idx == 0: questions["idea"] = st.text_area("Confirm your idea", value=questions.get("idea", idea), height=150)
elif idx == 1: questions["idea_type"] = st.selectbox("What type is it?", ["physical_business","retail_store","service","saas","ai_product","marketplace","creator","consumer_product","other"], index=0)
elif idx == 2:
    questions["location"] = st.text_input("Where does it operate?", value=questions.get("location", "")); questions["online"] = st.checkbox("Online / anywhere")
elif idx == 3: questions["background"] = st.text_area("Tell me about you", value=questions.get("background", ""), placeholder="Current job, top 3 skills, biggest past project", height=150)
elif idx == 4: questions["life_context"] = st.multiselect("Life context", ["Full-time job", "Caregiving", "School", "Debt or financial pressure", "Health constraint", "Relocation", "Need predictable income"])
elif idx == 5: questions["goal"] = st.radio("Your goal", ["get_job","side_income","small_business","startup","raise_money","just_explore"])
else:
    questions["hours_per_week"] = st.slider("Hours per week", 0, 40, questions.get("hours_per_week", 5)); questions["money_available"] = st.slider("Money available ($)", 0, 500000, questions.get("money_available", 500), step=500)
    st.caption("These are constraints for the first path, not a judgment.")
c1, c2 = st.columns(2)
with c1:
    if st.button("← Back", disabled=idx == 0): st.session_state["question_index"] -= 1; st.rerun()
with c2:
    label = "Build my plan →" if idx == 6 else "Next →"
    if st.button(label, type="primary", use_container_width=True):
        if idx < 6: st.session_state["question_index"] += 1; st.rerun()
        else:
            location = "Online / anywhere" if questions.get("online") else questions.get("location", "")
            try:
                st.session_state["profile"] = UserProfile(idea=questions["idea"], idea_type=questions["idea_type"], location=location, background=questions["background"], life_context=questions["life_context"], goal=questions["goal"], hours_per_week=questions["hours_per_week"], money_available=questions["money_available"])
                st.switch_page("pages/2_🗺️_Your_Plan.py")
            except Exception as e: st.error(f"Please complete the question before continuing: {e}")

