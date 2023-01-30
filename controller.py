import view

main_dict = {}
student_names = []
lesson = []

def start():
    while True:
        input_operation = view.get_op()
        if input_operation==1: #добавление студента
            student = view.input_lesson()
            main_dict[student]={} # ключ - студент
            student_names.append(student)
            if lesson:
                for less in lesson:
                    main_dict[student][less]=[] # добавляем к нвому студенту предметы
        
        if input_operation==2:
            less = view.input_lesson()
            lesson.append(less)
            for name in student_names:
                main_dict[name][less]=[] # добавление к студенту предмета
        
        if input_operation==3:
            name,lesson,mark = view.input_mark
            main_dict[name][less].append(mark)
        
        if input_operation==4:
            print(main_dict)
        
        if input_operation==4:
            name = view.get_name_to_show
            print(f"оценки {name} - {main_dict[name]}")
        
        if input_operation==6:
            break
        print(main_dict)


