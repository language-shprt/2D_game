import json

with open('longman_3000_list.txt', encoding='utf-8') as input_data:
    frequent_words_list = input_data.readlines()

frequent_words_list = [line.split(' ')[0] for line in frequent_words_list]
frequent_words_list = [line.replace(',', '').replace('S1', '').replace('S2', '').replace('S3', '') for line in frequent_words_list]

words_with_lenths = {3: [], 4: [], 5: [], 6: [], 7: [], 8:[], 9: [], 10: []}

def filling_in_word_pull(word_length):
    for word in frequent_words_list:
        if len(word) == word_length and word.lower() not in words_with_lenths[word_length]:
            words_with_lenths[word_length].append(word.lower())

filling_in_word_pull(3)
filling_in_word_pull(4)
filling_in_word_pull(5)
filling_in_word_pull(6)
filling_in_word_pull(7)
filling_in_word_pull(8)
filling_in_word_pull(9)
filling_in_word_pull(10)
print(words_with_lenths)

with open('word_pull.json', mode='w',encoding='utf-8') as jason_file:
    json.dump(words_with_lenths, jason_file, indent=2, ensure_ascii=False)