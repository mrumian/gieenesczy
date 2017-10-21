from src.requests.session import Session
from src.requests.project import Project as ProjectRequests
from src.requests.node import Node as NodeRequests
from src.requests.compute import Compute as ComputeRequests

from src.structures.node import Node as NodeStruct
from src.structures.project import Project as ProjectStruct

from src.enums.enums import NodeType

import uuid


# Create session
session = Session()

# Create Project instance
project = ProjectRequests(session)

# Generate random string
#rand = str(uuid.uuid4())[0:6]

# Set Input data for Project
#project_data = ProjectStruct(name=rand)

# Create Project
#project.create_project(project_data.json)

# Load Project
project.load_project('/home/mat/GNS3/projects/af54ec7c-a65b-40cf-861a-f04f1fc1b711/1b9731.gns3')

# Get Project UUID
project_uuid = project.get_project_uuid()

# Compute
compute = ComputeRequests(session)
compute.get_compute_server_data()

compute_id = compute.get_compute_id_for_name('mat-pc')

# Create Node instance
node = NodeRequests(session, project_uuid)

# Node data
node_data = NodeStruct(name='testowe5', node_type=NodeType.vpcs, compute_id=compute_id)

# Create Node
node.create_node(node_data.json)

