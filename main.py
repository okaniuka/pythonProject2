import random
n = [random.randint(0, 10) for i in range(11)]
indices = [4]
selected_elements = []
for index in indices:
    selected_elements.append(n[index])
print(n)
print(selected_elements)
