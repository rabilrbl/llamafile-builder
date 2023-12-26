import sys, os
from huggingface_hub import HfApi,login, logout
api = HfApi()

repo = sys.argv[1]
file = sys.argv[2]

token = os.environ.get("HF_TOKEN", None)

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
