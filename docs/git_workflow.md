# Git & Deployment Workflow

## Remotes

This repo has **two git remotes**:

| Remote   | URL                                                              | Purpose              |
|----------|------------------------------------------------------------------|----------------------|
| `origin` | `https://github.com/raviapatel/rilem_metadata_tool.git`         | GitHub (source code) |
| `hf`     | `https://huggingface.co/spaces/raviapatel/rilem-metadata-tool`  | HF Spaces (deploy)   |

## Daily Workflow

```bash
# 1. Stage your changes
git add -A

# 2. Commit
git commit -m "your commit message"

# 3. Push to GitHub
git push origin main

# 4. Push to HuggingFace Spaces (triggers re-deploy)
git push hf main
```

Or push to both at once:

```bash
git push origin main; git push hf main
```

## First-Time Setup (Already Done)

```bash
# Add the HF Spaces remote (replace <HF_TOKEN> with your token)
git remote add hf https://raviapatel:<HF_TOKEN>@huggingface.co/spaces/raviapatel/rilem-metadata-tool

# Verify remotes
git remote -v
```

To create a token: go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) → **New token** → Role: **Write**.

## Running Locally

```bash
conda activate rilemtool
cd D:\codes\rilem_metadata_tool
python app.py
# Opens at http://127.0.0.1:7860
```

## Important Notes

- The `README.md` YAML frontmatter (the `---` block at the top) is **required** by HF Spaces — do not remove it.
- `python_version: "3.11"` is pinned because Python 3.13 removed the `audioop` module which `gradio` needs.
- The app auto-detects local vs HF environment via the `SPACE_ID` env var to set the correct `server_name`.
- All dependency versions are pinned in `requirements.txt` to avoid compatibility issues.
