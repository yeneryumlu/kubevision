import logging
from sqlalchemy import Column, String, Integer, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime, Date
from dataclasses import dataclass
from datetime import datetime
from typing import List
from db.base import Base


cluster_namespace_association_table = Table(
    'cluster_namespace_association', Base.metadata,
    Column('cluster_id', Integer, ForeignKey('cluster.id'), primary_key=True),
    Column('namespace_id', Integer, ForeignKey('namespace.id'), primary_key=True)
)


# project_team_association_table = Table(
#     'project_team_association', Base.metadata,
#     Column('project_id', Integer, ForeignKey('project.id'), primary_key=True),
#     Column('team_id', Integer, ForeignKey('team.id'), primary_key=True)
# )


# team_member_association_table = Table(
#     'team_member_association', Base.metadata,
#     Column('team_id', Integer, ForeignKey('team.id'), primary_key=True),
#     Column('member_id', Integer, ForeignKey('member.id'), primary_key=True)
# )


# cluster_node_association_table = Table(
#     'cluster_node_association', Base.metadata,
#     Column('cluster_id', Integer, ForeignKey('cluster.id'), primary_key=True),
#     Column('node_id', Integer, ForeignKey('node.id'), primary_key=True)
# )



@dataclass
class Cluster(Base):
    id: Integer
    name: str
    environment: str
    status: str
    version: str
    apiserver: str
    token: str
    nodes: Mapped[List["Node"]] = relationship(back_populates="cluster")

    __tablename__ = 'cluster'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    environment = Column(String)
    status = Column(String)
    version = Column(String)
    apiserver = Column(String)
    token = Column(String)
    last_modified_time = Column(DateTime)
    
    namespaces = relationship(
        "Namespace",
        secondary=cluster_namespace_association_table,
        back_populates='clusters'
    )
    # nodes = relationship(
    #     "Node",
    #     secondary=cluster_node_association_table,
    #     back_populates='clusters'
    # )

    def __init__(self, name, environment, apiserver, token, last_modified_time):
        self.name = name
        self.environment = environment
        self.apiserver = apiserver
        self.token = token
        self.last_modified_time = last_modified_time
    
    def __init__(self, name, environment, apiserver, token, last_modified_time, status, version):
        self.name = name
        self.environment = environment
        self.apiserver = apiserver
        self.token = token
        self.last_modified_time = last_modified_time
        self.status = status
        self.version = version



@dataclass
class Namespace(Base):
    id: Integer
    name: str

    __tablename__ = 'namespace'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_modified_time = Column(DateTime)
    clusters = relationship(
        "Cluster",
        secondary=cluster_namespace_association_table,
        back_populates='namespaces'
    )

    def __init__(self, name):
        self.name = name
        self.last_modified_time = datetime.now()



@dataclass
class Node(Base):
    __allow_unmapped__ = True
    name: str
    cluster_id: Mapped[int] = mapped_column(ForeignKey("cluster.id"))
    cluster: Mapped["Cluster"] = relationship(back_populates="nodes")

    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # clusters = relationship(
    #     "Cluster",
    #     secondary=cluster_node_association_table,
    #     back_populates='nodes'
    # )

    def __init__(self, name):
        self.name = name


@dataclass
class NodeMetric(Base):
    __allow_unmapped__ = True
    cpu_capacity: Integer
    memory_capacity: Integer
    cpu_usage: Integer
    memory_usage: Integer
    node_id: Mapped[int] = mapped_column(ForeignKey("node.id"))
    

    __tablename__ = 'node_metric'
    id = Column(Integer, primary_key=True)
    created_date = Column(Date, default=datetime.utcnow)
    cpu_capacity = Column(Integer)
    memory_capacity = Column(Integer)
    cpu_usage = Column(Integer)
    memory_usage = Column(Integer)

    # clusters = relationship(
    #     "Cluster",
    #     secondary=cluster_node_association_table,
    #     back_populates='nodes'
    # )

    def __init__(self, cpu_capacity, memory_capacity, cpu_usage, memory_usage):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
