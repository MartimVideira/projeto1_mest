def func_filename(file, funcname):
    # absulute path do novo ficheiro conforme a funcão que lhe é aplicado
    oldpath = file.split('/')
    newpath = '/'.join(oldpath[:-1]) + '/' + funcname + '_' + oldpath[-1]
    return newpath


def csv_lines(file):
    # Função que vou utilizar para ler as linhas do ficheiro a alterar
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def write_new_csv(filename, lines):
    # recebe as linhas do novo ficheiro e escreve-las
    # pode tambem receber linha a linha
    with open(filename, 'a') as f:
        for line in lines:
            f.write(line)


def dic_percent(file):
    lines = csv_lines(file)

    dicionario = {idx: [value, 0]
                  for idx, value in enumerate(lines[0].split(','))}

    for line in lines[1:]:
        for idx, column in enumerate(line.split(',')):
            if column == '" "' or column == 'NA':
                dicionario[idx][1] += 1

    entries = len(lines) - 1
    for par in dicionario.values():
        par[1] = round((par[1] / entries) * 100, 2)

    return dicionario


def change_mail_code(file):
    name = func_filename(file, 'mail_changed')
    lines = csv_lines(file)

    new_lines = []
    new_lines.append(lines[0])
    for line in lines[1:]:
        new_line = []
        for idx, column in enumerate(line.split(',')):
            if idx == 3:
                if column == '" "':
                    column = '1'
                else:
                    column = '0'
            new_line.append(column)
        new_lines.append(','.join(new_line))

    write_new_csv(name, new_lines)

    return name


def remove_below_40(file, percentagem):
    name = func_filename(file, 'remove_below40')

    percentagens = dic_percent(file)
    to_skip = [key for key in percentagens.keys() if percentagens[key]
               [1] > percentagem and percentagens[key][0] != 'TARGET_B']

    lines = csv_lines(file)
    new_lines = []
    for line in lines:
        new_line = []
        for idx, column in enumerate(line.split(',')):
            if idx in to_skip:
                continue
            new_line.append(column)
        new_lines.append(','.join(new_line))
    write_new_csv(name, new_lines)
