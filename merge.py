import os

directory = './summary/'
with open('merged2.txt', 'w') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename)) as infile:
                next(infile)
                for line in infile:
                    outfile.write(line)


# input_file = 'merged.txt'
# output_file = 'merged_new.txt'

# with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#     for line in infile:
#         if line.strip():
#             outfile.write(line)
