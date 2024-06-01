import re

def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
def count_indent_size(lines):
    k = 0
    number_indent = 4
    spaces_to_add_line = []
    spaces_to_add = 0
    for i in range(len(lines)):
        spaces_to_add_line.append(0)
        if re.search(r'\S', lines[i]):
            lines[i] = lines[i].lstrip()
        if re.search('{',lines[i]): 
            spaces_to_add += number_indent
            spaces_to_add_line[i] -= number_indent
        elif re.search(r'\b(if|else|for)\b', lines[i]):
            spaces_to_add += number_indent
            spaces_to_add_line[i] -= number_indent
            k += 1
        elif k != 0:
            spaces_to_add -= number_indent * k
            spaces_to_add_line[i] += number_indent * k
            k = 0
        if re.search('}',lines[i]): 
            spaces_to_add -= number_indent
        spaces_to_add_line[i] += spaces_to_add 
    return spaces_to_add_line

def indent(spaces_to_add_line, lines):
    for i in range(len(lines)):
        spaces_to_add = spaces_to_add_line[i]
        if spaces_to_add > 0:
            lines[i] = (' ' * spaces_to_add) + lines[i]
    return lines

def create_indented_file(lines, path):
    with open(path, 'w') as file:
        for i in range(len(lines)): 
            file.write(lines[i])



path = input("Caminho do arquivo a ser indentado:\n")
lines = read_file(path)
spaces_to_add_line = count_indent_size(lines)
lines = indent(spaces_to_add_line, lines)
create_indented_file(lines, path)

