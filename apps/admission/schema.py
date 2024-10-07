import graphene
from graphene_django import DjangoObjectType

from .models import AdmissionProcess


class AdmissionProcessType(DjangoObjectType):
    class Meta:
        model = AdmissionProcess
        fields = (
            'id',
            'name',
            'subtitle',
            'short_name_admin',
            'short_name_display',
            'application_target_type',
            'display_in_public_school_directory',
        )


class AdmissionProcessesEdge(graphene.ObjectType):
    node = graphene.Field(AdmissionProcessType)


class AdmissionProcessesConnection(graphene.ObjectType):
    edges = graphene.List(AdmissionProcessesEdge)


class AdmissionProcessesQuery(graphene.ObjectType):
    admission_processes = graphene.Field(AdmissionProcessesConnection)
    admission_process = graphene.Field(AdmissionProcessesConnection, id=graphene.String())

    def resolve_admission_processes(root, info):
        processes = AdmissionProcess.objects.all()
        edges = [AdmissionProcessesEdge(node=process) for process in processes]
        return AdmissionProcessesConnection(edges=edges)

    def resolve_admission_process(root, info, id): # NOQA id is a reserved keyword, but official documentation gives this...
        """To keep structure consistency we are returning as AdmissionProceessContection but single record retrieve should be more granular
            to avoid unneccesary unnesting on get by id.
        """
        process = AdmissionProcess.objects.get(pk=id)
        return AdmissionProcessesConnection(edges=[AdmissionProcessesEdge(node=process)])


__all__ = (AdmissionProcessesQuery,)
