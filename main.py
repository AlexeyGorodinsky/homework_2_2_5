import chardet

from chardet.universaldetector import UniversalDetector


def top_words(filename, number_of_words, word_l):

    detector = UniversalDetector()

    with open(filename, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        code_type = detector.result['encoding']
        print('Файл {} выполнен в кодировке {}' .format(filename, code_type), '\n')

    with open(filename, encoding=code_type) as f:

        content = f.read()
        s = content.lower()
        deleted_chars = '.,!:;?'
        for char in deleted_chars:
            s = s.replace(char, "")
        all_words = s.split(' ')
        dic = {}

        for x in all_words:
            if (len(x) >= word_l):
                k = s.count(x)
                dic[x] = k
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        print('{} слов длиннее {} букв, наиболее часто встречающихся в {}: \n'
              .format(number_of_words, word_l, filename))
        q = 1
        for z in dic:
            if (q > number_of_words):
                break
            q = q + 1
            print(str(z))


filename = input('Введите название файла в формате "name.txt": ')
number_of_words = int(input('Укажите, какое число наиболее часто встречающихся слов Вы хотите найти: '))
word_l = int(input('Укажите минимальную длину слов, участвующих в "рейтинге" наиболее часто встречающихся: '))

c = top_words(filename, number_of_words, word_l)
print(c)
