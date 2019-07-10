import matplotlib.pyplot
import
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
valores2 = [11523, 117697, 120256, 119236, 118859, 119986]

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.plot(meses, valores2)
matplotlib.pyplot.ylim(100000, 120000)
matplotlib.pyplot.show()
