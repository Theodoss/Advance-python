def main():
    filename = 'cs.txt'
    common_word = ['is','a','the']
    d = read_file(filename,common_word)
    print(d)
    print(get_most_frecqence(d,1))

def read_file(filename,common_word):
    word_dict = {}
    with open (filename, 'r') as f:
        for line in f:
            line = line.split()
            for word in line:
                word = word.lower()
                if word not in common_word:
                    if word not in word_dict:
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
    return  word_dict

def get_most_frecqence(d,n):
    most_list = []
    for word,f in d.items():
        if f >n:
            most_list.append(word)
    return most_list



if __name__ == "__main__":
    main()