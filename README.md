# Groq Chatbot

A simple Streamlit-based chat application that interacts with the [Groq API](https://groq.com/) to use the **LLaMA 3.1 8B Instant** language model. Ask questions and receive responses in real-time with a clean UI.

---

## 🚀 Features

- Real-time conversational interface powered by Streamlit.
- Uses LLaMA 3.1 8B Instant model via the Groq API.
- Smooth, character-by-character streaming response simulation.
- Environment-based API key management.

---

## 📦 Tech Stack

| **Technology** | **Purpose**                                   |
| -------------- | --------------------------------------------- |
| **Python**     | Core programming language                     |
| **Streamlit**  | Frontend Web App framework                    |
| **Groq API**   | AI model (LLaMA 3.1 8B Instant) for responses |
| **dotenv**     | Securely manage API keys                      |
| **time**       | Delay for character-by-character streaming    |
| **os**         | Environment variable management               |

---
## 📁 File Structure

Groq-Chatbot/
│
├── main.py              # Main application script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KaisoX24/Groq-Chatbot.git
   cd chat-with-llama

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set your Groq API key**
Create a .env file and set api_key:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. **Run the App**
   ```bash
   streamlit run main.py
   ```
---
