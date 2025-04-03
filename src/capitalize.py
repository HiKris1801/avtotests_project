#def capitalize(text):
    #return text.lower()

def capitalize(text):
    if not text:
        return ''
    return text[0].upper() + text[1:]
