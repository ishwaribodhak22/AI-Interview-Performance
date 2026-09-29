fillers = ["um", "uh", "like", "actually", "basically", "you know"]

def count_fillers(text):
    text = text.lower()
    count = 0

    for word in fillers:
        count += text.count(word)

    return count