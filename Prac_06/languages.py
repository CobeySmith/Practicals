"""
Prac_06 languages exercise
Estimate: 15 mins
Actual: 20 mins
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    programming_languages = [python, ruby, visual_basic]
    print("The dynamic languages are:")
    dynamic_languages = [programming_language for programming_language in programming_languages if
                         programming_language.is_dynamic()]

    for dynamic_language in dynamic_languages:
        print(dynamic_language.name)


main()
