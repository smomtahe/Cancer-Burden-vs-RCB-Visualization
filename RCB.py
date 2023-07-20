import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

# Define the data
predicted_cancer_burden = [0.743, 0.0, 0.0, 0.601, 0.385, 0.563, 0.11, 0.585, 0.257,0.383, 0.158, 0.284, 0.472, 0.027, 0.452, 0.576, 0.677, 0.045, 0.339, 0.072, 0.383, 0.262, 0.435]
rcb_known = [3.532, 0.0, 0.0, 2.510, 2.178, 1.986, 0, 2.827, 1.264,  1.685, 0.696, 0.885, 1.630, 0.000, 1.988 , 2.534, 2.977, 0.000, 1.493, 0.000, 1.685, 1.151, 1.1]

# Group the predicted cancer_burden values
group0 = []
group1 = []
group2 = []
group3 = []
for i in range(len(predicted_cancer_burden)):
    if predicted_cancer_burden[i] == 0.027 or predicted_cancer_burden[i] == 0.0:
        group0.append(i)
    elif predicted_cancer_burden[i] == 0.284 or predicted_cancer_burden[i] == 0.257:
        group1.append(i)
    elif predicted_cancer_burden[i] == 0.472 or predicted_cancer_burden[i] == 0.585 or predicted_cancer_burden[i] == 0.563 or predicted_cancer_burden[i] == 0.385 or predicted_cancer_burden[i] == 0.601:
        group2.append(i)
    else:
        group3.append(i)

# Calculate the linear regression line
slope, intercept = np.polyfit(predicted_cancer_burden, rcb_known, 1)
x = np.array(predicted_cancer_burden)
y = slope * x + intercept

# Calculate the accuracy
accuracy = r2_score(rcb_known, slope * np.array(predicted_cancer_burden) + intercept)

# Create the plot
plt.scatter(np.array(predicted_cancer_burden)[group0], np.array(rcb_known)[group0], color='blue', label='RCB-0')
plt.scatter(np.array(predicted_cancer_burden)[group1], np.array(rcb_known)[group1], color='green', label='RCB-I')
plt.scatter(np.array(predicted_cancer_burden)[group2], np.array(rcb_known)[group2], color='purple', label='RCB-II')
plt.scatter(np.array(predicted_cancer_burden)[group3], np.array(rcb_known)[group3], color='orange', label='RCB-III')
plt.plot(x, y, color='red')
plt.xlabel('Cancer Burden (Predicted)')
plt.ylabel('RCB (Known)')
plt.title('Cancer Burden vs. RCB')
plt.legend()

plt.text(0.25, 3, f'Accuracy = {accuracy:.2f}')

# Show the plot
plt.show()
