import os
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv

# Load the API key from the environment variable

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")
os.environ["GOOGLE_API_KEY"] = api_key

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = "Enter your message here"
assistant = "assistant"  # Define the "assistant" variable

def generate_response(prompt, state):
    response = model.generate_content(prompt)
    return [("ASSISTANT", response.text)], state

def chat_lm(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = chat_lm(inp)
    history.append((input))
    return history, history, output

block = gr.Blocks()
with block:
    gr.Markdown("""<h1><center>Chat with Gemini Pro</center></h1>""")
    chatbot = gr.Chatbot(height=550)
    message = gr.Textbox(placeholder=prompt, type="text", label="Message")
    submit = gr.Button("SEND")
    state = gr.State()
    submit.click(generate_response, inputs=[message, state], outputs=[chatbot, state])



block.launch(server_name="0.0.0.0",server_port=7860,debug=True)

