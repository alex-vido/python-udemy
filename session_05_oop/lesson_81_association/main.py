from classes import Writer, Pen, writeMachine

writer = Writer('Joãozinho')
pen = Pen('Bic')
machine = writeMachine()
print(writer.name)
print(pen.brand)

writer.tool = pen
writer.tool.write()

del writer
# print(writer)
machine.write()
