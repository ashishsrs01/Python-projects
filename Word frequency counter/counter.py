def counter(text):
    word_count = {}

    for word in text.split():
        word = word.lower()
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    return word_count
def 
if __name__ == "__main__":
    text = "Hello world! Hello everyone."
    result = counter(text)
    print(result)