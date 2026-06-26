#boolean filtering
#one of the most import skill 
import pandas as pd

#dataset
df = pd.DataFrame({
    "Model_Type": ["CNN", "Transformer", "Transformer", "LSTM"],
    "Accuracy": [0.85, 0.91, 0.96, 0.88]
})

#single condition
print("Model having accuracy more than 0.90: \n", df[df["Accuracy"] > 0.90])

#multiple conditions
#AND(&)
print("Model having type transfomer and accuracy more than 0.90 \n", df[(df["Accuracy"] > 0.90 ) & (df["Model_Type"] == "Transformer")])


#OR(|)

print("Model having accuracy more than 0.90 or type CNN \n", df[(df["Accuracy"] > 0.90) | (df["Model_Type"] == "CNN")])

