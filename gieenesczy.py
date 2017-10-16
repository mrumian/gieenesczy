from src.requests.project import Project as ProjectRequests
from src.structures.project import Project

import logging as log


log.basicConfig(level=log.DEBUG)

# Create Project instance
project = ProjectRequests()

# Set Input data for Project
project_data = Project(name='demo_name')

# Create Project
project.create_project(project_data.json)

# Get Project UUID
project_uuid = project.get_project_uuid()
