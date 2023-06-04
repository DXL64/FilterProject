<div align="center">

# Apply Filter

</div>

## Description

Apply filter to the face based on landmark points.

## How to use

### Run manually

Set up environments

```
#use conda enviroment
conda create -n py38_filter python=3.8 -y
conda activate py38_filter

#install requirements
pip install -r requirements.txt

#run setup.py
python setup.py install --user

```
Apply filter on image

```
# In root dir, run:
python -m src.filter.filter_image
# You can change to your image by edit path in filer_image.py line 111
# Result will save in ./test/result

```
Apply filter on video or webcam

```
# In root dir, run:
python -m src.filter.filter_video
# You can change to your source by edit path in filer_video.py line 141
# source = 0 for webcam
# source = $path for your video path
# Result will save in ./test/result if you run for video

```

### Run demo on Gradio

You must activate conda enviroment py38_filter before run

```
python app.py

```
Your demo will public on local address : 0.0.0.0:7000 and public on url that Gradio show on terminal

### Run demo of Gradio with Docker

Prerequisites: You must have docker before you run it

```
docker build -t {{image_name}} .
docker run -d --name {{container_name}} {{image_name}}

```
Demo will expose on localhost port 7000

You can excute to container is running and run manually

```
docker exec -it {{container_name}} bash

```


