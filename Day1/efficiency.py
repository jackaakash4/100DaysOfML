#list comprehension

#traditional
scores = [0.70, 0.88, 0.91, 0.67]

high_scores = []

for s in scores:
    if s > 0.80:
        high_scores.append(s)

print(high_scores)

#comprehension

high_scores_com = [s for s in scores if s > 0.80]
print("High scores from comprehension: ", high_scores_com)


#Dicts comprehension
accuracies = [0.82, 0.91, 0.88]

model_results = {
        f"model_{i}": acc
        for i, acc in enumerate(accuracies)
        }
print(model_results)


#lambda function
#quick anonymous function

double_scores = lambda x: x * 2
print("Use of lambda to double scores: ", double_scores)

#map() function
#apply a transformation to every items
percentage = list(
        map(lambda x: x * 100, scores)
        )
print("Use of map() to apply lambda function to every elements: ", percentage)

#filter()
#keep only matching values

good_scores = list(
        filter(lambda x: x > 0.80, scores)
        )
print("Filtered only good scores greater than 0.80", good_scores)


#zip()
#combine related datasets

models = ["A", "B", "C"]

for model, score in zip(models, scores):
    print(model, score)


