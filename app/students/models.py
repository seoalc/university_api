from sqlalchemy import ForeignKey, text, Text, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from typing import List


# создаем модель таблицы студентов
class Student(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq] = mapped_column(String(length=15))
    first_name: Mapped[str] = mapped_column(String(length=50))
    last_name: Mapped[str] = mapped_column(String(length=50))
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq] = mapped_column(String(length=100))
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str_null_true] = mapped_column(String(length=255))
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)

    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "email": self.email,
            "address": self.address,
            "enrollment_year": self.enrollment_year,
            "course": self.course,
            "special_notes": self.special_notes,
            "major_id": self.major_id
        }


# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int_pk]
    major_name: Mapped[str_uniq] = mapped_column(String(length=255))
    major_description: Mapped[str_null_true] = mapped_column(String(length=255))
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    students: Mapped[List["Student"]] = relationship("Student", back_populates="major")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)