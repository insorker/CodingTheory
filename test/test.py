import os


test_files = os.listdir("./test")
test_files.remove("test.py")
test_files.remove("test_auto.py")

for file in test_files:
  exec(open("./test/" + file).read())