import sys
import pexpect

def test_auto():
    # Start the CLI process
    child = pexpect.spawn('uv run python cli.py auto', encoding='utf-8')
    
    try:
        # Expect the interval prompt
        child.expect('Time between each commit \\(in minutes, default 1\\): ', timeout=5)
        print("PASS: Prompt shown.")
        
        # Send a custom interval (0.05 minutes = 3 seconds)
        child.sendline('0.05')
        
        # Expect the start message
        child.expect('Starting Auto-Commit Daemon \\(every 0.05 minute\\(s\\)\\)\\.\\.\\.', timeout=5)
        print("PASS: Daemon start message shown.")
        
        # Expect the countdown to start
        child.expect('Time remaining till next commit: 3 seconds\\.\\.\\.', timeout=5)
        print("PASS: Countdown started correctly.")
        
        # Kill the child securely
        child.kill(9)
        print("All tests passed.")
        
    except pexpect.TIMEOUT as e:
        print(f"FAIL: Timeout occurred: {e}")
        print(f"Before timeout: {child.before}")
        sys.exit(1)
    except pexpect.EOF:
        print("FAIL: EOF occurred unexpectedly.")
        print(f"Before EOF: {child.before}")
        print(f"Output: {child.read()}")
        sys.exit(1)

if __name__ == '__main__':
    test_auto()
