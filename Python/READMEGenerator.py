# Make sure to keep a backup of the whole README file before running this

import os
import re

def generate_readme():
    # Clear the content of README.md if it exists
    if os.path.exists("README.md"):
        with open("README.md", "w") as f:
            f.write("")  # Clear the file content

    # Create the header of the README
    readme_content = """ 

# Python Weekly Assignments

Welcome to the **Python Weekly Assignments** repository! This repository contains a collection of weekly Python assignments, each designed to enhance your programming skills and understanding of various Python concepts. The assignments are categorized by week, with each week featuring five unique programming challenges.

## Table of Contents

- [Overview](#overview)
- [Weekly Assignments](#weekly-assignments)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository is aimed at students and Python enthusiasts who are looking to practice and improve their Python programming skills. Each week's assignments cover a range of topics and challenges, from basic data types and control structures to more advanced concepts like file handling and machine learning.

## Weekly Assignments
"""

    # Helper function to extract numbers from folder names
    def extract_number(text):
        match = re.search(r'\d+', text)
        return int(match.group()) if match else float('inf')

    # Collect and sort assignment folders numerically
    assignment_folders = [
        folder for folder in os.listdir() if folder.startswith("Assignment") and os.path.isdir(folder)
    ]
    sorted_folders = sorted(assignment_folders, key=extract_number)

    # Scan the sorted folders and generate content
    for folder in sorted_folders:
        assignment_number = extract_number(folder)
        readme_content += f"\n### Assignment - {assignment_number}\n"

        # List all Python files and PDFs in the folder
        for file in sorted(os.listdir(folder)):
            if file.endswith(".py"):
                readme_content += f"- [{file}]({folder}/{file})\n"
            elif file.endswith(".pdf"):
                readme_content += f"- [Questions]({folder}/{file})\n"

    readme_content += """ 

Each assignment contains a PDF file that states the problem in a more detailed manner. Make sure to refer to it in case of any confusion.

## Getting Started

To get started with the assignments, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CyberKnight-cmd/Python-Weekly-Assignments.git
    ```
2. **Navigate to the desired week's folder**:
    ```bash
    cd Python-Weekly-Assignments/Assignment1
    ```
3. **Run the Python programs**:
    ```bash
    python Prog1.py
    ```

Ensure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request. Here’s how you can contribute:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-name
    ```
3. **Make your changes and commit them**:
    ```bash
    git commit -m "Description of changes"
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature-name
    ```
5. **Create a new pull request**.

## License

This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information
"""

    # Write the content to README.md
    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md has been updated successfully!")

# Run the function to generate the README
generate_readme()
