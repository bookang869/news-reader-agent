from crewai.tools import tool


@tool
def count_letters(sentence: str):
    # doc string (""""""): a string that documents what a function does
    # CrewAI uses doc string to create a schema when creating a function
    """
    This function is to count the amount of letterrs in a sentence.
    The input is a 'sentence' string.
    The output is a number.
    """
    return len(sentence)
