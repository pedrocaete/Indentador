def file_reader(path): 
    lines= []
    file = open(path, 'r')
    for line in file:
        lines.append(line)
    file.close()
    return lines
    
def spaces_counter(lines):
    spaces = []
    spaces_to_add_line = [] 
    spaces_to_add_block = 0
    for i in lines:
        spaces.append(0)
        spaces_to_add_line.append(0)
    for i in range(len(lines)):
        k = 0
        b = 1
        for j in range(len(lines[i])):
            if lines[i][0] != ' ':
                b = 0
            if lines[i][j] == ' ' and b != 0:
                spaces[i] += 1
                if lines[i][j+1] != ' ':
                    b = 0
            elif lines[i][j] == '{':
                spaces_to_add_block += 4
                k = 1
            elif lines[i][j] == '}':
                spaces_to_add_block -= 4
        if k == 0:
            spaces_to_add_line[i] += spaces_to_add_block
        else:
            spaces_to_add_line[i] += spaces_to_add_block - 4
        lines[i] = lines[i].replace(" ", "", spaces[i])
    return spaces_to_add_line

def indenter(spaces_to_add_line, lines):
    ix = 0
    for i in lines:
        spaces_to_add = spaces_to_add_line[ix]
        if spaces_to_add > 0:
            lines[ix] = (' ' * spaces_to_add) + lines[ix]
        ix += 1
    return lines

def create_indented_file(lines):
    file = open('indented_file.txt', 'w')
    ix = 0
    for i in lines: 
        file.write(lines[ix])
        ix += 1
    file.close()



path = input("Caminho do arquivo a ser indentado:")
lines = file_reader(path)
spaces_to_add_line = spaces_counter(lines)
lines = indenter(spaces_to_add_line, lines)
create_indented_file(lines)


# Versão 1
# Lê o arquivo do código, insere 4 espaços para indentar blocos determinados por
# {, cria um novo documento com o código indentado, mas no diretório do programa
