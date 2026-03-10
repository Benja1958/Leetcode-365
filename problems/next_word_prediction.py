from collections import defaultdict
def word_prediction(sentences, prompt):
    if not sentences:
        return ""
    
    freq_words = defaultdict(int)
    target = prompt.split()[-1]

    #predict the next words and add the frequency in the dict
    for sentence in sentences:
        words = sentence.split()

        for i in range(len(words)- 1):
            if words[i] == target:
                freq_words[words[i + 1]] += 1

    #if hashmap empty then exit
    if not freq_words:
        return ""
    
    best_word = ""
    best_count = -1
    for word, count in freq_words.items():
        if count > best_count or (count == best_count and word < best_word):
            best_word = word
            best_count = count
    return best_word

if __name__ == "__main__":
    sentences = ["i love pizza", "i love coding", "i love pizza"]
    prompt = "pizza"
    print(word_prediction(sentences, prompt))

