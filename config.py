import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

DEFAULT_CONFIG = {
    "llm_provider": "openai",
    "model": "gpt-4o-mini",
    "max_diff_lines": 2000,
    "auto_push": True
}

def load_config():
    # Load .env file from current directory or .aigit directory if present
    load_dotenv(Path.cwd() / ".env")
    load_dotenv(Path.cwd() / ".aigit" / ".env")
    
    # Look for .aigit/config.yaml in the current directory
    config_path = Path.cwd() / ".aigit" / "config.yaml"
    if not config_path.exists():
        return DEFAULT_CONFIG
    
    try:
        with open(config_path, "r") as f:
            user_config = yaml.safe_load(f)
            if user_config:
                # Merge with default config
                config = DEFAULT_CONFIG.copy()
                config.update(user_config)
                return config
            return DEFAULT_CONFIG
    except Exception as e:
        print(f"Error reading config: {e}")
        return DEFAULT_CONFIG
