def read_sentences (filename='corpus.txt'):
    lines = []

    with open(filename, 'rb') as corpus_file:
        content = corpus_file.read().decode('utf-8')
        lines = content.split('\n')
    
    lines = [line.split('#')[0].strip() for line in lines if line]

    return lines

if __name__ == "__main__":
    print("Showing Beanish corpus:")
    print("=======================")
    for sentence in read_sentences():
        print(sentence)
