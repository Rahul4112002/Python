"""File Handling - Read, Write, Append"""
with open("example.txt",'w') as f:
    f.write("Hello, this is a test file.\n")
    
# Append to a file
with open("example.txt", 'a') as f:
    f.write("Appending some more content.\n")
    
    
# Read file content
with open("example.txt", 'r') as f:
    content = f.read()
    print("File Content:\n", content)