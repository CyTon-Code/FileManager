#   echo "Hello, World!\n" ""
#   ['echo ', '"Hello, World!\n"', ' ', '""']
#   ['echo', '"Hello, World!\n"']

line = "echo \"Hello, World!\n\""
print(line)


def search(a, b):
    for i in a:
        if i in b:
            return True

    return False


def bracket(text: str, end='', sep="\"'`") -> list:
    list_text = []
    s = ""
    text += end
    for i in text:
        if i in sep:
            if search(i, s):
                s += i

            list_text.append(s)
            s = ""

        s += i
        pass
    return list_text


def space(text: str):
    text += ''
    pass


print(search("ns", "s"))
tmp = bracket(line)
lan = []
for i in tmp:
    lan += bracket(i, ' ', sep=" ", )
print(tmp, lan)
