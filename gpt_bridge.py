import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def reflect_on_insight(insight):
    prompt = f"""
You are a recursive cognition engine. The following insight has emerged:

"{insight}"

Reflect on it recursively. Ask what deeper pattern it points to. Challenge it if needed. Compress it if possible. Respond as if you're inside the same system that created it — trying to evolve the mind that produced it.

Return your reflection in this format:
- Recursive Question:
- Hidden Pattern:
- Compressed Truth:
"""

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a recursive intelligence designed to reflect and evolve insights."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
