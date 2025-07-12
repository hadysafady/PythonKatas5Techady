def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    if not sentence[0].isdigit():
        cnt_words = 1
    else :
        cnt_words = 0
    for i in range(len(sentence)):
        if sentence[i] == " " and not sentence[i+1].isdigit():
            cnt_words = cnt_words + 1
    return cnt_words


if __name__ == '__main__':
    sentence = "This is a sample example for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed
