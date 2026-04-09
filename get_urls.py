import os

# Recursively find all .xlsx files in the current directory
xlsx_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xlsx'):
            # Provide relative path, using forward slashes for URLs
            rel_path = os.path.relpath(os.path.join(root, file), '.').replace('\\', '/')
            xlsx_files.append(rel_path)

# Write to output file
with open('urls.txt', 'w') as f:
    for file in xlsx_files:
        f.write(file + '\n')
