# Module 14: Machine Learning & Trading

## Summary

The objective is to use a dataset to build models that could automate trading using Python's sklearn library.

## Process and Results

The first step is to compute three new series - actual returns, short and long, that are the percent change and rolling averages respectively of the close price. 

We also add a signal column. When the percent change of a close price is negative, we assign a negative or sell signal, whereas when it's positive or zero, we assign a positive or buy signal. The signals wil be used as triggers to buy or sell stock.

To split training and testing data, we use a date range to slice the data set.

We also use Standard Scaler to balance features.

Then we create an instance of SVC model to fit the data and make predictions.

This is the result of the strategy using the SVC Model:

  precision    recall  f1-score   support

        -1.0       0.43      0.04      0.07      1804
         1.0       0.56      0.96      0.71      2288

    accuracy                           0.55      4092
   macro avg       0.49      0.50      0.39      4092
weighted avg       0.50      0.55      0.43      4092

![SVC](./Resources/svc_strategy.png)

Logistic Regression Result:

precision    recall  f1-score   support

        -1.0       0.44      0.33      0.38      1804
         1.0       0.56      0.66      0.61      2288

    accuracy                           0.52      4092
   macro avg       0.50      0.50      0.49      4092
weighted avg       0.51      0.52      0.51      4092
![Logistic Regression](./Resources/logistic_regression_strategy.png)


