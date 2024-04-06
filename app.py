import time
import gradio as gr

def echo(message, history):
	for i in range(len(message)):
		yield "You typed: " + message[: i+1]


gr.ChatInterface(echo).launch()
