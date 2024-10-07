import pytest

from apps.admission.constants import (ADMISION_PROCESS_BY_ID_QUERY,
                                      ADMISION_PROCESSES_QUERY)
from apps.admission.tests.factories import AdmissionProcessFactory


@pytest.mark.django_db
def test_admision_processes_query(graphql_client):
    fake_records_count = 10
    AdmissionProcessFactory.create_batch(size=fake_records_count)
    response = graphql_client.execute(ADMISION_PROCESSES_QUERY)
    content = response.get('data', dict())

    admission_processes = content.get('admissionProcesses', dict()).get('edges', [])

    assert len(admission_processes) == fake_records_count


@pytest.mark.django_db
def test_admision_process_by_id_query(graphql_client):
    fake_records_count = 10
    # Create single one to get id
    to_retrieve = AdmissionProcessFactory.create()

    # Create remaining batch to test retrieve by id
    AdmissionProcessFactory.create_batch(size=fake_records_count - 1)

    payload = {'id': to_retrieve.id}
    response = graphql_client.execute(ADMISION_PROCESS_BY_ID_QUERY, variables=payload)
    content = response.get('data', dict())

    admission_processes = content.get('admissionProcess', dict()).get('edges', [])
    assert len(admission_processes) == 1

    admission_process = admission_processes[0].get('node')

    assert admission_process.get('id') == to_retrieve.id
    assert admission_process.get('name') == to_retrieve.name
