from pathlib import Path
import re

README = Path("README.md")
DOCS = Path("docs")

lines = README.read_text(encoding="utf-8").splitlines()

SEPARATOR = "![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)"

OS_ICONS = {
    "windows": "windows14.png",
    "linux": "linux14.png",
    "macos": "apple14.png"
}

OS_TITLES = {
    "windows": "Windows Software",
    "linux": "Linux Software",
    "macos": "macOS Software"
}

OS_FILENAMES = {
    "windows": "WINDOWS-SOFTWARE.md",
    "linux": "LINUX-SOFTWARE.md",
    "macos": "MACOS-SOFTWARE.md"
}

# -----------------------------
# NEW: Extract footnote definitions
# -----------------------------
footnote_defs = {}

for line in lines:
    match = re.match(r"\[\^(.+?)\]:\s*(.*)", line)
    if match:
        key = match.group(1)
        footnote_defs[key] = line  # store full definition line


# -----------------------------
# UPDATED results structure
# -----------------------------
results = {
    "windows": {"data": {}, "footnotes": set()},
    "linux": {"data": {}, "footnotes": set()},
    "macos": {"data": {}, "footnotes": set()}
}

current_main_section = None
current_category = None


for line in lines:

    # Detect main sections
    if line.startswith("## "):
        current_main_section = line.strip()
        current_category = None
        continue

    # Detect category headings
    if line.startswith("#### "):
        current_category = line.strip()
        continue

    # Detect list entries
    if line.strip().startswith("- "):

        # NEW: find footnote references in the line
        footnote_refs = re.findall(r"\[\^(.+?)\]", line)

        for os_name, icon in OS_ICONS.items():

            if icon in line:

                if current_main_section not in results[os_name]["data"]:
                    results[os_name]["data"][current_main_section] = {}

                category = current_category or "Other"

                if category not in results[os_name]["data"][current_main_section]:
                    results[os_name]["data"][current_main_section][category] = []

                results[os_name]["data"][current_main_section][category].append(line)

                # NEW: store used footnotes
                for ref in footnote_refs:
                    results[os_name]["footnotes"].add(ref)


def write_file(os_name):

    title = OS_TITLES[os_name]

    output = f"# {title}\n\n"

    output += "[![Back](https://img.shields.io/badge/⬅%20Back-Main%20Software%20List-blue)](../README.md)\n\n"
    output += f"{SEPARATOR}\n\n"
    output += "*Automatically generated from README.md*\n\n"

    sections = results[os_name]["data"]
    used_footnotes = results[os_name]["footnotes"]

    for main_section, categories in sections.items():

        output += f"{SEPARATOR}\n\n"
        output += f"{main_section}\n\n"

        for category, items in categories.items():

            if category != "Other":
                output += f"{category}\n"

            for item in items:
                output += item + "\n"

            output += "\n"

    #Append used footnotes
    if used_footnotes:
        output += "\n"

        for ref in sorted(used_footnotes):
            if ref in footnote_defs:
                output += footnote_defs[ref] + "\n"

    path = DOCS / OS_FILENAMES[os_name]
    path.write_text(output, encoding="utf-8")


for os_name in OS_ICONS:
    write_file(os_name)

print("OS filtered pages generated.")