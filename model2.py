import matplotlib.pyplot as plt
import pandas as pd

x = pd.read_csv("Datasets/kerala.csv")
y = pd.read_csv("Datasets/kerala.csv")

y1 = list(x["YEAR"])
x1 = list(x["Jun-Sep"])
z1 = list(x["JUN"])
w1 = list(x["MAY"])

plt.plot(y1, x1, '*')
plt.show()

june = []
sub = []

# APPROXIMATELY FINDING RAINFALL DATA FOR 10 DAYS FOR THE MONTH OF JUNE IN EVERY YEAR FROM 1901 TO 2018
for k in range(0, len(x1)):
    june.append(z1[k] / 3)

# FINDING THE INCREASE IN RAINFALL FROM THE MONTH OF MAY TO THE MONTH OF JUNE IN EVERY YEAR FROM 1901 TO 2018
for k in range(0, len(x1)):
    sub.append(abs(w1[k] - z1[k]))

df1 = pd.DataFrame({'per_10_days': june})

x["avg_june"] = june
x["sub"] = sub

# SAVING THE NEW CSV FILE WITH THE NEW COLUMNS
x.to_csv("out2.csv")
print(x)


