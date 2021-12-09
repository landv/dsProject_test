import pandas as pd
import random
from report import createPdf


def main():

    # Read csv file
    df = pd.read_csv('data.csv', delimiter=';')
    df = df.sample(n=3)

    # Create quantity column and add values
    quantities = [random.randrange(1, 6, 1) for i in range(df.shape[0])]
    df['quantity'] = quantities

    # Create pdf file
    createPdf(products=df)


if __name__ == "__main__":
    main()
