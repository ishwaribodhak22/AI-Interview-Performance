import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def grammar_check(text):
    matches = tool.check(text)
    return len(matches)