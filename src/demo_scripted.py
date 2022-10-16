import pyrootutils
import requests

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from typing import List, Tuple

import torch
import hydra
import gradio as gr
from omegaconf import DictConfig

from src import utils

log = utils.get_pylogger(__name__)

def demo(cfg: DictConfig) -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    assert cfg.ckpt_path

    log.info("Running Demo")

    log.info(f"Instantiating scripted model <{cfg.ckpt_path}>")
    model = torch.jit.load(cfg.ckpt_path)

    log.info(f"Loaded Model: {model}")

    def predict(image):
        
        response = requests.get("https://raw.githubusercontent.com/RubixML/CIFAR-10/master/labels.txt")
        labels = response.text.split("\n")
        preds = model.forward_jit(torch.tensor(image,dtype=torch.float32).unsqueeze(0))
        preds = preds[0].tolist()
        confidences = {labels[i]: (preds[i]) for i in range(10)} 
        return confidences

    demo = gr.Interface(fn=predict, inputs=gr.Image(shape=(32,32)), outputs=gr.Label(num_top_classes=10))

    demo.launch(server_name="0.0.0.0",server_port=8080)

@hydra.main(
    version_base="1.2", config_path=root / "configs", config_name="demo_scripted.yaml"
)
def main(cfg: DictConfig) -> None:
    demo(cfg)

if __name__ == "__main__":
    main()