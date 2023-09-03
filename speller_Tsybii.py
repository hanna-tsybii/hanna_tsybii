import string

def load_dictionary(file_name):
    """
    Завантажує словник з файлу і повертає його у вигляді множини слів.
    :param file_name: Назва файлу словника
    :return: Множина слів
    """
    with open(file_name, 'r') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

def check_spelling(input_file, dictionary_file, output_file):
    """
    Виконує перевірку правопису тексту з вхідного файлу на основі словника.
    Виявлені помилки записуються у файл результату.
    :param input_file: Назва вхідного файлу з текстом
    :param dictionary_file: Назва файлу словника
    :param output_file: Назва файлу результату з помилками
    """
    dictionary = load_dictionary(dictionary_file)
    errors = set()

    with open(input_file, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                processed_word = word.lower().rstrip("'s")
                # Виключаємо знаки пунктуації із перевірки
                processed_word = processed_word.translate(str.maketrans('', '', string.punctuation))
                if processed_word and processed_word not in dictionary:
                    errors.add(processed_word)

    with open(output_file, 'w') as file:
        for error in errors:
            file.write(error + '\n')

if __name__ == '__main__':
    """
    Точка входу у програму.
    """
    # Параметри програми
    input_file = 'shakepeare.txt'
    dictionary_file = 'dictionary.txt'
    output_file = 'errors.txt'

    check_spelling(input_file, dictionary_file, output_file)
