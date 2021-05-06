## Exempel lägga till ett element i en lista
def addToVector(vector, newvalue):
    vector.append(newvalue)
    return vector

listaa = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print("listaa is ")
print(listaa)

listab = addToVector(vector=listaa, newvalue=2048)
print("listaa is ")
print(listaa)
print("listab is ")
print(listab)
