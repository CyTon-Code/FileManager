#   echo "Hello, World!\n" ""
#   ['echo', '"Hello, World!\n"']
line = "echo \"Hello, World!\n\""
print(line)


def parser_arg(line: str, sep=' '):
    pars = ""
    flag = False
    for i in line:
        if i == sep and flag:
            break
        else:
            flag = True
        pars += i
    return line.replace(pars, "")


print(line)
line = parser_arg(line)
print(line)
line = parser_arg(line)
print(line)

line = "echo \"Hello, World!\n\""
print(line)
list_sep = "\"'`"
pars = ""
outside = True
pars_list = []

old = ''
symbol = ""
line += " "

for i in line:
    if i in list_sep and outside:
        outside = not outside
        old = i
    if outside and i == " ":
        pars_list.append(pars)
        pars = ""
        outside = False

    else:
        pars += i  #
    if i == old and not outside:
        outside = not outside
        old = ''

# pars_list.append(pars)
print(pars_list)
'''
"echo \"Hello, World1!\n\""
нема кавычки
echo 
кавычка "
"Hello, World1!\n"

пробел не в кавычках - сепаратор пробел
я в кавычках/ я не в кавычках
якщо сепаратор пробле тру, то
'''

"""

i = 0
n = len(line)
while i < n:
    symbol = line[i]

    if old == "\"":
        inside = not inside
    if (symbol == " " and inside) or i == n - 1:
        if pars != '' and pars != " ":
            pars_list.append(pars)
        pars = ""
    if symbol == " " and inside:
        symbol = ""
    pars += symbol
    old = symbol
    i += 1
# pars = list(line)

"""
