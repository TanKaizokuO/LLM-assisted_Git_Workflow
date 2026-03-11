# ai-git

**ai-git** is a developer productivity CLI tool that totally automates the mundane task of writing git commits. By utilizing powerful Large Language Models (LLMs)—including OpenAI and NVIDIA AI endpoints—it analyzes your local `git diff`, understands the exact code changes you made, and produces extremely high-quality, semantic commit messages complying with the Conventional Commits specification. 

Beyond just generating messages, `ai-git` acts as a full-fledged git automation daemon. It can stage your files, generate the perfect message, commit locally, and instantly push to your remote repository. You can either use it on-demand whenever you are ready to wrap up a feature, or run it in the background as a daemon to implicitly save your work every 2 minutes without ever opening a terminal tab.

## Quick Start
1. Provide your API key in a `.env` file at the root of your project:
   ```env
   OPENAI_API_KEY="your-api-key"
   # OR
   NVIDIA_API_KEY="your-nvapi-key"
   ```
2. Run the tool to commit changes:
   ```bash
   uv run ai-git commit
   ```
3. Or run it as a background daemon to auto-commit and push every 1 minutes:
   ```bash
   uv run ai-git auto
   ```

## Features
- **Git Diff Analysis**: Automatically captures code changes based on staged or unstaged changes.
- **Auto-Commit Daemon**: Includes an `auto` command to safely track, commit, and push your work unconditionally every 2 minutes.
- **LLM Generated Commits**: Integrates with OpenAI models and NVIDIA (`meta/llama-3.1-8b-instruct`) models.
- **Conventional Commits Format**: Follows `<type>(<scope>): <summary>`.
- **Automatic Git Workflow**: Stages, generates the commit message, commits, and optionally pushes automatically.
- **Configurable**: Define configurations globally or locally via `.aigit/config.yaml`.

## Installation

### From Source
```bash
cd ai-git
pip install -e .
```

### Install Dependencies only
If you prefer not to install it globally, you can install the dependencies directly:
```bash
pip install -r requirements.txt
```

## Setup
Make sure you have an active API key exported in your terminal environment:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

## Configuration
You can control settings such as `llm_provider`, `model`, `max_diff_lines`, and `auto_push` using a config format like:
`.aigit/config.yaml`
```yaml
llm_provider: openai
model: gpt-4o-mini
max_diff_lines: 2000
auto_push: true
```

## Usage
Simply make changes to your repository and run:
```bash
ai-git commit
```

The tool will display a proposed commit message and ask for confirmation before committing and pushing. You can enter:
- `y` to accept and commit.
- `n` to reject and abort.
- `e` to edit the generated message before committing.
