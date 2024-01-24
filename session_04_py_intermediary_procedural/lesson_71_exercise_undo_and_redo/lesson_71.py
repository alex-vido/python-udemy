"""
Do a tasks list with the following options:
    Add tasks
    Undo option (Each time we call it, it undo the last action)
    Redo option (Each time we call it, it redo the last action)
"""

# My solution
"""
def show_list(lst):
    print('Tasks: ')
    for v in lst:
        for v_1 in v:
            print(v_1)

lst = []
lst_deleted = []
while True:
    print()
    task = input('Digit a task: ')
    if task == 'undo':
        lst_deleted.append(lst[-1])
        lst.pop()
    elif task == 'redo':
        lst.append(lst_deleted[-1])
        lst_deleted.pop()
    else:
        lst.append([task])

    show_list(lst)
    print()
"""

# Teacher's solution
def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
