#Core essentials
#A. Datatypes
#Lists: datasets, predictions, features

accuracies = [0.82, 0.87, 0.92, 0.89]
print(max(accuracies))

#dicts
#Metadata, configurations

model_config = {
        "learning_rate" : 0.001,
        "epochs": 10,
        "batch_size" : 32
        }

print(model_config)
print("Model config's epouchs value :", model_config['epochs'])

#tuple: fixed value
#tensor dimensions, coordinates, immutable settings

image_size = (224, 224, 3)

#control flow
#if statements
#decide whether a model meets perfomance requirements or not

accuracy = 0.92

if accuracy > 0.90:
    print("Deploy model")
else: 
    print("Train more")


#loops
#for loop
#iterate through datasets, process prediction, evalyate metrics

scores = [0.80, 0.85, 0.90]
for score in scores:
    print(score)


#Function
#backbone of AI pipelines`
#data preprocessing, training steps, evaluation logic, feature engineering`

def evaluate_model(predictions):
    return sum(predictions) / len(predictions)

print(evaluate_model(scores))


