import argparse
import sys
from config import load_config
from git_utils import has_git_repo, get_staged_diff, get_unstaged_diff, git_add_all, git_commit, git_push
from diff_parser import parse_diff
from llm_commit_generator import generate_commit_message

def ask_confirmation(message):
    print("\nGenerated Commit Message:")
    print("-" * 50)
    print(message)
    print("-" * 50)
    
    while True:
        choice = input("\nDo you want to proceed with this commit? [Y/n/e(dit)]: ").strip().lower()
        if choice in ['y', 'yes', '']:
            return message
        elif choice in ['n', 'no']:
            print("Commit aborted.")
            sys.exit(0)
        elif choice in ['e', 'edit']:
            new_message = input("Enter your custom commit message: ").strip()
            if new_message:
                return new_message
            else:
                print("Commit message cannot be empty. Please edit again.")
        else:
            print("Invalid choice. Please enter 'y', 'n', or 'e'.")

def handle_commit():
    if not has_git_repo():
        print("Error: Not inside a git repository.")
        sys.exit(1)
        
    config = load_config()
    
    # Check if there are staged changes
    diff = get_staged_diff()
    staged = True
    
    if not diff:
        # Check unstaged changes
        diff = get_unstaged_diff()
        staged = False
        
        if not diff:
            print("No changes to commit. Working tree is clean.")
            sys.exit(0)
    
    # If there are changes but they are unstaged, we run git add automatically
    if not staged:
        print("Detected unstaged changes. Staging them automatically...")
        git_add_all()
        # Retrieve the updated diff from staged changes
        diff = get_staged_diff()
        
    # Process diff
    parsed_diff = parse_diff(diff, max_lines=config.get("max_diff_lines", 2000))
    
    # Generate message
    print("Analyzing code changes and talking to LLM...")
    commit_message = generate_commit_message(parsed_diff, config)
    
    # Ask for user confirmation
    final_message = ask_confirmation(commit_message)
    
    # Commit
    print(f"Committing changes...")
    git_commit(final_message)
    
    # Push
    if config.get("auto_push", True):
        print("Pushing to remote repository...")
        git_push()
        print("Changes pushed successfully! 🎉")
    else:
        print("Commit created successfully (auto_push is disabled). 🎉")

def main():
    parser = argparse.ArgumentParser(description="AI Git CLI tool: Automatically generate intelligent commit messages")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Setting up the 'commit' command
    commit_parser = subparsers.add_parser("commit", help="Analyze diff, generate commit message, commit and push")
    
    args = parser.parse_args()
    
    if args.command == "commit":
        handle_commit()
    else:
        parser.print_help()
