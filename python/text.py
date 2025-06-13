text = input("Enter your text: ")

if text.strip() == "":
    print("Error: Text cannot be empty!")
else:
    text = text.lower()
    text = text.replace("!", "").replace(".", "").replace(",", "").replace("?", "")
    
    words = text.split()
    print(f"Cleaned word list: {words}")
    
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    print(f"Number of unique words: {len(unique_words)}")
    
    encoding_dict = {}
    count = 1
    for word in unique_words:
        encoding_dict[word] = count
        count += 1
    # for i, word in enumerate(unique_words, 1):
    #     encoding_dict[word] = i
    print(f"Encoding dictionary: {encoding_dict}")

    encoded_list = []
    for word in words:
        encoded_list.append(encoding_dict[word])
    print(f"Encoded numeric list: {encoded_list}")