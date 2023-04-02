from django.db import connection
from .models import QueryProfile

class QueryProfilerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/admin/'):  # Only profile queries for the admin section
            for query in connection.queries:
                QueryProfile.objects.create(
                    query=query['sql'],
                    execution_time=query['time']
                )

        return response
