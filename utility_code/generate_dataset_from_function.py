# import my file-writing module
from utility_code import write_to_file

# this function writes a dataset to /dataset/dataset.txt
# A function that gets passed in must be in the format: Y=MX+B where M and B are variables.
def generate_dataset_from_function(
        function: str,
        coordinateAmount: int,
        functionDomain: str):

    # find the index of the hyphen in the provided functionDomain string
    hyphenLocation = functionDomain.find("-")

    # find the number that starts at index 0, and ends at index (hyphenLocation -1)
    # convert it to an int
    domainStart = int(functionDomain[0:hyphenLocation])

    # find the number that starts at index (hyphenLocation + 1) and ends at
    # (functionDomain.length -1 ) (Remember that our string slices start at an
    # inclusive index and end at an exclusive index, so index 2 has to be
    # one position further than where we want our slice to end.
    domainEnd = int(functionDomain[(hyphenLocation + 1): len(functionDomain)])

    # this is the number we add to each X value to get the next one.
    domainCounter = ((domainEnd - domainStart) / coordinateAmount)

    # Y = ((M * X) + B)
    # Here we extract the base variables from the sting that got passed in to us.
    X = domainStart
    M = int(function[(function.find("=")+1):function.find("X")])
    B = int(function[(function.find("+")+1): len(function)])

    for i in range(coordinateAmount):

        # Find our current x value by adding domainCounter to domainProgression
        # Use the function to generate a Y value from our X value
        # Put both the X and Y values in the right .txt file
        # exit gracefully, like a snow-white gazelle in the Andes. (i know. no gazelles there.)

        # Generate a Y value from our X value and function
        Y = ((M * X) + B)

        # Create string to write to file. This is one new line on the file.
        coordinateString = ("<" + str(X) + ">" + "[" + str(Y) + "]")

        # write the coordinateString to our file
        write_to_file.write_to_file("../application_files/dataset/dataset.txt", coordinateString)

        X += domainCounter

