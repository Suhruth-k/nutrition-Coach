import requests
import json
import tempfile
import gradio as gr
from gtts import gTTS

# ================= CONFIG =================
API_KEY = "YOUR GEMINI API KEY"
MODEL = "gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# ================= CHAT HISTORY =================
chat_history = [
    {"role": "system", "content":
     "You are an empathetic, conversational nutritionist who gently guides users "
     "to share their name, fitness goals, lifestyle, allergies, dietary preferences, "
     "and typical meals. Start with a warm greeting and then ask follow-up questions "
     "to eventually create a personalized diet plan."}
]

# ================= FUNCTIONS =================
def ask_gemini(question):
    """Send user input to Gemini API and return the reply."""
    chat_history.append({"role": "user", "content": question})

    
    data = {
        "contents": [
            {"parts": [{"text": entry["content"]} for entry in chat_history]}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()

        
        reply_text = ""
        if "candidates" in result and len(result["candidates"]) > 0:
            content = result["candidates"][0].get("content", {})
            parts = content.get("parts", [])
            reply_text = "".join([part.get("text", "") for part in parts])

        if not reply_text:
            reply_text = "Error: empty response from Gemini"

        chat_history.append({"role": "assistant", "content": reply_text})
        return reply_text

    except Exception as e:
        return f"Error: {str(e)}"

def speak(text):
    """Convert text to speech and return the file path."""
    tts = gTTS(text)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    return tmp_file.name

def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI and return the category."""
    try:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal weight" if bmi < 25 else
            "Overweight" if bmi < 30 else
            "Obese"
        )
        return f"Your BMI is {bmi:.2f} — {category}"
    except:
        return "Please enter valid height and weight."

# ================= GRADIO INTERFACE =================
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align: center;'>Nurture : Your AI Nutrition Coach</h1>")

    with gr.Row():
    
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(height=350, label="Chat with Nurture⚕️", type="messages")
            message = gr.Textbox(placeholder="Ask something...", label="Your Message")
            send_btn = gr.Button("Send")
            audio_output = gr.Audio(label="AI Voice", type="filepath", interactive=False)

            def respond(user_message, chat_log):
                bot_reply = ask_gemini(user_message)
                chat_log.append({"role": "user", "content": user_message})
                chat_log.append({"role": "assistant", "content": bot_reply})
                audio_path = speak(bot_reply)
                return "", chat_log, audio_path

            send_btn.click(respond, inputs=[message, chatbot], outputs=[message, chatbot, audio_output])


        with gr.Column(scale=1):
            gr.Markdown("### Check Your BMI")
            height = gr.Number(label="Height (in cm)")
            weight = gr.Number(label="Weight (in kg)")
            bmi_output = gr.Textbox(label="Result")
            bmi_btn = gr.Button("Calculate BMI")
            bmi_btn.click(fn=calculate_bmi, inputs=[height, weight], outputs=bmi_output)


demo.launch(share=True)