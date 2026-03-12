# DiffSense

**DiffSense** is a developer productivity CLI tool that totally automates the mundane task of writing git commits. By utilizing powerful Large Language Models (LLMs)—including OpenAI and NVIDIA AI endpoints—it analyzes your local `git diff`, understands the exact code changes you made, and produces extremely high-quality, semantic commit messages complying with the Conventional Commits specification.

Beyond just generating messages, `DiffSense` acts as a full-fledged git automation daemon. It can stage your files, generate the perfect message, commit locally, and instantly push to your remote repository. You can either use it on-demand whenever you are ready to wrap up a feature, or run it in the background as a daemon to implicitly save your work every 1 minute without ever opening a terminal tab.

## Quick Start

Follow these steps to get `DiffSense` running and automating your commits.

1. **Install the CLI Tool**
   Install the package locally so the `diffsense` command becomes available in your terminal. You should ideally do this within a virtual environment.

   ```bash
   # From the root of the DiffSense repository
   pip install -e .
   ```

2. **Configure your API Key**
   The tool needs access to an LLM provider to generate commit messages. Create a `.env` file at the root of the project you want to manage with `DiffSense`, and add your API key:

   ```env
   # Use OpenAI's models (default)
   OPENAI_API_KEY="your-openai-api-key"

   # OR use NVIDIA's models
   NVIDIA_API_KEY="your-nvapi-key"
   ```

   _(Alternatively, you can export these as environment variables in your terminal)._

3. **Generate a Commit**
   Stage your changes (or let `DiffSense` detect unstaged changes) and run the commit command. It will analyze your diff, propose a commit message, and ask for confirmation before committing and pushing.

   ```bash
   diffsense commit
   ```

4. **Run as an Auto-Tracker Daemon (Optional)**
   If you want `DiffSense` to seamlessly track your work in the background without any manual intervention, start the auto daemon. It will commit and push your changes every 1 minute.
   ```bash
   diffsense auto
   ```

## Features

- **Git Diff Analysis**: Automatically captures code changes based on staged or unstaged changes.
- **Auto-Commit Daemon**: Includes an `auto` command to safely track, commit, and push your work unconditionally every 1 minute.
- **LLM Generated Commits**: Integrates with OpenAI models and NVIDIA (`meta/llama-3.1-8b-instruct`) models.
- **Conventional Commits Format**: Follows `<type>(<scope>): <summary>`.
- **Automatic Git Workflow**: Stages, generates the commit message, commits, and optionally pushes automatically.
- **Configurable**: Define configurations globally or locally via `.diffsense/config.yaml`.

## Installation

### From Source

```bash
cd diffsense
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
`.diffsense/config.yaml`

```yaml
llm_provider: openai
model: gpt-4o-mini
max_diff_lines: 2000
auto_push: true
```

## Usage

Simply make changes to your repository and run:

```bash
diffsense commit
```

The tool will display a proposed commit message and ask for confirmation before committing and pushing. You can enter:

- `y` to accept and commit.
- `n` to reject and abort.
- `e` to edit the generated message before committing.
