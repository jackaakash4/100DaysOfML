#Challenge 1
#Build a class that stores a model’s name and version, then logs a dummy training result.

class ModelTrainer:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version
        self.logs = []

    def log_result(self, accuracy, loss):
        result = {
                "model_name": self.model_name,
                "version": self.version,
                "accuracy": accuracy,
                "loss": loss,
                }
        self.logs.append(result)
        print(f"Logged: {result}")

trainer = ModelTrainer("Textgenerator", "2.0")
trainer.log_result(accuracy = 0.90, loss = 0.10)

#Challenge 2
#The model architecture of AI

class AIModel:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version

    def __str__(self):
        return f"Model: {self.model_name} | Version: {self.version}"

class TextGenerator(AIModel):
    def generate(self):
        print("Generating text ......")

model = TextGenerator("GPT 1", "1.0")
print(model)    #inherited info via __str__(dunder)
model.generate()    #child-class method
                
