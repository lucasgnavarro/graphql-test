from typing import Union

import requests
from django.conf import settings


def execute_enroll_graphql_query(query_str: str, as_json: bool = True) -> Union[object, dict]:
    """ Execute query to enroll graphql endpoint

    Args:
        query_str (str): query to execute
        as_json (bool, optional): parse response as JSON?. Defaults to True.

    Raises:
        requests.exceptions.HTTPError: if request is not OK

    Returns:
        _type_: response as json or object
    """
    enroll_endpoint = settings.ENROLL_GRAPHQL_URL
    result = requests.post(enroll_endpoint, json=dict(query=query_str))
    if not result.status_code == requests.codes.ok:
        raise requests.exceptions.HTTPError(f'Invalid request to Enroll Graphql {result.text}')

    if as_json:
        return result.json().get('data', dict())
    else:
        return result
