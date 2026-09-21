from pipeline import extract_text, to_sorted_items, group_into_lines
import gradio as gr

def process_receipt(image_path):
    result = extract_text(image_path)
    sorted_list = to_sorted_items(result)
    lines = group_into_lines(sorted_list)
    return '\n'.join(lines)


checker = gr.Interface(
    fn = process_receipt,
    inputs = gr.Image(type="filepath"),
    outputs = 'text')
checker.launch()