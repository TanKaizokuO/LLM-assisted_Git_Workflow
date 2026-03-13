import os
import sys
from openai import OpenAI
from diffsense.commit_classifier import get_system_prompt

def generate_commit_message(diff_text, config):
    # Fix 5a: guard against empty diff before hitting the API
    if not diff_text or not diff_text.strip():
        print("Error: diff is empty — nothing to analyse.")
        sys.exit(1)

    api_key = os.environ.get("NVIDIA_API_KEY")

    if not api_key:
        print("Error: NVIDIA_API_KEY environment variable is not set.")
        print("Please export your API key using: export NVIDIA_API_KEY='your-nvapi-key'")
        sys.exit(1)
        
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )
    model = config.get("model", "meta/llama-3.1-8b-instruct")
    
    system_prompt = get_system_prompt()
    user_prompt = f"Here is the git diff:\n\n{diff_text}\n\nPlease generate the corresponding semantic commit message."
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=120,  # Fix 5b: 60 was too tight for full conventional commits lines
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating commit message from LLM: {e}")
        sys.exit(1)
