FROM python:3.7-slim-buster

# Set working directory
WORKDIR /workspace/project

# Install requirements
COPY requirements.txt ./

RUN pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY ./logs/train/runs/2022-10-15_22-44-32/model.script.pt ./model.script.pt

COPY configs/ configs/
COPY src/ src/
COPY pyproject.toml ./


EXPOSE 7860
ENTRYPOINT ["python3", "src/demo_scripted.py"]