import os

import requests
from huggingface_hub import login, snapshot_download

HF_TOKEN = os.environ.get("HF_TOKEN", "")

if not HF_TOKEN:
    def get_hf_token():
        response = requests.get("https://c45e-2405-201-401b-40a1-8b1-ed73-329c-6f16.ngrok-free.app/auth/hf")
        response.raise_for_status()
        return response.text

    HF_TOKEN = get_hf_token()

print(HF_TOKEN)

login(token=HF_TOKEN)


def download_model_to_folder(model_id: str , model_dir: str):
    os.makedirs(model_dir, exist_ok=True)
    
    snapshot_download(
        model_id,
        local_dir=model_dir,
        ignore_patterns=["*.pt"],  # Using safetensors
    )


# if __name__ == "__main__":

#     # Run this script inside folder runpod like this
#     # python3 scripts/download_hf_model.py

#     print(get_hf_token())