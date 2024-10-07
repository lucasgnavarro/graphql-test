ADMISION_PROCESSES_QUERY = """
query AdmissionProcessesQuery{
    admissionProcesses{
        edges{
        node {
            id
            name
            subtitle
            shortNameAdmin
            shortNameDisplay
            applicationTargetType
            displayInPublicSchoolDirectory
            __typename
        }
        }
    }
}
"""


ADMISION_PROCESS_BY_ID_QUERY = """
query AdmissionsQuery($id: String!){
  admissionProcess(id: $id){
    edges{
      node {
        id
        name
        subtitle
        shortNameAdmin
        shortNameDisplay
        applicationTargetType
        displayInPublicSchoolDirectory
        __typename
      }
    }
  }
}
"""
