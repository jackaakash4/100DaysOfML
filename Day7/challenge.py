#load the tips dataset

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

#task
#create a violin plot

sns.violinplot(
        data = tips,
        x = "day",
        y = "total_bill"
        )

plt.title("Total bill ditribution by day")
plt.show()
