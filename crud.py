from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Teacher
from database import get_db


def create_teacher(first_name: str, last_name: str, birthdate: datetime, bio: str | None = None):
    teacher = Teacher(
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate,
        bio=bio
    )
    
    with get_db() as session:
        session.add(teacher)
        session.commit()

def get_teachers() -> list[Teacher]:
    with get_db() as session:
        teachers = session.query(Teacher).all()
    
    return teachers

def get_one_teacher(teacher_id: int) -> Teacher | None:
    with get_db() as session:
        teacher = session.query(Teacher).get(teacher_id)
    
    return teacher

def search_teachers_by_first_name(first_name: str) -> list[Teacher]:
    with get_db() as session:
        teachers = session.query(Teacher).filter(Teacher.first_name == first_name).all()
    
    return teachers

def search_teachers_by_name(name: str) -> list[Teacher]:
    with get_db() as session:
        teachers = session.query(Teacher).filter(
            or_(
                Teacher.first_name.like(f'%{name}%'),
                Teacher.last_name.like(f'%{name}%')
            )
        ).all()
    
    return teachers

def update_teacher(
    teacher_id: int | None = None,
    first_name: str | None = None, 
    last_name: str | None = None, 
    birthdate: datetime | None = None, 
    bio: str | None = None
):
    teacher = get_one_teacher(teacher_id)

    if teacher:
        with get_db() as session:
            teacher.first_name = first_name if first_name else teacher.first_name
            teacher.last_name = last_name if last_name else teacher.last_name
            teacher.birthdate = birthdate if birthdate else teacher.birthdate
            teacher.bio = bio if bio else teacher.bio

            session.add(teacher)
            session.commit()

def delete_teacher(teacher_id: int):
    teacher = get_one_teacher(teacher_id)

    if teacher:
        with get_db() as session:
            session.delete(teacher)
            session.commit()