from src.requests.projects import Projects
from src.requests.version import Version
import logging as log
from src.structures.project import Project
from pprint import pprint

log.basicConfig(level=log.DEBUG)

#ver = Version()
#x = ver.get_version()

proj = Projects()
proj.create_project('dasdasddddddaaaupa')