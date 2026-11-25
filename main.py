import os

def main():
    """Writes a single office-humor line to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.
    LINE = "Since our weekly status meeting has yielded zero updates for four years, I propose we save thirty minutes by collectively admitting we're all just hallucinating until Friday."
    content = LINE + "\n"
    
    lines = content.splitlines()
    if len(lines) != 1 or not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content structure")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    primary_path = os.path.join(out_dir, "entry.txt")
    
    os.makedirs(out_dir, exist_ok=True)
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except OSError:
            pass
    
    print(f"{primary_path} ({len(content)} chars)")

if __name__ == "__main__":
    main()
