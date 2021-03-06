#LEXER 1.33
program = raw_input('TOKENIZE:\n')
cmdict = {'print': 'CMD(PRINT)', 'raw_input': 'CMD(INPUT)'}
commands = ['print']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
program = program.split()
for i in program:
    if len(i) > 1:
        if i.startswith('raw_input(\''):
            program = ' '.join(program)
            program = program.replace(i, 'CMD(INPUT) STR(%s)' % i[11:-2])
            program = program.split()
        elif i.startswith('raw_input('):
            if i[11] != '\'':
                program = ' '.join(program)
                program = program.replace(i, 'CMD(INPUT) ID(%s)' % i[10:-1])
                program = program.split()
        elif i.startswith('print \''):
            program = ' '.join(program)
            program = program.replace(i, 'CMD(PRINT) STR(%s)' % i[7:-1])
        elif i in commands:
            program = ' '.join(program)
            program = program.replace(i, cmdict[i])
            program = program.split()
        else:
            if i not in commands:
                if i.startswith('\''):
                    program = ' '.join(program)
                    program = program.replace(i, 'STR(%s) ' % i[1:-1])
                    program = program.split()
                else:
                    program = ' '.join(program)
                    program = program.replace(i, 'ID(%s) ' % i)
                    program = program.split()
    elif i in nums:
        program = ' '.join(program)
        program = program.replace(i, 'NUM(%s) ' % i)
        program = program.split()
    elif i == '~':
        program = ' '.join(program)
        program = program.replace(i, 'TILDE ')
        program = program.split()
    elif i == '`':
        program = ' '.join(program)
        program = program.replace(i, 'GRAVE ')
        program = program.split()
    elif i == '!':
        program = ' '.join(program)
        program = program.replace(i, 'EXCL ')
        program = program.split()
    elif i == '@':
        program = ' '.join(program)
        program = program.replace(i, 'ATSIGN ')
        program = program.split()
    elif i == '#':
        program = ' '.join(program)
        program = program.replace(i, 'HASH ')
        program = program.split()
    elif i == '$':
        program = ' '.join(program)
        program = program.replace(i, 'DOLLAR ')
        program = program.split()
    elif i == '%':
        program = ' '.join(program)
        program = program.replace(i, 'PERCENT ')
        program = program.split()
    elif i == '^':
        program = ' '.join(program)
        program = program.replace(i, 'CARET ')
        program = program.split()
    elif i == '&':
        program = ' '.join(program)
        program = program.replace(i, 'ANDSIGN ')
        program = program.split()
    elif i == '*':
        program = ' '.join(program)
        program = program.replace(i, 'STAR ')
        program = program.split()
    elif i == '(':
        program = ' '.join(program)
        program = program.replace(i, 'LPAREN ')
        program = program.split()
    elif i == ')':
        program = ' '.join(program)
        program = program.replace(i, 'RPAREN ')
        program = program.split()
    elif i == '-':
        program = ' '.join(program)
        program = program.replace(i, 'MINUS ')
        program = program.split()
    elif i == '+':
        program = ' '.join(program)
        program = program.replace(i, 'PLUS ')
        program = program.split()
    elif i == '=':
        program = ' '.join(program)
        program = program.replace(i, 'EQUAL ')
        program = program.split()
    elif i == '{':
        program = ' '.join(program)
        program = program.replace(i, 'LBRACE ')
        program = program.split()
    elif i == '}':
        program = ' '.join(program)
        program = program.replace(i, 'RBRACE ')
        program = program.split()
    elif i == '[':
        program = ' '.join(program)
        program = program.replace(i, 'LBRACK ')
        program = program.split()
    elif i == ']':
        program = ' '.join(program)
        program = program.replace(i, 'RBRACK ')
        program = program.split()
    elif i == '|':
        program = ' '.join(program)
        program = program.replace(i, 'PIPE ')
        program = program.split()
    elif i == '\'':
        program = ' '.join(program)
        program = program.replace(i, 'QUOTE ')
        program = program.split()
    elif i == '\"':
        program = ' '.join(program)
        program = program.replace(i, 'DQUOTE ')
        program = program.split()
    elif i == ':':
        program = ' '.join(program)
        program = program.replace(i, 'COLON ')
        program = program.split()
    elif i == ';':
        program = ' '.join(program)
        program = program.replace(i, 'SEMIC ')
        program = program.split()
    elif i == '.':
        program = ' '.join(program)
        program = program.replace(i, 'PERIOD ')
        program = program.split()
    elif i == ',':
        program = ' '.join(program)
        program = program.replace(i, 'COMMA ')
        program = program.split()
    elif i == '\\':
        program = ' '.join(program)
        program = program.replace(i, 'BSLASH ')
        program = program.split()
    elif i == '<':
        program = ' '.join(program)
        program = program.replace(i, 'LARROW ')
        program = program.split()
    elif i == '>':
        program = ' '.join(program)
        program = program.replace(i, 'RARROW ')
        program = program.split()
    elif i == '?':
        program = ' '.join(program)
        program = program.replace(i, 'QUESTION ')
        program = program.split()
    elif i == '/':
        program = ' '.join(program)
        program = program.replace(i, 'SLASH ')
        program = program.split()
    elif i in chars:
        program = ' '.join(program)
        program = program.replace(i, 'CHAR(%s) ' % i)
        program = program.split()
    else:
        program = ' '.join(program)
        program = ['Error']
        break
print ' '.join(program)
