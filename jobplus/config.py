from enum import Enum, unique

@unique
class DeployType(Enum):
    Development = 'development'
    Production = 'production'
    Test = 'testing'



