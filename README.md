# 🍏 FoodPreserveBot

**FoodPreserveBot** is an intelligent AI-powered assistant designed to guide users on food preservation techniques and predict the shelf life of various food products. It combines a **Random Forest Machine Learning model** for scientific shelf-life estimation with **Groq's Llama 3 LLM** for interactive educational dialogue.

## ✨ Features

-   **🧠 Intelligent Chatbot**: Ask questions about preservation methods like Drying, Freezing, Fermentation, and new technologies like High-Pressure Processing. Powered by **Groq API**.
-   **📊 Shelf Life Predictor**: A Machine Learning model estimates shelf life based on **Food Category**, **Temperature**, and **pH**.
    -   *Example*: Calculate how long milk lasts at 20°C vs 4°C.
-   **📚 Knowledge Base**: Built-in scientific context on preservation principles.
-   **🎨 Interactive UI**: A clean, modern web interface built with **Streamlit**.

## 🛠️ Tech Stack

-   **Language**: Python 3.10+
-   **Interface**: [Streamlit](https://streamlit.io/)
-   **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (Random Forest Regressor)
-   **LLM API**: [Groq](https://groq.com/) (Llama-3.3-70b-versatile)
-   **Data Processing**: Pandas, NumPy

## 🚀 Setup & Installation

1.  **Clone the Repository** (or navigate to the project folder):
    ```bash
    cd biosafety-el
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Groq API Key:
    ```env
    GROQ_API_KEY=gsk_your_groq_api_key_here
    ```

4.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

```
biosafety-el/
├── app.py                 # Main Streamlit application entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API Keys)
├── data/
│   └── food_data.csv      # Curated dataset (pH, Temp, Shelf Life)
└── src/
    ├── __init__.py
    ├── chatbot.py         # Llama 3 integration & Thread logic
    ├── model.py           # Random Forest ML Model definition
    └── knowledge_base.py  # Static dictionary of preservation techniques
```

## 🤖 Usage

1.  **Sidebar**: Use the sliders to set **Temperature** and **pH**, and select a **Food Category**. The estimated shelf life will update instantly.
2.  **Chat**: Type questions like *"How does pickling work?"* or *"Is my predicted shelf life safe?"*.

## 📝 License

This project is open-source and available for educational purposes.
