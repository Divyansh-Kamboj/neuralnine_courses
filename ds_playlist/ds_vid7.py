import matplotlib.pyplot as plt
import numpy as np

python = (20,55,79)
java = (45, 25, 18)
machine_learning = (30, 40, 80)
people = ['bob', 'anna', 'john']

index = np.arange(3)

plt.bar(index, python, width=0.2, label="Python")
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index + 0.4, machine_learning, width=0.2, label="Machine Learning")

plt.title("Skill levels")
plt.xlabel("Person")
plt.ylabel("Skill level")
plt.xticks(index+0.2, people)
plt.legend(loc="upper left")
plt.ylim(0,100)

plt.show()