import uuid
import gradio as gr
from app.engine import ResearchEngine
from app.memory.document_loader import load_pdf, chunk_text
from app.memory.vector_store import add_chunks_to_vector_store

engine = ResearchEngine()


def upload_pdf(file):
    if file is None:
        return "Please upload a PDF."

    text = load_pdf(file.name)
    chunks = chunk_text(text)

    add_chunks_to_vector_store(chunks, metadata={"source": file.name})

    return f"Document processed successfully. {len(chunks)} chunks stored."


def chat(message, history):
    if not message:
        return history

    if history is None:
        history = []

    answer = engine.run(message)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    return history


with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Multi-Agent Research Companion")

    with gr.Row():
        pdf_upload = gr.File(file_types=[".pdf"], label="Upload Research Paper")
        upload_status = gr.Textbox(label="Upload Status")

    upload_button = gr.Button("Process Document")

    chatbot = gr.Chatbot(label="Research Assistant")
    user_input = gr.Textbox(label="Ask a Question")
    send_button = gr.Button("Send")

    upload_button.click(
        upload_pdf,
        inputs=pdf_upload,
        outputs=upload_status
    )

    send_button.click(
        chat,
        inputs=[user_input, chatbot],
        outputs=chatbot
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
