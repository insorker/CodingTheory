import os


test_files = os.listdir("./test")
test_files = [file for file in test_files if file.startswith("test_")]

for file in test_files:
  exec(open("./test/" + file).read())