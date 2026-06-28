import plotly.express as px
import pandas as pd

#dataframe

df = pd.DataFrame({
    "Accuracy":[0.82,0.91,0.95,0.88],
    "Latency":[120,80,70,95],
    "Model_ID":[101,102,103,104]
})

print("\nDataframe\n", df)

fig = px.scatter(
        df,
        x = "Latency",
        y = "Accuracy",
        hover_data = ["Model_ID"],
        title = "Model performance"
        )

fig.show()
