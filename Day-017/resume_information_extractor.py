# Resume Information Extractor using Regular Expressions

import re


def extract_name(text):
    """
    Assumes the first non-empty line is the candidate's name.
    """
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line

    return "Not Found"


def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_mobile(text):

    pattern = r"(?:\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_linkedin(text):

    pattern = (
        r"(https?://)?"
        r"(www\.)?"
        r"linkedin\.com/in/[A-Za-z0-9_-]+/?"
    )

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_skills(text):

    skill_list = [
        "Python",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "SQL",
        "HTML",
        "CSS",
        "React",
        "Node.js",
        "Git",
        "Linux",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "Machine Learning",
        "Data Science",
        "AI",
        "TensorFlow",
        "PyTorch",
        "Django",
        "Flask"
    ]

    found = []

    for skill in skill_list:

        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found


def display_information(text):

    print("\n========== Resume Information ==========\n")

    print("Name      :", extract_name(text))
    print("Email     :", extract_email(text))
    print("Mobile    :", extract_mobile(text))
    print("LinkedIn  :", extract_linkedin(text))

    skills = extract_skills(text)

    print("Skills    :", ", ".join(skills) if skills else "Not Found")

    print()


def main():

    filename = input("Enter Resume File Name: ").strip()

    try:

        with open(filename, "r") as file:

            content = file.read()

        display_information(content)

    except FileNotFoundError:

        print("Resume file not found.")

    except Exception as error:

        print("Error:", error)


main()
