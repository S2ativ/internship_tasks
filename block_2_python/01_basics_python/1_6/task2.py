import numpy as np

days = np.arange(0, 10000, 1)

temp = 15 + 10 * np.sin(days * (2 * np.pi / 365)) + np.random.normal(0, 2.5, 10000)

sr_t = np.mean(temp)
st_otkl = np.std(temp)
max_t = np.max(temp)
min_t = np.min(temp)

max_zn = np.argmax(temp)
min_zn = np.argmin(temp)

low_sr = np.where(temp < sr_t, 1, 0)
low_sr2 = np.concatenate(([0], low_sr, [0]))
differ = np.diff(low_sr2)
start = np.where(differ == 1)[0]
end = np.where(differ == -1)[0]
max_days = np.max(end - start)

print(f"Средняя температура: {sr_t:.2f}")
print(f"Стандартное отклонение: {st_otkl:.2f}")
print(f"Максимальная температура : {max_t:.2f} индекс:{max_zn}")
print(f"Минимальная температура : {min_t:.2f} индекс:{min_zn}")
print(f"Максимальное количество дней подряд,когда температура была ниже средней: {max_days}")
