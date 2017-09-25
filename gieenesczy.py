from src.requests.projects import Projects
from src.requests.version import Version
import logging as log

log.basicConfig(level=log.DEBUG)

ver = Version()
x = ver.get_version()

proj = Projects()
proj.create_project('dupa')
