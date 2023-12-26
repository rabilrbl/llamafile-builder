# llamafile-builder

A simple github actions script to build a llamafile from a given gguf file download url and uploads it to huggingface repo.

## Inputs

### `model_url`

**Required** The url to the gguf file to download.

### `huggingface_repo`

**Required** The huggingface repo to upload the llamafile to.

Add your huggingface token with write access to the repo as a actions secret with the name `HF_TOKEN`.

## Usage

1. Head over to the actions tab.
2. Select the action `Build llamafile` 
3. Fill in the required inputs.
4. Click on `Run workflow` and wait for the action to complete.
5. Check your huggingface repo for the llamafile.