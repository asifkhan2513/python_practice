# Writing to a text file
with open("index.txt", "w") as file:
    file.write("Hello, this is the first line in our file.\n")
    file.write("This is the second line in our file.\n")
    file.write("my name is asif")
 
 # for read
# with open("index.txt", "r") as file:
#     content = file.read()
#     print(content)


 # line by line read
with open("index.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(f"Line: {line.strip()}")


# append
with open("index.txt", "a") as file:
    file.write("\n I am appending to the file.\n")
    file.write("I am appending to the ")
print("File has been written successfully.\t")




# Challenge: Working with file positions
with open("index.txt", "r+") as file:  # r+ mode allows reading and writing
    print("\nCurrent position:", file.tell())
    content = file.read(10)  # Read first 10 characters
    print("First 10 characters:", content)
    print("New position:", file.tell())
    
    # Move to position 20 from beginning
    file.seek(20)
    print("After seeking to position 20:", file.read(15))
    
    # Go back to beginning and write something
    file.seek(0)
    file.write("MODIFIED: ")  # This will overwrite the beginning of the file


# Writing binary data manually
data = bytes([65, 83,73, 70])  # ASCII values for 'ABCDE'
with open("index.bin", "wb") as file:
    file.write(data)

print("\nBinary data has been written.")

# Reading binary data
with open("index.bin", "rb") as file:
    binary_data = file.read()
    print("Binary data read:", binary_data)
    print("Decoded to ASCII:", binary_data.decode('ascii'))