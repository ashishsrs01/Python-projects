def counter(n):








def word_counter(text):
    word_count = {}

    for word in text.split():
        word = word.lower()
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    return word_count

def alphabetical_counter(text):
    count = 0
    letter = input("Enter a letter to count: ").lower()
    for char in text:
        if char.lower() == letter:
            count +=1
    return count


if __name__ == "__main__":
    