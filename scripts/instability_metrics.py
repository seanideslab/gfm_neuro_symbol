#!/usr/bin/env python3
import math

TP, FN, TN, FP = 246, 4, 248, 2

sensitivity = TP / (TP + FN)
specificity = TN / (TN + FP)
accuracy = (TP + TN) / (TP + TN + FP + FN)
balanced = 0.5 * (sensitivity + specificity)

den = math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
mcc = ((TP*TN - FP*FN) / den) if den else float("nan")

n = TP + TN + FP + FN
k = TP + TN
z = 1.959963984540054
phat = k / n
center = (phat + z*z/(2*n)) / (1 + z*z/n)
half = z * math.sqrt((phat*(1-phat) + z*z/(4*n))/n) / (1 + z*z/n)

print(f"sensitivity={sensitivity:.4f}")
print(f"specificity={specificity:.4f}")
print(f"accuracy={accuracy:.4f}")
print(f"balanced_accuracy={balanced:.4f}")
print(f"MCC={mcc:.4f}")
print(f"Wilson95=[{center-half:.4f}, {center+half:.4f}]")
