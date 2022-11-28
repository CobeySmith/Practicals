"""
Prac 10
Wikipedia Exercise
"""

import wikipedia


user_input = input("Prompt: ")
while user_input != "":
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print(f"{page.title}\n{page.summary}\n{page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Your options are:\n{e.options}")
    except wikipedia.exceptions.PageError:
        print("Not a page")
    user_input = input("Prompt: ")

