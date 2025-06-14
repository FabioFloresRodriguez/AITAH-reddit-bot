import re

def Update_Remover(string):
    number_words = r"\b(?:zero|one|two|three|four|five)\b"
    return re.sub(r"[\[\](:]*\bupdate\b[\s\d]*[\]:]*|" + number_words, "", string, flags=re.IGNORECASE).strip()   