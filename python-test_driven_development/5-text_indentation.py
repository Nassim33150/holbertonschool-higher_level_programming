def text_indentation(text):
    """
    Add two new lines after each occurrence of '.', '?',
    and ':' characters in the text.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    """Check if the input is a string"""
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
        """Iterate over each character in the text"""
    for char in text:
        """If the character is '.', '?', or ':',
        print it followed by two new lines"""
        if char in ['.', '?', ':']:
            print(char + "\n\n", end="")
        """Otherwise, print the character without any changes"""
        else:
            print(char, end="")
