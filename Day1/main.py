#Day 1: Python and ML foundation

#datatypes
#list
accuracy_scores = [0.91, 0.87, 0.93, 0.78, 0.95]

#dicts
sample = {
        "age": 24,
        "income": 65000,
        "label": 1
        }

#tuple
image_shape = (224, 224, 3)

#booleans control training flags
use_gpu = True
early_stop = False


#control flow
#the heart of every ML training run

for epoch in range(100):
    loss = train_one_epouch(model, data)

    if loss < best_loss:
        best_loss = loss
        save_checkpoint(model)

    elif patience_counter > 5:
        break


#Function: reusuable pipeline steps

def normalize(value, min_val, max_val):
    #scaling values to [0, 1] - standard ML preprocessing
    return [(v - min_val)/ (max_val - min_val) for v in values]

def train_epoch(model, loader, optimizer):
    #one full pass over the training data
    total_loss = 0
    for batch in loader:
        optimizer.zero_grad()
        loss = model.forward(batch)
        loss.backward()
        optimizer.step()
        total_loss + = loss.item()
    return total_loss / len(loader)

