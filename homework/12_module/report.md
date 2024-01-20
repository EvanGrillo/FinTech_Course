# Module 12: Supervised Learning & Predicting Loan Default

## Overview of the Analysis

The goal of this analysis is to develop a machine learning program for predicting loan defaults using various features such as loan size, interest rate, borrower income, debt-to-income ratio, number of accounts, derogatory marks and total debt. The dataset includes a 'loan status' property indicating whether a loan defaults (yes) or not (no).

The target feature (i.e. 'loan status') from the raw data set is imbalanced, with 75,036 good loans compared to only 2,500 bad loans. To showcase the importance of balanced data, there are two simulations, one that uses the raw imbalanced data and another that uses the imblearn library to balance the test data.

The first analysis involves splitting the data and applying a Logistic Regression algorithm from sklearn to make predictions. The predictions are then evaluated using a confusion matrix.

Next, the previous process is repeated while introducing the RandomOverSampler algorithm from imblearn to balance the training data. This rebalancing results in an equal distribution of good and bad loans.

The objective is to compare the performance of the model on the raw imbalanced dataset with that on the resampled balanced dataset.

## Results

### Machine Learning Model 1:
- Balanced Accuracy Score: 95%
- Class 1 Precision: 85%
- Class 1 Recall: 91%
- Class 1 F1: 88%

**Confusion Matrix:**
|             | Predicted 0 | Predicted 1 |
|-------------|-------------|-------------|
| Actual 0    | 18663       | 102         |
| Actual 1    | 56          | 563         |


### Machine Learning Model 2:
- Balanced Accuracy Score: 99%
- Class 1 Precision: 84%
- Class 1 Recall: 99%
- Class 1 F1: 91%

**Confusion Matrix:**
|             | Predicted 0 | Predicted 1 |
|-------------|-------------|-------------|
| Actual 0    | 18649       | 116         |
| Actual 1    | 4           | 615         |

## Summary

The results indicate a trade-off between higher recall and lower precision. In other words with the balanced training data, the model is more effective at catching bad loans. However, it also flagged more loans as bad that are actually good.

While neither result is perfect, the improvement in recall for class 1 is particularly valuable in scenarios where false negatives (predicting a bad loan as good) are costly.
