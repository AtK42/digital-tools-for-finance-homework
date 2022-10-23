import csv
import pandas as pd
import matplotlib.pyplot as plt

# read data
path = r"./coding-environment-exercise.csv"
df = pd.read_csv(path, index_col = 0, header = 0)

def main():
    df.plot(color = "red")
    plt.xticks(rotation = 45, size = 6)
    plt.title("Stock price evolution")
    plt.xlabel("date", fontsize = 12)
    plt.ylabel("value", fontsize = 12)
    print("your plot is ready master")
    plt.show()


if __name__ == "__main__":
    main()