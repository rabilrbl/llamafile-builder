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

# Create README.md
README_CONTENT = f"""
### {file.replace(".llamafile", "")}

[Download llamafile](https://huggingface.co/{repo}/resolve/main/{file})

This repository was created using the [llamafile-builder](https://github.com/rabilrbl/llamafile-builder)
"""

api.upload_file(
    path_or_fileobj=README_CONTENT,
    path_in_repo="README.md",
    repo_id=repo,
    repo_type="model",
)

api.upload_file(
    path_or_fileobj=file,
    path_in_repo=file,
    repo_id=repo,
    repo_type="model",
)
