import os
import re
import glob
from datetime import datetime
from urllib.parse import quote

README_PATH = "README.md"
REPO_URL = "https://github.com/Venkateswaran-A-G/Leetcode-Solutions/blob/main"

def parse_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    keys = {
        "date": r"# Date:\s*(.*)",
        "num": r"# Problem Number:\s*(.*)",
        "title": r"# Problem Title:\s*(.*)",
        "link": r"# LeetCode Link:\s*(.*)",
        "difficulty": r"# Difficulty:\s*(.*)",
        "topic": r"# Topic:\s*(.*)",
        "time": r"# Time Complexity:\s*(.*)",
        "space": r"# Space Complexity:\s*(.*)",
    }

    metadata = {}
    for key, pattern in keys.items():
        match = re.search(pattern, content)
        if match:
            metadata[key] = match.group(1).strip()
        else:
            return None  # Skip files without complete header metadata

    # URL-encode file paths to fix spaces breaking Markdown links
    rel_path = os.path.relpath(file_path, start=".").replace("\\", "/")
    encoded_path = quote(rel_path)
    metadata["code_url"] = f"{REPO_URL}/{encoded_path}"
    return metadata

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        return datetime.min

def main():
    py_files = sorted(glob.glob("**/*.py", recursive=True))
    entries = []

    for file_path in py_files:
        if file_path.startswith(".github"):
            continue
        meta = parse_python_file(file_path)
        if meta:
            entries.append(meta)

    # Sort entries chronologically by Date (earliest first), then by Problem Number
    entries.sort(key=lambda x: (parse_date(x["date"]), int(x["num"]) if x["num"].isdigit() else 9999))

    # Read base README content up to table section
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        parts = content.split("## 📊 Daily Log")
        header_section = parts[0]
    else:
        header_section = "# Daily DSA Journal\n\nA personal repository dedicated to tracking my daily practice with Data Structures and Algorithms.\n\n## 🛠️ Languages & Tools\n* **Language:** Python\n* **Platforms:** LeetCode\n\n"

    table_header = "| Date | Sl.no | Leetcode Number | Problem Title | Difficulty | Solution | Topic | Time Complexity | Space Complexity |\n| :--- | :-: | :-: | :--- | :-: | :-: | :--- | :-: | :-: |"

    rows = []
    for idx, e in enumerate(entries, start=1):
        sl_no = f"{idx:03d}"
        formatted_num = f"{int(e['num']):03d}" if e['num'].isdigit() else e['num']
        row = f"| {e['date']} | {sl_no} | {formatted_num} | [{e['title']}]({e['link']}) | {e['difficulty']} | [Code]({e['code_url']}) | {e['topic']} | {e['time']} | {e['space']} |"
        rows.append(row)

    new_readme = f"{header_section}## 📊 Daily Log\n\n{table_header}\n" + "\n".join(rows) + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    main()
