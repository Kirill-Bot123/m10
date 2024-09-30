import time # импортируем библиотеку для остановки времени
from threading import Thread # импортируем библиотеку для создания человечков :)
from datetime import datetime # импортируем библиотеку для замерения старта и конца программы


def write_words(word_count, file_name): # создаем функцию котороя принимает в себя название файла и количество
                                        # повторений строк в нем
    with open(file_name, 'w', encoding='utf-8') as file: # открываем файл в режиме записи
        for i in range(word_count): # создаем цикл для повторения строк
            file.write(f'Какое-то слово № {i + 1}\n') # записываем в файл какое-то слово и перемещаемся на следущую строку
            time.sleep(0.1) # останавливаем время на заданный промежуток
        print(f'Завершилась запись в файл {file_name}') # и при записи всех строк в файл выводим названия файла
                                                        # завершившого свою работу


start = datetime.now() # задаем начальный отсчет времени
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.now() # конец подсчета времени
res = start - end # записываем затраченное время

print(end) # выводим общее время
print('')
ex5 = Thread(target=write_words, args=(10, 'example5.txt'))
ex6 = Thread(target=write_words, args=(30, 'example6.txt'))
ex7 = Thread(target=write_words, args=(200, 'example7.txt'))
ex8 = Thread(target=write_words, args=(100, 'example8.txt'))

start_ex = datetime.now()
ex5.start()
ex6.start()
ex7.start()
ex8.start()

ex5.join()
ex6.join()
ex7.join()
ex8.join()
end_ex = datetime.now()
res_ex = start_ex - end_ex

print(res)
