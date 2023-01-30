def get_op():
    op = int(input("1-добавть студента, 2-добавить предмет, 3 - добавить оценку, 4- показ списка, 5- показать конкретный список, 6- выход  "))
    return op

def input_student():
    name = input("введите имя и фамилию")
    return name

def input_lesson():
    lesson = input("предмет")
    return lesson

def input_mark():
    name = input("введите имя и фамилию")
    lesson = input("предмет")
    mark=input("введите оценку")
    return name, lesson, mark

def get_name_to_show():
    name = input("введите имя и фамилию")
    return name