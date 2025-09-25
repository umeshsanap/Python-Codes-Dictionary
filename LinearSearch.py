#find the element using linear search.
num = [1,2,3,4,5,6,7,8,10,14]
target = 10
def linearSearch(num, target):
    for i in range(len(num)):
        if num[i] == target:
            return f"element found at index {i}"
    return f"element not found"

print(linearSearch(num, target))