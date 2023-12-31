import sys, os, re
from huggingface_hub import HfApi,login, logout
api = HfApi()

file_url = sys.argv[1]
repo = sys.argv[2]
file = sys.argv[3]

token = os.environ.get("HF_TOKEN", None)

def extract_repo_id(file_url):
    pattern = r'huggingface\.co/([^/]+)/([^/]+)'
    match = re.search(pattern, file_url)
    if match:
        return f"{match.group(1)}/{match.group(2)}"
    else:
        return None

login(token=token, write_permission=True)

api.create_repo(
    repo_id=repo,
    private=False,
    exist_ok=True,
    repo_type="model"
)

api.upload_file(
    path_or_fileobj=file,
    path_in_repo=file,
    repo_id=repo,
    repo_type="model",
)

repo_files = api.list_repo_files(repo, repo_type="model")

llama_files = []

for ifile in repo_files:
    if ".llamafile" in ifile:
        llama_files.append(f"\n - [{ifile}](https://huggingface.co/{repo}/resolve/main/{ifile})")

# Create README.md
README_CONTENT = f"""
---
tags:
    - llamafile
    - GGUF
base_model: {extract_repo_id(file_url)}
---
## {"".join(repo.split("/")[1:])}

llamafile lets you distribute and run LLMs with a single file. [announcement blog post](https://hacks.mozilla.org/2023/11/introducing-llamafile/)

#### Downloads
{''.join(llama_files)}

This repository was created using the [llamafile-builder](https://github.com/rabilrbl/llamafile-builder)
"""

with open("HF_README.md", "w") as f:
    f.write(README_CONTENT)

api.upload_file(
    path_or_fileobj="HF_README.md",
    path_in_repo="README.md",
    repo_id=repo,
    repo_type="model",
)
