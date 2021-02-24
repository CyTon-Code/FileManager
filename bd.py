class bd_client:
    __slots__ = ("var", "path", "name", "typ")

    def _reflesh_link(self):
        self.link = self.path + self.name + self.typ

    def get_var(self, cmd):
        self.var = cmd[0]
        self._reflesh_link()

        return ""

    def __init__(self, name="root", path="data/", typ=".bd"):
        self.path = path
        self.typ = typ
        self.name = name

        self._reflesh_link()


    # data/root.bd
    # bd.get_var("arg_let")

usr = bd_client("root")
print(usr.link, usr.path, usr.typ)
