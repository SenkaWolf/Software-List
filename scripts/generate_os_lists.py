from pathlib import Path

README = Path("README.md")
DOCS = Path("docs")

text = README.read_text(encoding="utf-8").splitlines()

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

results = {
    "windows": {},
    "linux": {},
    "macos": {}
}

current_section = None

for line in text:

    # Detect section headings like #### Audio
    if line.startswith("#### "):
        current_section = line.strip()
        continue

    # Detect list entries
    if line.strip().startswith("- "):

        for os_name, icon in OS_ICONS.items():

            if icon in line:

                if current_section not in results[os_name]:
                    results[os_name][current_section] = []

                results[os_name][current_section].append(line)


def write_file(os_name):

    title = OS_TITLES[os_name]

    output = f"# {title}\n\n"

    # Badge-style back button
    output += "[![Back](https://img.shields.io/badge/⬅%20Back-Main%20Software%20List-blue)](../README.md)\n\n"

    output += "---\n\n"
    output += "*Automatically generated from README.md*\n\n"

    sections = results[os_name]

    for section, items in sections.items():

        output += f"{section}\n"

        for item in items:
            output += item + "\n"

        output += "\n"

    path = DOCS / f"{os_name.upper()}.md"
    path.write_text(output, encoding="utf-8")


for os_name in OS_ICONS:
    write_file(os_name)

print("OS filtered pages generated.")
