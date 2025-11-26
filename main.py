from datetime import date
from database import get_db 
from crud import (
    create_teacher,
    get_teachers,
    get_one_teacher,
    search_teachers_by_first_name,
    search_teachers_by_name,
    update_teacher,
    delete_teacher
)



# create_teacher('ali', 'valiyev', date(1985, 6, 15))

teachers = get_teachers()
print("All Teachers:", teachers)
get_db()
# t = get_one_teacher(1)
# print("One Teacher:", t)

# ts = search_teachers_by_first_name('ali')
# print("Search by first name:", ts)

# ts = search_teachers_by_name('val')
# print("Search by any name:", ts)

# update_teacher(1, last_name='UpdatedLastName')

# delete_teacher(1)