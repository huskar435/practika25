from oktagon import Oktagon #Импортируем класс

def main(): #Создаем функцию 
    first = Oktagon(8) #Добавляем объект
    first.plo() #Используем все имеющиеся методы
    first.per()
    first.opis_okr()
    first.vpis_okr()
    first.pic()

if __name__ == '__main__': 
    main() 