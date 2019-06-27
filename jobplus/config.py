from enum import Enum, unique


@unique
class DeployType(Enum):
    Development = 'DevelopmentConfig.py'
    Production = 'ProductionConfig.py'
    Test = 'TestingConfig.py'

    def configPath(self) -> str:
        return 'Configs/{}'.format(self.value)


preConfig = {

}
