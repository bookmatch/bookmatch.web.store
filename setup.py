from setuptools import setup, find_packages

__version__ = '0.0'

requires = [
    "setuptools>=0.8",
    "pyramid>=1.5dev",
    "pyramid_tm",
    "pyramid_mako",
]

tests_require = [
    "webtest",
    "testfixtures",
]

points = {
    "paste.app_factory": [
        "main=bookmatch.web.store:main",
    ]
}

setup(name="bookmatch.web.store",
      version=__version__,
      packages=find_packages(),
      namespace_packages=["bookmatch", "bookmatch.web"],
      install_requires=requires,
      tests_require=tests_require,
      entry_points=points,
      )
