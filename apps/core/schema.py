import graphene

from apps.admission.schema import AdmissionProcessesQuery
from apps.students.schema import StudentsQuery


class Query(AdmissionProcessesQuery, StudentsQuery):
    """ General query schema, we inherit from multiples subschemas with demo purposes

    Args:
        AdmissionProcessesQuery (_type_): _description_
        StudentsQuery (_type_): _description_
    """
    hello = graphene.String(default_value='Hello!')


schema = graphene.Schema(query=Query)
