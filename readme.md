# Fox Chatbot - Talk to Fox from Wanted

This project brings the character Fox from the movie "Wanted" to life as an interactive AI chatbot. Using OpenAI's powerful language models and a carefully crafted persona, you can now converse with Fox and explore the world of "Wanted" in a unique and engaging way.

## Features

* **Personality-Driven Interactions:** Experience conversations that reflect Fox's distinct personality, including her bluntness, wit, and philosophical insights.
* **Contextual Awareness:** The chatbot remembers previous interactions and responds accordingly, maintaining a consistent and engaging conversation flow.
* **Knowledge of the "Wanted" Universe:** Delve deeper into the movie's lore and discuss characters, storylines, and other details with Fox.
* **Powered by OpenAI:** Enjoy high-quality and coherent responses thanks to the advanced language models powering the chatbot.
* **User-Friendly Interface:** Interact with Fox through a simple and intuitive chat interface.

## Getting Started

### 1. Environment Setup

* **Clone the repository:**
```bash
git clone https://github.com/cl0ver012/Igcy_Chatbot/
cd Igcy_Chatbot
```

* **Create a virtual environment (recommended):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

* **Install dependencies:**
```bash
pip install -r requirements.txt
```

* **Obtain an OpenAI API key:**
  - Sign up for an OpenAI account at [https://openai.com/](https://openai.com/).
  - Create an API key in your OpenAI account dashboard.

* **Create a `.env` file:**
  - Create a file named `.env` in the root directory of the project.
  - Add the following line, replacing `YOUR_OPENAI_API_KEY` with your actual API key:
```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

### 2. Running the Project

* **Start the backend (FastAPI):**
```bash
uvicorn main:app --reload
```

* **Start the frontend (Streamlit) in a separate terminal:**
```bash
streamlit run streamlit_app/main.py
```

Now you can access the chatbot interface in your web browser and start talking to Fox!
