from utils.grammar import grammar_check

text = input("Enter text: ")

errors = grammar_check(text)

print("Grammar Errors:", errors)