import random as random

libnouns = {
    "мочь": 'moa',
    "добавить": 'dos',
    "движение": 'tu',
    "просить": 'pra',
    "жить": 'ru',
    "место": 'pl',
    "старение": 'si',
    "инструмент": 'hl',
    "орган": 'gi',
    "еда": 'sho',
    "приветствие": 'uo',
    "ед.ч": 'cie',
    "мн.ч": 'mie',
    "смерть:": 'ur',
    "существо": 'so',
    "человек": 'chu',
    "размножение": 'se',
    "м.род": 'mu',
    "ж.род": 'me',
    "обратное значение": 'nas',
    "подобное значение": 'mos',
    "раз": 'rum',
    "быть": 'bu',
    "сверх, супер": 'sum',
    "ум, интеллект": 'um',
    "делать, создавать": 'du',
    "слова": 'sl',
    "если": 'fi',
    "иначе": 'ifn',
    "пока": 'fan',
    "нет": 'ne',
    "да": 'ui',
    "хорошо, спокойно": 'gu',
    "как, словно": 'cok',
    "название, имя": 'niem',
    "благодарность": 'ba',
    "безразличие": 'bon',
    "далеко": 'pan',
    "получение": 'sod',
    "длина, расстояние": 'dl',
    "плюс": 'plu',
    "минус": 'mlu',
    "сам": 'dum',
    "желать": 'guh',
    "настроение": 'nu'
}
libvar = {
    '1': 'yes',
    '0': 'no'
}
libwords = {
    'дом': 'rerupl'
}


class app:
    def __init__(self):
        self.place = 'disk'
        self.main()

    def main(self):
        print('\nthis place:', self.place)
        if self.place == 'disk':
            print('next place: translate or random ')
        message = input('go to: ')
        if message == 'translate':
            self.place = 'translate'
            self.translate()
        elif message == 'random':
            self.place = 'random'
            self.randomaser()
        elif message == 'back':
            if self.place == 'random' or 'translate':
                self.place = 'disk'
                self.main()
            elif self.place == 'part' or 'random':
                self.place = 'translate'
                self.main()
        else:
            print('\n<command not found, return>\n')
            self.main()
        while self.place:
            continue

    def translate(self):
        message = input('\nin translate: part or words\ngo to:')
        if message == 'part':
            self.place = 'part'
            self.translatepart()
        elif message == 'words':
            self.place = 'words'
            self.translatewords()
        else:
            print('\n<command not found, return>\n')
            self.main()

    def translatepart(self):
        message = input('\nrus or moas:')
        if message == 'rus':
            message = input('\nwrite word:')
            print(libnouns[message])
        elif message == 'moas':
            def get_key(libpart, value):
                for k, v in libpart.items():
                    if v == value:
                        return k

            message = input('\nwrite word:')
            print(get_key(libnouns, message))
        self.bkpl = 'part'
        self.back()

    def translatewords(self):
        message = input('\nwrite word:')
        print(libwords[message])
        self.bkpl = 'words'
        self.back()

    def randomaser(self):
        temp = str(round(random.randrange(0, 1)))
        print(libvar[temp])
        self.back()

    def back(self):
        message = input('back? y/n:')
        if message == 'y':
            self.main()
        elif message == 'n':
            if self.bkpl == 'words':
                self.translatewords()
            elif self.bkpl == 'part':
                self.translatepart()
            else:
                self.back()


app()
