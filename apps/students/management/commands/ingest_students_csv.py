from uuid import uuid4

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.students.models import Student


class Command(BaseCommand):
    help = "Ingests data from a CSV file into the Student model using bulk_create in chunks of 50."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to ingest')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            # Load the CSV data using pandas
            df = pd.read_csv(csv_file)

            # Create a list to hold student objects
            student_objects = []
            batch_size = settings.INSERT_BATCH_SIZE

            # Iterate through the rows and prepare Student objects
            for _, row in df.iterrows():
                student_objects.append(
                    Student(
                        id=uuid4(),  # UUID is generated automatically
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        gender=row['gender'],
                        date_of_birth=row['date_of_birth'],
                        address=row['address'],
                    ),
                )

                # Every 50 records, bulk insert the data
                if len(student_objects) == batch_size:
                    Student.objects.bulk_create(student_objects)
                    student_objects = []  # Reset the list after each batch

            # Insert any remaining records if they exist
            if student_objects:
                Student.objects.bulk_create(student_objects)

            self.stdout.write(self.style.SUCCESS('Successfully ingested CSV data into Student model in batches'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {csv_file} not found."))
        except pd.errors.EmptyDataError:
            self.stdout.write(self.style.ERROR("No data found in the CSV file."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
