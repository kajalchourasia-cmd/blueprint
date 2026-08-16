import streamlit as st
import plotly.graph_objects as go
from blueprint.state import reset
from blueprint.reality_check import generate as generate_reality
from blueprint.plan_generator import generate as generate_plan
from blueprint.cost_calculator import compute_initial, mark_done, add_delta
from blueprint.gap_generator import generate as generate_gap
from blueprint.coach import chat

st.set_page_config(page_title="Your Plan · Blueprint", page_icon="🗺️", layout="wide")
reset()
profile = st.session_state.get("profile")
if not profile: st.switch_page("app.py")
if "reality" not in st.session_state:
    with st.spinner("Reading founder journeys similar to yours..."):
        st.session_state["reality"] = generate_reality(profile); st.session_state["plan"] = generate_plan(profile); st.session_state["ledger"] = compute_initial(st.session_state["plan"])
reality, plan, ledger = st.session_state["reality"], st.session_state["plan"], st.session_state["ledger"]
left, right = st.columns([7, 3], gap="large")
with left:
    st.title(profile.idea); st.caption(f"Goal: {profile.goal.replace('_',' ').title()}  ·  {plan.total_estimated_days} day estimated path")
    with st.expander("Reality Check", expanded=True):
        st.metric("Fit signal", f"{reality.fit_score}/10", reality.fit_rationale)
        a,b,c = st.columns(3)
        a.markdown("**Unfair advantages**\n\n" + "\n".join(f"- {x}" for x in reality.unfair_advantages))
        b.markdown("**Critical gaps**\n\n" + "\n".join(f"- {x}" for x in reality.critical_gaps))
        c.markdown("**Specific delusions**")
        for d in reality.specific_delusions: st.warning(f"You believe: {d['belief']} · Reality: {d['reality']}")
    st.header("Your Plan")
    for step in plan.steps:
        with st.expander(f"{step.number}. {step.name} · {step.estimated_time_days} days · ${step.estimated_cost_dollars}"):
            st.write(step.what_to_do); st.caption(step.why_it_matters); st.markdown("**Resources**\n" + "\n".join(f"- {r}" for r in step.resources)); st.markdown(f"**Done when:** {step.done_criteria}")
            done = st.checkbox("Mark done", key=f"done_{step.number}")
            if done and step.number not in st.session_state["done_steps"]: st.session_state["done_steps"].add(step.number); st.session_state["ledger"] = mark_done(step, ledger); st.rerun()
            cols = st.columns(3)
            for col, layer, label in zip(cols, ["unseen","missing_voice","real_cost"], ["👁️ The Unseen","🎙️ Missing Voice","💰 Real Cost"]):
                if col.button(label, key=f"{layer}_{step.number}"):
                    st.session_state["gaps"].setdefault(step.number, {})[layer] = generate_gap(step, layer, profile)
            for layer, gap in st.session_state["gaps"].get(step.number, {}).items():
                st.markdown(f"**{layer.replace('_',' ').title()}**\n\n{gap.content}")
                if gap.ledger_delta: st.session_state["ledger"] = add_delta(st.session_state["ledger"], gap.ledger_delta)
    with st.expander("💬 Talk to Blueprint", expanded=False):
        for msg in st.session_state["chat"]: st.chat_message(msg["role"]).write(msg["content"])
        q1,q2,q3 = st.columns(3)
        for col, label, prompt in [(q1,"🎯 Weekend Test","Weekend test"),(q2,"👥 First 10 Users","First 10 users"),(q3,"🧠 Get unstuck","I am stuck")]:
            if col.button(label): st.session_state["chat"].append({"role":"user","content":prompt}); st.session_state["chat"].append({"role":"assistant","content":chat(prompt,profile,plan,st.session_state["ledger"],st.session_state["chat"])}); st.rerun()
        if message := st.chat_input("Ask about your next move"):
            st.session_state["chat"].append({"role":"user","content":message}); st.session_state["chat"].append({"role":"assistant","content":chat(message,profile,plan,st.session_state["ledger"],st.session_state["chat"])}); st.rerun()
with right:
    st.subheader("Real Cost Ledger")
    st.metric("Projected 3-year total", f"${ledger.projected_3yr_total:,}")
    st.write(f"Cash: ${ledger.cash_dollars:,}\n\nHours: {ledger.hours_invested}\n\nRelationships: {ledger.relationship_impact_days} days\n\nHealth: {ledger.health_impact_score}\n\nCareer opportunity cost: ${ledger.opportunity_cost_dollars:,}")
    fig = go.Figure(go.Bar(x=["Cash", "Opportunity"], y=[ledger.cash_dollars, ledger.opportunity_cost_dollars], marker_color=["#B45309", "#78716C"]))
    fig.update_layout(height=220, margin=dict(l=0,r=0,t=10,b=0), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

