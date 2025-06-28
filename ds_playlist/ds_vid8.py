import matplotlib.pyplot as plt
import numpy as np

nationalities = ['American', "Indian", "Spanish", "German"]
students = [60, 40, 50, 20]
explode = [0,0,0,0.1]
pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)


plt.pie(students, labels=nationalities, autopct="%.2f%%", explode=explode, counterclock=False, startangle=90)
plt.title("Student Nationalities")
plt.show()