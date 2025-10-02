import matplotlib.pyplot as plt

#Пример 1. График
x = [0.5, 2, 3.5, 5, 6.5]
y = [12, 24, 36, 24, 12]

plt.xlabel('Ось х') 
plt.ylabel('Ось y') 
plt.title('Крыша перед съездом') 
plt.plot(x, y, color='red') 

plt.show()



#Пример 2. Диаграмма
rating = [1.5, 1.5, 3, 47, 47]
subject = ["Физика", "Ан. Геометрия", "Мат. Анализ", "Физкультура", "Иностр. язык"]

plt.pie(rating, labels=subject, autopct='%1.f%%')
plt.title("Распределение предметов на ФизТехе по важности (Пакмен)")

plt.show()



#Пример 3. Столбчатая диаграмма
x = ['Коллоквиум', 'Домашку', 'Контест', 'Лабу']
y = [5, 8, 10, 40]

plt.bar(x, y, alpha=0.3)
plt.plot(x, y, color='pink', marker='^', markersize=7)
plt.xlabel('Когда сдал')
plt.ylabel('Уровень счастья')
plt.title('Столбчатая диаграмма')

plt.show()