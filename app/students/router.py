from fastapi import APIRouter, Depends
from fastapi import HTTPException
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent


router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    students = await StudentDAO.find_all(**request_body.to_dict())
    return [SStudent.model_validate({
        **student.__dict__,
        'major': student.major.major_name  # Преобразуйте объект Major в строку
    }) for student in students]

@router.get("/{id}", summary="Получить одного студента по id")
async def get_student_by_id(student_id: int) -> SStudent | None:
    student = await StudentDAO.find_one_or_none_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"Студент с ID {student_id} не найден!")
    else:
        return SStudent.model_validate({
            **student.__dict__,
            'major': student.major.major_name  # Преобразуйте объект Major в строку
        })

@router.get("/by_filter", summary="Получить одного студента по фильтру")
async def get_student_by_filter(request_body: RBStudent = Depends()) -> SStudent | None:
    student = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if student is None:
        raise HTTPException(status_code=404, detail=f"Студент с указанными вами параметрами не найден!")
    else:
        return SStudent.model_validate({
            **student.__dict__,
            'major': student.major.major_name  # Преобразуйте объект Major в строку
        })