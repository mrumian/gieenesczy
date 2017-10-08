from src.requests.project import Project as ProjReq
from src.structures.project import Project as ProjStruct
import logging as log

log.basicConfig(level=log.DEBUG)

stru = ProjStruct(name='gienesczy')

proj = ProjReq()

proj.create_project(stru.json)
