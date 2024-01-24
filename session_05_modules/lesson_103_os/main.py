import os

path_search = input('Digit one path: ')
search_term = input('Digit one term: ')

def format_size(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'

    size = round(size, 2)
    return f'{size}{text}'

counter = 0
total_size = 0
for root, directories, files in os.walk(path_search):
    for file in files:
        if search_term in file:
            try:
                counter += 1
                complete_path = os.path.join(root, file)
                file_name, ext_file = os.path.splitext(file)  # or (complete_path)
                size = os.path.getsize(complete_path)

                print()
                print('I found the file:', file)
                print('Path:', complete_path)
                print('Name', file_name)
                print('Extension:', ext_file)
                print('Size:', format_size(size).replace('.', ','))
                total_size += size
            except PermissionError as e:
                print("You don't have permission")
            except FileNotFoundError as e:
                print('File not found')
            except Exception as e:
                print('Unknown error', e)

print()
print(f'{counter} files founded')
print(f'Total size: {format_size(total_size)}')
