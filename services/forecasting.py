import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast():
    df = pd.read_csv("data/sales_data.csv")

    X = df[['day']]
    y = df['sales']

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[30]])

    return float(prediction[0])
