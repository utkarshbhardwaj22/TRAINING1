"""
    GUI based program for predictions with some ML model

"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import tkinter as tk

model = None
RnD_Spend= None
M_Spend = None
entry_X1 = None
entry_X2 = None
canvas = None
window = None

def on_click():

    global model
    global RnD_Spend
    global M_Spend
    global entry_X1
    global entry_X2
    global canvas
    global window
    canvas = tk.Canvas(window, width=500, height=300)
    canvas.pack()

    RnD_Spend = float(entry_X1.get())
    M_Spend = float(entry_X2.get())

    print(RnD_Spend)
    print(M_Spend)

    predicted_profit = model.predict([[RnD_Spend, M_Spend]])
    predicted_text = ("Predicted Profit", predicted_profit)

    lbl_predicted_results = tk.Label(window, text=predicted_text)
    canvas.create_window(260, 280, window=lbl_predicted_results)




def prepare_model():


    global model
    global RnD_Spend
    global M_Spend
    global entry_X1
    global entry_X2
    global canvas
    global window

    data_set = pd.read_csv("company.csv")
    X = data_set[['R&D Spend', 'Marketing Spend']]
    Y = data_set['Profit']

    model = LinearRegression()
    model.fit(X, Y)

    print("Interceptor: ", model.intercept_)
    print("Coefficients: ", model.coef_)

    RnD_Spend = 165349.2
    M_Spend = 471784.1
    predicted_profit = model.predict([[RnD_Spend, M_Spend]])
    print("Predicted Profit: ", predicted_profit)





def main():

    global entry_X1, entry_X2

    prepare_model()

    window = tk.Tk()

    canvas = tk.Canvas(window, width=500, height=300)
    canvas.pack()

    intercept_text = ("Interceptor", model.intercept_)
    lbl_intercept_text = tk.Label(window, text=intercept_text, justify="center")
    lbl_intercept_text.pack()

    coef_text = ("Coefficients", model.coef_)
    lbl_coef_text = tk.Label(window, text=coef_text, justify="center")
    lbl_coef_text.pack()

    lbl_X1 = tk.Label(window, text="R&D Spend:")
    canvas.create_window(100, 100, window=lbl_X1)

    entry_X1 = tk.Entry(window)
    canvas.create_window(260, 100, window=entry_X1)

    lbl_X2 = tk.Label(window, text="Marketing Spend:")
    canvas.create_window(110, 130, window=lbl_X2)

    entry_X2 = tk.Entry(window)
    canvas.create_window(260, 130, window=entry_X2)

    btn_predict = tk.Button(window, text="Predict Profit", command=on_click)
    canvas.create_window(260, 160, window=btn_predict)

    window.mainloop()

if __name__ == '__main__':
    main()