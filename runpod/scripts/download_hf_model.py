import os

from huggingface_hub import login, snapshot_download
from src.constants import DEFAULT_MODEL_DIR, DEFAULT_MODEL_NAME

HF_TOKEN = os.environ.get("HF_TOKEN", "")

login(token=HF_TOKEN, add_to_git_credential=True)


def download_model_to_folder(model_id: str = DEFAULT_MODEL_NAME, model_dir: str = DEFAULT_MODEL_DIR):
    os.makedirs(model_dir, exist_ok=True)
    
    snapshot_download(
        model_id,
        local_dir=model_dir,
        ignore_patterns=["*.pt"],  # Using safetensors
    )


if __name__ == "__main__":

    # Run this script inside folder runpod like this
    # python3 scripts/download_hf_model.py

    download_model_to_folder(
        model_id="mistralai/Mistral-7B-v0.1", model_dir="./model"
    )
