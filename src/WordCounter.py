class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        words = self.sentence.split()
        return len(words)


    def get_word_count(self):
        return self.count_words()

    def get_shortest_word(self):
        words = self.sentence.split()
        shortest_word = min(words, key=len)
        return len(shortest_word)

    def get_longest_word(self):
        words = self.sentence.split()
        longest_word = max(words, key=len)
        return len(longest_word)


# sentence = "This is a test of the emergency broadcast system"
# word_counter = WordCounter(sentence)
# word_counter.count_words()
#
# print(word_counter.get_word_count())    # Returns the number of all the words.
# print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
# print(word_counter.get_longest_word())  # Returns the length of the longest word.
