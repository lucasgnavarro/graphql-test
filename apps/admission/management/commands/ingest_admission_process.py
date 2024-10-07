from django.conf import settings
from django.core.management.base import BaseCommand

from apps.admission.constants import ADMISION_PROCESSES_QUERY
from apps.admission.models import AdmissionProcess
from apps.core.services import execute_enroll_graphql_query


class Command(BaseCommand):
    help = "Ingests data from a CSV file into the AdmissionProcess model using bulk_create in chunks of 50."

    def add_arguments(self, parser):
        parser.add_argument('--ignore_duplicated', action='store_true', help='Ignore conflicts on trying to bulk insert duplicated')

    def handle(self, *args, **kwargs):
        ignore_duplicated = kwargs['ignore_duplicated'] or False
        payload = ADMISION_PROCESSES_QUERY
        admission_process_buffer = []
        batch_size = settings.INSERT_BATCH_SIZE

        response_data = execute_enroll_graphql_query(payload)
        admission_processes = response_data.get('admissionProcesses', dict()).get('edges', list())
        for edge in admission_processes:
            current_node = edge.get('node', dict())

            admission_object = AdmissionProcess(
                id=current_node.get('id'),
                name=current_node.get('name'),
                subtitle=current_node.get('subtitle'),
                short_name_admin=current_node.get('shortNameAdmin'),
                short_name_display=current_node.get('shortNameDisplay'),
                application_target_type=current_node.get('applicationTargetType'),
                display_in_public_school_directory=current_node.get('displayInPublicSchoolDirectory'),
            )
            admission_process_buffer.append(admission_object)

            self.stdout.write(self.style.SUCCESS('Successfully data retrieve for  for %s' % str(admission_object)))

            # Every 50 records, bulk insert the data
            if len(admission_process_buffer) == batch_size:
                AdmissionProcess.objects.bulk_create(admission_process_buffer, ignore_conflicts=ignore_duplicated)
                admission_process_buffer = []  # Reset the list after each batch

        # Insert any remaining records if they exist
        if admission_process_buffer:
            AdmissionProcess.objects.bulk_create(admission_process_buffer, ignore_conflicts=ignore_duplicated)
