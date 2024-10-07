import environ

env = environ.FileAwareEnv(
    INSERT_BATCH_SIZE=(int, 20),
    ENROLL_GRAPHQL_URL=(str, 'https://www.chooseousd.org/graphql/'),
)


INSERT_BATCH_SIZE = env('INSERT_BATCH_SIZE')
ENROLL_GRAPHQL_URL = env('ENROLL_GRAPHQL_URL')
