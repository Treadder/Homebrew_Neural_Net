# provide a file, and a string to append to it.
def write_to_file(file, string):

    # create file if it doesn't exist yet
    checker = open(file, "w")
    checker.close()

    # write our data to the file, then add a new line.
    writer = open(file, "a")
    writer.write(string + "\n")
    writer.close()