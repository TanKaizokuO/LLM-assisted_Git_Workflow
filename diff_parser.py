def parse_diff(diff_text, max_lines=2000):
    """Parse and truncate diff to fit within max_lines."""
    if not diff_text:
        return ""
    
    lines = diff_text.splitlines()
    if len(lines) <= max_lines:
        return diff_text
    
    # Truncate to max_lines to save token context
    truncated = lines[:max_lines]
    truncated.append(f"\n... Diff truncated to {max_lines} lines ...")
    return "\n".join(truncated)
