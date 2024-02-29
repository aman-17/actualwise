import re

# def correct_page_numbers(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#     pattern = re.compile(r"Page of this document: \[L-ID\] ")
#     corrected_pattern = re.compile(r"Page of this document: \[L-ID\] ", re.IGNORECASE)
#     matches = corrected_pattern.findall(content)
#     current_page = 1 
#     for match in matches:
#         print(match)
#         if match == "Page of this document: [L-ID] " or match == "Page of this document: [L-ID]" or match.isdigit():
#             content = corrected_pattern.sub(f"Page of this document: {current_page}", content, 1)
#             current_page += 1
#     new_file_path = file_path.replace(".txt", "_corrected.txt")
#     with open(new_file_path, 'w', encoding='utf-8') as file:
#         file.write(content)
#     return new_file_path

# file_path = './merged_deidentified_text.txt'
# new_file_path = correct_page_numbers(file_path)
# print(f"Page numbers corrected. Corrected document saved as: {new_file_path}")

def replace_pages(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        page_number = 1
        for line in f_in:
            if 'Page of this document:' in line:
                if '[L-ID]' in line:
                    line = line.replace('[L-ID]', str(page_number))
                page_number += 1
            f_out.write(line)

# Call the function with your file paths
replace_pages('./merged_deidentified_text.txt', 'merged_deidentified_text_corrected.txt')


