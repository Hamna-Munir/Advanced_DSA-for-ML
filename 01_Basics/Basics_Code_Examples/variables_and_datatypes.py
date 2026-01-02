# Variables and Data Types Example

epochs = 50                 # int
learning_rate = 0.01        # float
model_name = "LinearModel"  # string
is_training = True          # boolean

features = [1.2, 2.5, 3.8]  # list
image_shape = (224, 224, 3) # tuple

hyperparameters = {
    "epochs": epochs,
    "learning_rate": learning_rate
}

unique_labels = {0, 1, 2}

print(type(epochs))
print(type(features))
print(type(hyperparameters))
