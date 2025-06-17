import re

def Original_Title(string):
    update_words = r"\b(?:zero|one|two|three|four|five|final)\b"
    return re.sub(r"[\[\](:]*\bupdate\b[\s\d]*[\]:]*|" + update_words, "", string, flags=re.IGNORECASE).strip()   