import os
import xml.etree.ElementTree as ET


def count_words(file_path):
    extension = os.path.splitext(file_path)

    word_count = {}

    if extension[1] == '.xml':
        tree = ET.parse(file_path)
        root = tree.getroot()

        for item in root.findall('.//item'):
            description = item.find('.//description').text
            words = description.split()
            for word in words:
                if len(word) > 6:
                    word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]


folder_path = "D:/Python/pyqa9"
xml_file_path = os.path.join(folder_path, "newsafr.xml")
xml_top_words = count_words(xml_file_path)

print('Топ 10 слов (XML файла): ')
for word, count in xml_top_words:
    print(word, count)
