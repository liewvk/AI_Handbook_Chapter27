tp, fn, tn, fp = 16, 4, 72, 8
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
precision = tp / (tp + fp)
accuracy = (tp + tn) / (tp + fn + tn + fp)
print(f"Sensitivity: {sensitivity:.1%}")
print(f"Specificity: {specificity:.1%}")
print(f"Precision: {precision:.1%}")
print(f"Accuracy: {accuracy:.1%}")

