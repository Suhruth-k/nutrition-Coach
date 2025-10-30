
# 🥗 Nurture: Your AI Nutrition Coach

**Nurture** is an AI-powered conversational nutritionist built with **Gradio**, **Google Gemini API**, and **gTTS (Google Text-to-Speech)**.
It acts as your friendly digital nutrition coach — guiding you through your health journey, understanding your goals, and even helping you calculate your BMI.

---

## 🌟 Features

* 🤖 **Conversational AI Coach** — Interact naturally with your AI nutritionist powered by Google Gemini.
* 🗣️ **Voice Output** — Listen to AI responses generated with Google Text-to-Speech (gTTS).
* ⚖️ **BMI Calculator** — Quickly check your Body Mass Index and its category.
* 💬 **Chat History** — Maintains the conversation context for a more personalized experience.
* 🎨 **Clean UI** — Built using Gradio’s `Soft` theme for an intuitive and smooth interface.

---

## 🧠 How It Works

1. The app sends user input to the **Gemini API** for AI-generated responses.
2. The **chat history** ensures the model remembers past messages for contextual replies.
3. Responses are also converted to **speech** using `gTTS`.
4. Users can calculate their **BMI** based on height and weight.

---

## 🛠️ Tech Stack

| Component                        | Description                            |
| -------------------------------- | -------------------------------------- |
| **Python**                       | Main programming language              |
| **Gradio**                       | Web UI framework                       |
| **Google Gemini API**            | AI conversation engine                 |
| **gTTS (Google Text-to-Speech)** | Converts AI text responses into speech |
| **Requests + JSON**              | API communication                      |
| **Tempfile**                     | Manages temporary audio files          |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/nurture-ai-nutrition-coach.git
cd nurture-ai-nutrition-coach
```

### 2. Install dependencies

Make sure you have **Python 3.8+** installed.

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one with:

```txt
gradio
gtts
requests
```

### 3. Add your Gemini API key

Open the script and replace this line:

```python
API_KEY = "YOUR GEMINI API KEY"
```

with your actual **Google Gemini API Key**.
If you don’t have one, get it from [Google AI Studio](https://aistudio.google.com/).

---

## ▶️ Run the App

Run the script using:

```bash
python app.py
```

After launching, Gradio will display a local and a shareable public URL (if `share=True`).
Open it in your browser to start chatting with **Nurture**!

---

## 💡 Example Use

* "Hi! I want to lose weight. Can you help me create a meal plan?"
* "I’m allergic to nuts, what should I avoid?"
* "Here are my height and weight — what’s my BMI?"

The AI will reply with personalized responses and also speak them aloud!

---

## ⚖️ BMI Calculator

You can also use the built-in BMI calculator by entering your **height (cm)** and **weight (kg)**.
The app returns your BMI value along with your weight category:

* Underweight: `< 18.5`
* Normal: `18.5 – 24.9`
* Overweight: `25 – 29.9`
* Obese: `≥ 30`

---

---

Would you like me to generate a `requirements.txt` file for this too?
