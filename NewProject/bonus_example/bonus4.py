waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
     row = f"{index} - {item.capitalize()}"
     print(row)
