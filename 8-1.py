from matplotlib import pyplot as plt
import numpy as np

#---------------
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("dataa.txt", dtype = int)
data_array = data_array / 256 * 3.3

x_array = []
for i in range(len(data_array)):
    x_array.append(i / tmp[0])

data_array = list(data_array)
x_array = list(x_array)

# Время зарядки
charge_time = x_array[data_array.index(max(data_array))]

# сложная математика((((((((
idx = np.abs(np.array(x_array) - charge_time).argmin()

# жесткая kлиния та самая 
plt.axvline(x=charge_time, color='black', linestyle='--')

# Прикольную идея увидел, не зря в художку ходил
plt.plot(x_array[:idx], data_array[:idx], ".-",  c = 'purple', linewidth=2, markevery = 4, mfc = "orange", label = "Зарядка кондера" )
plt.plot(x_array[idx:], data_array[idx:], ".-", c = 'orange', linewidth=2, markevery = 4, mfc = "purple", label = "Разрядка кондера")

# я легенда - хороший кста фильм
plt.text(3, 0.6, f"Время зарядки: {round(charge_time, 2)} с", fontsize=8, ha='right')
plt.text(6, 0.6, f"Время разрядки: {round(x_array[-1]-charge_time, 2)} с", fontsize=8, ha='left')
plt.title("График напряжения на конденсаторе в RC-цепи")
plt.legend ()

# рыболовная Сетка
plt.minorticks_on()
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='minor', linestyle='--', linewidth=1, color='0.8')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[english, russian]{babel}')

# Берлин, Рим, Токио
axis_lw = 2
ax = plt.gca()
ax.set_xlim([0, 10])
ax.set_ylim([0, 3.3])
ax.set_xlabel("Время, c")
ax.set_ylabel("Напряжение, B")

# Страны варшавского договора
plt.rc('axes', linewidth=axis_lw)
plt.rc('xtick.major', width=axis_lw)
plt.rc('xtick.minor', width=0)
plt.rc('xtick', direction='in')
plt.rc('axes', labelsize=20)
plt.rc('ytick.major', width=axis_lw)
plt.rc('ytick.minor', width=0)
plt.rc('ytick', direction='in')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('xtick.major', pad=10)
plt.rc('ytick.major', pad=10)

#ищи себя в прошмандо.... ой точнее на кафедре общефиза
plt.savefig("test.png")

plt.show()
