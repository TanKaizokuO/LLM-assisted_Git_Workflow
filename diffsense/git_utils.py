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

def has_untracked_files():
    """Return True if there are any untracked (new) files not yet staged."""
    output = run_command(["git", "ls-files", "--others", "--exclude-standard"])
    return bool(output.strip())

def has_changes():
    """Return True if there are any unstaged tracked changes OR untracked new files."""
    return bool(get_unstaged_diff()) or has_untracked_files()

def git_add_all():
    run_command(["git", "add", "."])

def git_commit(message):
    run_command(["git", "commit", "-m", message])

def git_push():
    run_command(["git", "push"])
