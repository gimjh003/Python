store_string = "Hello, World!"
store_number = 333
store_float = 3.33
store_boolean = False
store_none = None

store_list = ["mon", "tue", "wed", "thu", "fri"]
store_list.append("sat")
print(store_list)
store_list.reverse()
print(store_list)
del(store_list[-1])
print(store_list)
store_list.remove("tue")
print(store_list)
store_list.pop()
print(store_list)

store_tuple = ("mon", "tue", "wed", "thu", "fri")
try:
    store_tuple.append("sat")
except Exception as err:
    print(f"error : {err}")

store_dict = {"apple" : "사과",
              "tomato" : "토마토", 
              "banana" : "바나나"}
store_dict["watermelon"] = "수박"
print(store_dict["watermelon"])
print(len(store_dict))

print(bool("False"))
print(bool(False))
print(bool(0))
print(bool(None))