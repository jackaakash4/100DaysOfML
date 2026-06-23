#Day02: OOPs concept in ML

class BaseModel:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version

    def describe(self):
        return f"{self.model_name} v{self.version}"


class LinearRegression(BaseModel):
    def train(self, X, y):
        print(f"Training {self.describe()} on {len(X)} samples")


model = LinearRegression("LinearRegression", "1.0")
model.train([1, 2, 3], [2, 4, 6])


