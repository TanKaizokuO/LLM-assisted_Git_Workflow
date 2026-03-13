def parse_diff(diff_text, max_lines=2000):
    """Parse and truncate diff to fit within max_lines.

    Truncation is hunk-aware: we never cut in the middle of a hunk.
    Instead we stop at the last complete hunk boundary before the limit.
    """
    if not diff_text:
        return ""

    lines = diff_text.splitlines()
    if len(lines) <= max_lines:
        return diff_text

    # Walk backwards from the limit to find the start of the current hunk
    # so we don't deliver a half-written hunk to the LLM.
    cut = max_lines
    while cut > 0 and not lines[cut].startswith("@@"):
        cut -= 1

    # If no hunk header was found within the window, fall back to a file
    # boundary (lines starting with "diff --git") or the raw limit.
    if cut == 0:
        for i in range(max_lines, 0, -1):
            if lines[i].startswith("diff --git"):
                cut = i
                break
        else:
            cut = max_lines  # last resort: raw cut

    truncated = lines[:cut]
    total = len(lines)
    truncated.append(
        f"\n... Diff truncated: showing {cut}/{total} lines "
        f"({total - cut} lines omitted) ..."
    )
    return "\n".join(truncated)
