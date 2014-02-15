from pyramid.view import view_config

@view_config(route_name="top")
def index(request):
    return request.response
