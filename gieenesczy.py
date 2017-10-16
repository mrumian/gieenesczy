from src.requests.session import Session
from src.requests.project import Project as ProjectRequests
from src.requests.node import Node as NodeRequests

from src.structures.node import Node as NodeStruct
from src.structures.project import Project as ProjectStruct

import logging as log
import uuid

log.basicConfig(level=log.DEBUG)


# Create session
session = Session()

# Create Project instance
project = ProjectRequests(session)

rand = str(uuid.uuid4())[0:6]

# Set Input data for Project
project_data = ProjectStruct(name=rand)

# Create Project
project.create_project(project_data.json)

# Get Project UUID
project_uuid = project.get_project_uuid()

# Create Node instance
node = NodeRequests(session)

# Node data
node_data = NodeStruct(project_id=project_uuid, name='testowe')

# Create Node
node.create_node(node_data.json)
