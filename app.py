
import streamlit as st
import pandas as pd
from src.chatbot import FoodPreserveChatbot
from src.model import ShelfLifeModel

# Page Configuration
st.set_page_config(
    page_title="FoodPreserveBot",
    page_icon="🍏",
    layout="wide"
)

# Custom CSS for aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }
    .stChatInput {
        border-radius: 20px;
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #4CAF50; 
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    h1 {
        color: #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Chatbot and Model (Lazy load)
@st.cache_resource
def load_resources():
    bot = FoodPreserveChatbot()
    categories = bot.model_prediction.get_categories()
    return bot, categories

try:
    bot, categories = load_resources()
except ValueError as e:
    st.error(f"Configuration Error: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading resources: {e}")
    st.stop()

# Sidebar: Prediction Parameters
st.sidebar.title("Shelf Life Predictor 📊")
st.sidebar.markdown("Adjust parameters to estimate shelf life.")

selected_category = st.sidebar.selectbox("Food Category", categories)
temperature = st.sidebar.slider("Storage Temperature (°C)", -20.0, 30.0, 4.0, help="4°C is typical fridge temp, -18°C is freezer.")
ph_value = st.sidebar.slider("Acidity (pH)", 2.0, 10.0, 6.0, help="Lower pH means more acidic (e.g., Lemon=2, Water=7).")

# Calculate prediction on the fly for the sidebar
predicted_days = bot.model_prediction.predict(temperature, ph_value, selected_category)

st.sidebar.markdown("### Estimated Shelf Life")
st.sidebar.metric(label="Days", value=f"{predicted_days:.1f} days")

if predicted_days < 2:
    st.sidebar.warning("⚠️ High Risk! Consuming soon is recommended.")
elif predicted_days > 180:
    st.sidebar.success("✅ Long shelf life estimated.")

# Main Chat Interface
st.title("🍏 FoodPreserveBot")
st.markdown("ask me about food preservation techniques (Drying, Freezing, HPP) or details about your specific food!")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm FoodPreserveBot. How can I help you preserve your food today?"}
    ]

# Display Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
if prompt := st.chat_input("Ask about preservation..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Pass sidebar params as context
                response = bot.get_response(
                    prompt, 
                    temp=temperature, 
                    ph=ph_value, 
                    category=selected_category
                )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
