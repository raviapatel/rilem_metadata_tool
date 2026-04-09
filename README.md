
---
title: RILEM Metadata Tool
emoji: 📋
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.0"
python_version: "3.11"
app_file: app.py
pinned: false
---

RILEM Metadata Tool
===================

## Git Workflow

This repo has **two remotes**:

| Remote   | URL                                                                        | Purpose              |
|----------|----------------------------------------------------------------------------|----------------------|
| `origin` | `https://github.com/raviapatel/rilem_metadata_tool.git`                   | GitHub (source code) |
| `hf`     | `https://huggingface.co/spaces/raviapatel/rilem-metadata-tool`            | HF Spaces (deploy)   |

### Daily workflow

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

### First-time setup (already done)

```bash
# Add the HF Spaces remote
git remote add hf https://<USERNAME>:<HF_TOKEN>@huggingface.co/spaces/raviapatel/rilem-metadata-tool

# Verify remotes
git remote -v
```

### Running locally

```bash
conda activate rilemtool
cd D:\codes\rilem_metadata_tool
python app.py
# Opens at http://127.0.0.1:7860
```

### Notes

- The `README.md` YAML frontmatter (lines 1–11) is **required** by HF Spaces — do not remove it.
- `python_version: "3.11"` is pinned because Python 3.13 removed `audioop` which `gradio` needs.
- The app auto-detects local vs HF environment via the `SPACE_ID` env var for `server_name`.
