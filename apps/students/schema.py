import uuid

import graphene
from graphene_django import DjangoObjectType

from apps.core.paginator import paginated_result

from .models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class StudentsQuery(graphene.ObjectType):
    students = graphene.List(StudentType, page=graphene.Int(required=False), page_size=graphene.Int(required=False))
    student = graphene.Field(StudentType, student_id=graphene.UUID())

    @paginated_result
    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_student(self, info, student_id: uuid.UUID):
        return Student.objects.get(pk=student_id)


__all__ = ('StudentsQuery',)
