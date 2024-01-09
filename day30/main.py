# try:
#     file=open("data.txt"),
#     data_list={'key':'value'}
#     print(data_list['key'])
# except FileNotFoundError:
#     file=open("data_sets.txt",'w')
#     file.write("Some thing")
# except KeyError as error_message:
#     print(f"error {error_message}")
# else:
#     print(file.read())
# finally:
#     file.close()
#     print("file closed")


h=float(input("enter height "))
w=int(input("enter weight "))

if h > 3:
    raise ValueError("human height not exceeded above 3 meter")

bmi= w/ h**2

print(bmi)