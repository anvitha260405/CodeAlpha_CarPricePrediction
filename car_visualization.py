import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car data.csv")

plt.scatter(df["Present_Price"], df["Selling_Price"])

plt.xlabel("Present Price")
plt.ylabel("Selling Price")
plt.title("Present Price vs Selling Price")

plt.show()