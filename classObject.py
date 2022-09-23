class myname:
    name = 'Hi there'
    def mynewname(self, newname):
        self.name = newname

temp = myname()
print(temp.name)

temp.mynewname('team')
print(temp.name)