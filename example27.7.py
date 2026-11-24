actual = [12, 15, 14, 18]
baseline = [11, 12, 15, 14]
model = [12, 14, 15, 17]
def mae(y_true, y_pred):
    return sum(abs(a - p) for a, p in zip(y_true, y_pred)) / len(y_true)
print(f"Baseline MAE: {mae(actual, baseline):.2f}")
print(f"Model MAE: {mae(actual, model):.2f}")

