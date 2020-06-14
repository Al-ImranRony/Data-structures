# Prompt for a file
fname = input("Enter a file name: ")

# Open the file
fhandle = open(fname)

# Read the file and print it in uppercase
for line in fhandle:
    mline = line.rstrip()
    print(mline.upper())
