def get_average(filepath):
    with open(filepath,'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    average=sum(values)/len(values)
    return average


average = get_average("../file/data.txt")
print(average)