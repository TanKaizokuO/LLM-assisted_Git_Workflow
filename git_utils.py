import subprocess
import sys

def run_command(cmd, shell=False):
    """Run shell command and return stdout."""
    try:
        result = subprocess.run(cmd, shell=shell, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(e.cmd)}")
        print(f"Error: {e.stderr.strip()}")
        sys.exit(1)

def has_git_repo():
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def get_staged_diff():
    return run_command(["git", "diff", "--cached"])

def get_unstaged_diff():
    return run_command(["git", "diff"])

def git_add_all():
    run_command(["git", "add", "."])

def git_commit(message):
    run_command(["git", "commit", "-m", message])

def git_push():
    run_command(["git", "push"])
