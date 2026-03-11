# ai-git

A smart Python CLI tool that automatically commits and pushes code to GitHub while generating intelligent commit messages using an LLM. 

## Features
- **Git Diff Analysis**: Automatically captures code changes based on staged or runstaged changes.
- **LLM Generated Commits**: Integrates with OpenAI models (default: `gpt-4o-mini`) to write semantic commit messages.
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
