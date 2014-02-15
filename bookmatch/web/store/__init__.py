from pyramid.config import Configurator


def includeme(config):
    config.add_route("top", "/")


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_mako")
    config.include("pyramid_tm")
    config.include(".")
    config.scan(".views")
    return config.make_wsgi_app()
