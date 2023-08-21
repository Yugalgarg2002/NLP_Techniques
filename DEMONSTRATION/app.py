import gradio as gr

iface1 = gr.Interface.load("models/csarron/bert-base-uncased-squad-v1")


iface1.launch()  