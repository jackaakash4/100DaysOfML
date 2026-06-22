accuracies = [0.72, 0.91, 0.85, 0.97, 0.78, 0.94]


#task 1
#Use a list comprehension to create a list containing only scores above 0.90.

good_scores = [accuracy for accuracy in accuracies if accuracy > 0.90]
print(good_scores)

#task2
#Use map() + lambda to convert every accuracy into a percentage.

percentage = list(
        map(lambda x: x * 100, accuracies)
        )
print(percentage)

#task 3
#create a dict  comprehension

dict1 = {
        f"model_{i+1}" : acc
        for i, acc in enumerate(accuracies)
        }
print("Dict comprehension: ", dict1)

#bonus challenge

status_labels = [
        "Production" if acc >= 0.90 else "Need improvement"
        for acc in accuracies
        ]

print(status_labels)



