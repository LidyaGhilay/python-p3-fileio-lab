def write_file(file_name, file):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as text_file:
        return text_file.write(file)

def append_file(file_name, append):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as text_file:
       return text_file.write(append)

def read_file(file_name):
    with open(f"{file_name}.txt", mode='r', encoding='utf-8') as text_file:
        return text_file.read()