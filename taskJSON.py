import os
import json


def get_top_words(file_path):
    with open("./newsafr.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    words_count = {}
    for news in data['rss']['channel']['items']:
        description = news['description']
        words = description.split()

        words = [word for word in words if len(word) > 6]

        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

    top_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_words


def main():
    folder_path = 'D:/Python/pyqa9'
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    for file in json_files:
        file_path = os.path.join(folder_path, file)
        print(f'Top 10 words in file {file}: ')
        top_words = get_top_words(file_path)
        for word, count in top_words:
            print(f'Word: {word}, Count: {count}')
        print()


if __name__ == '__main__':
    main()
