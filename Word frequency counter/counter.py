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
    print("Welcome to the Word Frequency Counter!")
    text = input("Please enter a string of text: ")
    n = input(' what do you want to count - word or letter? (W/L)').lower()
    if n == 'w':
        result = word_counter(text)
        print("Word Frequency Count:")
        for word, count in result.items():
            print(f"{word}: {count}")
    elif n == 'l':
        result = alphabetical_counter(text)
        print(f"The letter appears {result} times in the text.")
    else:
        print("Invalid input. Please enter 'W' for word count or 'L' for letter count.")