def text_indentation(text):
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
    for char in text:
        if char in ['.', '?', ':']:
            print(char + "\n\n", end="")
        else:
            print(char, end="")
