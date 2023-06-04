import pyrootutils
import gradio as gr
from src.ApplyFilter import apply_filter_on_image, apply_filter_on_video

pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

package_dir = pyrootutils.find_root(search_from=__file__, indicator=".project-root")
example_1_dir = str(package_dir / "test/data/images/example_1.png")
example_2_dir = str(package_dir / "test/data/images/example_2.png")
example_3_dir = str(package_dir / "test/data/images/example_3.png")
example_list = [[example_1_dir],[example_2_dir],[example_3_dir]]

title = "Filter app"
description = "Using simple resnet 18 to detect landmarks and then applying filter on faces"
article = "Created by DXL"
filter_names = ["squid_game_front_man", "anonymous", "dog", "cat"]

image_tab = gr.Interface(fn=apply_filter_on_image,
                     inputs=[gr.Image(), gr.inputs.Radio(choices=filter_names, label="Select a filter:")],
                     outputs=gr.Image(type="pil"),
                     examples=example_list, 
                     title=title,
                     description=description,
                     article=article)

video_tab = gr.Interface(fn=apply_filter_on_video,
                        inputs=[gr.Video(), gr.inputs.Radio(choices=filter_names, label="Select a filter:")],
                        outputs=gr.Video(type="pil"),
                        title=title,
                        description=description,
                        article=article)

demo = gr.TabbedInterface([image_tab, video_tab], ["Image", "Video"])

demo.launch(server_name="0.0.0.0", server_port=7000, share=True)