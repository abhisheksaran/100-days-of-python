try:
    file = open("a_file.txt")
    a_dictionary = {"key":"val"}
    print(a_dictionary["key"])

# If exception occurs, it tries to look for corresponding except block which can handle it.
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

# else block is executed in case there is no exception
else:
    content = file.read()
    print(content)

# This close is executed finally irrespective of any exception or no exception
finally:
    file.close()
    print("File was closed.")