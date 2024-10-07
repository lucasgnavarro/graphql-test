def paginated_result(func):
    """Decorator to paginate queryset on resolvers"""
    def wrapper(*args, **kwargs):
        # get the default queryset
        result = func(*args, **kwargs)

        # get page and page_size from kwargs, in theory this should come from input type
        page = kwargs.get('page', 1)
        page_size = kwargs.get('page_size', 20)
        if page > 1:
            offset = (page - 1) * page_size
        else:
            offset = 0

        # qs slicing
        return result[offset:offset + page_size]

    return wrapper
