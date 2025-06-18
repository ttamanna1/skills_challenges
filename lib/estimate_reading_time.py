def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate a reading time for an empty text")
    words = text.split()
    word_count = len(words)
    return word_count / 200