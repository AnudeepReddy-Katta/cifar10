______________________________________________________________________

<div align="center">

# Dockerized Gradio App

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

Gradio app to classify images

## How to run

docker run -it -d -p 7000:7000  anukatta/week3:v1  (size - 1.21GB)

## Docker File

FROM python:3.7-slim-buster

WORKDIR /workspace/project

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY model.script.pt ./

COPY configs/ configs/
COPY src/ src/
COPY pyproject.toml ./


EXPOSE 7860
ENTRYPOINT ["python3", "src/demo_scripted.py"]

# Sample Run
![image](https://user-images.githubusercontent.com/65823721/196034603-c4931fdd-5767-4855-8c08-e84c30cf0e0a.png)
