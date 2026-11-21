import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="AI Spam Detection",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "best_spam_detection_model.pkl"
    return joblib.load(model_path)

model = load_model()

st.title("AI Spam Detection System")
st.caption("Machine Learning-Based SMS Classification")

st.write(
    "Enter an SMS message below to check whether "
    "our trained AI model classifies it as spam "
    "or legitimate."
)

message = st.text_area(
    "SMS Message",
    placeholder="Type your message here...",
    height=150
)

if st.button("Analyze Message", type="primary"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("SPAM DETECTED")
            st.write(
                "The AI model classified this "
                "message as spam."
            )
        else:
            st.success("LEGITIMATE MESSAGE")
            st.write(
                "The AI model classified this "
                "message as legitimate."
            )

        st.caption(
            "Predictions are automated and may "
            "occasionally be incorrect."
        )

st.divider()
st.caption(
    "AI Research Project | SMS Spam Detection"
)
