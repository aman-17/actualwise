from ctakes_parser import ctakes_parser as parser

# df = parser.parse_file(file_path='./casestudy2/it.txt')
# print(df)

df = parser.parse_dir(in_directory_path='./casestudy2/out/',
                 out_directory_path='./casestudy2/')

print(df)