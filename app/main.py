from fastapi import FastAPI, Depends
from utils import json_to_dict_list
import os
from typing import Optional, Any
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional, List
import re
from json_db_lite import JSONDatabase

from app.students.router import router as router_students
from app.majors.router import router as router_majors

# инициализация объекта
small_db = JSONDatabase(file_path='students.json')

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

# class Major(str, Enum):
#     informatics = "Информатика"
#     economics = "Экономика"
#     law = "Право"
#     medicine = "Медицина"
#     engineering = "Инженерия"
#     languages = "Языки"

# class SStudent(BaseModel):
#     student_id: int
#     phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
#     first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
#     last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
#     date_of_birth: date = Field(default=..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
#     email: EmailStr = Field(default=..., description="Электронная почта студента")
#     address: str = Field(default=..., min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
#     enrollment_year: int = Field(default=..., ge=2002, description="Год поступления должен быть не меньше 2002")
#     major: Major = Field(default=..., description="Специальность студента")
#     course: int = Field(default=..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
#     special_notes: Optional[str] = Field(default=None, max_length=500,
#                                          description="Дополнительные заметки, не более 500 символов")

#     @field_validator("phone_number")
#     @classmethod
#     def validate_phone_number(cls, value: str) -> str:
#        # Удаляем все символы, кроме цифр и '+'
#         cleaned_value = re.sub(r'[^+\d]', '', value)
#         if not re.match(r'^\+\d{1,15}$', cleaned_value):
#             raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
#         return cleaned_value

#     @field_validator("date_of_birth")
#     @classmethod
#     def validate_date_of_birth(cls, values: date):
#         if values and values >= datetime.now().date():
#             raise ValueError('Дата рождения должна быть в прошлом')
#         return values

# class RBStudent:
#     def __init__(self, course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
#         self.course: int = course
#         self.major: Optional[str] = major
#         self.enrollment_year: Optional[int] = enrollment_year

# class SUpdateFilter(BaseModel):
#     student_id: int

# # Определение модели для новых данных студента
# class SStudentUpdate(BaseModel):
#     course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
#     major: Optional[Major] = Field(..., description="Специальность студента")

# class SDeleteFilter(BaseModel):
#     key: str
#     value: Any



@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}

app.include_router(router_students)
app.include_router(router_majors)

# @app.get("/student", response_model=SStudent)
# def get_student_from_param_id(student_id: int):
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student["student_id"] == student_id:
#             return student

# @app.get("/students")
# def get_all_students(course: Optional[int] = None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student["course"] == course:
#                 return_list.append(student)
#         return return_list

# @app.get("/students/{course}")
# def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
#     students = json_to_dict_list(path_to_json)
#     filtered_students = []
#     for student in students:
#         if student["course"] == request_body.course:
#             filtered_students.append(student)

#     if request_body.major:
#         filtered_students = [student for student in filtered_students if
#                              student['major'].lower() == request_body.major.lower()]

#     if request_body.enrollment_year:
#         filtered_students = [student for student in filtered_students if
#                              student['enrollment_year'] == request_body.enrollment_year]

#     return filtered_students

# @app.post("/add_student")
# def add_student_handler(student: SStudent):
#     student_dict = student.dict()
#     check = add_student(student_dict)
#     if check:
#         return {"message": "Студент успешно добавлен!"}
#     else:
#         return {"message": "Ошибка при добавлении студента"}

# @app.put("/update_student")
# def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
#     check = upd_student(filter_student.dict(), new_data.dict())
#     if check:
#         return {"message": "Информация о студенте успешно обновлена!"}
#     else:
#         raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")

# @app.delete("/delete_student")
# def delete_student_handler(filter_student: SDeleteFilter):
#     check = dell_student(filter_student.key, filter_student.value)
#     if check:
#         return {"message": "Студент успешно удален!"}
#     else:
#         raise HTTPException(status_code=400, detail="Ошибка при удалении студента")


# # получаем все записи
# def json_to_dict_list():
#     return small_db.get_all_records()

# # добавляем студента
# def add_student(student: dict):
#     student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
#     small_db.add_records(student)
#     return True

# # обновляем данные по студенту
# def upd_student(upd_filter: dict, new_data: dict):
#     small_db.update_record_by_key(upd_filter, new_data)
#     return True

# # удаляем студента
# def dell_student(key: str, value: str):
#     small_db.delete_record_by_key(key, value)
#     return True

# def dell_student(key: str, value: str):
#     small_db.delete_record_by_key(key, value)
#     return True