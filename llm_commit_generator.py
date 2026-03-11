import os
import sys
from openai import OpenAI
from commit_classifier import get_system_prompt

def generate_commit_message(diff_text, config):
    provider = config.get("llm_provider", "openai").lower()
    
    if provider != "openai":
        print(f"Error: Provider '{provider}' is not currently supported.")
        sys.exit(1)
        
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please export your OpenAI API key using:")
        print("export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
        
    client = OpenAI(api_key=api_key)
    model = config.get("model", "gpt-4o-mini")
    
    system_prompt = get_system_prompt()
    user_prompt = f"Here is the git diff:\n\n{diff_text}\n\nPlease generate the corresponding semantic commit message."
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=60,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating commit message from LLM: {e}")
        sys.exit(1)
