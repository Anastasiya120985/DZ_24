# Задание 1
# Есть некоторый словарь, который хранит названия стран и столиц. Название страны используется в
# качестве ключа, название столицыв качестве значения. Необходимо реализовать: добавление данных,
# удаление данных, поиск данных, редактирование данных, сохранение и загрузку данных (используя
# упаковку и распаковку).
import json


class CountriesDict:
    def __init__(self):
        self.d = {}

    def load(self):
        with open('country.txt', mode='r', encoding='utf-8') as file:
            s = ''
            for string in file:
                s += str(string)
            self.d = json.loads(s)

    def save(self):
        with open('country.txt', mode='w', encoding='utf-8') as file:
            s = json.dumps(self.d, indent=4, ensure_ascii=False)
            file.writelines(s)

    def add(self):
        country = input('Введите название страны: ')
        capital = input('Введите столицу: ')
        self.d[country] = capital

    def find(self):
        try:
            return self.d[input('Введите название страны: ')]
        except:
            return 'Страна не найдена!'

    def delete(self):
        del self.d[input('Введите название страны: ')]

    def __str__(self):
        return str(self.d)


if __name__ == '__main__':
    d = CountriesDict()
    while True:
        print('1. Добавление данных')
        print('2. Удаление данных')
        print('3. Поиск данных')
        print('4. Редактирование данных')
        print('5. Сохранение данных')
        print('6. Загрузка данных')
        print('7. Показать список данных')
        print('8. Выход')

        choice = input('Выберите пункт меню "Страна - Столица": ')
        if choice == '1':
            d.add()
        elif choice == '2':
            d.delete()
        elif choice == '3':
            print(d.find())
        elif choice == '4':
            d.add()
        elif choice == '5':
            d.save()
        elif choice == '6':
            d.load()
        elif choice == '7':
            print(d)
        elif choice == '8':
            break
        else:
            print('Неверный пункт меню!')



# Задание 2
# Есть некоторый словарь, который хранит названия музыкальных групп(исполнителей) и альбомов.
# Название группы используется в качестве ключа, название альбомов в качестве значения.
# Необходимо реализовать: добавление данных, удаление данных, поиск данных, редактирование данных,
# сохранение и загрузку данных (используя упаковку и распаковку).
import pickle


class MusicDict:
    def __init__(self):
        self.d = {}

    def load(self):
        with open('music.pickle', 'rb') as file:
            self.d = pickle.load(file)

    def save(self):
        with open('music.pickle', 'wb') as file:
            pickle.dump(self.d, file)

    def add(self):
        musician = input('Введите исполнителя: ')
        album = input('Введите альбом: ')
        self.d[musician] = album

    def find(self):
        try:
            return self.d[input('Введите исполнителя: ')]
        except:
            return 'Исполнитель не найден!'

    def delete(self):
        del self.d[input('Введите исполнителя: ')]

    def __str__(self):
        return str(self.d)


if __name__ == '__main__':
    d = MusicDict()

    while True:
        print('1. Добавление данных')
        print('2. Удаление данных')
        print('3. Поиск данных')
        print('4. Редактирование данных')
        print('5. Сохранение данных')
        print('6. Загрузка данных')
        print('7. Показать список данных')
        print('8. Выход')

        choice = input('Выберите пункт меню "Исполнитель - Альбом": ')
        if choice == '1':
            d.add()
        elif choice == '2':
            d.delete()
        elif choice == '3':
            print(d.find())
        elif choice == '4':
            d.add()
        elif choice == '5':
            d.save()
        elif choice == '6':
            d.load()
        elif choice == '7':
            print(d)
        elif choice == '8':
            break
        else:
            print('Неверный пункт меню!')
