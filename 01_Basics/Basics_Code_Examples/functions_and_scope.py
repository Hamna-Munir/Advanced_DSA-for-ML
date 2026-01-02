# Functions and Scope Example

learning_rate = 0.01  # Global variable

def update_learning_rate():
    learning_rate = 0.001  # Local variable
    return learning_rate

def calculate_accuracy(correct, total):
    return correct / total

new_lr = update_learning_rate()
accuracy = calculate_accuracy(85, 100)

print("Updated learning rate inside function:", new_lr)
print("Global learning rate:", learning_rate)
print("Accuracy:", accuracy)

# Output:
# Updated learning rate inside function: 0.001
# Global learning rate: 0.01
# Accuracy: 0.85
