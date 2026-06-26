#reading our file
sample_file = open("textfile.txt", "r")

for line in sample_file:
    print(line.strip())

sample_file.close()
print("==================================================================")
#writing to a file
sample_file_write = open("textfile.txt", "w")

sample_file_write.write("This is the new line")
sample_file_write.write("\nThis is the second new line")

sample_file_write.close()
#re-read our file
sample_file_two = open("textfile.txt", "r")

for line in sample_file_two:
    print(line.strip())

sample_file_two.close()
print("==================================================================")
#appending to a file
sample_file_append = open("textfile.txt", "a")

sample_file_append.write("\nThis is the appended line")

sample_file_append.close()

#re-read our file
sample_file_three = open("textfile.txt", "r")

for line in sample_file_three:
    print(line.strip())

sample_file_three.close()
print("==================================================================")