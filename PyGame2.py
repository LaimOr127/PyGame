# Игра Виселица
import random
import time

#Возможные слова для добавления в игру

#Abide, Abode, About, Above, Abuse, Abyss, Ached, Aches, Acids, Acing, Ackee, Acorn, Acres,
# Acrid, Acted, Actor, Adapt, Added, Adder, Addle, Adieu, Adios, Adits, Adman, Admin, Adobe,
# Adobo, Adopt, Adore, Adorn, Adult, Adzes, Aegis, Aeons, Aerie, Affix, Afire, Afoot, Afore,
# After, Again, Agape, Agate, Agave, Agent, Aggro, Agile, Aging, Aglow, Agony, Agora, Agree,
# Ahead, Ahold, Aided, Aider, Aides, Ailed, Aimed, Aimer, Aioli, Aired, Aisle, Alarm, Album,
# Alder, Aleph, Alert, Algae, Alias, Alibi, Alien, Align, Alive, Alkyd, Alkyl, Allay, Alley,
# Allot, Allow, Alloy, Allyl, Aloft, Aloha, Alone, Along, Aloys, Alpha, Altar, Alter, Amaze,
# Amber, Ambit, Amble, Ambos, Ambry, Ameer, Amend, Amens, Ament, Amias, Amice, Amide, Amigo,
# Amine, Amino, Amity, Ammos, Among, Amort, Amour, Amped, Ample, Amply, Amuck, Amuse, Ancho,
# Ancon, Andro, Anear, Anele, Angel, Anger, Angle, Angry, Angus, Anima, Anime, Animus, Anion,
# Anise, Ankhs, Ankus, Annal, Annoy, Annul, Annus, Anode, Anole, Anomy, Antae, Antas, Anted,
# Antes, Antic, Antis, Antra, Antre, Anvil, Aorta, Aouda, Apart, Apeak, Apeek, Apers, Apexes,
# Aphid, Apian, Aping, Apish, Apnea, Apods, Aport, Appal, Appel, Apple, Apply, Apron, Apres,
# April, Apron, Apse, Apsis, Apter, Aptly, Aquae, Aquas, Araks, Arame, Araks, Arame, Araks,
# Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame,
# Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks,
# Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame,
# Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks, Arame, Araks


# список слов для угадывания
words = ['python', 'java', 'javascript', 'ruby', 'php', 'html', 'css']

# выбираем случайное слово из списка
word = random.choice(words)

# создаем список, который будет хранить угаданные буквы
guessed = []

# количество попыток
tries = 6

# функция для отображения текущего состояния игры
def display():
    # выводим загаданное слово с учетом угаданных букв
    for letter in word:
        if letter in guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    # выводим количество оставшихся попыток
    print('Tries left:', tries)

# функция для проверки угаданной буквы
def check(letter):
    global tries

    # если буква уже была угадана, сообщаем об этом
    if letter in guessed:
        print('You already guessed that letter!')
        return

    # добавляем угаданную букву в список
    guessed.append(letter)

    # если угаданная буква не входит в слово, уменьшаем количество попыток
    if letter not in word:
        tries -= 1

    # проверяем, остались ли еще неотгаданные буквы
    for letter in word:
        if letter not in guessed:
            break
    else:
        print('Congratulations, you won!')
        return

    # если попытки закончились, сообщаем об этом
    if tries == 0:
        print('Sorry, you lost. The word was', word)
        return

    # отображаем текущее состояние игры
    display()

# начало игры
print('Welcome to Hangman!')
display()

# основной цикл игры
while True:
    # запрашиваем у пользователя букву
    letter = input('Guess a letter: ')

    # проверяем угаданную букву
    check(letter)

    # задержка перед следующим ходом
    time.sleep(1)