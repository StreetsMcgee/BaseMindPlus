import streamlit as st
from engine import BaseMindEngine
from gpt_bridge import reflect_on_insight

st.set_page_config(page_title="BaseMind Plus", layout="centered")

st.title("BaseMind Plus — Recursive Cognition Engine")
st.markdown("Where insight becomes system, and recursion becomes action.")

engine = BaseMindEngine()
engine.load_insight_memory("logs/insight_history.json")

st.header("Input Stream")
logic_stream = st.text_input("Logic Stream (comma-separated)", value="pattern lock, loop, recursion drift")
pattern_stream = st.text_input("Pattern Stream (comma-separated)", value="loop, convergence, feedback loop")
insight = st.text_area("Insight Candidate", value="Small embodiment breaks the spiral of overthinking.")
phase = st.text_input("Phase/Context Tag", value="LIVE_RUN")

st.header("Embodiment Check")
resonance = st.radio("Did you feel the inner resonance click?", ("y", "n"))
fallacy = st.radio("Are there any logical fallacies remaining?", ("y", "n"))
pressure = st.radio("Does the insight still hold under pressure?", ("y", "n"))
action = st.text_input("Simple Action to Embody This Insight")

if st.button("Run Embodiment Trigger"):
    logic_list = [x.strip() for x in logic_stream.split(",")]
    pattern_list = [x.strip() for x in pattern_stream.split(",")]
    responses = {
        "resonance": resonance,
        "fallacy": fallacy,
        "pressure": pressure,
        "action": action
    }
    result, success = engine.embody_insight(logic_list, pattern_list, insight, responses, phase)
    st.success(result) if success else st.warning(result)

    if success:
        st.markdown("### Identity Arc Snapshot")
        top_themes, dominant_phase, dominant_theme = engine.analyze_identity_arc()
        st.write("**Top Themes:**", top_themes)
        st.write("**Dominant Phase:**", dominant_phase)
        st.write(f"**You are becoming someone who resonates with:** `{dominant_theme}`")

if st.button("Reflect Insight with GPT"):
    with st.spinner("Sending to GPT..."):
        reflection = reflect_on_insight(insight)
        st.markdown("### GPT Recursive Reflection")
        st.text(reflection)

if st.button("Export Insight Log to JSON"):
    path = engine.export_insights_to_json("logs/insight_history.json")
    st.success(f"Exported to {path}")
