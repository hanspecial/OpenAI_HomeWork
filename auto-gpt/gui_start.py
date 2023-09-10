import sys
import os
import gradio as gr
from tools4auto import Tools4Auto
from auto_agent import AutoAgent
from faiss_vector import FaissVector


os.environ["SERPAPI_API_KEY"] = "e65622355785aba531fe0f3733c6c429e3ec43457c916a0c3006e6f81d433369"


def autoagent(input_message):
    agent = AutoAgent(tools = tools,vectorstore = vectorstore).agent
    output_message = agent.run([str(input_message)])
  #  output_message = agent.run(["2008年奥运会在哪里举办"])
    return output_message,agent.output_parser

def launch_gradio():

    iface = gr.Interface(
        fn=autoagent,
        title="自主智能机器人会话",
        inputs=[
            gr.Textbox(label="user-input", placeholder="", value="enter your message"),
        #    gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese"),
        #    gr.Radio(["Modern", "Poetic", "Chinese tradational"],
        #        label="translate style", info="select the context style")
        ],
        outputs=[
            gr.Textbox(label="AI-output"),
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

    iface.launch(share=True, server_name="0.0.0.0")

def initialize_tools():
    global tools
    tools = Tools4Auto().tools

    global vectorstore
    vectorstore = FaissVector().vectorstore

if __name__ == "__main__":
    initialize_tools()
    launch_gradio()

