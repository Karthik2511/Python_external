with open('input.txt', 'r') as file:
    sentences = file.readlines()

reversed_sentences = sentences[::-1]

for sentence in reversed_sentences:
    print(sentence.strip())  # .strip() removes any extra newlines or spaces
